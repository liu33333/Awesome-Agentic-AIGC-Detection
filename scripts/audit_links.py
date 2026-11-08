#!/usr/bin/env python3
"""Conservative, report-only link audit. Python standard library only."""
import argparse
import concurrent.futures
from email.utils import parsedate_to_datetime
import html
from html.parser import HTMLParser
import ipaddress
import json
from pathlib import Path
import re
import socket
import threading
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request


class HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append((self.getpos()[0], attrs[key]))
        for key in ('id', 'name'):
            if attrs.get(key):
                self.anchors.add(attrs[key])


def without_blocks(text):
    # Keep line offsets intact while excluding comments and fenced/inline code.
    text = re.sub(r'<!--.*?-->', lambda m: '\n' * m[0].count('\n'), text, flags=re.S)
    text = re.sub(r'^ {0,3}(`{3,}|~{3,})[^\n]*\n.*?^ {0,3}\1[^\n]*$',
                  lambda m: '\n' * m[0].count('\n'), text, flags=re.M | re.S)
    return text


def without_code(text):
    return re.sub(r'(`+)([^`]*?)\1', lambda m: ' ' * len(m[0]), without_blocks(text))


def extract(text):
    text = without_code(text)
    parser = HTMLLinks()
    parser.feed(text)
    links = list(parser.links)
    # Inline links/images, angle autolinks, and reference definitions. The inline
    # destination supports balanced parentheses common in paper/wiki URLs.
    patterns = [r'!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|(?:[^\s()\\]|\\.|\([^()]*\))+)\s*(?:["\'][^\n]*?["\']\s*)?\)',
                r'<(https?://[^<>\s]+)>',
                r'^ {0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)']
    for pattern in patterns:
        for match in re.finditer(pattern, text, re.M):
            url = html.unescape(match[1].strip('<>'))
            url = re.sub(r'\\([\\()`*_{}\[\]<>#+.!-])', r'\1', url)
            links.append((text.count('\n', 0, match.start()) + 1, url))
    return sorted(set(links))


def anchors(text):
    parser = HTMLLinks()
    parser.feed(without_code(text))
    found = set(parser.anchors)
    counts = {}
    # GFM heading slugs; explicit HTML anchors are preferred for complex markup.
    text = without_blocks(text)
    headings = re.findall(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$', text, re.M)
    headings += re.findall(r'^([^\n]+)\n {0,3}(?:=+|-+)\s*$', text, re.M)
    for heading in headings:
        heading = re.sub(r'!?\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        heading = html.unescape(re.sub(r'<[^>]+>', '', heading)).lower()
        slug = ''.join(c for c in heading if c in '-_ ' or unicodedata.category(c)[0] in 'LNM')
        slug = slug.replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        found.add(slug + (f'-{count}' if count else ''))
    return found


def local_check(root, source, url):
    parts = urllib.parse.urlsplit(url)
    target = (source.parent / urllib.parse.unquote(parts.path)).resolve() if parts.path else source
    if not target.is_relative_to(root):
        return {'category': 'unverified', 'detail': 'Local path leaves repository'}
    if not target.exists():
        return {'category': 'broken', 'detail': 'Local target does not exist'}
    if parts.fragment and target.suffix.lower() in ('.md', '.markdown'):
        if urllib.parse.unquote(parts.fragment) not in anchors(target.read_text(encoding='utf-8')):
            return {'category': 'broken', 'detail': 'Local Markdown anchor not found'}
    elif parts.fragment:
        return {'category': 'unverified', 'detail': 'Non-Markdown fragment not checked'}
    return {'category': 'ok', 'detail': 'Local target and Markdown anchor verified'}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def retry_seconds(headers, now=None):
    value = next((v.strip() for k, v in headers.items() if k.lower() == 'retry-after'), '')
    if value.isdigit():
        return float(value)
    try:
        parsed = parsedate_to_datetime(value)
        return max(0.0, parsed.timestamp() - (time.time() if now is None else now))
    except (ValueError, TypeError, OverflowError):
        return 0.0


class DeferredRequest(Exception):
    def __init__(self, status):
        self.status = status
        super().__init__('Host Retry-After cooldown active; request deferred to a later run')


class Checker:
    def __init__(self, timeout=12, retries=2, delay=0.5, allow_private=False):
        self.timeout, self.retries, self.delay = timeout, retries, delay
        self.allow_private = allow_private  # Test fixture use only; not a CLI option.
        self.lock = threading.Lock()
        self.hosts = {}
        self.cooldowns = {}

    def validate(self, url):
        p = urllib.parse.urlsplit(url)
        if p.scheme not in ('http', 'https') or not p.hostname or p.username or p.password:
            raise ValueError('Unsupported or credential-bearing URL')
        if not self.allow_private:
            addresses = socket.getaddrinfo(p.hostname, p.port or (443 if p.scheme == 'https' else 80), type=socket.SOCK_STREAM)
            if any(not ipaddress.ip_address(item[4][0]).is_global for item in addresses):
                raise ValueError('Private/reserved network destination not requested')
        return p.hostname

    def request(self, url, method):
        host = self.validate(url)
        with self.lock:
            lock = self.hosts.setdefault(host, threading.Lock())
        with lock:
            until, status = self.cooldowns.get(host, (0, None))
            if until > time.monotonic():
                raise DeferredRequest(status)
            time.sleep(self.delay)
            req = urllib.request.Request(url, method=method, headers={
                'User-Agent': 'Awesome-Agentic-AIGC-Detection-LinkAudit/1.0',
                'Accept': '*/*',
            })
            opener = urllib.request.build_opener(NoRedirect())
            try:
                with opener.open(req, timeout=self.timeout) as response:
                    status, headers = response.status, dict(response.headers)
            except urllib.error.HTTPError as error:
                with error:
                    status, headers = error.code, dict(error.headers)
            if status in (429, 503):
                cooldown = retry_seconds(headers)
                if cooldown:
                    self.cooldowns[host] = (time.monotonic() + cooldown, status)
            return status, headers

    def check(self, url):
        url = urllib.parse.urldefrag(url)[0]
        chain, seen = [], set()
        result = {'final_url': url, 'redirects': chain}
        try:
            for _ in range(11):
                if url in seen:
                    return dict(result, category='unverified', detail='Redirect loop')
                seen.add(url)
                for attempt in range(self.retries + 1):
                    try:
                        status, headers = self.request(url, 'HEAD')
                        # GET confirms missing targets and method rejection, but
                        # never bypasses HEAD access/rate restrictions or cooldowns.
                        if status in (400, 404, 405, 410, 501):
                            status, headers = self.request(url, 'GET')
                    except DeferredRequest as error:
                        return dict(result, category='restricted' if error.status == 429 else 'unverified',
                                    detail=str(error), cooldown_status=error.status)
                    except (OSError, ValueError, urllib.error.URLError) as error:
                        if attempt == self.retries or isinstance(error, ValueError):
                            return dict(result, category='unverified', detail=f'{type(error).__name__}: {error}')
                        time.sleep(min(2 ** attempt, 8))
                        continue
                    if status == 429 or status >= 500:
                        if attempt < self.retries:
                            cooldown = retry_seconds(headers)
                            # A long requested cooldown is respected by deferring;
                            # request() also prevents other URLs hitting this host.
                            if cooldown > 30:
                                break
                            time.sleep(max(cooldown, 2 ** attempt))
                            continue
                    break
                result['status'] = status
                if status in (301, 302, 303, 307, 308):
                    location = next((v for k, v in headers.items() if k.lower() == 'location'), None)
                    if not location:
                        return dict(result, category='unverified', detail='Redirect without Location')
                    destination = urllib.parse.urljoin(url, location)
                    # Never follow HTTPS downgrades automatically.
                    if url.startswith('https:') and not destination.startswith('https:'):
                        chain.append({'from': url, 'status': status, 'to': destination})
                        return dict(result, category='unverified', detail='HTTPS downgrade not followed')
                    chain.append({'from': url, 'status': status, 'to': destination})
                    url = urllib.parse.urldefrag(destination)[0]
                    result['final_url'] = url
                    continue
                if 200 <= status < 300:
                    detail = 'HTTP reachable; page identity and remote fragments require human review'
                    path = urllib.parse.urlsplit(url).path.rstrip('/').lower()
                    if chain and (not path or any(part in ('login', 'signin', 'sign-in', 'auth', 'oauth', 'sso') for part in path.split('/'))):
                        detail += '; possible login/home landing page, not verified as intended content'
                    return dict(result, category='redirected' if chain else 'ok', detail=detail)
                if status in (404, 410):
                    return dict(result, category='http_not_found', detail=f'GET returned HTTP {status}; may be missing, private or access-masked; human review required')
                if status in (401, 403, 407, 429, 451):
                    return dict(result, category='restricted', detail=f'Access/rate restriction: HTTP {status}')
                return dict(result, category='unverified', detail=f'Ambiguous/transient HTTP {status}')
            return dict(result, category='unverified', detail='Redirect hop limit exceeded')
        except (OSError, ValueError) as error:
            return dict(result, category='unverified', detail=f'{type(error).__name__}: {error}')


def audit(root, files, checker, local_only=False):
    rows, external = [], {}
    for source in files:
        for line, url in extract(source.read_text(encoding='utf-8')):
            origin = {'file': str(source.relative_to(root)), 'line': line}
            try:
                parts = urllib.parse.urlsplit(url)
                if parts.scheme in ('http', 'https'):
                    external.setdefault(url, []).append(origin)
                elif not parts.scheme and not parts.netloc:
                    rows.append(dict(url=url, sources=[origin], **local_check(root, source, url)))
                else:
                    rows.append(dict(url=url, sources=[origin], category='skipped', detail='Unsupported URL scheme'))
            except ValueError as error:
                rows.append(dict(url=url, sources=[origin], category='unverified', detail=str(error)))
    if local_only:
        rows.extend(dict(url=url, sources=sources, category='skipped', detail='External check not requested') for url, sources in external.items())
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            futures = {executor.submit(checker.check, url): url for url in external}
            for future in concurrent.futures.as_completed(futures):
                url = futures[future]
                rows.append(dict(url=url, sources=external[url], **future.result()))
    return sorted(rows, key=lambda row: (row['category'], row['url'], row['sources'][0]['file']))


def markdown(rows):
    counts = {key: sum(r['category'] == key for r in rows) for key in ('ok', 'redirected', 'http_not_found', 'broken', 'restricted', 'unverified', 'skipped')}
    output = ['# Link audit', '', 'Report only. Remote 404/410, restricted and unverified links are **not proven broken**. The broken category is reserved for missing local files/anchors. HTTP success does not prove the destination is the intended paper or repository. Remote fragments are not validated.', '', ', '.join(f'**{k}: {v}**' for k, v in counts.items()), '']
    for row in rows:
        if row['category'] in ('ok', 'skipped'):
            continue
        safe = lambda value: re.sub(r'([\\`*_{}\[\]()#+.!|>-])', r'\\\1', html.escape(str(value), quote=True).replace('\n', ' '))
        output += [f"## {row['category']}: {safe(row['url'])}", '', safe(row['detail']), '']
        output += [f"- Source: {safe(s['file'])}:{s['line']}" for s in row['sources']]
        output += [f"- HTTP {hop['status']}: {safe(hop['from'])} → {safe(hop['to'])}" for hop in row.get('redirects', [])]
        output += ['']
    return '\n'.join(output) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, default=Path('link-audit'))
    parser.add_argument('--local-only', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    files = [root / 'README.md', root / 'README_CN.md'] + sorted((root / 'docs').rglob('*.md'))
    rows = audit(root, files, Checker(), args.local_only)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'results.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (args.output / 'summary.md').write_text(markdown(rows), encoding='utf-8')
    print(markdown(rows))
    # Findings never fail CI. Exceptions, missing input files, and failed tests do.
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
