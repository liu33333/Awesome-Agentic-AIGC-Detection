import importlib.util
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import socket
import tempfile
import threading
import time
import unittest
from unittest.mock import patch
import urllib.error

spec = importlib.util.spec_from_file_location('audit_links', Path(__file__).resolve().parents[1] / 'scripts/audit_links.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class Handler(BaseHTTPRequestHandler):
    counts = {}

    def log_message(self, *args):
        pass

    def do_HEAD(self):
        self.respond()

    def do_GET(self):
        self.respond()

    def respond(self):
        key = (self.command, self.path)
        self.counts[key] = self.counts.get(key, 0) + 1
        if self.path == '/timeout':
            time.sleep(0.15)
        if self.path == '/disconnect':
            self.connection.close()
            return
        redirects = {'/move': '/chain', '/chain': '/ok', '/loop': '/loop'}
        status = 302 if self.path in redirects else 200
        if self.path.startswith('/status/'):
            status = int(self.path.rsplit('/', 1)[1])
        if self.path in ('/head-blocked', '/head-false404') and self.command == 'HEAD':
            status = 405 if self.path == '/head-blocked' else 404
        if self.path == '/recover':
            status = 503 if self.counts.get(('HEAD', '/recover'), 0) <= 1 else 200
        self.send_response(status)
        if self.path in redirects:
            self.send_header('Location', redirects[self.path])
        if status == 429:
            self.send_header('Retry-After', '120')
        self.end_headers()


class NetworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f'http://127.0.0.1:{cls.server.server_port}'

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def setUp(self):
        self.checker = audit.Checker(timeout=.03, retries=0, delay=0, allow_private=True)

    def test_success_and_head_fallback(self):
        for path in ('/ok', '/head-blocked', '/head-false404'):
            with self.subTest(path=path):
                self.assertEqual(self.checker.check(self.base + path)['category'], 'ok')
        self.assertGreater(Handler.counts[('GET', '/head-false404')], 0)

    def test_redirect_destination_and_chain(self):
        result = self.checker.check(self.base + '/move')
        self.assertEqual(result['category'], 'redirected')
        self.assertEqual(len(result['redirects']), 2)
        self.assertEqual(result['final_url'], self.base + '/ok')

    def test_redirect_loop(self):
        self.assertEqual(self.checker.check(self.base + '/loop')['category'], 'unverified')

    def test_status_categories(self):
        for status, category in [(404, 'http_not_found'), (410, 'http_not_found'), (401, 'restricted'), (403, 'restricted'), (429, 'restricted'), (451, 'restricted'), (500, 'unverified'), (503, 'unverified'), (400, 'unverified')]:
            with self.subTest(status=status):
                self.checker.cooldowns.clear()
                result = self.checker.check(self.base + '/status/' + str(status))
                self.assertEqual(result['category'], category)
                self.assertEqual(result['status'], status)

    def test_timeout_and_connection_failure(self):
        for path in ('/timeout', '/disconnect'):
            self.assertEqual(self.checker.check(self.base + path)['category'], 'unverified')

    def test_retry_recovers(self):
        checker = audit.Checker(retries=1, delay=0, allow_private=True)
        with patch.object(audit.time, 'sleep'):
            self.assertEqual(checker.check(self.base + '/recover')['category'], 'ok')
        self.assertEqual(Handler.counts[('HEAD', '/recover')], 2)

    def test_rate_limit_long_wait_not_retried(self):
        checker = audit.Checker(retries=2, delay=0, allow_private=True)
        before = Handler.counts.get(('HEAD', '/status/429'), 0)
        result = checker.check(self.base + '/status/429')
        self.assertEqual(result['category'], 'restricted')
        self.assertEqual(Handler.counts[('HEAD', '/status/429')] - before, 1)
        self.assertEqual(Handler.counts.get(('GET', '/status/429'), 0), 0)
        self.assertEqual(checker.check(self.base + '/ok')['category'], 'restricted')

    def test_private_address_blocked_by_default(self):
        self.assertEqual(audit.Checker(delay=0).check(self.base)['category'], 'unverified')

    def test_network_failure_retried_and_never_broken(self):
        checker = audit.Checker(retries=2, delay=0)
        with patch.object(checker, 'request', side_effect=urllib.error.URLError('DNS failure')) as request, patch.object(audit.time, 'sleep'):
            self.assertEqual(checker.check('https://example.com')['category'], 'unverified')
            self.assertEqual(request.call_count, 3)

    def test_redirect_to_restricted_preserves_destination(self):
        with patch.object(self.checker, 'request', side_effect=[(301, {'Location': '/login'}), (403, {}), (403, {})]):
            result = self.checker.check('https://example.com/old')
            self.assertEqual(result['category'], 'restricted')
            self.assertEqual(result['final_url'], 'https://example.com/login')
            self.assertEqual(len(result['redirects']), 1)

    def test_retry_after_short_wait(self):
        checker = audit.Checker(retries=1, delay=0)
        with patch.object(checker, 'request', side_effect=[(429, {'Retry-After': '3'}), (200, {})]), patch.object(audit.time, 'sleep') as sleep:
            self.assertEqual(checker.check('https://example.com')['category'], 'ok')
            sleep.assert_called_once_with(3)

    def test_http_date_retry_after(self):
        self.assertEqual(audit.retry_seconds({'Retry-After': 'Wed, 21 Oct 2015 07:28:00 GMT'}, now=1445412470), 10)
        self.assertEqual(audit.retry_seconds({'Retry-After': 'Wed, 21 Oct 2015 07:28:00 GMT'}, now=1445412490), 0)
        self.assertEqual(audit.retry_seconds({'Retry-After': 'invalid'}), 0)
        checker = audit.Checker(retries=1, delay=0)
        with patch.object(checker, 'request', return_value=(429, {'Retry-After': 'Wed, 21 Oct 2015 07:28:00 GMT'})) as request, patch.object(audit.time, 'time', return_value=1445412400):
            self.assertEqual(checker.check('https://example.com')['category'], 'restricted')
            request.assert_called_once_with('https://example.com', 'HEAD')

    def test_head_restrictions_do_not_trigger_get(self):
        for status in (401, 403, 407, 451):
            with patch.object(self.checker, 'request', return_value=(status, {})) as request:
                self.assertEqual(self.checker.check('https://example.com')['category'], 'restricted')
                request.assert_called_once_with('https://example.com', 'HEAD')

    def test_404_is_not_permanent_dead_link_proof(self):
        with patch.object(self.checker, 'request', return_value=(404, {})) as request:
            result = self.checker.check('https://github.com/owner/private')
            self.assertEqual(result['category'], 'http_not_found')
            self.assertEqual(result['status'], 404)
            self.assertIn('private', result['detail'])
            self.assertEqual(request.call_args_list[-1].args[1], 'GET')

    def test_redirect_login_and_home_are_reviewed(self):
        for path in ('/login', '/'):
            with patch.object(self.checker, 'request', side_effect=[(302, {'Location': path}), (200, {})]):
                result = self.checker.check('https://example.com/repo')
                self.assertEqual(result['category'], 'redirected')
                self.assertIn('possible login/home', result['detail'])

    def test_redirect_edge_cases(self):
        scenarios = [([(302, {})], 'Redirect without'), ([(302, {'Location': 'http://example.com'})], 'downgrade')]
        for responses, reason in scenarios:
            with patch.object(self.checker, 'request', side_effect=responses):
                result = self.checker.check('https://example.com')
                self.assertEqual(result['category'], 'unverified')
                self.assertIn(reason, result['detail'])
        with patch.object(self.checker, 'request', side_effect=[(302, {'Location': f'/hop{i}'}) for i in range(11)]):
            self.assertIn('limit', self.checker.check('https://example.com')['detail'])


class DocumentTests(unittest.TestCase):
    def test_extraction(self):
        text = '''[paper](https://example.com/paper_(one))
![image](assets/a.svg)
<a href="https://example.com?a=1&amp;b=2">HTML</a>
[reference]: <https://example.com/ref> "Title"
<https://example.com/auto>
`[skip](https://skip.example)`
```
[skip](https://skip.example)
```
<!-- [skip](https://skip.example) -->
'''
        links = audit.extract(text)
        self.assertEqual(len(links), 5)
        self.assertIn((1, 'https://example.com/paper_(one)'), links)
        self.assertIn((3, 'https://example.com?a=1&b=2'), links)

    def test_code_headings_are_not_anchors(self):
        found = audit.anchors('# A `code` heading\n```\n# Hidden\n```\n')
        self.assertIn('a-code-heading', found)
        self.assertNotIn('hidden', found)

    def test_local_paths_and_anchors(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            source = root / 'README.md'
            source.write_text('# Hello, World!\n# Hello, World!\n<a name="中文"></a>\n', encoding='utf-8')
            for url in ('#hello-world', '#hello-world-1', '#%E4%B8%AD%E6%96%87'):
                self.assertEqual(audit.local_check(root, source, url)['category'], 'ok')
            for url in ('#missing', 'missing.md'):
                self.assertEqual(audit.local_check(root, source, url)['category'], 'broken')
            self.assertEqual(audit.local_check(root, source, '../outside')['category'], 'unverified')

    def test_audit_deduplicates_external_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            sources = [root / 'README.md', root / 'README_CN.md']
            for path in sources:
                path.write_text('[same](https://example.com)\n', encoding='utf-8')
            checker = audit.Checker()
            with patch.object(checker, 'check', return_value={'category': 'ok', 'detail': 'fixture'}) as check:
                rows = audit.audit(root, sources, checker)
                self.assertEqual(check.call_count, 1)
                self.assertEqual(len(rows[0]['sources']), 2)
            rows = audit.audit(root, sources, checker, local_only=True)
            self.assertEqual(rows[0]['category'], 'skipped')


if __name__ == '__main__':
    unittest.main()
