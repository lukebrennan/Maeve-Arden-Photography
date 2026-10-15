"""Export only public website files; keep design/source tooling out of hosting."""
from pathlib import Path
import shutil
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
for name in ('assets', 'stories', 'journal'):
    shutil.copytree(ROOT / name, OUT / name)
for file in ROOT.glob('*.html'):
    shutil.copy2(file, OUT / file.name)
for name in ('robots.txt', 'sitemap.xml', 'site.webmanifest', '.nojekyll'):
    shutil.copy2(ROOT / name, OUT / name)
print('Exported public website to dist/ (no development context).')
