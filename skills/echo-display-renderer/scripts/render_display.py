"""Render specified OLED pixels with Echo/Atlas firmware fonts and icons."""

import argparse
from functools import lru_cache
import json
from pathlib import Path
import re
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw


def source_text(path):
    """Read C data without comments that could be mistaken for bitmap values."""
    source = path.read_text(encoding="utf-8-sig")
    return re.sub(r"//[^\n]*|/\*.*?\*/", "", source, flags=re.S)


@lru_cache(maxsize=None)
def load_font(directory, size):
    """Extract bitmap bytes, descriptors, and metrics from a firmware font."""
    if size not in (8, 12, 16):
        raise ValueError(f"Unsupported firmware font: {size}")
    source = source_text(directory / f"MSS{size}.cpp")
    bitmap = source.split("Bitmaps[]", 1)[1].split("};", 1)[0]
    data = bytes(int(value, 16) for value in re.findall(r"0x([0-9a-fA-F]+)", bitmap))
    descriptors = source.split("Descriptors[]", 1)[1].split("};", 1)[0]
    metrics = [(int(w), int(o)) for w, o in re.findall(r"\{\s*(\d+),\s*(\d+)\s*\}", descriptors)]
    info = source.split(f"microsoftSansSerif_{size}ptFontInfo", 1)[1].split("{", 1)[1].split("}", 1)[0]
    fields = [field.strip() for field in info.split(",")]
    return data, metrics, int(fields[0]), ord(fields[1].strip("'")), int(fields[3]), int(fields[4])


def require_box(screen, x, y, width, height):
    """Reject clipping instead of silently losing requested display content."""
    if not all(isinstance(value, int) and not isinstance(value, bool) for value in (x, y, width, height)):
        raise ValueError("Pixel coordinates and dimensions must be integers")
    if width < 1 or height < 1 or x < 0 or y < 0 or x + width > screen.width or y + height > screen.height:
        raise ValueError(f"Box {(x, y, width, height)} exceeds display {screen.size}")


def draw_text(screen, directory, element):
    """Draw exact glyphs using the firmware's character width and spacing."""
    text = element["text"]
    if not text:
        return
    data, metrics, height, start, spacing, space = load_font(directory, element.get("font", 8))
    widths = []
    for char in text:
        if char == " ":
            widths.append(space)
        elif start <= ord(char) < start + len(metrics):
            widths.append(metrics[ord(char) - start][0])
        else:
            raise ValueError(f"Character {char!r} is absent from the firmware font")
    width = sum(widths) + spacing * (len(text) - 1)
    align = element.get("align", "center")
    if align not in ("left", "center", "right"):
        raise ValueError(f"Unknown text alignment: {align}")
    x = element.get("x", {"left": 0, "center": (screen.width - width) // 2, "right": screen.width - width}[align])
    y = element["y"]
    require_box(screen, x, y, width, height)
    inverse = bool(element.get("inverse", False))
    for index, (char, char_width) in enumerate(zip(text, widths)):
        stride = (char_width + 7) // 8
        offset = 0 if char == " " else metrics[ord(char) - start][1]
        for row in range(height):
            for column in range(char_width):
                lit = char != " " and bool(data[offset + row * stride + column // 8] & (128 >> (column % 8)))
                screen.putpixel((x + column, y + row), int(lit != inverse))
        x += char_width
        if inverse and index < len(text) - 1:
            # Draw_string fills inverse inter-character columns through y + height.
            ImageDraw.Draw(screen).rectangle((x, y, x + spacing - 1, min(y + height, screen.height - 1)), fill=1)
        x += spacing


def draw_icon(screen, directory, element):
    """Draw a named row-major bitmap from the current firmware assets."""
    name = element["name"]
    match = re.fullmatch(r"\w+_(\d+)x(\d+)", name)
    if not match:
        raise ValueError(f"Icon name must contain its dimensions: {name}")
    width, height = map(int, match.groups())
    x, y = element["x"], element["y"]
    require_box(screen, x, y, width, height)
    source = source_text(directory / "bitmaps.c")
    match = re.search(r"\b" + re.escape(name) + r"\s*\[\s*\]\s*=\s*\{([^}]+)\}", source)
    if not match:
        raise ValueError(f"Firmware icon not found: {name}")
    values = [int(value, 16) for value in re.findall(r"0x([0-9a-fA-F]+)", match.group(1))]
    stride = (width + 7) // 8
    if len(values) != stride * height:
        raise ValueError(f"Unexpected bitmap format for {name}")
    for row in range(height):
        for column in range(width):
            if values[row * stride + column // 8] & (128 >> (column % 8)):
                screen.putpixel((x + column, y + row), 1)


def draw_title(screen, directory, text):
    """Render the inverse padded title and full-width separator."""
    height = load_font(directory, 8)[2]
    ImageDraw.Draw(screen).rectangle((0, 0, screen.width - 1, height - 1), fill=0)
    draw_text(screen, directory, {"text": f" {text} ", "font": 8, "y": 0, "inverse": True})
    ImageDraw.Draw(screen).line((0, height, screen.width - 1, height), fill=1)


def render(spec, directory):
    """Render a screen specification to a native monochrome pixel grid."""
    width, height = spec.get("width", 128), spec.get("height", 64)
    if not all(isinstance(value, int) and 1 <= value <= 1024 for value in (width, height)):
        raise ValueError("Display dimensions must be integers between 1 and 1024")
    screen = Image.new("1", (width, height))
    for element in spec["elements"]:
        kind = element["type"]
        if kind == "text":
            draw_text(screen, directory, element)
        elif kind == "icon":
            draw_icon(screen, directory, element)
        elif kind == "title":
            draw_title(screen, directory, element["text"])
        elif kind == "menu":
            if screen.size != (128, 64):
                raise ValueError("The firmware menu layout requires a 128 by 64 display")
            draw_title(screen, directory, element["title"])
            small_height = load_font(directory, 8)[2]
            y1 = small_height + 4
            y2 = y1 + small_height + 2
            y3 = y2 + load_font(directory, 12)[2] + 2
            if element.get("previous") is not None:
                draw_text(screen, directory, {"text": element["previous"], "y": y1})
                draw_icon(screen, directory, {"name": "up_7x7", "x": 0, "y": 57})
            draw_text(screen, directory, {"text": element["selected"], "font": 12, "y": y2})
            if element.get("next") is not None:
                draw_text(screen, directory, {"text": element["next"], "y": y3})
                draw_icon(screen, directory, {"name": "down_7x7", "x": 121, "y": 57})
        elif kind == "line":
            x1, y1, x2, y2 = (element[key] for key in ("x1", "y1", "x2", "y2"))
            require_box(screen, min(x1, x2), min(y1, y2), abs(x2 - x1) + 1, abs(y2 - y1) + 1)
            ImageDraw.Draw(screen).line((x1, y1, x2, y2), fill=int(element.get("lit", True)))
        elif kind == "rect":
            x, y, w, h = (element[key] for key in ("x", "y", "width", "height"))
            require_box(screen, x, y, w, h)
            ImageDraw.Draw(screen).rectangle((x, y, x + w - 1, y + h - 1), fill=int(element.get("lit", True)))
        else:
            raise ValueError(f"Unknown drawing operation: {kind}")
    return screen


def save_outputs(screen, spec, output, name, scale):
    """Save a native grid, scalable pixel illustration, enlarged preview and spec."""
    output.mkdir(parents=True, exist_ok=True)
    width, height = screen.size
    screen.save(output / f"{name}-{width}x{height}.png")
    pixels = [(x, y) for y in range(height) for x in range(width) if screen.getpixel((x, y))]
    outer_width, outer_height = width + 24, height + 24
    title = escape(spec.get("title", "Device display"))
    description = escape(spec.get("description", f"{width} by {height} pixel display"))
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{outer_width * scale}" height="{outer_height * scale}" viewBox="0 0 {outer_width} {outer_height}" role="img" aria-labelledby="title desc">',
           f'<title id="title">{title}</title>', f'<desc id="desc">{description}</desc>',
           f'<rect width="{outer_width}" height="{outer_height}" fill="white"/>',
           f'<rect x="6" y="6" width="{width + 12}" height="{height + 12}" rx="8" fill="#03060b"/>',
           '<g fill="#f4f8ff" transform="translate(12 12)">']
    svg += [f'<rect x="{x + .08:g}" y="{y + .08:g}" width=".84" height=".84" rx=".12"/>' for x, y in pixels]
    svg += ['</g></svg>']
    (output / f"{name}.svg").write_text("\n".join(svg) + "\n", encoding="utf-8")
    preview = Image.new("RGB", (outer_width * scale, outer_height * scale), "white")
    draw = ImageDraw.Draw(preview)
    draw.rounded_rectangle((6 * scale, 6 * scale, (width + 18) * scale - 1, (height + 18) * scale - 1), radius=8 * scale, fill="#03060b")
    for x, y in pixels:
        left, top = (12 + x + .08) * scale, (12 + y + .08) * scale
        draw.rounded_rectangle(tuple(round(value) for value in (left, top, left + .84 * scale - 1, top + .84 * scale - 1)), radius=max(1, round(.12 * scale)), fill="#f4f8ff")
    preview.save(output / f"{name}-preview.png")
    (output / f"{name}.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    """Parse explicit inputs and create reproducible documentation assets."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--firmware-display", type=Path, required=True)
    parser.add_argument("--spec", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--scale", type=int, default=8)
    args = parser.parse_args()
    if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]*", args.name):
        parser.error("--name must be a filename stem containing letters, digits, hyphens or underscores")
    if args.scale < 2:
        parser.error("--scale must be at least 2")
    spec = json.loads(args.spec.read_text(encoding="utf-8-sig"))
    screen = render(spec, args.firmware_display.resolve())
    save_outputs(screen, spec, args.output, args.name, args.scale)
    print(f"Created {screen.width} x {screen.height} display: {args.output / args.name}")


if __name__ == "__main__":
    main()
