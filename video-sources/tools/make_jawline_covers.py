import sys
from covers import *

# ---------- V1: JAWLINE MAGIC (sunset purple, profile shot) ----------
c = background("fr_profile.png", "#2b0a4a", "#c2185b", "#2a0845", "#ffb36b", shift=330).convert("RGBA")
d = ImageDraw.Draw(c)
crown(d, 80, 110, 80)
paste(c, text_layer("JAWLINE", MARKER, 200, YEL, 12, angle=5), 30, 160)
paste(c, brush_band(600, 130, (255, 222, 0, 255), seed=3).rotate(5, expand=True), 90, 420)
paste(c, text_layer("MAGIC", MARKER, 180, "white", 12, angle=5), 140, 385)
inset(c, f"{LIB}/before_after/ba_full_face_beige_TOP_HOOK.png", 640, 660, 380, 250, angle=4, crop_y="bottom")
checklist(c, ["DEFINE YOUR JAWLINE", "LIFT YOUR FACE", "REMOVE DOUBLE CHIN", "YOUTHFUL LOOK"], 30, 660, size=40, gap=66, angle=4)
arrows(d, [[(610, 1640), (630, 1560), (670, 1470)], [(700, 1660), (720, 1580), (760, 1500)]])
badge(c, "SUBSCRIBE", 540, 1720)
c.convert("RGB").save("cover_v1_jawline_magic.jpg", quality=92)

# ---------- V2: 4 EXERCISES (neon blue/pink, front shot + own before/after) ----------
c = background("fr_front.png", "#0b0530", "#3a0ca3", "#14002e", "#ff5ec4", shift=330).convert("RGBA")
d = ImageDraw.Draw(c)
paste(c, text_layer("4", MARKER, 330, YEL, 14, angle=-4), 30, 70)
paste(c, text_layer("EXERCISES", MARKER, 150, YEL, 12, angle=-4), 230, 130)
paste(c, text_layer("FOR A SHARP", MARKER, 105, "white", 10, angle=-4), 240, 300)
paste(c, brush_band(860, 150, (255, 222, 0, 255), seed=7).rotate(-4, expand=True), 90, 420)
paste(c, text_layer("JAWLINE", MARKER, 165, "black", 0, angle=-4, shadow=False), 180, 410)
inset(c, f"{LIB}/before_after/ba_self_jawline_HOOK.jpg", 300, 640, 480, 384, angle=0, crop_y="bottom")
checklist(c, ["STRONGER JAWLINE", "NO DOUBLE CHIN", "BETTER PROFILE"], 560, 1250, size=40, gap=66, angle=-5)
badge(c, "SUBSCRIBE", 540, 1700, bg=(255, 0, 110))
c.convert("RGB").save("cover_v2_4_exercises.jpg", quality=92)

# ---------- V3: clean & bold (warm, pencil shot) ----------
c = background("fr_pencil.png", "#1a0f00", "#5a2d0c", "#1b0d02", "#ffcf8a", shift=200).convert("RGBA")
d = ImageDraw.Draw(c)
crown(d, 470, 110, 110, w=8)
paste(c, text_layer("SHARP", ANTON, 230, YEL, 10), 540, 230, "mt")
paste(c, text_layer("JAWLINE", ANTON, 230, "white", 10), 540, 470, "mt")
paste(c, brush_band(700, 90, (229, 57, 53, 255), seed=11), 190, 760)
paste(c, text_layer("PENCIL TRICK", MARKER, 72, "white", 6, shadow=False), 540, 758, "mt")
inset(c, f"{LIB}/jaw/jaw_12_anatomy_muscles.jpg", 60, 1150, 330, 330, angle=-5)
badge(c, "SUBSCRIBE", 540, 1700)
c.convert("RGB").save("cover_v3_sharp_jawline.jpg", quality=92)
