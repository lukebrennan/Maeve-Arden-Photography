#!/usr/bin/env python3
"""Recreate local responsive images from the stock photographs selected in V2.

Requires Pillow with WebP and AVIF support. Originals are cached outside the site
at ../tmp/maeve-photo-sources. No source image is enlarged. Run --download to
download sources again; licensing must be checked separately before new use.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import urllib.request

from PIL import Image, ImageDraw, ImageOps, features


SITE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = SITE_ROOT.parent / "tmp" / "maeve-photo-sources"
IMAGE_DIR = SITE_ROOT / "assets" / "images"
WIDTHS = (480, 800, 1200, 1600)
LICENSE_URL = "https://unsplash.com/license"
VERIFIED_DATE = "2026-10-15"
PHOTOS = {
    "hero": {
        "photographer": "Rafa Sanfilippo",
        "photoId": "cWLEzYAcI3Q",
        "originalWidth": 4000,
        "originalHeight": 6000,
        "cdnId": "photo-1772634734681-9db90f08684c",
        "sourceUrl": "https://unsplash.com/photos/a-bride-and-groom-laughing-together-on-their-wedding-day-cWLEzYAcI3Q",
        "alt": "Bride and groom laughing together in a black and white wedding portrait",
    },
    "still-water": {
        "photographer": "Sabesh Photography LTD",
        "photoId": "gpGfPhSr3rQ",
        "originalWidth": 8192,
        "originalHeight": 5464,
        "cdnId": "photo-1728348829982-7f19100827a8",
        "sourceUrl": "https://unsplash.com/photos/a-bride-and-groom-are-standing-on-a-dock-gpGfPhSr3rQ",
        "alt": "Bride and groom standing on a wooden jetty in the Lake District",
    },
    "city-softened": {
        "photographer": "Howard Walsh",
        "photoId": "P_jDtRMQxL0",
        "originalWidth": 3373,
        "originalHeight": 5060,
        "cdnId": "photo-1775664377581-7ca46ddb619b",
        "sourceUrl": "https://unsplash.com/photos/bride-and-groom-posing-on-tower-bridge-P_jDtRMQxL0",
        "alt": "A bride being photographed beneath the arches of Tower Bridge in London",
    },
    "celebration": {
        "photographer": "Ben Atkins",
        "photoId": "CkQxfER9FvA",
        "originalWidth": 3185,
        "originalHeight": 3981,
        "cdnId": "photo-1722805740128-b01efd09b4b7",
        "sourceUrl": "https://unsplash.com/photos/a-bride-and-groom-are-posing-for-a-picture-CkQxfER9FvA",
        "alt": "Newlyweds dancing together beneath red confetti",
    },
    "bridal": {
        "photographer": "Alexander Mass",
        "photoId": "HVTDyWXQkrA",
        "originalWidth": 4000,
        "originalHeight": 6000,
        "cdnId": "photo-1773688199736-579b6928e417",
        "sourceUrl": "https://unsplash.com/photos/bride-in-a-wedding-dress-looking-away-HVTDyWXQkrA",
        "alt": "A bride looking towards the camera in soft black and white light",
    },
    "table": {
        "photographer": "Ben Atkins",
        "photoId": "zjJiX9txwRU",
        "originalWidth": 3757,
        "originalHeight": 5010,
        "cdnId": "photo-1775126964424-913480443772",
        "sourceUrl": "https://unsplash.com/photos/a-beautifully-set-table-for-a-wedding-reception-zjJiX9txwRU",
        "alt": "Wedding breakfast table with flowers, wine and place settings",
    },
    "lake-sunset": {
        "photographer": "c k",
        "photoId": "o6u_mqxYGDg",
        "originalWidth": 3100,
        "originalHeight": 1744,
        "cdnId": "photo-1758727654358-a90614d694eb",
        "sourceUrl": "https://unsplash.com/photos/couple-in-wedding-attire-by-a-serene-lake-at-sunset-o6u_mqxYGDg",
        "alt": "Bride and groom standing together beside a lake in evening light",
    },
    "evening": {
        "photographer": "Foto Pettine",
        "photoId": "AXaQzYRIb4w",
        "originalWidth": 3923,
        "originalHeight": 2615,
        "cdnId": "photo-1571727226062-18a510ab1211",
        "sourceUrl": "https://unsplash.com/photos/wedding-couple-on-focus-photography-AXaQzYRIb4w",
        "alt": "Wedding couple beside a pool in dramatic backlit evening mist",
    },
}


def download_source(stem, info, source_dir):
    source_dir.mkdir(parents=True, exist_ok=True)
    target = source_dir / f"{stem}.jpg"
    if target.exists():
        return
    url = f"https://images.unsplash.com/{info['cdnId']}?fm=jpg&q=90&w=2400&fit=max"
    request = urllib.request.Request(url, headers={"User-Agent": "MaeveArdenAssetPreparation/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
    # Validate the download before writing it to the source cache.
    from io import BytesIO
    with Image.open(BytesIO(data)) as image:
        image.verify()
    target.write_bytes(data)


def save_variants(stem, image):
    variants = []
    for width in WIDTHS:
        if width > image.width:
            continue
        height = round(image.height * width / image.width)
        resized = image.resize((width, height), Image.Resampling.LANCZOS)
        for extension, options in (
            ("webp", {"quality": 74, "method": 6}),
            ("avif", {"quality": 50, "speed": 6}),
        ):
            filename = f"{stem}-{width}.{extension}"
            path = IMAGE_DIR / filename
            resized.save(path, **options)
            with Image.open(path) as check:
                if check.size != (width, height):
                    raise RuntimeError(f"Incorrect output dimensions: {path}")
                check.verify()
            variants.append({
                "file": filename,
                "width": width,
                "height": height,
                "format": extension,
                "bytes": path.stat().st_size,
            })
    return variants


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download", action="store_true", help="Download missing source files")
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    args = parser.parse_args()
    if not features.check("webp") or not features.check("avif"):
        raise RuntimeError("Pillow must include both WebP and AVIF encoding support")
    if args.download:
        with ThreadPoolExecutor(max_workers=4) as pool:
            tasks = [pool.submit(download_source, stem, info, args.source_dir) for stem, info in PHOTOS.items()]
            for task in tasks:
                task.result()
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {}
    opened = {}
    for stem, info in PHOTOS.items():
        source_path = args.source_dir / f"{stem}.jpg"
        if not source_path.exists():
            raise FileNotFoundError(f"Missing {source_path}; use --download")
        with Image.open(source_path) as source:
            image = ImageOps.exif_transpose(source).convert("RGB")
        opened[stem] = image
        download_url = f"https://images.unsplash.com/{info['cdnId']}?fm=jpg&q=90&w=2400&fit=max"
        manifest[stem] = {
            **info,
            "width": image.width,
            "height": image.height,
            "sourceWidth": image.width,
            "sourceHeight": image.height,
            "sourceBytes": source_path.stat().st_size,
            "sourceSha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
            "downloadUrl": download_url,
            "license": "Unsplash License",
            "licenseUrl": LICENSE_URL,
            "licenseVerifiedOn": VERIFIED_DATE,
            "widths": [width for width in WIDTHS if width <= image.width],
            "variants": save_variants(stem, image),
        }
        print(f"Prepared {stem}: {image.width} x {image.height}", flush=True)

    # A separate 5:4 hero crop avoids downloading portrait pixels hidden by CSS.
    hero = opened["hero"]
    landscape = ImageOps.fit(hero, (2000, 1600), method=Image.Resampling.LANCZOS, centering=(0.5, 0.3))
    manifest["hero-landscape"] = {
        "photographer": PHOTOS["hero"]["photographer"],
        "sourceUrl": PHOTOS["hero"]["sourceUrl"],
        "sourceStem": "hero",
        "width": landscape.width,
        "height": landscape.height,
        "crop": {"aspectRatio": "5:4", "centering": [0.5, 0.3]},
        "widths": list(WIDTHS),
        "variants": save_variants("hero-landscape", landscape),
    }
    social = ImageOps.fit(hero, (1200, 630), method=Image.Resampling.LANCZOS, centering=(0.5, 0.33))
    social_path = IMAGE_DIR / "social.jpg"
    social.save(social_path, "JPEG", quality=82, optimize=True, progressive=True)
    manifest["social"] = {
        "file": "social.jpg", "sourceStem": "hero", "width": 1200, "height": 630,
        "bytes": social_path.stat().st_size,
        "photographer": PHOTOS["hero"]["photographer"],
        "sourceUrl": PHOTOS["hero"]["sourceUrl"],
        "crop": {"aspectRatio": "1200:630", "centering": [0.5, 0.33]},
    }
    (IMAGE_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

    sheet = Image.new("RGB", (1400, 970), "#eee9e2")
    draw = ImageDraw.Draw(sheet)
    for index, (stem, image) in enumerate(opened.items()):
        thumb = image.copy()
        thumb.thumbnail((330, 430))
        x = (index % 4) * 350 + (350 - thumb.width) // 2
        y = (index // 4) * 485 + 10
        sheet.paste(thumb, (x, y))
        draw.text(((index % 4) * 350 + 14, (index // 4) * 485 + 447),
                  f"{stem} / {image.width} x {image.height}", fill="#292824")
    sheet_path = SITE_ROOT.parent / "tmp" / "maeve-photo-contact-sheet.jpg"
    sheet_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(sheet_path, quality=88)

    lines = [
        "# Local stock photo sources", "",
        "These eight Unsplash photographs were selected in V2. Their source pages and the Unsplash License were checked on **15 October 2026**. Each page identified the photograph as free to use under that license.", "",
        "[Unsplash License](https://unsplash.com/license) permits downloading, modifying and using these photographs for commercial and noncommercial purposes without required attribution. The license excludes selling unmodified images and creating a competing image collection. Attribution is retained here for provenance.", "",
        "The images are concept stock photography, not work photographed by Maeve Arden. Avoid presenting them as the photographer's own commissioned work.", "",
        "## Source mapping", "",
        "| Filename stem | Photographer | Original photo page | Original dimensions | Downloaded source dimensions |", 
        "| --- | --- | --- | --- | --- |",
    ]
    for stem, info in PHOTOS.items():
        entry = manifest[stem]
        lines.append(f"| `{stem}` | {info['photographer']} | [Unsplash photo {info['photoId']}]({info['sourceUrl']}) | {info['originalWidth']} × {info['originalHeight']} | {entry['width']} × {entry['height']} |")
    lines += ["", "Original dimensions were verified in the metadata embedded in each Unsplash photo page. Source downloads were JPEGs requested at a maximum width of 2400 pixels and quality 90, without cropping. Responsive variants retain the source aspect ratio and are never enlarged. Served variants omit camera metadata.", "",
        "## Responsive assets", "", "Files are under `assets/images/`. Each source has WebP and AVIF variants with suffixes `-480`, `-800`, `-1200` and `-1600`. WebP uses quality 74; AVIF uses quality 50. `manifest.json` records every actual width, height, byte size, download URL and source hash.", "",
        "| Stem | Width × height | WebP bytes | AVIF bytes |", "| --- | --- | ---: | ---: |"]
    for stem, entry in manifest.items():
        if "variants" not in entry:
            continue
        for width in entry["widths"]:
            variants = [variant for variant in entry["variants"] if variant["width"] == width]
            webp = next(variant for variant in variants if variant["format"] == "webp")
            avif = next(variant for variant in variants if variant["format"] == "avif")
            lines.append(f"| `{stem}` | {width} × {webp['height']} | {webp['bytes']:,} | {avif['bytes']:,} |")
    lines += ["", "## Hero and sharing crops", "",
        "`hero-landscape-{width}.webp` and `.avif` are a separate 5:4 crop of the hero, centered at 50% horizontally and 30% vertically. The crop preserves both faces and removes pixels outside the displayed composition. The full portrait hero variants remain available for portfolio use.", "",
        f"`social.jpg` is a 1200 × 630 progressive JPEG, {manifest['social']['bytes']:,} bytes, cropped from the same hero photograph for social previews.", "",
        "## Rebuilding", "", "With Pillow 12 or later built with WebP and AVIF support, run `python3 scripts/prepare-images.py --download`. This downloads missing source JPEGs into the adjacent workspace `tmp/maeve-photo-sources/` cache and regenerates the local assets, manifest, source notes and contact sheet. Source cache files are deliberately outside the deployable site.", ""]
    (SITE_ROOT / "IMAGE-SOURCES.md").write_text("\n".join(lines), encoding="utf-8")
    total = sum(path.stat().st_size for path in IMAGE_DIR.iterdir() if path.suffix in {".avif", ".webp", ".jpg"})
    print(f"Image asset total: {total:,} bytes", flush=True)
    print(f"Contact sheet: {sheet_path}", flush=True)


if __name__ == "__main__":
    main()
