#!/usr/bin/env python3
"""Serve only generated pages, on this Mac only."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path

root = Path(__file__).resolve().parent.parent / 'dist'
if not (root / 'index.html').exists():
    raise SystemExit('Build first: python3 scripts/build.py')
server = ThreadingHTTPServer(('127.0.0.1', 8892), partial(SimpleHTTPRequestHandler, directory=str(root)))
print('Private local preview: http://127.0.0.1:8892/', flush=True)
try:
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()
