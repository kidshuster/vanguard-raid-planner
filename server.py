#!/usr/bin/env python3
"""Serve the standalone planner; requires Python 3.7+ and no extra packages."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

parser = argparse.ArgumentParser(description='Launch Vanguard Raid Planner')
parser.add_argument('--host', default='0.0.0.0', help='Bind address (default: 0.0.0.0)')
parser.add_argument('--port', type=int, default=8080, help='Listen port (default: 8080)')
args = parser.parse_args()
root = Path(__file__).resolve().parent / 'public'
handler = partial(SimpleHTTPRequestHandler, directory=str(root))
with ThreadingHTTPServer((args.host, args.port), handler) as server:
    print(f'Vanguard Raid Planner listening on http://{args.host}:{args.port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
