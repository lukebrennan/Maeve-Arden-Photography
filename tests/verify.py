"""Verify static output and deployment paths, with no third-party dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []

class Document(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.ids = set()
        self.links = []
        self.h1s = 0
        self.titles = 0
        self.description = False
        self.canonical = False
        self.schema = []
        self.in_schema = False
        self.schema_text = ''
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids: errors.append(f'{self.path}: duplicate id {a["id"]}')
            self.ids.add(a['id'])
        if tag == 'h1': self.h1s += 1
        if tag == 'title': self.titles += 1
        if tag == 'meta' and a.get('name') == 'description': self.description = bool(a.get('content'))
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = True
        if tag == 'script' and a.get('type') == 'application/ld+json': self.in_schema = True
        if tag in ('a', 'link') and a.get('href'): self.links.append(a['href'])
        if tag in ('img','script') and a.get('src'): self.links.append(a['src'])
        for attribute in ('srcset', 'imagesrcset'):
            if a.get(attribute): self.links.extend(part.strip().split(' ')[0] for part in a[attribute].split(','))
        if tag == 'img':
            if 'alt' not in a: errors.append(f'{self.path}: image missing alt')
            if 'width' not in a or 'height' not in a: errors.append(f'{self.path}: missing intrinsic image dimensions')
            if a.get('src','').startswith('http'): errors.append(f'{self.path}: remote image request')
    def handle_endtag(self, tag):
        if tag == 'script' and self.in_schema:
            self.in_schema = False
            try: self.schema.append(json.loads(self.schema_text))
            except json.JSONDecodeError: errors.append(f'{self.path}: invalid JSON-LD')
            self.schema_text = ''
    def handle_data(self, data):
        if self.in_schema: self.schema_text += data

documents = {}
for file in sorted(ROOT.rglob('*.html')):
    relative = file.relative_to(ROOT)
    if any(part.startswith('.') or part == 'dist' for part in relative.parts): continue
    document = Document(relative)
    document.feed(file.read_text())
    documents[file] = document
    if document.h1s != 1: errors.append(f'{relative}: expected one H1, found {document.h1s}')
    if document.titles != 1 or not document.description or not document.canonical or not document.schema:
        errors.append(f'{relative}: incomplete metadata')
for file, document in documents.items():
    for link in document.links:
        url = urlsplit(link)
        if url.scheme or url.netloc: continue
        if link == '#': errors.append(f'{document.path}: placeholder link')
        if url.path.startswith('/'): errors.append(f'{document.path}: root path breaks GitHub project hosting: {link}')
        target = (file.parent / unquote(url.path)).resolve() if url.path else file
        if not target.exists(): errors.append(f'{document.path}: missing target {link}')
        elif url.fragment and target in documents and url.fragment not in documents[target].ids:
            errors.append(f'{document.path}: broken fragment {link}')
sitemap = ET.parse(ROOT / 'sitemap.xml')
locations = [node.text for node in sitemap.findall('.//{*}loc')]
if len(locations) != len(documents)-1: errors.append('Sitemap should contain all pages except the 404')
for location in locations:
    if not location.startswith('https://maeveardenphotography.co.uk/'):
        errors.append(f'Unexpected sitemap URL: {location}')
manifest = json.loads((ROOT/'assets/images/manifest.json').read_text())
variants = sum(len(photo.get('variants', [])) for photo in manifest.values())
for photo in manifest.values():
    for variant in photo.get('variants', []):
        # Manifest paths are filenames relative to assets/images.
        path = ROOT/'assets/images'/variant['file']
        if not path.exists(): errors.append(f'Missing manifest variant: {path.name}')
        elif path.stat().st_size != variant['bytes']: errors.append(f'Stale image size: {path.name}')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'PASS: {len(documents)} pages; internal links and fragments; metadata and schema; sitemap; {variants} image variants.')
