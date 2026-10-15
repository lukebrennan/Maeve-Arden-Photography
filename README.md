# Maeve Arden Photography

An editorial wedding photography website concept, designed and developed by Luke Brennan. Maeve Arden is a fictional brand; the photographs are credited stock images and the enquiry form is a transparent browser-only demonstration.

A cream-and-charcoal photographic folio pairs a refined Bodoni Moda wordmark and headings with clear Geologica UI, unequal image pairings and a place selector that changes the photographs and story links. The portfolio remains a complete, lightweight static website.

## Experience

- An image-led homepage with Lake District, London and celebration scenes, a clear enquiry action and visible collection pricing.
- A filterable photography portfolio with a full-screen image viewer, arrow-key navigation, Escape to close, focus containment and focus return.
- Three visual story pages and three complete planning articles, with useful internal links.
- Collection links that carry the selected collection into a two-step enquiry.
- Inline and summary validation for dates, names and email addresses; a flexible date option; editable enquiry preview; clipboard copy.
- Mobile navigation built on native dialogs, visible focus states, reduced-motion support and a skip link.
- A mobile enquiry shortcut that appears when the main enquiry actions are out of view and hides when they are visible.

## Performance and SEO

No framework, third-party font requests, analytics, stock-image CDN calls or runtime dependencies. Two Latin WOFF2 fonts total about 40 KB: Geologica for body/UI and Bodoni Moda Roman 400 for editorial headings. Both are hosted locally under the SIL Open Font License. The generated pages work on a simple static server and use GitHub Pages-compatible relative paths. The 404 page has inline styles and absolute recovery links so it works at nested missing URLs.

Every photograph is served locally in AVIF with responsive WebP fallback, at 480, 800, 1200 and 1600 pixels. The homepage begins with the landscape source, with responsive art direction for smaller screens. The chosen image is prioritised and preloaded; below-the-fold images are lazy-loaded, with intrinsic dimensions and CSS aspect ratios to reserve their space.

The site includes unique titles and descriptions, canonical URLs, Open Graph and Twitter metadata, a local 1200 × 630 social image, a sitemap, robots.txt and Website, WebPage, Article and Breadcrumb structured data. It intentionally makes no claims about a real business, reviews, clients or bookings.

## Preview

From this directory:

```sh
python3 scripts/build.py
python3 scripts/export.py
python3 -m http.server 4173 --bind 127.0.0.1 --directory dist
```

Open `http://127.0.0.1:4173/`. The static files also open directly from disk; browser clipboard and source-credit enhancements work best over HTTP.

## Edit and verify

Page content and shared templates are maintained in `scripts/build.py`. Styles are maintained in `src/style.css`; the generator produces the compact served stylesheet at `assets/css/style.css`. The interaction code is `assets/js/main.js`. Generated HTML is committed and verified. scripts/export.py creates a clean dist/ directory containing only public website files; development context, source tooling and design contracts stay out of hosting.

```sh
python3 scripts/build.py
python3 tests/verify.py
node --check assets/js/main.js
```

The checks verify all 15 pages, internal links and fragments, image source paths, dimensions, metadata, valid structured data, the sitemap and image manifest byte sizes. GitHub Actions runs these checks and verifies that the generated output is current.

The redesigned home was checked in a browser at 390, 1280 and 1440 pixels. Gallery, collections, articles, about, journal, story and contact layouts were captured at 390 and 1440 pixels, with selector, gallery and enquiry interaction checks. Earlier V2 keyboard and navigation checks are documented separately. These checks do not constitute a measured Lighthouse or field Core Web Vitals score.

## Image provenance

See [IMAGE-SOURCES.md](IMAGE-SOURCES.md) and [the asset manifest](assets/images/manifest.json). Eight original V2 photographs were downloaded from Unsplash and verified against their source pages and license. Attribution is visible on the site’s image-credit page and in the gallery viewer. Every image also carries embedded XMP with creator, source and license; AVIF/WebP retain Impeccable origin sidecars. Rebuilding the library requires reapplying this provenance.

The served image library contains 73 files (about 5.45 MB for every format and size combined); the browser requests only the matching variants. Original JPEG downloads remain outside the served site. To recreate the image library, use Python with Pillow and AVIF/WebP support:

```sh
python3 scripts/prepare-images.py --download
```

## GitHub Pages

The Publish website GitHub Actions workflow verifies, exports and deploys dist/ on every main push. Pages uses GitHub Actions as its source. The live address is:

https://lukebrennan.github.io/Maeve-Arden-Photography/

If the deployment address changes, update `BASE` in `scripts/build.py` and regenerate. The manifest start URL stays relative to the project path.

## Form behaviour

The enquiry form does not check real availability, send mail, store personal details or reserve a date. It validates the details in the current page and creates a clearly labelled preview. No invented mailbox or social-media links are included. Clipboard copying happens only when the visitor chooses it. Production enquiry delivery would require a configured service, server-side validation and a revised privacy notice.
