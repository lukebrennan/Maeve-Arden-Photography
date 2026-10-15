---
name: Maeve Arden Photography
description: A cool, photograph-led folio with a compact modern voice.
colors:
  ground: "#dce6ea"
  paper: "#f5f7f6"
  ink: "#243239"
  muted: "#4c606b"
  blue: "#254b60"
  blue-hover: "#17394c"
  line: "#a5b7c0"
  light-line: "#6d8a9b"
  inverse-muted: "#cedde4"
  error: "#9d2926"
  viewer: "#142b38"
typography:
  display:
    fontFamily: "Geologica, sans-serif"
    fontSize: "clamp(29px,2.65vw,39px)"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-.035em"
  page-title:
    fontFamily: "Geologica, sans-serif"
    fontSize: "clamp(30px,3.1vw,44px)"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-.035em"
  headline:
    fontFamily: "Geologica, sans-serif"
    fontSize: "clamp(25px,2.4vw,34px)"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-.035em"
  title:
    fontFamily: "Geologica, sans-serif"
    fontSize: "21px"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-.025em"
  body:
    fontFamily: "Geologica, sans-serif"
    fontSize: "16px"
    fontWeight: 300
    lineHeight: 1.65
  article-body:
    fontFamily: "Geologica, sans-serif"
    fontSize: "16px"
    fontWeight: 300
    lineHeight: 1.85
  label:
    fontFamily: "Geologica, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.4
  brand:
    fontFamily: "Geologica, sans-serif"
    fontSize: "26px"
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: "-.04em"
rounded:
  square: "0"
  indicator: "50%"
spacing:
  gutter: "clamp(20px,3.6vw,64px)"
  space: "clamp(64px,7vw,112px)"
components:
  button-primary:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    padding: "12px 23px"
  button-primary-hover:
    backgroundColor: "{colors.blue-hover}"
  button-light:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.blue}"
    typography: "{typography.label}"
    padding: "12px 23px"
  button-light-hover:
    backgroundColor: "{colors.ground}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.blue}"
    typography: "{typography.label}"
    padding: "12px 23px"
  button-outline-hover:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.paper}"
  input:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "11px"
    width: "100%"
  navigation-link:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
  collection-option:
    padding: "12px"
  collection-option-selected:
    backgroundColor: "{colors.ground}"
  pricing-band:
    padding: "42px 30px"
  pricing-band-featured:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.paper}"
  enquiry-panel:
    backgroundColor: "{colors.paper}"
    padding: "32px"
---

# Design System: Maeve Arden Photography

## Overview

**Creative North Star: "Folded atlas"**

A cool, open folio gives photographs the largest and most varied surfaces. A single modern sans serif keeps the interface compact, while uneven image groupings, practical margins and quiet rules create an authored rhythm. The full-name wordmark feels professional without competing with the work.

This system uses flat fields of lake blue, cool paper and deep ink blue. It supports browsing, reading and an enquiry preview through modest headings, visible links and restrained controls. Photography supplies the warmth and texture; the interface stays clear and spare.

**Key Characteristics:**

- Cool tonal surfaces with deep blue actions.
- One locally served type family in normal case.
- Unequal image groupings with deliberate subject preservation.
- Flat, square controls and thin dividing rules.
- User-directed changes with brief, optional motion.

## Colors

The palette is cool and low in saturation, with deep blue providing both action emphasis and full-width tonal contrast. The frontmatter is the value authority; names below describe its application.

### Primary

- **Ink blue** (`blue`): primary actions, selected filters, checked controls, selection color and the experience section. The featured collection also uses this field with paper text.
- **Deep action blue** (`blue-hover`): primary button hover treatment.

### Neutral

- **Lake blue** (`ground`): the default page, sticky header, selected collection option and enquiry summary.
- **Cool paper** (`paper`): enquiry panel, closing invitation and inverse foregrounds; also the light button on a blue section.
- **Dark ink** (`ink`): default reading text and headings.
- **Slate** (`muted`): supporting copy, image captions, breadcrumbs and form metadata.
- **Cool rule** (`line`): borders and separators on light surfaces.
- **Blue rule** (`light-line`): separators within the dark experience section.
- **Pale blue text** (`inverse-muted`): secondary text on that blue field.
- **Validation red** (`error`): invalid field borders, field messages and the error summary. It is a functional state rather than a decorative accent.
- **Viewer ink** (`viewer`): the full-screen photo viewer, keeping uncropped photography distinct from the page.

**The Tonal Field Rule.** Use the established blue and paper fields to separate major content; recurring cards and content bands stay flat.

## Typography

**Display Font:** Geologica, with sans-serif fallback.

**Body Font:** Geologica, with sans-serif fallback.

**Character:** A single variable sans serif supplies calm, contemporary type. The local normal-style WOFF2 supports weights (100–900); the interface uses light body copy and moderate heading and selection weights. Emphasis remains upright.

### Hierarchy

- **Display:** the compact home heading uses the `display` role with a short measure (21ch). It becomes (30px / 1.17) at widths up to (600px), and (40px) from (1600px).
- **Page title:** the `page-title` role introduces inner pages with a measure of roughly (24ch), or (25ch) for article headings. It becomes (31px) on small screens.
- **Headline:** the `headline` role anchors sections. Article subheads use (26px), reducing to (24px) on small screens; component headings vary by their local content density.
- **Title:** the `title` role is the base for smaller headings. Photo captions use smaller titles (16px), collection names use (25px), and journal titles use (22–23px).
- **Body:** light weight, comfortable leading and a default maximum measure (70ch). Supporting sections use (14–15px). Article paragraphs use the more generous `article-body` leading and become (15px) on small screens.
- **Label:** primary button and text-link labels use (14px). Navigation uses (13px); captions and supporting metadata use (11–13px). These are ordinary labels, not headings above headings.
- **Brand:** the full-name wordmark uses the `brand` role. It reduces to (24px) below (900px); its descriptive second line remains (11px), weight (350), with tracking (.04em).

**The One Family Rule.** Build hierarchy with Geologica's size, weight and spacing; keep display emphasis upright and normal case.

## Layout

The shared container has a maximum width (1504px), centered within the fluid `gutter` spacing. Main sections use the fluid `space` spacing. Thin rules and generous image boundaries separate content without adding generic boxes. Repeated gaps are local to the layout rather than a fabricated universal spacing scale.

Unequal columns recur in stories, the journal and image-and-copy sections. Reading content has a bounded measure (70ch); desktop articles pair it with a sticky contents column. Journal cards have no enclosing fill, border or shadow. Home journal links put the title before the category and reading-time metadata.

The main responsive thresholds are:

- At (1100px) and below, navigation gaps and folio columns tighten; enquiry fields collapse to one column and panel padding reduces (25px).
- At (900px) and below, the desktop navigation becomes a menu dialog; the header shortens (80px), and folio place controls move above its two photographs. Pricing changes from three content columns to two.
- At (600px) and below, the header is (77px), most split sections stack, article contents stop sticking, and story images form one column. The folio shows one main photograph; the secondary photograph is hidden. Gallery columns reduce to one, while the collection selector remains a compact two-column choice. The enquiry aside follows the form and its photograph is hidden.
- At (1600px) and above, only the home display heading receives its documented size adjustment.

Desktop gallery photographs retain their native proportions in two columns (52px gap), with the second tile offset (60px). They become a single column without the offset on small screens. Story galleries start with a full-width photograph, then two unevenly positioned photographs; the first is contained within a maximum height (780px), not forced into a cropped frame.

## Elevation & Depth

The system is flat at rest. Tonal fields, scale and borders establish hierarchy. The full-screen viewer and navigation dialog use native modal behavior; the navigation backdrop is a translucent deep ink field (`rgb(13 31 42/.65)`). No recurring content card uses a shadow.

### Shadow Vocabulary

- **Mobile enquiry** (`0 5px 20px rgb(0 0 0/.17)`): the small, fixed enquiry action on screens up to (600px). This is the only interface shadow. Its position above scrolling photography explains the separation.

**The Flat Content Rule.** Reserve the existing shadow for the floating mobile enquiry action; ordinary panels, journal items and pricing remain flat.

## Shapes

Interface panels, buttons, rules and image frames use square geometry. Text fields explicitly use the `square` corner token. Place-selection indicators use the circular `indicator` token; they are functional selected-state marks. Thin strokes (1px) define controls and dividers; selected gallery filters and invalid inputs use stronger strokes (2px).

The header and footer use the full-name wordmark. The separate favicon draws an unmistakable MA in a small cool-blue asset; its rounded asset boundary is not a card or button radius. UI icons are small inline SVG strokes.

## Components

### Buttons and links

Compact, direct actions use a solid tonal rectangle.

- **Primary:** ink-blue fill and paper text, minimum height (48px), with `button-primary` padding. Hover uses `button-primary-hover` over a short background transition (180ms).
- **Light:** paper fill on a blue field; hover changes to lake blue. The closing invitation deliberately presents the normal primary color assignment even though its markup shares the light-button modifier.
- **Outline:** transparent fill, blue text and a blue border; hover fills blue and reverses the text.
- **Small:** header actions use a minimum height (44px) and padding (10px 20px).
- **Text:** underlined labels, a minimum height (44px), and an underline offset (5px). The next-story link includes the words “Next story” in the link and underlines its heading with an offset (7px).
- **Focus:** interactive elements use a visible outline (2px solid currentColor), offset (5px). Disabled buttons use reduced opacity (.6) and the waiting cursor.

### Navigation

The sticky lake-blue header has a thin bottom rule. Desktop links use normal case and show an underline on hover or the current page. Below the navigation breakpoint, a labelled menu button opens a native dialog aligned to the right, with a maximum width (460px), large links (26px) and inline SVG close control. Escape, explicit close and focus return are preserved. The no-JavaScript fallback keeps the ordinary navigation links available.

On small screens a fixed “Check your date” action can appear near the bottom edge. Its visibility responds to the practical enquiry link, closing invitation and footer, avoiding a duplicate action when one of those is in view.

### Place index and folio

This home-specific signature groups a large landscape image, a narrower portrait and a small place index. Selected places use a heavier blue label and filled circle. Choices are user-triggered; there is no autoplay. The implementation decodes the next pair before replacing it, indicates loading with muted controls and `aria-busy`, then updates both photographs, the caption and story link together.

The scene-change animation lasts (300ms) with `cubic-bezier(.16,1,.3,1)`, using a slight clip reveal and brightness change. Reduced-motion preferences remove it, all other animations and transitions, and smooth scrolling. Keep image-specific subject positioning: the London photograph uses the bottom of its image (`50% 100%`), while the celebration uses an upper framing (`50% 30%`). These are photo treatments, not global crop defaults.

### Gallery and image viewer

Category filters are flat text controls with a minimum height (50px), reducing to (44px) on small screens. The selected category has a blue underline (2px) and weight (500), with `aria-pressed` carrying the state. Filtering changes only visibility, and the photograph count updates in a live status.

Tiles preserve natural image ratios and expose a small paper-backed expand control. Their image viewer contains the entire image with `object-fit: contain`; it provides visible previous, next and close controls, arrow-key navigation, a count and photographer credit. Closing returns focus to the original photograph. Without the enhanced viewer, image links still lead to image files.

### Pricing bands

Collections are contiguous flat rows separated by rules. Desktop composition puts description, price and included coverage in separate columns. The featured collection uses the blue field; its light button provides contrast. At small widths the price stays beside the name, followed by the description, included coverage and action. Tabular numerals keep price information orderly. Preserve these bands rather than inheriting an unrelated equal-card layout.

### Inputs and enquiry preview

Fields are transparent, square and outlined with the cool rule, with a minimum height (48px). Labels remain visible above them. Mobile text entry uses (16px) type; placeholders use Slate at full opacity. Focus uses the shared outline. Invalid inputs receive a stronger red border and a nearby error; a linked error summary focuses the first failing field. The flexible-date choice disables and dims the date field (.55 opacity) and changes its required-state wording.

The paper enquiry panel carries the demo notice, two-step progress and form. Selected collection options use a blue border and lake-blue fill; their minimum height is (78px). The form preserves the selected collection from collection links. Step changes move focus to the new heading. Valid details produce an editable, browser-only preview, with a copy action and visible success or failure status. Keep clear that the preview sends, saves and reserves nothing.

### Journal, details and utility content

Journal items use unboxed photographs and titles; home article metadata follows the title. Native expandable questions use thin row rules and a small rotating open-state mark. Credits, privacy and error pages reuse the same bounded text, headings and links without adding another visual theme.

## Do's and Don'ts

### Do:

- Do use the cool tonal fields, compact Geologica hierarchy and visible underlined links.
- Do preserve the subject when a photograph is cropped, and retain native ratios in the gallery and contained images in the viewer.
- Do make scene changes user-triggered and honor reduced-motion preferences.
- Do keep selected, focus, invalid, disabled and loading states distinguishable through more than copy alone.
- Do preserve the full-name identity, clear MA favicon and unobtrusive fictional-brand and enquiry-demo disclosures.
- Do edit the maintained stylesheet and generator when extending the site; the served CSS and HTML are generated outputs, and the public export excludes development contracts.

### Don't:

- Don't introduce oversized or italic display typography, a second display family, or a boxed monogram in the header.
- Don't turn the native gallery photographs into equal-height crops or the collection bands into generic floating cards.
- Don't remove visible focus, image credits, current navigation states or the enquiry preview's operating limits.
- Don't promote hidden legacy eyebrow markup, decorative numbering or text-arrow characters into new component conventions.

Not canonized: hidden legacy eyebrow and numbering hooks, plus text-arrow characters in a few utility and form links, are not a reusable visual vocabulary. This documentation records the frozen implementation; it does not repair UI source.
