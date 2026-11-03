"""Recreate the photographed Echo menu using its firmware bitmap fonts."""

from pathlib import Path
import re

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]  # Documentation repository.
DISPLAY = ROOT.parent / "Echo2Atlas/source/components/display"  # Firmware assets.
OUTPUT = ROOT / "docs/assets/echo"  # Manual image assets.


def font(size):
    """Read the firmware's row-major glyphs and character metrics."""
    source = (DISPLAY / f"MSS{size}.cpp").read_text()
    source = re.sub(r"//[^\n]*", "", source)
    bitmap = source.split("Bitmaps[]", 1)[1].split("};", 1)[0]
    data = bytes(int(value, 16) for value in re.findall(r"0x([0-9a-fA-F]+)", bitmap))
    descriptors = source.split("Descriptors[]", 1)[1].split("};", 1)[0]
    metrics = [(int(w), int(o)) for w, o in re.findall(r"\{\s*(\d+),\s*(\d+)\s*\}", descriptors)]
    return data, metrics, 12 if size == 8 else 17, 1 if size == 8 else 2


def centered(screen, text, y, size, inverse=False):
    """Place text using the same centering, spacing and glyphs as the device."""
    data, metrics, height, spacing = font(size)
    widths = [2 if char == " " else metrics[ord(char) - 33][0] for char in text]
    x = (128 - sum(widths) - spacing * (len(text) - 1)) // 2
    for index, (char, width) in enumerate(zip(text, widths)):
        stride = (width + 7) // 8
        offset = 0 if char == " " else metrics[ord(char) - 33][1]
        for row in range(height):
            for column in range(width):
                lit = char != " " and bool(data[offset + row * stride + column // 8] & (128 >> (column % 8)))
                screen.putpixel((x + column, y + row), int(lit != inverse))
        x += width
        if inverse and index < len(text) - 1:
            ImageDraw.Draw(screen).rectangle((x, y, x + spacing - 1, y + height), fill=1)
        x += spacing


def main():
    """Write a native 128 by 64 bitmap and matching scalable manual rendering."""
    screen = Image.new("1", (128, 64))
    centered(screen, " Signal Type ", 0, 8, inverse=True)
    ImageDraw.Draw(screen).line((0, 12, 127, 12), fill=1)
    centered(screen, "Pink MLS", 16, 8)
    centered(screen, "ESweep", 30, 12)
    centered(screen, "STIPA", 49, 8)
    for x, name in ((0, "up"), (121, "down")):
        source = (DISPLAY / "bitmaps.c").read_text()
        values = source.split(f"{name}_7x7 []", 1)[1].split("};", 1)[0]
        rows = [int(value, 16) for value in re.findall(r"0x([0-9a-fA-F]+)", values)]
        for row, bits in enumerate(rows):
            for column in range(7):
                if bits & (128 >> column):
                    screen.putpixel((x + column, 57 + row), 1)
    screen.save(OUTPUT / "signal-type-128x64.png")
    pixels = [(x, y) for y in range(64) for x in range(128) if screen.getpixel((x, y))]
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="1216" height="704" viewBox="0 0 152 88" role="img" aria-labelledby="title desc">',
           '<title id="title">Echo 2 signal type menu</title>',
           '<desc id="desc">128 by 64 pixel display. Signal Type heading, Pink MLS above selected ESweep, STIPA below, and navigation arrows.</desc>',
           '<rect width="152" height="88" fill="white"/>',
           '<rect x="6" y="6" width="140" height="76" rx="8" fill="#03060b"/>',
           '<g fill="#f4f8ff" transform="translate(12 12)">']
    svg += [f'<rect x="{x + .08:g}" y="{y + .08:g}" width=".84" height=".84" rx=".12"/>' for x, y in pixels]
    svg += ['</g></svg>']
    (OUTPUT / "signal-type.svg").write_text("\n".join(svg) + "\n", encoding="utf-8")
    preview = Image.new("RGB", (1216, 704), "white")
    draw = ImageDraw.Draw(preview)
    draw.rounded_rectangle((48, 48, 1167, 655), radius=64, fill="#03060b")
    for x, y in pixels:
        draw.rounded_rectangle((96 + x * 8 + 1, 96 + y * 8 + 1, 96 + x * 8 + 6, 96 + y * 8 + 6), radius=1, fill="#f4f8ff")
    preview.save(OUTPUT / "signal-type-preview.png")


if __name__ == "__main__":
    main()
