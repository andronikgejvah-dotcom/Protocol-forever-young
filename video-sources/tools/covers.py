import random, math, sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

FD = os.environ["FONTS"]
MARKER = f"{FD}/fontsource-permanent-marker-5.3.0/files/permanent-marker-latin-400-normal.woff"
BANG = f"{FD}/fontsource-bangers-5.3.0/files/bangers-latin-400-normal.woff"
ANTON = f"{FD}/fontsource-anton-5.3.0/files/anton-latin-400-normal.woff"
LIB = os.environ["LIB"]
W, H = 1080, 1920
YEL = (255, 222, 0)


def hex2(c):
    return np.array([int(c[i:i + 2], 16) for i in (1, 3, 5)], float)


def grade(img, dark, light, amt=0.55, sat=1.15):
    a = np.asarray(img.convert("RGB"), float)
    lum = (a @ [0.299, 0.587, 0.114])[..., None] / 255
    gm = hex2(dark) * (1 - lum) + hex2(light) * lum
    out = a * (1 - amt) + gm * amt
    out = (out - 128) * 1.12 + 128
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


def vgrad(w, h, top, bottom):
    t = np.linspace(0, 1, h)[:, None, None]
    g = hex2(top) * (1 - t) + hex2(bottom) * t
    return Image.fromarray(np.repeat(g, w, 1).astype(np.uint8))


def background(frame, top, mid, dark, light, shift=260, scale=1.0):
    bg = vgrad(W, H, top, mid)
    ph = Image.open(frame).convert("RGB")
    ph = ph.resize((int(W * scale), int(H * scale)))
    ph = grade(ph, dark, light)
    # fade photo top edge into gradient
    m = Image.new("L", ph.size, 255)
    md = ImageDraw.Draw(m)
    for y in range(420):
        md.line([(0, y), (ph.size[0], y)], fill=int(255 * y / 420))
    bg.paste(ph, ((W - ph.size[0]) // 2, shift), m)
    # vignette
    v = Image.new("L", (W, H), 0)
    ImageDraw.Draw(v).ellipse([-300, -200, W + 300, H + 300], fill=255)
    v = v.filter(ImageFilter.GaussianBlur(160))
    dark_img = Image.new("RGB", (W, H), (10, 0, 20))
    return Image.composite(bg, dark_img, v)


def brush_band(w, h, color, seed=1):
    random.seed(seed)
    img = Image.new("RGBA", (w + 60, h + 60), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    pts = []
    for x in range(0, w + 1, 18):
        pts.append((30 + x, 30 + random.randint(0, 18)))
    for x in range(w, -1, -18):
        pts.append((30 + x, 30 + h - random.randint(0, 18)))
    d.polygon(pts, fill=color)
    for _ in range(14):  # streaks at ends
        y = random.randint(30, 30 + h)
        x0 = random.choice([random.randint(0, 50), w - random.randint(0, 40)])
        d.line([(x0, y), (x0 + random.randint(40, 110), y + random.randint(-4, 4))], fill=color, width=random.randint(3, 8))
    return img


def text_layer(txt, font, size, fill, stroke=10, angle=0, shadow=True):
    f = ImageFont.truetype(font, size)
    l, t, r, b = f.getbbox(txt, stroke_width=stroke)
    img = Image.new("RGBA", (r - l + 40, b - t + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if shadow:
        d.text((20 - l + 8, 20 - t + 10), txt, font=f, fill=(0, 0, 0, 170), stroke_width=stroke, stroke_fill=(0, 0, 0, 170))
    d.text((20 - l, 20 - t), txt, font=f, fill=fill, stroke_width=stroke, stroke_fill="black")
    return img.rotate(angle, expand=True, resample=Image.BICUBIC)


def paste(base, layer, x, y, anchor="lt"):
    if anchor == "mt":
        x -= layer.size[0] // 2
    base.alpha_composite(layer, (int(x), int(y)))


def crown(d, x, y, s, color=YEL, w=6):
    pts = [(x, y + s), (x, y + s * 0.3), (x + s * 0.35, y + s * 0.65), (x + s * 0.6, y), (x + s * 0.85, y + s * 0.65), (x + s * 1.2, y + s * 0.3), (x + s * 1.2, y + s)]
    d.line(pts + [(x, y + s)], fill=color, width=w, joint="curve")
    for px, py in [pts[1], pts[3], pts[5]]:
        d.ellipse([px - 7, py - 7, px + 7, py + 7], fill=color)


def checklist(base, items, x, y, size=50, gap=78, font=MARKER, angle=0):
    layer = Image.new("RGBA", (620, gap * len(items) + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    f = ImageFont.truetype(font, size)
    for i, it in enumerate(items):
        yy = 10 + i * gap
        d.rectangle([4, yy + 8, 54, yy + 58], outline=YEL, width=6)
        d.line([(12, yy + 30), (28, yy + 52), (66, yy - 2)], fill=YEL, width=9, joint="curve")
        d.text((84, yy), it, font=f, fill=YEL, stroke_width=4, stroke_fill="black")
    paste(base, layer.rotate(angle, expand=True, resample=Image.BICUBIC), x, y)


def inset(base, path, x, y, w, h, angle=-3, border=10, crop_y="center", label=None):
    im = Image.open(path).convert("RGB")
    im = ImageOps.fit(im, (w, h), centering=(0.5, {"top": 0.0, "center": 0.5, "bottom": 1.0}[crop_y]))
    fr = Image.new("RGBA", (w + 2 * border, h + 2 * border), (255, 255, 255, 255))
    fr.paste(im, (border, border))
    if label:
        d = ImageDraw.Draw(fr)
        f = ImageFont.truetype(MARKER, 40)
        d.text((fr.size[0] // 2, fr.size[1] - 18), label, font=f, anchor="mb", fill=YEL, stroke_width=4, stroke_fill="black")
    sh = Image.new("RGBA", (fr.size[0] + 60, fr.size[1] + 60), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle([30, 40, 30 + fr.size[0], 40 + fr.size[1]], fill=(0, 0, 0, 160))
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    sh.alpha_composite(fr, (30, 30))
    paste(base, sh.rotate(angle, expand=True, resample=Image.BICUBIC), x - 30, y - 30)


def badge(base, txt, x, y, size=78, bg=(229, 57, 53), angle=-4):
    f = ImageFont.truetype(ANTON, size)
    l, t, r, b = f.getbbox(txt)
    pad = 30
    img = Image.new("RGBA", (r - l + 2 * pad, b - t + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, img.size[0] - 1, img.size[1] - 1], radius=24, fill=bg)
    d.text((pad - l, pad - t), txt, font=f, fill="white")
    paste(base, img.rotate(angle, expand=True, resample=Image.BICUBIC), x, y, "mt")


def arrows(d, pts_list, color="white", w=9):
    for pts in pts_list:
        d.line(pts, fill=color, width=w, joint="curve")
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        a = math.atan2(y2 - y1, x2 - x1)
        for da in (2.5, -2.5):
            d.line([(x2, y2), (x2 + 34 * math.cos(a + da), y2 + 34 * math.sin(a + da))], fill=color, width=w)
