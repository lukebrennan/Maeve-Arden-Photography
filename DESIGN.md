---
name: Maeve Arden Photography
description: A cream-and-charcoal photographic folio with refined editorial display
  type.
colors:
  ground: "#f7f5ef"
  paper: "#fdfbf7"
  ink: "#302f2c"
  muted: "#67625b"
  charcoal: "#343330"
  charcoal-hover: "#22221f"
  line: "#c9c1b5"
  inverse-line: "#827b70"
  inverse-muted: "#e1dbd1"
  control-line: "#8a8379"
  error: "#9d2926"
  viewer: "#22221f"
typography:
  display:
    fontFamily: Bodoni Moda, Georgia, serif
    fontSize: clamp(36px,3.25vw,46px)
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: "-.015em"
  page-title:
    fontFamily: Bodoni Moda, Georgia, serif
    fontSize: clamp(34px,3.3vw,46px)
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: "-.015em"
  headline:
    fontFamily: Bodoni Moda, Georgia, serif
    fontSize: clamp(29px,2.6vw,37px)
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: "-.015em"
  title:
    fontFamily: Bodoni Moda, Georgia, serif
    fontSize: 25px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: "-.015em"
  body:
    fontFamily: Geologica, sans-serif
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.65
  article-body:
    fontFamily: Geologica, sans-serif
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.85
  label:
    fontFamily: Geologica, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
  brand:
    fontFamily: Bodoni Moda, Georgia, serif
    fontSize: 33px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "-.025em"
rounded:
  square: '0'
spacing:
  gutter: clamp(20px,3.6vw,64px)
  space: clamp(64px,7vw,112px)
components:
  button-primary:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    padding: 12px 23px
  button-primary-hover:
    backgroundColor: "{colors.charcoal-hover}"
  button-light:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.charcoal}"
    typography: "{typography.label}"
    padding: 12px 23px
  button-light-hover:
    backgroundColor: "{colors.ground}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.charcoal}"
    typography: "{typography.label}"
    padding: 12px 23px
  button-outline-hover:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.paper}"
  input:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: 11px
    width: 100%
  navigation-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
  collection-option:
    padding: 12px
  collection-option-selected:
    backgroundColor: "{colors.ground}"
  pricing-band:
    padding: 42px 30px
  pricing-band-featured:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.paper}"
  enquiry-panel:
    backgroundColor: "{colors.paper}"
    padding: 32px
  scene-preview:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    padding: 9px 0
  photo-open-action:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    padding: 9px 12px
  photo-open-action-hover:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.paper}"
---

# Design System: Maeve Arden Photography

## Overview

**Creative North Star: "Folded atlas"**

An open photographic folio in warm cream and dark charcoal. The user explicitly restored this palette and asked to regain an elegant, premium feel. Bodoni Moda provides the full-name wordmark and editorial headings; compact Geologica keeps reading, navigation and forms clear. Unequal photographs, precise captions and practical margins remain the defining layout.

**Key Characteristics:**

- Warm cream and ivory surfaces with dark grey actions and sections.
- Refined upright serif display type paired with a restrained sans serif UI.
- Unequal image groupings and subject-aware crops.
- Flat square controls, thin warm-grey rules and visible underlined links.
- Explicit photographic preview choices, manual photo browsing and brief, optional motion.

## Colors

The frontmatter is the value authority. Cream (`ground`) is the page and header; ivory (`paper`) supports the enquiry and closing invitation. Charcoal (`charcoal`) owns primary actions, active states, the experience section and the featured collection. Its hover role is darker. Dark ink (`ink`) is the reading foreground; warm grey (`muted`) supports captions and metadata.

Use the light `line` for decorative separators. Form fields and collection choices use the darker `control-line`, preserving a 3:1 boundary against paper. Dark sections use `inverse-line` and `inverse-muted`; errors retain `error`. The photo viewer uses `viewer`. No blue or sage belongs to this approved palette.

Body text on cream is 12.28:1, muted text on cream 5.54:1, paper on charcoal 12.22:1, inverse secondary text on charcoal 9.18:1, and form borders on paper 3.63:1.

**The Tonal Field Rule.** Separate major content with cream, ivory and charcoal fields. Keep recurring content and pricing bands flat.

## Typography

**Display Font:** Bodoni Moda, Georgia, serif.

**Body Font:** Geologica, sans-serif.

Bodoni Moda is a local 14,556-byte Latin WOFF2, normal Roman 400, using the source's 11pt optical cut. It is static: do not request other weights or synthesize italic. Geologica remains a local 24,964-byte Latin variable WOFF2 with weights 100–900. Both use `font-display: swap`, are preloaded, and retain their SIL OFL licenses under assets/fonts.

### Hierarchy

- **Home display:** 36–46px fluid desktop scale, line-height 1.12; 26–32px on mobile. Keep the explicit two-part sentence compact above the photographs.
- **Page titles:** 34–46px desktop scale, 32px on mobile; line-height 1.15.
- **Section headlines:** 29–37px base scale; supporting local headings use 28–30px.
- **Content titles:** serif journal titles use 26–28px and collection names 31px (29px mobile).
- **Wordmark:** outlined Bodoni Moda 400 and a Geologica 400 Photography descriptor. The primary SVG is 450×96, rendered in a 260×56px slot, or 238×54px on phones. Screens up to 360px use the 360×96 name-only wordmark in a 190–228×54px slot. Descriptor size stays at least 11px.
- **Body:** Geologica 300, 16px / 1.65, with supporting passages at 14–15px. Article text uses 16px / 1.85, 15px on mobile, bounded to 70ch.
- **UI:** Geologica for navigation, labels, buttons, forms and metadata. Small functional headings in the gallery, image viewer, menu, enquiry panel and experience steps remain sans serif. The enquiry panel headings are 25px, 23px mobile.
- **Tracking:** serif headings use -.015em; small UI roles retain their local tracking. Display emphasis stays upright.

**The Two Role Rule.** Use the serif for editorial voice and the sans serif for reading and operation. Keep headings restrained so photography leads.

## Layout

The shared container has a maximum width (1504px), centered within the fluid `gutter` spacing. Main sections use the fluid `space` spacing. Thin rules and generous image boundaries separate content without adding generic boxes. Repeated gaps are local to the layout rather than a fabricated universal spacing scale.

Unequal columns recur in stories, the journal and image-and-copy sections. Reading content has a bounded measure (70ch); desktop articles pair it with a sticky contents column. Journal cards have no enclosing fill, border or shadow. Home journal links put the title before the category and reading-time metadata.

The main responsive thresholds are:

- At (1100px) and below, navigation gaps and folio columns tighten; enquiry fields collapse to one column and panel padding reduces (25px).
- At (900px) and below, the desktop navigation becomes a menu dialog and the header shortens (80px). Folio thumbnail choices become a horizontal row below its two photographs. Pricing changes from three content columns to two; photo-rail items occupy (38%) of the rail width.
- At (600px) and below, the header is (77px), most split sections stack, article contents stop sticking, and story images form one column. The folio shows one main photograph, with paging beneath it and three full-width thumbnail rows below; the secondary photograph is hidden. The main photograph uses a landscape ratio (1.3). Photo-rail items occupy (76%) of the rail width, leaving a clear glimpse of the next image. Gallery columns reduce to one, while the collection selector remains a compact two-column choice. The enquiry aside follows the form and its photograph is hidden.
- At (1600px) and above, only the home display heading receives its documented size adjustment.

Desktop portfolio photographs retain their native proportions in two columns (52px gap), with the second tile offset (60px). They become a single column without the offset on small screens. Story galleries start with a full-width photograph, then paired photographs with an offset third image; the first is contained within a maximum height (780px), not forced into a cropped frame. The home rail is a separate, horizontal photographic sequence with snap alignment; it does not change the portfolio gallery’s native-ratio layout.

## Elevation & Depth

The system is flat at rest. Tonal fields, scale and borders establish hierarchy. The full-screen viewer and navigation dialog use native modal behavior; the navigation backdrop is a translucent deep ink field (`rgb(24 23 21/.65)`). No recurring content card uses a shadow.

### Shadow Vocabulary

- **Mobile enquiry** (`0 5px 20px rgb(0 0 0/.17)`): the small, fixed enquiry action on screens up to (600px). This is the only interface shadow. Its position above scrolling photography explains the separation.

**The Flat Content Rule.** Reserve the existing shadow for the floating mobile enquiry action; ordinary panels, journal items and pricing remain flat.

## Shapes

Interface panels, buttons, rules and image frames use square geometry. Text fields explicitly use the `square` corner token. Thin strokes (1px) define controls and dividers; selected thumbnail rows, selected gallery filters and invalid inputs use stronger strokes (2px). Thumbnail rows use authored SVG arrows rather than circular selection indicators.

The header and footer use the serif MA plus full-name SVG lockup. The M and A remain separate for immediate recognition. Narrow screens use the name-only wordmark. The favicon uses the same MA with stronger hairlines on cream. Logo lettering is outlined, with no external font or raster dependency. UI icons are small inline SVG strokes.

## Components

### Buttons and links

Compact, direct actions use a solid tonal rectangle.

- **Primary:** charcoal fill and paper text, minimum height (48px), with `button-primary` padding. Hover uses `button-primary-hover` over a short background transition (180ms).
- **Light:** paper fill on a charcoal field; hover changes to cream. The closing invitation deliberately presents the normal primary color assignment even though its markup shares the light-button modifier.
- **Outline:** transparent fill, charcoal text and a charcoal border; hover fills charcoal and reverses the text.
- **Small:** header actions use a minimum height (44px) and padding (10px 20px).
- **Text:** underlined labels, a minimum height (44px), and an underline offset (5px). The next-story link includes the words “Next story” in the link and underlines its heading with an offset (7px).
- **Focus:** interactive elements use a visible outline (2px solid currentColor), offset (5px). Disabled buttons use reduced opacity (.6) and the waiting cursor.

### Navigation

The sticky cream header has a thin bottom rule. Desktop links use normal case and show an underline on hover or the current page. Below the navigation breakpoint, a labelled menu button opens a native dialog aligned to the right, with a maximum width (460px), large links (26px) and inline SVG close control. Escape, explicit close and focus return are preserved. The no-JavaScript fallback keeps the ordinary navigation links available.

On small screens a fixed “Check your date” action can appear near the bottom edge. It stays hidden while the home folio or photo rail is in view, keeping photograph controls clear, and while the closing invitation or footer is visible.

### Photographic previews and folio

This home-specific signature pairs a large landscape image with a narrower portrait and three explicit photographic thumbnail choices. Each button combines a real thumbnail, a descriptive name, supporting category and authored SVG arrow. Desktop choices form a narrow vertical index; tablet choices sit in a row beneath the photographs; phone choices become full-width rows beneath the main image. The selected row uses a charcoal bottom rule (2px), a stronger label (550) and a rotated arrow. Hover adds the paper field; focus uses the shared visible outline.

The three choices are “All the feeling,” “Room to breathe” and “Just the two of you.” Previous and next selection buttons beneath the main photograph use (44px) square controls, with a tabular (1 / 3) count and live feedback. Both control methods select the same wrapping sequence; there is no autoplay. Changing a selection decodes the next responsive image pair before replacing both photographs, the caption and story destination. Loading dims the thumbnail choices (.65), sets `aria-busy` and announces “Loading photographs…”; success announces the selected scene, and failure leaves the current photographs in place with a retry message. Rapid requests only apply the latest selection. Without JavaScript, the initial photography and direct story links remain available.

The scene-change animation lasts (300ms) with `cubic-bezier(.16,1,.3,1)`, using a slight clip reveal and brightness change. Reduced-motion preferences remove it, all other animations and transitions, and smooth scrolling. Current portrait selection uses a deliberate bridge-photo crop (`50% 55%`). Individual photograph crops remain local treatments rather than a global default.

### Home photographic rail

Six photographs form a manually scrollable sequence. Desktop items occupy (29%) of the rail with gaps (28px); tablet and phone widths follow the Layout rules. Each print uses a portrait-shaped frame (.82 aspect ratio), a caption and a visible “View photograph” action with an authored expand SVG. Hover or keyboard focus changes that action from paper to charcoal with inverse text. The rail is a labelled, keyboard-focusable region and retains its native horizontal scrollbar, touch and trackpad scrolling, and snap alignment.

Previous and next controls move by one print plus its gap. They use (44px) square targets; the relevant end control is disabled at each boundary with opacity (.35). Scripted scrolling is smooth except under reduced-motion preferences, where it is instant. The six initially lazy images are warmed only as the rail approaches the viewport (400px margin); the observer then disconnects. This does not preload the full image library during the opening view.

### Portfolio and image viewer

The portfolio curates fourteen photographs from a seventeen-source library. Category filters are flat text controls with a minimum height (50px), reducing to (44px) on small screens. The selected category has a charcoal underline (2px) and weight (500), with `aria-pressed` carrying the state. Filtering changes visibility, and the photograph count updates in a live status. Each of the three visual story pages presents five photographs.

Portfolio tiles preserve natural image ratios and expose a small paper-backed expand control. The shared viewer opens from the home rail, portfolio or story images and contains the entire photograph with `object-fit: contain`. It provides visible previous, next and close controls, a live count and a photographer-credit link with the existing authored SVG arrow. Navigation wraps through the currently visible photographs; a one-image set disables previous and next. Native modal behavior and the keyboard trap preserve focus, Escape closes, left/right arrow keys move between images, and closing returns focus to the opening photograph. Without the enhanced viewer, image links still lead to image files.

On touch screens the image area accepts a single-finger horizontal swipe only when travel exceeds (60px) and is more than (1.5) times its vertical travel; it preserves vertical panning and pinch zoom. Credit text and destination update from the local provenance manifest, with the credits page as fallback. A late credit response cannot overwrite the currently displayed photograph’s credit.

### Pricing bands

Collections are contiguous flat rows separated by rules. Desktop composition puts description, price and included coverage in separate columns. The featured collection uses the charcoal field; its light button provides contrast. At small widths the price stays beside the name, followed by the description, included coverage and action. Tabular numerals keep price information orderly. Preserve these bands rather than inheriting an unrelated equal-card layout.

### Inputs and enquiry preview

Fields are transparent, square and outlined with the control rule, with a minimum height (48px). Labels remain visible above them. Mobile text entry uses (16px) type; placeholders use warm grey at full opacity. Focus uses the shared outline. Invalid inputs receive a stronger red border and a nearby error; a linked error summary focuses the first failing field. The flexible-date choice disables and dims the date field (.55 opacity) and changes its required-state wording.

The paper enquiry panel carries the demo notice, two-step progress and form. Selected collection options use a charcoal border and cream fill; their minimum height is (78px). The form preserves the selected collection from collection links. Step changes move focus to the new heading. Valid details produce an editable, browser-only preview, with a copy action and visible success or failure status. Keep clear that the preview sends, saves and reserves nothing.

### Journal, details and utility content

Journal items use unboxed photographs and titles; home article metadata follows the title. Native expandable questions use thin row rules and a small rotating open-state mark. Credits, privacy and error pages reuse the same bounded text, headings and links without adding another visual theme.

## Do's and Don'ts

### Do:

- Do use the cream and charcoal fields, refined Bodoni Moda headings, compact Geologica UI and visible underlined links.
- Do preserve the subject when a photograph is cropped, and retain native ratios in the gallery and contained images in the viewer.
- Do keep photographic choices and rail controls explicit, make scene changes user-triggered and honor reduced-motion preferences.
- Do keep selected, focus, invalid, disabled and loading states distinguishable through more than copy alone.
- Do preserve the full-name identity, clear MA favicon and unobtrusive fictional-brand and enquiry-demo disclosures.
- Do edit the maintained stylesheet and generator when extending the site; the served CSS and HTML are generated outputs, and the public export excludes development contracts.

### Don't:

- Don't introduce oversized or italic display typography, another display family, or a boxed monogram in the header.
- Don't turn the native gallery photographs into equal-height crops or the collection bands into generic floating cards.
- Don't remove visible focus, image credits, current navigation states or the enquiry preview's operating limits.
- Don't promote hidden legacy eyebrow markup, decorative numbering or text-arrow characters into new component conventions.

Not canonized: hidden legacy eyebrow and numbering hooks, plus text-arrow characters in a few utility and form links, are not a reusable visual vocabulary. This documentation records the frozen implementation; it does not repair UI source.

## Logo assets

The primary and reversed SVG lockups, narrow wordmark, monogram and matching favicon live under assets/icons. Bodoni Moda and Geologica glyphs are converted to paths, preserving the supplied typefaces and local OFL licenses. scripts/brand-assets.py recreates these committed assets with development-only fontTools and Brotli; ordinary site generation needs neither dependency. The small favicon is optically strengthened. Keep its M/A separation and avoid stretching the SVG. The 404 embeds the narrow vector directly, preserving recovery branding at nested URLs.
