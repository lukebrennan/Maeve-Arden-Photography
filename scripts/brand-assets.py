#!/usr/bin/env python3
"""Regenerate the outlined Maeve Arden brand assets from the local font files.

Development-only dependency: fonttools and brotli. The website and its build do
not invoke this script or need those packages. Run from any working directory:
    python scripts/brand-assets.py
"""

from html import escape
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "icons"
INK = "#343330"
IVORY = "#f7f5ef"


def number(value):
    return f"{value:.3f}".rstrip("0").rstrip(".") or "0"


def load_font(filename, weight=None):
    font = TTFont(ROOT / "assets" / "fonts" / filename)
    if weight is not None and "fvar" in font:
        font = instantiateVariableFont(font, {"wght": weight}, inplace=True)
    return font


def kerning(font, left, right):
    if "GPOS" not in font:
        return 0
    gpos = font["GPOS"].table
    indices = sorted({i for feature in gpos.FeatureList.FeatureRecord
                      if feature.FeatureTag == "kern"
                      for i in feature.Feature.LookupListIndex})
    adjustment = 0
    for index in indices:
        lookup = gpos.LookupList.Lookup[index]
        for sub in lookup.SubTable:
            kind = lookup.LookupType
            if kind == 9:
                kind, sub = sub.ExtensionLookupType, sub.ExtSubTable
            if kind != 2 or left not in sub.Coverage.glyphs:
                continue
            value = None
            if sub.Format == 1:
                pairs = sub.PairSet[sub.Coverage.glyphs.index(left)]
                value = next((pair.Value1 for pair in pairs.PairValueRecord
                              if pair.SecondGlyph == right), None)
            elif sub.Format == 2:
                first = sub.ClassDef1.classDefs.get(left, 0)
                second = sub.ClassDef2.classDefs.get(right, 0)
                value = sub.Class1Record[first].Class2Record[second].Value1
            if value is not None:
                adjustment += getattr(value, "XAdvance", 0)
                break
    return adjustment


def text_width(font, text, size, tracking=0):
    cmap = font.getBestCmap()
    glyphs = [cmap[ord(char)] for char in text]
    units = sum(font["hmtx"].metrics[glyph][0] for glyph in glyphs)
    units += sum(kerning(font, a, b) for a, b in zip(glyphs, glyphs[1:]))
    return units * size / font["head"].unitsPerEm + tracking * (len(text) - 1)


def text_path(font, text, size, x, baseline, tracking=0):
    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()
    scale = size / font["head"].unitsPerEm
    pen = SVGPathPen(glyph_set, ntos=number)
    previous = None
    for char in text:
        glyph = cmap[ord(char)]
        if previous is not None:
            x += kerning(font, previous, glyph) * scale
        glyph_set[glyph].draw(TransformPen(pen, (scale, 0, 0, -scale, x, baseline)))
        x += font["hmtx"].metrics[glyph][0] * scale + tracking
        previous = glyph
    return pen.getCommands()


def glyph_bounds(font, char):
    glyph_set = font.getGlyphSet()
    pen = BoundsPen(glyph_set)
    glyph_set[font.getBestCmap()[ord(char)]].draw(pen)
    return pen.bounds


def monogram(font, size, x, baseline, gap=4.8):
    # Keep both complete glyphs. The M's two vertical stems and two diagonals
    # remain distinct; the A's counter and crossbar are never overlaid.
    scale = size / font["head"].unitsPerEm
    m = glyph_bounds(font, "M")
    a = glyph_bounds(font, "A")
    m_width = (m[2] - m[0]) * scale
    a_width = (a[2] - a[0]) * scale
    paths = [text_path(font, "M", size, x - m[0] * scale, baseline),
             text_path(font, "A", size, x + m_width + gap - a[0] * scale, baseline)]
    return paths, m_width + gap + a_width


def svg(viewbox, title, body, fill=INK):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" '
            f'role="img" aria-labelledby="brand-title" fill="{fill}">\n'
            f'  <title id="brand-title">{escape(title)}</title>\n'
            '  <desc>Custom Maeve Arden brand artwork drawn as vector paths. '
            'No external font required.</desc>\n'
            f'{body}\n</svg>\n')


def path_group(paths, label, extra=""):
    return (f'  <g aria-label="{escape(label)}"{extra}>\n' +
            "\n".join(f'    <path d="{path}"/>' for path in paths) + "\n  </g>")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    display = load_font("bodoni-moda-latin.woff2")
    sans = load_font("geologica-latin.woff2", 400)
    name = "Maeve Arden"
    name_size = 327 / text_width(display, name, 1)
    descriptor_size = 21.2
    descriptor_tracking = 1.65
    descriptor_width = text_width(sans, "PHOTOGRAPHY", descriptor_size,
                                  descriptor_tracking)

    mark_paths, mark_width = monogram(display, 59, 6, 70.5)
    full = path_group(mark_paths, "M A") + "\n"
    full += path_group([text_path(display, name, name_size, 117, 51)], name) + "\n"
    full += path_group([text_path(sans, "PHOTOGRAPHY", descriptor_size,
                                  117 + (327 - descriptor_width) / 2, 82,
                                  descriptor_tracking)], "Photography")
    (OUT / "maeve-arden-logo.svg").write_text(
        svg("0 0 450 96", "Maeve Arden Photography", full))
    (OUT / "maeve-arden-logo-reversed.svg").write_text(
        svg("0 0 450 96", "Maeve Arden Photography", full, IVORY))

    narrow = path_group([text_path(display, name, name_size, 16.5, 51)], name) + "\n"
    narrow += path_group([text_path(sans, "PHOTOGRAPHY", descriptor_size,
                                    (360 - descriptor_width) / 2, 82,
                                    descriptor_tracking)], "Photography")
    (OUT / "maeve-arden-wordmark.svg").write_text(
        svg("0 0 360 96", "Maeve Arden Photography", narrow))

    # A square artboard gives the matching unframed pair breathing room.
    square_scale = 144 / mark_width
    square_paths, _ = monogram(display, 59 * square_scale, 8,
                              80 + (1529 - 20) * 59 * square_scale / 4000,
                              4.8 * square_scale)
    square = svg("0 0 160 160", "Maeve Arden MA monogram",
                 path_group(square_paths, "M A"))
    (OUT / "maeve-arden-monogram.svg").write_text(square)
    (OUT / "logo-mark.svg").write_text(square)

    # The small-icon treatment keeps the same pair and optically strengthens
    # its hairlines. The cream ground is intrinsic only to the favicon.
    icon_scale = 43 / mark_width
    icon_paths, _ = monogram(display, 59 * icon_scale, 2.5,
                            24 + (1529 - 20) * 59 * icon_scale / 4000,
                            4.8 * icon_scale)
    icon = f'  <rect width="48" height="48" rx="4" fill="{IVORY}"/>\n'
    icon += path_group(icon_paths, "M A",
                       f' stroke="{INK}" stroke-width="1.25" stroke-linejoin="round"')
    (OUT / "favicon.svg").write_text(
        svg("0 0 48 48", "Maeve Arden MA monogram", icon))

    print(f"Name outline size: {name_size:.3f}; descriptor: {descriptor_size}; "
          f"full-logo descriptor at 235px: {descriptor_size * 235 / 450:.3f}px")
    for filename in ("maeve-arden-logo.svg", "maeve-arden-logo-reversed.svg",
                     "maeve-arden-wordmark.svg", "maeve-arden-monogram.svg",
                     "logo-mark.svg", "favicon.svg"):
        path = OUT / filename
        print(f"{filename}: {path.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
