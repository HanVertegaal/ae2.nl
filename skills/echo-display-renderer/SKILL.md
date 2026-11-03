---
name: echo-display-renderer
description: Recreate photographs of Echo 2, Atlas, or related firmware OLED screens as accurate pixel-grid illustrations for manuals, using the device bitmap fonts and icons. Use for display screenshots and menu renderings, rather than photographs of the whole product.
---

# Echo display renderer

Create a clean rendering of the screen shown in the user's photograph. Use the existing manual illustration style unless the user requests another appearance. Reconstruct the screen from firmware assets; avoid generative lettering or resampling a perspective photograph when exact bitmap fonts are available.

## Workflow

1. Inspect the photograph and an existing manual rendering. Record visible text, selected item, icons and display dimensions. Echo 2 uses a **128 × 64** active pixel grid; the bezel and white margin are outside that grid.
2. Locate the matching firmware checkout and verify its assets and layout. The usual local directory is `~/Documents/Projects/Echo2Atlas/source/components/display`. Read `MSS8.cpp`, `MSS12.cpp`, `MSS16.cpp`, `bitmaps.c`, and the relevant UI implementation as needed. Photographs remain the authority for the requested screen state when current firmware has different wording or options. Ask only if a material detail cannot be resolved.
3. Write a JSON screen specification using [references/screen-spec.md](references/screen-spec.md). Use [assets/signal-type.json](assets/signal-type.json) for the accepted Signal Type example. For other layouts, use positioned text, firmware icons, lines and rectangles. Keep the specification with the deliverables so the image is reproducible.
4. Run the bundled renderer with explicit paths:

   ```powershell
   python <skill-dir>/scripts/render_display.py --firmware-display <firmware>/components/display --spec <screen.json> --output <output-directory> --name <screen-name>
   ```

   Requires Python and Pillow. Do not install packages unless needed; use the available Python environment. Fonts and icons are read from the checkout rather than bundled snapshots.
5. Verify that the native PNG has the required dimensions, inspect the enlarged PNG against the photograph, and check the SVG renders correctly before describing it as visually verified. Check text, selection, centering, header, bottom arrows and clipping. A photo can have perspective, glow or uneven brightness; preserve the lit pixel pattern instead of reproducing those artifacts.
6. Deliver the enlarged preview inline, with links to the SVG and native PNG. The SVG contains individual pixel shapes and needs no installed fonts. Keep the existing overview image unless the user asks to replace or insert an image. Do not modify firmware to create an illustration.

## Layout and appearance

- The `menu` operation follows `Options::Display` and `Display::DrawTitle`: padded inverse 8 pt title at y=0, separator at y=12, previous item 8 pt at y=16, selection 12 pt at y=30, next item 8 pt at y=49, and 7 × 7 arrows at the bottom corners. Read current source if the layout has changed.
- Point labels are firmware font identifiers, not CSS or physical point sizes: 8 pt is 12 pixels high, 12 pt is 17, and 16 pt is 22 in the current assets. Use the actual metrics loaded by the script.
- Preserve UI spelling and capitalization, including `Pink MLS` and `ESweep`. Infer obscured detail from source, but do not silently substitute a different screen state.
- Default illustration: white pixels, nearly black rounded bezel, white outer margin, no glow. The raw PNG is exactly the active display size; the SVG and preview include surrounding framing.
- The helper deliberately fails for unknown glyphs, icons and invalid coordinates. Resolve the source/layout discrepancy rather than silently replacing characters. Add narrowly scoped support if a later screen uses another bitmap format or font.
