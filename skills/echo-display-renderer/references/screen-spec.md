# Screen specification

The JSON document has integer `width` and `height` (default 128 and 64), an accessible `title` and `description`, and an ordered `elements` array. Coordinates are native pixels, with origin at the upper left. Elements draw in array order.

Supported elements:

| Type | Fields | Meaning |
| --- | --- | --- |
| `menu` | `title`, `selected`, optional `previous`, `next` | Firmware options layout, including header and arrows. Omit previous/next at list boundaries. Requires 128 × 64. |
| `title` | `text` | Centered inverse 8 pt title, padded with spaces, with full-width separator. |
| `text` | `text`, `y`, optional `font` (8, 12, 16; default 8), `x`, `align`, `inverse` | Explicit x or `align`: `center` (default), `left`, `right`. The entire glyph box must fit. |
| `icon` | `name`, `x`, `y` | Named row-major bitmap in `bitmaps.c`, such as `up_7x7`, `down_7x7`, `bat100_16x9`, `wifi_12x9`. Width/height come from the name. Verify names in source. |
| `line` | `x1`, `y1`, `x2`, `y2`, optional `lit` (default true) | Inclusive line endpoints. |
| `rect` | `x`, `y`, `width`, `height`, optional `lit` (default true) | Filled rectangle; useful for highlights and clearing areas. |

Example of a different screen using explicit elements (confirm its content and positions against the requested photo):

```json
{
  "width": 128,
  "height": 64,
  "title": "Echo 2 home screen",
  "description": "Pink MLS, continuous 2.7 s at 60 dBA, battery and Wi-Fi indicators.",
  "elements": [
    {"type": "icon", "name": "bat100_16x9", "x": 0, "y": 0},
    {"type": "icon", "name": "wifi_12x9", "x": 116, "y": 0},
    {"type": "text", "text": "Pink MLS", "font": 16, "y": 12},
    {"type": "text", "text": "C 2.7s 60dB", "font": 8, "y": 36},
    {"type": "icon", "name": "menu_10x10", "x": 59, "y": 54}
  ]
}
```

The renderer produces `<name>-128x64.png` (or the selected native dimensions), `<name>.svg`, `<name>-preview.png`, and `<name>.json`. The last file is a copy of the specification. `--scale` changes the enlarged preview scale (default 8); it does not alter the native display dimensions or pixel coordinates.

SVG and preview use a 12-pixel margin around the active grid, with a rounded bezel extending six pixels outside it. Neither margin nor bezel counts toward the 128 × 64 display resolution.
