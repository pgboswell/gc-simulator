"""Build the standalone GC Simulator using Python's standard library."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT / 'public'
body = (ROOT / 'simulator/workspace.html').read_text(encoding='utf-8')
document = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>GC Simulator</title><meta name="description" content="Interactive gas chromatography simulator"><link rel="icon" href="assets/favicon.svg"><link rel="stylesheet" href="assets/site.css"><link rel="stylesheet" href="assets/simulator/simulator.css"><script type="module" src="assets/simulator/app.js"></script></head><body><a class="skip" href="#main">Skip to content</a><header class="header"><div class="wrap masthead"><a class="brand" href="index.html"><img src="assets/favicon.svg" width="44" height="44" alt=""><span><strong>GC Simulator</strong><small>the free, open-source GC simulator</small></span></a></div></header><main id="main" class="wrap">{body}</main><footer class="footer"><div class="wrap"><a href="https://github.com/pgboswell/gc-simulator">Source code</a> · <a href="MODEL.md">Model notes</a> · <a href="https://creativecommons.org/licenses/by-nc-sa/3.0/us/">CC BY-NC-SA 3.0 US</a></div></footer></body></html>'''
for asset in (PUBLIC / 'assets').rglob('*'):
    if asset.is_file() and asset.suffix in ['.css', '.js', '.svg']:
        relative = asset.relative_to(PUBLIC).as_posix()
        digest = hashlib.sha256(asset.read_bytes()).hexdigest()[:10]
        document = document.replace(f'"{relative}"', f'"{relative}?v={digest}"')
(PUBLIC / 'index.html').write_text(document, encoding='utf-8')
print('Built standalone GC Simulator.')
