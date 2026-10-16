# Maeve Arden Photography

An editorial wedding photography website concept, designed and developed by Luke Brennan. Maeve Arden is a fictional brand; the photographs are credited stock images and the enquiry form is a transparent browser-only demonstration.

A cream-and-charcoal photographic folio pairs a refined Bodoni Moda wordmark and headings with clear Geologica UI, unequal image pairings and explicit photographic previews that change the images and story links. The portfolio remains a complete, lightweight static website.

## Experience

- A photo-led homepage with thumbnail choices, previous/next controls, a clear enquiry action and visible collection pricing.
- A six-photo home gallery with native horizontal scrolling, explicit open-image controls and full-size viewing.
- A filterable photography portfolio with a full-screen image viewer, arrow-key and touch-swipe navigation, Escape to close, focus containment and focus return.
- Fourteen curated portfolio photographs, three five-image visual stories and three complete planning articles, with useful internal links.
- Collection links that carry the selected collection into a two-step enquiry.
- Inline and summary validation for dates, names and email addresses; a flexible date option; editable enquiry preview; clipboard copy.
- Mobile navigation built on native dialogs, visible focus states, reduced-motion support and a skip link.
- A mobile enquiry shortcut that appears when the main enquiry actions are out of view and hides while home photo controls or closing actions are visible.

## Performance and SEO

No framework, third-party font requests, analytics, stock-image CDN calls or runtime dependencies. Two Latin WOFF2 fonts total about 40 KB: Geologica for body/UI and Bodoni Moda Roman 400 for editorial headings. Both are hosted locally under the SIL Open Font License. The generated pages work on a simple static server and use GitHub Pages-compatible relative paths. The 404 page has inline styles and absolute recovery links so it works at nested missing URLs.

Every photograph is served locally in AVIF with responsive WebP fallback, at 480, 800, 1200 and 1600 pixels. The homepage opens with a candid black-and-white confetti photograph. The chosen image is prioritised and preloaded; below-the-fold images are lazy-loaded, with intrinsic dimensions and CSS aspect ratios to reserve their space. The home photo rail warms its six images as it approaches the viewport to avoid delayed images during horizontal scrolling.

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

The latest home photo/gallery refinement was checked at 320, 375, 487, 768 and 1440 pixels, including photo selection, rail navigation, filtered viewer sequences, Escape and focus return. The expanded portfolio and five-image stories were captured at 375 and 1440 pixels. The original redesign was checked at 390, 1280 and 1440 pixels. Gallery, collections, articles, about, journal, story and contact layouts were captured at 390 and 1440 pixels, with selector, gallery and enquiry interaction checks. Earlier V2 keyboard and navigation checks are documented separately. These checks do not constitute a measured Lighthouse or field Core Web Vitals score.

## Image provenance

See [IMAGE-SOURCES.md](IMAGE-SOURCES.md) and [the asset manifest](assets/images/manifest.json). Seventeen source photographs, including nine additions for the expanded gallery, were downloaded from Unsplash and checked against their source pages and license. Attribution is visible on the site’s image-credit page and in the gallery viewer. Every image also carries embedded XMP with creator, source and license; AVIF/WebP retain Impeccable origin sidecars. The preparation script preserves existing encoded files and their provenance by default. Re-encoding with --rebuild requires reapplying provenance.

The served image library contains 145 files (about 10.53 MB for every format and size combined); the browser requests only the matching variants. Original JPEG downloads remain outside the served site. To recreate the image library, use Python with Pillow and AVIF/WebP support:

```sh
python3 scripts/prepare-images.py --download
```

## GitHub Pages

The Publish website GitHub Actions workflow verifies, exports and deploys dist/ on every main push. Pages uses GitHub Actions as its source. The configured deployment address is:

https://maeveardenphotography.co.uk/

If the deployment address changes, update `BASE` in `scripts/build.py` and regenerate. The manifest start URL stays relative to the site root.

### Custom domain connection

Set the custom domain in repository Settings → Pages to `maeveardenphotography.co.uk` before changing DNS. This repository deploys with GitHub Actions, so Pages stores the custom domain in its settings; a CNAME file is not required.

Replace the holding-page apex A record with these four GitHub Pages addresses:

| Type | Host | Value |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | lukebrennan.github.io |

Preserve unrelated mail and verification records. After DNS validates and GitHub issues the certificate, enable Enforce HTTPS. Check the apex, www redirect, a nested article and the 404 recovery links. DNS propagation and certificate issuance can take up to 24 hours.

Reference: [GitHub Pages custom domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

## Form behaviour

The enquiry form does not check real availability, send mail, store personal details or reserve a date. It validates the details in the current page and creates a clearly labelled preview. No invented mailbox or social-media links are included. Clipboard copying happens only when the visitor chooses it. Production enquiry delivery would require a configured service, server-side validation and a revised privacy notice.

## Logo

The serif MA monogram and Maeve Arden Photography wordmark are committed as outlined SVG, with a reversed version, narrow-screen wordmark and matching favicon under assets/icons. They use Bodoni Moda and Geologica outlines and require no fonts to display. The optional scripts/brand-assets.py generator needs development-only fontTools and Brotli; normal page builds do not.
