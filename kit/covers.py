# Three cover options for Worthy Numbers in the Worth series look (navy, heavy condensed title, one red word,
# a mark made of dots, author in spaced capitals), Milan 21 October 09:01. Each is an A5 board, 559 x 794.
import random, json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/project"
NAVY, NAVY2, RED, INK, PAPER = "#033b61", "#012b4f", "#ef402c", "#0f2236", "#ffffff"
random.seed(7)

def page(title, inner):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&amp;family=Nunito:wght@400;600;700;800;900&amp;display=swap">
<style>
body{{margin:0}}
</style>
</helmet>
{inner}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":559,"height":794}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''

def dot(x, y, r, c=RED, o=1.0):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="{c}" opacity="{o:.2f}"/>'

def bowl_svg(w=300, h=230):
    out = []
    cx, rim = w / 2, 120
    # the bowl: dots on a half ellipse grid, denser at the rim line
    for gy in range(0, 90, 10):
        for gx in range(-140, 141, 10):
            x, y = cx + gx + (5 if (gy // 10) % 2 else 0), rim + gy
            if (gx / 132) ** 2 + (gy / 86) ** 2 <= 1 and random.random() < 0.92:
                out.append(dot(x, y, 2.9 + random.random() * 0.6, RED, 0.95))
    # the granola: a dome over the rim, thinning upwards into loose particles
    for _ in range(420):
        gx = random.gauss(0, 52); gy = abs(random.gauss(0, 30))
        if abs(gx) > 125: continue
        x, y = cx + gx, rim - 4 - gy * (1 - (gx / 140) ** 2)
        far = gy / 70
        out.append(dot(x, y, max(0.9, 2.8 - far * 1.6 + random.random() * 0.5), RED, max(0.25, 1 - far * 0.7)))
    for _ in range(70):
        x, y = cx + random.gauss(0, 70), rim - 60 - random.random() * 55
        out.append(dot(x, y, 0.8 + random.random() * 1.1, RED, 0.25 + random.random() * 0.35))
    # one bright dot under the bowl, as the dot under the question mark on Worth Building
    out.append(dot(cx, rim + 112, 9, RED, 1))
    return f'<svg width="{w}" height="{h + 20}" viewBox="0 0 {w} {h + 20}" aria-hidden="true">{"".join(out)}</svg>'

GLYPH = {
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "D": ["11100", "10010", "10001", "10001", "10001", "10010", "11100"],
}
def pd_svg(w=330, h=230):
    out, cell = [], 24
    x0, y0 = (w - (5 * 2 + 2) * cell) / 2 + cell / 2, 40
    for i, ch in enumerate("PD"):
        for r, row in enumerate(GLYPH[ch]):
            for c, on in enumerate(row):
                if on == "1":
                    out.append(dot(x0 + (i * 7 + c) * cell + random.uniform(-1.2, 1.2), y0 + r * cell + random.uniform(-1.2, 1.2), 8.2 + random.random() * 1.4))
    # a halo of loose particles around the letters, thinning outwards
    for _ in range(260):
        x, y = random.uniform(0, w), random.uniform(0, h)
        inside = 0
        for i in range(2):
            lx = x0 + i * 7 * cell
            if lx - 30 < x < lx + 5 * cell + 6 and y0 - 30 < y < y0 + 7 * cell + 6: inside = 1
        if not inside and random.random() < 0.5: continue
        out.append(dot(x, y, 0.8 + random.random() * 1.6, RED, 0.18 + random.random() * 0.4))
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true">{"".join(out)}</svg>'

ROOT = f"width: 559px; height: 794px; box-sizing: border-box; padding: 52px 48px 44px; background: linear-gradient(160deg, {NAVY} 0%, {NAVY2} 100%); font-family: Nunito, ui-sans-serif, system-ui, sans-serif; color: {PAPER}; display: flex; flex-direction: column; align-items: center; text-align: center; overflow: hidden"
KICK = lambda t: f'<div style="display: flex; align-items: center; gap: 12px; font-size: 13px; font-weight: 800; letter-spacing: 0.18em; text-transform: uppercase; color: #c9d6e6"><span style="width: 34px; height: 1.5px; background: #c9d6e6"></span>{t}<span style="width: 34px; height: 1.5px; background: #c9d6e6"></span></div>'
TITLE = f'<h1 style="margin: 16px 0 0; font-family: Anton, Impact, sans-serif; font-weight: 400; font-size: 92px; line-height: 0.92; letter-spacing: 0.005em; text-transform: uppercase"><span style="display: block; color: {PAPER}">Worthy</span><span style="display: block; color: {RED}">Numbers</span></h1>'
TAG = '<p style="margin: 18px 0 0; font-size: 21px; line-height: 1.35; font-weight: 700; color: #eef3f9; text-wrap: balance">The numbers on your food, and which ones help you decide.</p>'
AUTHOR = '<div style="margin-top: auto; display: flex; flex-direction: column; align-items: center; gap: 6px"><b style="font-size: 20px; font-weight: 800; letter-spacing: 0.16em; text-transform: uppercase">Milan Stancevic</b><span style="font-size: 13.5px; font-weight: 600; color: #c9d6e6">Product builder, and the maker of Chef Mealan</span></div>'

A = f'<div style="{ROOT}">{KICK("A guide to food labels")}{TITLE}{TAG}<div style="margin-top: 22px">{bowl_svg()}</div>{AUTHOR}</div>'
C = f'<div style="{ROOT}">{KICK("A short read")}{TITLE}{TAG}<div style="margin-top: 18px">{pd_svg()}</div>{AUTHOR}</div>'

ROWS = [("The label", "100 g"), ("Nutri-Score", "A to E"), ("High protein", "20%"), ("Protein quality", "1.0"), ("GI and GL", "how fast, how much")]
rows = "".join(f'<div style="display: flex; justify-content: space-between; align-items: baseline; padding: 7px 0; border-bottom: 1.5px solid {INK}; font-size: 16px"><span style="font-weight: 700">{a}</span><b style="font-weight: 900">{b}</b></div>' for a, b in ROWS)
label = (f'<div style="margin-top: 26px; width: 100%; background: {PAPER}; color: {INK}; border-radius: 6px; padding: 14px 18px 16px; text-align: left; box-sizing: border-box">'
         f'<div style="display: flex; justify-content: space-between; align-items: baseline; padding-bottom: 6px; border-bottom: 6px solid {INK}"><b style="font-size: 20px; font-weight: 900">Numbers on your food</b><span style="font-size: 13px; font-weight: 800">and what they tell you</span></div>'
         f'{rows}'
         f'<div style="margin-top: 10px; background: {RED}; color: {PAPER}; border-radius: 4px; padding: 10px 12px; display: flex; justify-content: space-between; align-items: center"><b style="font-size: 18px; font-weight: 900">PD, for your meal</b><b style="font-family: Anton, Impact, sans-serif; font-weight: 400; font-size: 34px; line-height: 1">6.3</b></div>'
         f'</div>')
B = f'<div style="{ROOT}">{KICK("A short read")}{TITLE}{label}{AUTHOR}</div>'

for name, title, html in [("CoverA-bowl", "Worthy Numbers, cover option A", A), ("CoverB-label", "Worthy Numbers, cover option B", B), ("CoverC-pd", "Worthy Numbers, cover option C", C)]:
    open(f"{D}/{name}.dc.html", "w").write(page(title, html))

cj = json.load(open(f"{D}/canvas.json"))
for i, (n, t) in enumerate([("CoverA-bowl", "Cover A · a bowl in dots"), ("CoverB-label", "Cover B · the label"), ("CoverC-pd", "Cover C · PD in dots")]):
    f = n + ".dc.html"
    cj["boards"][f] = {"h": 794, "title": t, "w": 559, "x": 639 * i, "y": 1828 + 160}
    if f not in cj["order"]: cj["order"].append(f)
cj.setdefault("notes", {})["covers"] = {"kind": "title1", "maxW": 3115, "text": "Cover options, in the Worth series look", "w": 240, "x": 0, "y": 1828 + 40}
json.dump(cj, open(f"{D}/canvas.json", "w"), indent=2, ensure_ascii=False)
print("ok")
