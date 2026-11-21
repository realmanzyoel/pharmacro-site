"""Shared helpers from the Investor Labs design system (copied for the PharmaCRO site).

Content modules (c_*.py) do:  from lib import *   and then call page(...).
Every helper returns an HTML string. Animation is driven by assets/site.js (adds .in to .reveal elements).
"""
import os, re, html, math

OUT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://pharma.eliteleadgrow.com"
MAIL = "contact@eliteleadgrow.com"  # forms open the visitor's mail client addressed here; change if wrong
DISC = ("Corporate information on this site is not an offer of securities. Private investment materials are available "
        "only to verified investors in jurisdictions where access is legally permitted. Simulations, venture stages and "
        "the assistant examples shown are illustrative. Industry background is general context, not company data.")
BG = "Background on this page is general industry context, not company data, a forecast or an offer."

# ---------- basic helpers ----------
def P(*t): return "".join(f"<p>{x}</p>" for x in t)
def H2(t): return f"<h2>{t}</h2>"
def H3(t): return f"<h3>{t}</h3>"
def UL(items): return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
def OL(items): return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"
def CALL(t): return f'<div class="call">{t}</div>'
def T(head, rows, cls=""):
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tw reveal"><table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'
def KV(rows): return '<dl class="kv reveal">' + "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows) + "</dl>"
def GRID(cards, n=3):
    return f'<div class="grid g{n}">' + "".join(
        f'<div class="card tilt reveal" style="--i:{i}"><h3>{t}</h3><p>{b}</p>' + (f'<p><a href="{l}">{lt} &rsaquo;</a></p>' if l else "") + "</div>"
        for i, (t, b, l, lt) in enumerate(cards)) + "</div>"
def FLOW(steps):
    return '<ol class="flow">' + "".join(f'<li class="reveal" style="--i:{i}"><b>{a}</b><span>{b}</span></li>' for i, (a, b) in enumerate(steps)) + "</ol>"
def STATS(rows):
    return '<div class="stats">' + "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in rows) + "</div>"
def FAQ(qa): return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in qa)
def BTN(t, l, o=False): return f'<a class="btn{" o" if o else ""}" href="{l}">{t}</a>'

# ---------- images ----------
# name -> alt text. Files live in img/<name>.jpg  (all from Unsplash, free licence; illustrative only)
from img_meta import IMG_ALT
ALT = dict(IMG_ALT)
ALT.update({
 "pharma-lab": "Scientists working in a modern laboratory", "pharma-pipette": "A scientist pipetting samples into a rack of vials",
 "pharma-chalk": "A scientist testing a sample in front of a chemistry chalkboard", "pharma-team": "A laboratory team reviewing notes at a bench",
 "pharma-plate": "A pipette filling a multi-well sample plate", "pharma-scopes": "Rows of laboratory microscopes on a bench",
 "pharma-scope": "A laboratory microscope next to a computer", "pharma-duo": "Two scientists in lab coats discussing results",
 "pharma-tubes": "Colourful liquids in a rack of test tubes", "data-laptop": "A laptop showing an analytics dashboard",
 "data-dash": "A dark analytics dashboard with performance charts", "data-charts": "Reviewing charts on a laptop",
 "group-team": "A team meeting in a modern office", "lead-1": "Portrait of an older man with glasses in a green shirt", "lead-2": "Portrait of a smiling woman in a striped blazer",
 "lead-3": "Portrait of a man with glasses and folded arms", "lead-4": "Portrait of a smiling woman with dark hair", "lead-5": "Portrait of a man with glasses in a dark blazer", "corp-skyline": "A city skyline at sunset across the water",
})
IMGS = {}
def alt(n): return html.escape(ALT.get(n, n))

def IMG(name, cap=None, cls=""):
    c = cap if cap is not None else ALT[name]
    return f'<figure class="fig reveal {cls}"><img src="/img/{name}.jpg" alt="{alt(name)}" loading="lazy"><figcaption>{c}</figcaption></figure>'

def SPLIT(name, inner, flip=False, cap=None):
    """Photo beside text. inner = HTML (headings, paragraphs, lists...)."""
    return (f'<div class="split{" flip" if flip else ""}"><div class="sp-img reveal"><img class="px" data-px="0.06" src="/img/{name}.jpg" alt="{alt(name)}" loading="lazy">'
            f'<span>{cap if cap is not None else ALT[name]}</span></div><div class="sp-tx reveal" style="--i:1">{inner}</div></div>')

def GALLERY(names, caps=None):
    cells = "".join(f'<figure class="gl reveal" style="--i:{i}"><img src="/img/{n}.jpg" alt="{alt(n)}" loading="lazy"><figcaption>{(caps[i] if caps else ALT[n])}</figcaption></figure>' for i, n in enumerate(names))
    return f'<div class="gallery">{cells}</div>'

def STRIP(names):
    """Auto-scrolling photo marquee."""
    row = "".join(f'<img src="/img/{n}.jpg" alt="{alt(n)}" loading="lazy">' for n in names)
    return f'<div class="strip" aria-hidden="false"><div>{row}{row}</div></div>'

def BAND(name, h, text="", btn=None):
    """Full-width parallax photo band with overlaid heading."""
    b = f'<p>{btn}</p>' if btn else ""
    return (f'<section class="band reveal"><img class="px" data-px="0.12" src="/img/{name}.jpg" alt="{alt(name)}" loading="lazy">'
            f'<div class="bt"><h2>{h}</h2>' + (f"<p>{text}</p>" if text else "") + f'{b}</div></section>')

def MOSAIC(items):
    """items: (img, title, text, link)."""
    return '<div class="mos">' + "".join(
        f'<a href="{l}" class="reveal" style="--i:{i}"><img src="/img/{n}.jpg" alt="{alt(n)}" loading="lazy"><span><b>{t}</b>{d}</span></a>'
        for i, (n, t, d, l) in enumerate(items)) + "</div>"

def QUOTE(text, who=""):
    return f'<blockquote class="bq reveal"><p>{text}</p>' + (f"<cite>{who}</cite>" if who else "") + "</blockquote>"

# ---------- animated stats & charts ----------
PAL = ["var(--ac)", "#2f6bff", "#ff9500", "#ff2d95", "#7a2bff", "#00c8ff", "#7ddf00", "#ffd400"]
_num = re.compile(r"^([^\d\-]*)(\d[\d,]*\.?\d*)(.*)$")

def KPI(items):
    """items: (display_text, label). The first number in display_text counts up when scrolled into view."""
    out = []
    for i, (v, l) in enumerate(items):
        m = _num.match(v)
        if m:
            pre, num, suf = m.groups(); dec = len(num.split(".")[1]) if "." in num else 0
            b = f'<b class="cnt" data-to="{num.replace(",", "")}" data-dec="{dec}" data-pre="{html.escape(pre)}" data-suf="{html.escape(suf)}" data-comma="{1 if "," in num else 0}">{v}</b>'
        else:
            b = f"<b>{v}</b>"
        out.append(f'<div class="kpi reveal tilt" style="--i:{i}">{b}<span>{l}</span></div>')
    return f'<div class="kpis">{"".join(out)}</div>'

def BARS(title, rows, note=""):
    """Horizontal bars. rows: (label, value, display_text[, color])."""
    mx = max(abs(r[1]) for r in rows) or 1
    body = "".join(
        f'<div class="br" style="--w:{abs(r[1]) / mx * 100:.1f}%;--c:{r[3] if len(r) > 3 else PAL[i % len(PAL)]};--i:{i}"><span>{r[0]}</span><i><u></u></i><b>{r[2]}</b></div>'
        for i, r in enumerate(rows))
    return f'<div class="chart reveal"><h4>{title}</h4>{body}' + (f'<p class="cn">{note}</p>' if note else "") + "</div>"

def _legend(series):
    return '<div class="lgd">' + "".join(f'<span style="--c:{s[2] if len(s) > 2 else PAL[i % len(PAL)]}">{s[0]}</span>' for i, s in enumerate(series)) + "</div>"

def COLS(title, labels, series, note="", fmt=lambda v: f"{v:g}"):
    """Grouped vertical columns (SVG). series: (name, [values], color?). Negative values hang below the baseline."""
    W, H, pl, pr, pt, pb = 680, 300, 16, 16, 26, 34
    vals = [v for s in series for v in s[1] if v is not None]
    hi, lo = max(max(vals), 0), min(min(vals), 0)
    span = (hi - lo) or 1
    y = lambda v: pt + (hi - v) / span * (H - pt - pb)
    base = y(0)
    n, m = len(labels), len(series)
    gw = (W - pl - pr) / n
    bw = min(34, gw * 0.7 / m)
    g = [f'<line x1="{pl}" x2="{W - pr}" y1="{base:.1f}" y2="{base:.1f}" class="ax"/>']
    for i, lab in enumerate(labels):
        cx = pl + gw * (i + .5)
        for j, s in enumerate(series):
            v = s[1][i]
            if v is None: continue
            x = cx + (j - (m - 1) / 2) * (bw + 4) - bw / 2
            top, bot = (y(v), base) if v >= 0 else (base, y(v))
            c = s[2] if len(s) > 2 else PAL[j % len(PAL)]
            g.append(f'<rect class="cb{" ng" if v < 0 else ""}" x="{x:.1f}" y="{top:.1f}" width="{bw:.1f}" height="{max(bot - top, 1):.1f}" rx="4" fill="{c}" style="--i:{i * m + j}"/>')
            ty = top - 6 if v >= 0 else bot + 13
            g.append(f'<text class="vl" x="{x + bw / 2:.1f}" y="{ty:.1f}" text-anchor="middle" style="--i:{i * m + j}">{fmt(v)}</text>')
        g.append(f'<text class="xl" x="{cx:.1f}" y="{H - 10}" text-anchor="middle">{lab}</text>')
    return (f'<div class="chart reveal"><h4>{title}</h4><svg viewBox="0 0 {W} {H}" role="img" aria-label="{html.escape(title)}">{"".join(g)}</svg>{_legend(series) if m > 1 else ""}'
            + (f'<p class="cn">{note}</p>' if note else "") + "</div>")

def _smooth(pts):
    if len(pts) < 3: return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, len(pts) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d

def LINE(title, labels, series, note="", fmt=lambda v: f"{v:g}"):
    """Animated line/area chart. series: (name, [values], color?)."""
    W, H, pl, pr, pt, pb = 680, 300, 30, 24, 24, 34
    vals = [v for s in series for v in s[1] if v is not None]
    hi, lo = max(max(vals), 0), min(min(vals), 0)
    span = (hi - lo) or 1
    y = lambda v: pt + (hi - v) / span * (H - pt - pb)
    n = len(labels)
    x = lambda i: pl + (W - pl - pr) * (i / max(n - 1, 1))
    g = []
    for k in range(5):
        gy = pt + (H - pt - pb) * k / 4
        g.append(f'<line x1="{pl}" x2="{W - pr}" y1="{gy:.1f}" y2="{gy:.1f}" class="gd"/>')
    g.append(f'<line x1="{pl}" x2="{W - pr}" y1="{y(0):.1f}" y2="{y(0):.1f}" class="ax"/>')
    for i, lab in enumerate(labels): g.append(f'<text class="xl" x="{x(i):.1f}" y="{H - 10}" text-anchor="middle">{lab}</text>')
    for j, s in enumerate(series):
        c = s[2] if len(s) > 2 else PAL[j % len(PAL)]
        pts = [(x(i), y(v)) for i, v in enumerate(s[1]) if v is not None]
        d = _smooth(pts)
        area = d + f" L{pts[-1][0]:.1f},{y(0):.1f} L{pts[0][0]:.1f},{y(0):.1f} Z"
        g.append(f'<defs><linearGradient id="lg{abs(hash((title, j))) % 99999}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{c}" stop-opacity=".35"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></linearGradient></defs>')
        g.append(f'<path class="ar" d="{area}" fill="url(#lg{abs(hash((title, j))) % 99999})"/>')
        g.append(f'<path class="ln" pathLength="1" d="{d}" stroke="{c}" style="--j:{j}"/>')
        for i, (px, py) in enumerate(pts):
            g.append(f'<circle class="dt" cx="{px:.1f}" cy="{py:.1f}" r="4.5" fill="{c}" style="--i:{i}"><title>{labels[i]}: {fmt(s[1][i])}</title></circle>')
    return (f'<div class="chart reveal"><h4>{title}</h4><svg viewBox="0 0 {W} {H}" role="img" aria-label="{html.escape(title)}">{"".join(g)}</svg>{_legend(series) if len(series) > 1 else ""}'
            + (f'<p class="cn">{note}</p>' if note else "") + "</div>")

def DONUT(title, parts, center=("", ""), note=""):
    """parts: (label, value, color?). Animated ring with legend."""
    tot = sum(p[1] for p in parts) or 1
    off, segs, leg = 0, [], []
    for i, p in enumerate(parts):
        pct = p[1] / tot * 100
        c = p[2] if len(p) > 2 else PAL[i % len(PAL)]
        segs.append(f'<circle class="sg" cx="60" cy="60" r="46" pathLength="100" stroke="{c}" stroke-dasharray="{max(pct - .8, .1):.2f} 100" stroke-dashoffset="{-off:.2f}" style="--i:{i}"/>')
        leg.append(f'<li style="--c:{c}"><span>{p[0]}</span><b>{pct:.0f}%</b></li>')
        off += pct
    return (f'<div class="chart donut reveal"><h4>{title}</h4><div class="dn"><svg viewBox="0 0 120 120" role="img" aria-label="{html.escape(title)}"><circle cx="60" cy="60" r="46" class="tr"/>{"".join(segs)}'
            f'<text x="60" y="58" text-anchor="middle" class="c1">{center[0]}</text><text x="60" y="72" text-anchor="middle" class="c2">{center[1]}</text></svg><ul>{"".join(leg)}</ul></div>'
            + (f'<p class="cn">{note}</p>' if note else "") + "</div>")

def RING(pct, label, color="var(--ac)"):
    return (f'<div class="ringw reveal"><svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="46" class="tr"/><circle class="sg" cx="60" cy="60" r="46" pathLength="100" stroke="{color}" stroke-dasharray="{pct} 100"/>'
            f'<text x="60" y="68" text-anchor="middle" class="c1">{pct}%</text></svg><span>{label}</span></div>')

def FUNNEL(title, steps, note=""):
    """steps: (label, value, display). Narrowing bars centred."""
    mx = max(s[1] for s in steps) or 1
    body = "".join(f'<div class="fn" style="--w:{max(s[1] / mx * 100, 38):.1f}%;--i:{i}"><i><span>{s[0]}</span><b>{s[2]}</b></i></div>' for i, s in enumerate(steps))
    return f'<div class="chart funnel reveal"><h4>{title}</h4>{body}' + (f'<p class="cn">{note}</p>' if note else "") + "</div>"

def TIMELINE(items):
    """items: (when, title, body). Vertical animated timeline."""
    return '<ol class="tl">' + "".join(f'<li class="reveal" style="--i:{i % 3}"><em>{w}</em><div><h3>{t}</h3><p>{b}</p></div></li>' for i, (w, t, b) in enumerate(items)) + "</ol>"

def VS(a_title, a_rows, b_title, b_rows):
    """Before/after (or A/B) comparison cards; rows are (label, value)."""
    f = lambda rows: "".join(f"<li><span>{k}</span><b>{v}</b></li>" for k, v in rows)
    return (f'<div class="vs"><div class="reveal a"><h3>{a_title}</h3><ul>{f(a_rows)}</ul></div><div class="mid reveal">&rarr;</div>'
            f'<div class="reveal b" style="--i:1"><h3>{b_title}</h3><ul>{f(b_rows)}</ul></div></div>')

def PILLS(items):
    return '<div class="chips">' + "".join(f'<span class="reveal" style="--i:{i}">{t}</span>' for i, t in enumerate(items)) + "</div>"

def SECTION(eyebrow, title, lede=""):
    return f'<div class="sh2 reveal"><p class="ey">{eyebrow}</p><h2>{title}</h2>' + (f"<p>{lede}</p>" if lede else "") + "</div>"

# ---------- page registry ----------
PAGES = {}
PAGEX = {}   # slug -> {"img": name, "chips": [(value, label), ...]}
def page(slug, group, title, lede, body, img=None, chips=None):
    PAGES[slug] = (group, title, lede, body)
    PAGEX[slug] = {"img": img, "chips": chips or []}
