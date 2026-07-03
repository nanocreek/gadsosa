#!/usr/bin/env python3
"""Generate favicon.svg and favicon.ico for gadsosa.com.

Design: a refined "G" monogram inside a rounded-square badge. The mark adapts
to the user's color-scheme preference in the SVG; the ICO uses the light-mode
version (dark badge, light mark) for broad compatibility.
"""

from pathlib import Path
from PIL import Image, ImageDraw

# Design tokens (must match the site's visual system)
INK = "#0d1621"
PAPER = "#f6f7f8"

# Canvas geometry (relative to a 128x128 viewBox)
SIZE = 128
RADIUS_BG = 26          # rounded-square corner radius
R_ARC = 40              # arc radius for the G bowl
R_ARC_END_X = 92        # x of arc end-points (cx + R_ARC * cos(45°))
R_ARC_TOP_Y = 36        # y of top arc end-point (cy - R_ARC * sin(45°))
R_ARC_BOTTOM_Y = 92     # y of bottom arc end-point
BAR_X = 58              # crossbar inner edge (left of center for a stronger G)
BAR_RIGHT = 92          # crossbar outer edge
BAR_TOP = 54            # crossbar top
BAR_BOTTOM = 74         # crossbar bottom


def svg() -> str:
    """Return the SVG favicon source."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}">
  <rect class="bg" width="{SIZE}" height="{SIZE}" rx="{RADIUS_BG}" fill="{INK}"/>
  <path class="fg" fill="{PAPER}" d="M {R_ARC_END_X} {R_ARC_TOP_Y} A {R_ARC} {R_ARC} 0 1 1 {R_ARC_END_X} {R_ARC_BOTTOM_Y} Z"/>
  <rect class="fg" x="{BAR_X}" y="{BAR_TOP}" width="{BAR_RIGHT - BAR_X}" height="{BAR_BOTTOM - BAR_TOP}" rx="2" fill="{PAPER}"/>
  <style>
    @media (prefers-color-scheme: dark) {{
      .bg {{ fill: {PAPER}; }}
      .fg {{ fill: {INK}; }}
    }}
  </style>
</svg>
"""


def render(size: int, bg: str, fg: str) -> Image.Image:
    """Render the favicon mark at ``size`` x ``size`` pixels."""
    img = Image.new("RGBA", (size, size), bg)
    draw = ImageDraw.Draw(img)

    s = size / SIZE
    cx = cy = size // 2
    r = int(R_ARC * s)
    bg_px = ImageColor(bg)
    fg_px = ImageColor(fg)

    # Rounded-square badge background
    radius_bg = int(RADIUS_BG * s)
    draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius_bg, fill=bg_px)

    # G bowl: filled sector from 45° to 315° (Pillow angles, clockwise long arc)
    bbox = [cx - r, cy - r, cx + r, cy + r]
    draw.pieslice(bbox, start=45, end=315, fill=fg_px)

    # Crossbar
    x1 = int(BAR_X * s)
    y1 = int(BAR_TOP * s)
    x2 = int(BAR_RIGHT * s)
    y2 = int(BAR_BOTTOM * s)
    radius_bar = max(1, int(2 * s))
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius_bar, fill=fg_px)

    return img


def ImageColor(color: str) -> tuple:
    """Convert #rrggbb to an RGBA tuple."""
    color = color.lstrip("#")
    return tuple(int(color[i:i + 2], 16) for i in (0, 2, 4)) + (255,)


def main() -> None:
    public = Path(__file__).resolve().parents[1] / "public"
    public.mkdir(parents=True, exist_ok=True)

    # SVG
    (public / "favicon.svg").write_text(svg(), encoding="utf-8")

    # ICO with multiple sizes for crisp rendering in tabs/bookmarks.
    # Pillow's ICO writer filters sizes against the first image's dimensions,
    # so the largest frame must come first.
    sizes = [16, 32, 48]
    frames = [render(s, INK, PAPER).convert("RGBA") for s in sorted(sizes, reverse=True)]
    frames[0].save(
        public / "favicon.ico",
        format="ICO",
        sizes=[(s, s) for s in sizes],
        append_images=frames[1:],
    )

    print(f"Wrote {public / 'favicon.svg'}")
    print(f"Wrote {public / 'favicon.ico'} ({', '.join(map(str, sizes))}px)")


if __name__ == "__main__":
    main()
