# Validation record

Checked on 15 October 2026.

## Automated checks

- Static verifier: 15 pages; internal links and fragments; sitemap coverage; unique IDs; one H1 per page; required metadata; valid JSON-LD; local responsive source paths; 72 AVIF/WebP variants with recorded byte sizes.
- JavaScript syntax check passed.
- Whitespace/diff check passed.
- Generated output is deterministic; rebuilding produces the committed HTML, sitemap, manifest and compact stylesheet.
- All 73 served photograph files (including the JPEG social image) were decoded and their dimensions verified during asset preparation.

## Browser checks

The Codex in-app browser checked all 15 pages at widths 320, 768, 1024 and 1440 pixels: 60 combinations passed with no horizontal overflow, missing H1 or broken visible loaded image. A lazy-loaded image inside the hidden mobile enquiry aside was excluded from image-failure detection because it is intentionally not requested.

Interaction checks passed:

- Portfolio filtering to Places shows three photographs.
- Opening a photograph uses only the currently visible filtered selection.
- The ArrowRight key advances the image and title.
- Escape closes the gallery, clears the body scroll lock and restores focus to the opening image.
- The mobile menu opens and closes; Shift+Tab from the first control cycles to the last control, and Escape restores focus to the menu button.
- An enquiry opened with collection=complete selects The Complete.
- Missing dates and past dates produce inline errors and a focusable error summary.
- The unset-date option disables the date input and allows the enquiry to continue.
- Missing names and emails, and an invalid email address, produce specific validation errors.
- The enquiry preview displays literal user input safely as text, including angle brackets.
- Editing the preview preserves entered names and plans.
- Native FAQ disclosures open and show their answers.

## Limits

This records browser and static checks, not an independent WCAG conformance audit, a conversion-rate experiment, a Lighthouse measurement or field Core Web Vitals data. Clipboard copying is implemented with a browser permission-aware fallback; the browser interaction check did not overwrite the user's clipboard.

The form is a browser-only demonstration. It does not send enquiries, check calendar availability or reserve dates. GitHub Pages deployment is a separate step after review.

## October 2026 visual redesign

Replaced the cream/sage serif identity with a lake-blue photographic folio and local variable Geologica. All fifteen pages retain their content, source credits and primary functions. The home place selector changes the photo pairing, caption and story link only on visitor input; reduced-motion preferences disable its short reveal. The header uses the full name, removing the ambiguous monogram from navigation.

Build verification: all 15 pages, links/fragments, unique metadata, valid JSON-LD, sitemap and 72 image variants pass the static checks; JavaScript syntax passes. Captured home at 1440, 390 and the user's 1280 pixel width; seven supporting page classes at 1440 and 390. DOM checks found no horizontal overflow or missing in-viewport images in those captures. Tested London selector, collection preselection, required-date guidance, flexible date, names/email enquiry preview, gallery details filter, viewer and close.

One design detector run identified undersized functional text, journal heading hierarchy and initial viewer image source; these were corrected. Padding reports refer to full-width sections with inset containers and are passed to the independent finish reviewer. Local images carry creator/source/license metadata with unchanged decoded pixels. The clean dist export excludes development briefs and tooling.

No Lighthouse score, field Core Web Vitals result or real booking availability is claimed. Enquiry remains an explicitly labelled browser-only preview.

Independent Impeccable finish review: **ship**. All 19 final captures were valid. The review verified type, colour, photo framing, the place selector, responsive adaptation, pricing/enquiry honesty, next-story navigation and journal hierarchy. Three material findings were corrected and rescored resolved. Browser keyboard checks also confirmed mobile-menu Escape, gallery arrow-key progression and focus return after Escape.
