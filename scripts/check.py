#!/usr/bin/env python3
"""Check every generated page, anchor and local asset; enforce preview privacy."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'dist'


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.ids, self.errors = [], set(), []
        self.h1, self.main, self.noindex = 0, 0, False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.h1 += tag == 'h1'
        self.main += tag == 'main'
        if a.get('id'):
            if a['id'] in self.ids: self.errors.append(f'Duplicate id: {a["id"]}')
            self.ids.add(a['id'])
        for key in ['href', 'src']:
            if key in a: self.refs.append((tag, a[key]))
        if tag == 'img' and 'alt' not in a: self.errors.append('Image without alt text')
        if tag == 'meta' and a.get('name') == 'robots' and 'noindex' in a.get('content', ''): self.noindex = True
        if tag in ['iframe', 'form']: self.errors.append(f'Unexpected {tag} in static preview')


pages = {}
for path in OUT.rglob('*.html'):
    p = Page()
    p.feed(path.read_text())
    pages[path.resolve()] = p
errors = []
for path, p in pages.items():
    if p.h1 != 1: p.errors.append(f'Expected one h1, found {p.h1}')
    if p.main != 1: p.errors.append(f'Expected one main, found {p.main}')
    if not p.noindex: p.errors.append('Missing private-preview noindex metadata')
    for tag, ref in p.refs:
        u = urlsplit(ref)
        if u.scheme:
            if u.scheme != 'https': p.errors.append(f'Unexpected URL scheme: {ref}')
            if tag in ['script', 'img', 'link']: p.errors.append(f'Nonlocal runtime dependency: {ref}')
            continue
        if ref.startswith('//'): p.errors.append(f'Protocol-relative URL: {ref}'); continue
        target = (path.parent / unquote(u.path)).resolve() if u.path else path
        if target.is_dir(): target /= 'index.html'
        if not target.is_relative_to(OUT): p.errors.append(f'Link escapes output: {ref}')
        elif not target.exists(): p.errors.append(f'Missing target: {ref}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids: p.errors.append(f'Missing fragment: {ref}')
    errors.extend(f'{path.relative_to(OUT)}: {error}' for error in p.errors)
if (ROOT / '.github/workflows').exists():
    errors.append('Publishing automation is intentionally absent for this private draft')
if len(pages) != 13: errors.append(f'Expected 13 pages, found {len(pages)}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(pages)} pages; local links, fragments, assets, headings, alt text, and private-preview metadata.')
