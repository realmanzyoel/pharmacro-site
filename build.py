#!/usr/bin/env python3
"""Builds the PharmaCRO site into ./public.  Run: python3 build.py"""
import os, sys, glob, hashlib, shutil, importlib, re, json
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import ph as S
MODS = ["c_home", "c_services", "c_services2", "c_industries", "c_labs", "c_quality_tech", "c_resources", "c_methods", "c_tools", "c_company", "c_convert"]
# ONLY=c_x,c_y builds just those modules into public_<first>/ and treats links to planned-but-unbuilt pages as fine (for parallel work).
ONLY = [m for m in os.environ.get("ONLY", "").split(",") if m]
OUT = os.path.join(ROOT, "public" + ("_" + ONLY[0] if ONLY else ""))

def main():
    for m in (ONLY or MODS):
        if os.path.exists(os.path.join(ROOT, m + ".py")): importlib.import_module(m)
        else: print("skip (missing):", m)
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets"))
    css = "".join(open(os.path.join(ROOT, "assets", f)).read() for f in ("il.css", "ph.css")) + "".join(open(f).read() for f in sorted(glob.glob(os.path.join(ROOT, "assets", "m_*.css"))))
    js = open(os.path.join(ROOT, "assets", "il.js")).read() + "\n" + open(os.path.join(ROOT, "assets", "ph.js")).read() + "".join("\n" + open(f).read() for f in sorted(glob.glob(os.path.join(ROOT, "assets", "m_*.js"))))
    v = hashlib.md5((css + js).encode()).hexdigest()[:8]
    open(os.path.join(OUT, "assets", "site.css"), "w").write(css)
    open(os.path.join(OUT, "assets", "site.js"), "w").write(js)
    shutil.copytree(os.path.join(ROOT, "img"), os.path.join(OUT, "img"))
    # search index for the header search and the Ask the Lab assistant
    idx = [dict(p=p + ".html", t=re.sub("<[^>]+>", "", d["title"]), d=re.sub(r"\s+", " ", re.sub("<[^>]+>", "", d["desc"] or d["lede"] or ""))[:220],
                s=(p.split("/")[0] if "/" in p else "page").replace("-", " "), k=re.sub(r"\s+", " ", re.sub("<[^>]+>", " ", d["body"]))[:1400].lower())
           for p, d in S.PAGES.items() if p not in ("404", "maintenance")]
    open(os.path.join(OUT, "assets", "search.json"), "w").write(json.dumps(idx, ensure_ascii=False))
    targets = {p + ".html" for p in S.PAGES} | ({p + ".html" for p in S.PLANNED} if ONLY else set()) | {"img/" + f for f in os.listdir(os.path.join(ROOT, "img"))} | {"assets/site.css", "assets/site.js", "assets/search.json"}
    missing = set()
    for path, d in S.PAGES.items():
        h = S.render(path, d, v)
        fn = os.path.join(OUT, path + ".html")
        os.makedirs(os.path.dirname(fn), exist_ok=True)
        open(fn, "w").write(h)
        for u in re.findall(r'(?:href|src)="([^"#?:]+)', h):
            if u.startswith(("http", "mailto", "tel", "sms", "data")): continue
            parts = path.split("/")[:-1]
            for seg in u.split("/"):
                if seg == "..": parts = parts[:-1]
                elif seg not in ("", "."): parts.append(seg)
            if "/".join(parts) not in targets: missing.add((path, u))
    open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' +
        "".join(f"<url><loc>{S.DOMAIN}/{'' if p == 'index' else p}</loc><lastmod>2026-11-21</lastmod></url>" for p in S.PAGES if p not in ("404", "maintenance", "portal/login", "search")) + "</urlset>")
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /portal/login\n\nUser-agent: GPTBot\nAllow: /\n\nUser-agent: ClaudeBot\nAllow: /\n\nUser-agent: PerplexityBot\nAllow: /\n\nUser-agent: Google-Extended\nAllow: /\n\nSitemap: {S.DOMAIN}/sitemap.xml\n")
    llms = [f"# {S.BRAND}\n\n> A planned network of GMP pharmaceutical analytical testing laboratories (pre-launch). Figures on this site are illustrative placeholders until verified.\n"]
    for sec in ["services", "solutions", "industries", "labs", "quality", "technology", "method-library", "insights", "tools"]:
        ps = [(p, d) for p, d in S.PAGES.items() if p.startswith(sec + "/")]
        if ps: llms.append(f"\n## {sec.replace('-', ' ').title()}\n" + "".join(f"- [{re.sub('<[^>]+>', '', d['title'])}]({S.DOMAIN}/{p}): {re.sub('<[^>]+>', '', d['lede'])[:140]}\n" for p, d in ps))
    open(os.path.join(OUT, "llms.txt"), "w").write("".join(llms))
    unplanned = sorted(set(S.PAGES) - set(S.PLANNED))
    if unplanned: print("PAGES NOT IN ph.PLANNED (add links carefully):", unplanned[:40])
    print(len(S.PAGES), "pages ->", OUT)
    if missing:
        print("BROKEN LINKS:", len(missing))
        for m in sorted(missing)[:80]: print("  ", m)

if __name__ == "__main__":
    main()
