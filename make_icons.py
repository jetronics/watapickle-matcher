"""Builds Android launcher icons from icon.png. Run after `npx cap add android`."""
import os, sys
from PIL import Image, ImageDraw

RES = sys.argv[1] if len(sys.argv) > 1 else "android/app/src/main/res"
BG = (6, 16, 29, 255)
logo = Image.open("icon.png").convert("RGBA")
dens = {"mdpi": 1, "hdpi": 1.5, "xhdpi": 2, "xxhdpi": 3, "xxxhdpi": 4}

for d, f in dens.items():
    folder = os.path.join(RES, "mipmap-" + d)
    os.makedirs(folder, exist_ok=True)
    s = int(48 * f)
    logo.resize((s, s), Image.LANCZOS).save(os.path.join(folder, "ic_launcher.png"))
    big = s * 4
    c = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    ImageDraw.Draw(c).ellipse((0, 0, big - 1, big - 1), fill=BG)
    inner = int(big * 0.86)
    l = logo.resize((inner, inner), Image.LANCZOS)
    c.paste(l, ((big - inner) // 2, (big - inner) // 2), l)
    c.resize((s, s), Image.LANCZOS).save(os.path.join(folder, "ic_launcher_round.png"))
    S = int(108 * f)
    fg = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    li = int(S * 60 / 108)
    l = logo.resize((li, li), Image.LANCZOS)
    fg.paste(l, ((S - li) // 2, (S - li) // 2), l)
    fg.save(os.path.join(folder, "ic_launcher_foreground.png"))

xml = '''<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
  <background android:drawable="@color/ic_launcher_background"/>
  <foreground android:drawable="@mipmap/ic_launcher_foreground"/>
</adaptive-icon>
'''
v26 = os.path.join(RES, "mipmap-anydpi-v26")
os.makedirs(v26, exist_ok=True)
for n in ("ic_launcher.xml", "ic_launcher_round.xml"):
    open(os.path.join(v26, n), "w").write(xml)
vals = os.path.join(RES, "values")
os.makedirs(vals, exist_ok=True)
open(os.path.join(vals, "ic_launcher_background.xml"), "w").write(
    '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n  <color name="ic_launcher_background">#06101D</color>\n</resources>\n')
print("icons written to", RES)
