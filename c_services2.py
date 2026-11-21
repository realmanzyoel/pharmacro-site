"""Service pages 7 to 12 (blueprint 4.4 template + 4.5 unique content).
Module styles/behaviour: assets/m_services2.css / m_services2.js (prefix .sv2-)."""
from ph import *

M = "/method-library/"
def ml(s): return M + s + ".html"

# ---------- hero visuals (animated SVG; CSS in m_services2.css) ----------
_col = [(150, 120, 9), (182, 96, 6), (120, 170, 7), (205, 150, 11), (160, 205, 5), (98, 120, 6), (230, 112, 5), (135, 85, 4), (215, 200, 7), (182, 168, 4), (110, 210, 5), (250, 160, 4)]
V_PETRI = ('<svg class="sv2-petri" viewBox="0 0 360 320" role="img" aria-label="A petri dish where colonies bloom and are then counted">'
           '<circle cx="175" cy="150" r="130" class="sv2-dish"/><circle cx="175" cy="150" r="118" class="sv2-agar"/>'
           + "".join(f'<g class="sv2-col" style="--k:{i}"><circle cx="{x}" cy="{y}" r="{r}"/><text x="{x + r + 3}" y="{y - r}">{i + 1}</text></g>' for i, (x, y, r) in enumerate(_col))
           + '<text x="175" y="306" text-anchor="middle" class="sv2-cnt">CFU counted: <tspan data-sv2-count="12">0</tspan></text></svg>')

V_HEPA = ('<svg class="sv2-hepa" viewBox="0 0 360 320" role="img" aria-label="Particles drifting down through a HEPA filtered unidirectional airflow">'
          '<rect x="30" y="18" width="300" height="34" rx="6" class="sv2-filt"/>' + "".join(f'<line x1="{40 + i * 14}" y1="22" x2="{40 + i * 14}" y2="48" class="sv2-pleat"/>' for i in range(21))
          + "".join(f'<line x1="{52 + i * 32}" y1="60" x2="{52 + i * 32}" y2="290" class="sv2-flow" style="--k:{i}"/>' for i in range(9))
          + "".join(f'<circle cx="{44 + (i * 47) % 280}" cy="70" r="{1.6 + (i % 3)}" class="sv2-pt" style="--k:{i};--x:{(i % 5 - 2) * 6}px"/>' for i in range(26))
          + '<rect x="70" y="270" width="220" height="22" rx="4" class="sv2-bench"/><text x="180" y="312" text-anchor="middle" class="sv2-lbl">Grade A zone &middot; 0.45 m/s unidirectional airflow</text></svg>')

V_VIAL = ('<svg class="sv2-vial" viewBox="0 0 360 320" role="img" aria-label="A vial wall turning transparent while compounds migrate from the stopper and glass into the product">'
          '<rect x="120" y="40" width="120" height="24" rx="5" class="sv2-stop"/><rect x="132" y="62" width="96" height="12" class="sv2-neck"/>'
          '<path d="M120 80h120v190a22 22 0 0 1-22 22h-76a22 22 0 0 1-22-22z" class="sv2-wall"/><path d="M128 150h104v118a16 16 0 0 1-16 16h-72a16 16 0 0 1-16-16z" class="sv2-liq"/>'
          + "".join(f'<circle cx="{x}" cy="{y}" r="3.2" class="sv2-mig" style="--k:{i};--dx:{dx}px;--dy:{dy}px"/>' for i, (x, y, dx, dy) in enumerate([(124, 170, 34, 10), (236, 190, -36, 8), (124, 230, 30, -6), (236, 250, -32, -10), (150, 66, 6, 110), (205, 66, -8, 120), (124, 205, 40, 18), (236, 215, -40, 4)]))
          + '<text x="40" y="120" class="sv2-lbl">Stopper: oligomers, antioxidants</text><text x="248" y="200" class="sv2-lbl">Glass: Si, B, Al</text>'
          '<text x="180" y="312" text-anchor="middle" class="sv2-lbl">Extractables become leachables</text></svg>')

V_LCMS = ('<svg class="sv2-lcms" viewBox="0 0 360 320" role="img" aria-label="A plasma sample moving through an LC-MS/MS system, producing chromatographic peaks">'
          '<rect x="20" y="40" width="40" height="64" rx="8" class="sv2-tube"/><rect x="24" y="70" width="32" height="30" rx="5" class="sv2-plasma"/><text x="40" y="124" text-anchor="middle" class="sv2-lbl">Plasma</text>'
          '<path id="sv2-p" d="M60 72H110V60H220V72H270" class="sv2-line"/><rect x="110" y="56" width="110" height="20" rx="10" class="sv2-colm"/><text x="165" y="96" text-anchor="middle" class="sv2-lbl">C18 column</text>'
          '<rect x="270" y="40" width="72" height="64" rx="10" class="sv2-ms"/><text x="306" y="66" text-anchor="middle" class="sv2-lbl">Q1 &gt; Q2 &gt; Q3</text><text x="306" y="84" text-anchor="middle" class="sv2-lbl">MRM</text>'
          '<circle r="5" class="sv2-drop"><animateMotion dur="3s" repeatCount="indefinite" path="M60 72H110V60H220V72H270"/></circle>'
          '<circle r="5" class="sv2-drop b"><animateMotion dur="3s" begin="1.5s" repeatCount="indefinite" path="M60 72H110V60H220V72H270"/></circle>'
          '<path d="M24 290H336" class="sv2-axis"/><path pathLength="1" class="sv2-trace" d="M24 288H90c8 0 9-2 12-20l8-90c2-8 4-8 6 0l8 90c3 18 4 20 12 20H190c6 0 7-1 9-14l6-50c2-6 4-6 6 0l6 50c2 13 3 14 9 14H336"/>'
          '<text x="114" y="170" class="sv2-lbl">Analyte</text><text x="198" y="214" class="sv2-lbl">SIL-IS</text></svg>')

_peaks = [(60, 70), (92, 30), (118, 120), (150, 55), (176, 90), (214, 40), (240, 75), (282, 35), (310, 50)]
_xr = "M20 290" + "".join(f"L{x - 6} 288L{x} {288 - h}L{x + 6} 288" for x, h in _peaks) + "L340 290"
V_XRPD = ('<svg class="sv2-xrpd" viewBox="0 0 360 320" role="img" aria-label="Powder crystals resolving into an X-ray powder diffraction pattern">'
          + "".join(f'<polygon class="sv2-xtal" style="--k:{i}" points="{x},{y - 14} {x + 12},{y - 4} {x + 8},{y + 12} {x - 8},{y + 12} {x - 12},{y - 4}"/>' for i, (x, y) in enumerate([(70, 70), (120, 50), (180, 80), (240, 55), (290, 85), (150, 120), (220, 125), (95, 120)]))
          + '<path d="M20 292H340M20 292V150" class="sv2-axis"/>' f'<path pathLength="1" class="sv2-trace" d="{_xr}"/>'
          '<text x="180" y="312" text-anchor="middle" class="sv2-lbl">2&theta; (degrees), Cu K&alpha;</text></svg>')

_mods = ["3.2.S.4.2 Analytical procedures", "3.2.S.4.3 Validation", "3.2.P.5.1 Specifications", "3.2.P.5.4 Batch analyses", "3.2.P.8.3 Stability data", "Response to query"]
V_DOSS = ('<svg class="sv2-doss" viewBox="0 0 360 320" role="img" aria-label="A CTD Module 3 dossier assembling page by page">'
          + "".join(f'<g class="sv2-pg" style="--k:{i}"><rect x="{70 + i * 8}" y="{230 - i * 30}" width="190" height="62" rx="8"/><text x="{84 + i * 8}" y="{256 - i * 30}">{t}</text><line x1="{84 + i * 8}" y1="{270 - i * 30}" x2="{220 + i * 8}" y2="{270 - i * 30}"/></g>' for i, t in enumerate(_mods))
          + '<text x="180" y="312" text-anchor="middle" class="sv2-lbl">CTD Module 3, analytical sections</text></svg>')

# ---------- local components ----------
def INSTR(items, pct, cap):
    """Image slider with spec overlays + capacity gauge. items: (img, name, [spec lines])."""
    sl = "".join(f'<figure class="sv2-sl"><img src="/img/{im}.jpg" alt="{alt(im)}" loading="lazy"><figcaption><b>{n}</b>' + "".join(f"<span>{s}</span>" for s in sp) + '</figcaption></figure>' for im, n, sp in items)
    return (f'<div class="sv2-ins reveal"><div class="sv2-trk" tabindex="0" aria-label="Instruments, scroll sideways">{sl}</div>'
            f'<div class="sv2-g"><svg viewBox="0 0 120 70" aria-hidden="true"><path d="M10 64a50 50 0 0 1 100 0" class="sv2-gt"/><path d="M10 64a50 50 0 0 1 100 0" class="sv2-gf" pathLength="100" style="--p:{pct}"/></svg>'
            f'<b>{pct}%</b><span>{cap}</span><small>Planned network capacity committed {ILL("Placeholder")}</small>'
            '<p><button type="button" class="btn sm o sv2-prev" aria-label="Previous instrument">&larr;</button> <button type="button" class="btn sm o sv2-next" aria-label="Next instrument">&rarr;</button></p></div></div>')

def SCOPE(rows):
    return T(["Scope item", "Standard", "Target accreditation"], rows) + f'<p class="cn">Target scope for planned sites {ILL("Not yet held")} Certificates appear on the <a href="/quality/accreditations.html">accreditation wall</a> once issued.</p>'

def GUIDES(items):
    """Standout content: short substantive guides. items: (title, html, link or '')."""
    return '<div class="sv2-gd">' + "".join(f'<article class="sv2-gi reveal" style="--i:{i}"><h3>{t}</h3>{b}' + (f'<p><a href="{l}">Read the full article &rsaquo;</a></p>' if l else "") + '</article>' for i, (t, b, l) in enumerate(items)) + '</div>'

def TOOLBOX(eyebrow, title, lede, inner):
    return SH(eyebrow, title, lede) + f'<div class="sv2-tool box reveal">{inner}</div>'

def build(slug, d):
    s = SVC[slug]; i = SERVICES.index(s); n = SCI[s[8]][0]; first = n.replace("Dr ", "").split()[0]
    hb = (f'<a class="btn big mag" href="/request-quote.html?service={i}"><span>Request a quote</span></a> '
          f'<a class="btn o big" href="mailto:{MAIL}?subject={html.escape("Question for " + n)}">Ask {first}</a>')
    body = (ANSWER(d["answer"]) + SVCHEAD(slug, d["visual"], d["vchips"])
            + SH("What we test", d["tests_h"], "Search or filter by standard. Open a row for the method summary and instruments.") + TESTS(d["tests"])
            + SH("Regulatory coverage", "Data your regulator will recognise.", d["reg"]) + REGBADGES()
            + d.get("mid", "")
            + SH("Instruments and capability", d["ins_h"]) + INSTR(*d["ins"])
            + SH("Turnaround tiers", "Pick a tier, see the date.") + TIERS(d["tiers"])
            + SH("Sample requirements", "Send it right the first time.", d["samp_l"]) + CHECKRING(d["samp"])
            + SH("How it works", d["how_h"]) + VIAL(d["how"])
            + SH("Proof", "What good looks like.") + '<div class="two"><div>' + CHIP(*d["chip"]) + SCICARD(s[8]) + '</div><div>' + SCOPE(d["scope"]) + '</div></div>'
            + d.get("gal", "")
            + SH("Questions", "Answers first.") + FAQS(d["faq"], "faq")
            + TOOLBOX(*d["tool"])
            + SH("Guides", d["guides_h"]) + GUIDES(d["guides"])
            + d.get("band", "")
            + RELATED(d["related"]))
    page(f"services/{slug}", s[1], d["lede"], body, img=s[4], chips=d["chips"], crumbs=[("Services", "/services/index.html")], cta=d["cta"], hb=hb,
         eyebrow="Services", desc=d["answer"])

# =====================================================================================
# 7. Microbiology and Sterility
# =====================================================================================
ENDO = ('<div class="sv2-endo" data-sv2="endo"><div class="sv2-in">'
        '<label><span>Maximum dose</span><input type="number" min="0" step="any" value="10" data-e="dose"></label>'
        '<label><span>Dose unit</span><select data-e="unit"><option value="mg">mg</option><option value="mL">mL</option><option value="Units">Units</option></select></label>'
        '<label><span>Given over (hours)</span><input type="number" min="0.01" step="any" value="1" data-e="hrs"></label>'
        '<label><span>Patient weight (kg)</span><input type="number" min="1" step="any" value="70" data-e="kg"></label>'
        '<label><span>Route</span><select data-e="route"><option value="5">Parenteral: IV, IM, SC (K = 5 EU/kg)</option><option value="0.2">Intrathecal (K = 0.2 EU/kg)</option>'
        '<option value="2.5">Radiopharmaceutical, IV (K = 175 EU per dose basis, shown per kg for 70 kg)</option></select></label>'
        '<label><span>Product concentration (unit per mL)</span><input type="number" min="0" step="any" value="5" data-e="conc"></label>'
        '<label><span>Method sensitivity &lambda; (EU/mL)</span><select data-e="lam"><option value="0.005">0.005 (kinetic chromogenic / rFC)</option><option value="0.01">0.01 (kinetic turbidimetric)</option><option value="0.03">0.03 (gel-clot)</option><option value="0.125">0.125 (gel-clot)</option></select></label></div>'
        '<div class="sv2-out" aria-live="polite"><span class="k">Endotoxin limit</span><b data-e="lim">&nbsp;</b><span data-e="mvd"></span><p data-e="rec"></p></div></div>'
        '<p class="cn">Formula per USP &lt;85&gt; / Ph. Eur. 2.6.14 and 5.1.10: limit = K / M, where M is the maximum dose per kg per hour. MVD = (limit &times; concentration) / &lambda;. '
        'General information to plan a test, not a release specification. For the full version see the <a href="/tools/endotoxin-limit-calculator.html">Endotoxin Limit Calculator</a>.</p>')

build("microbiology-sterility", dict(
    lede="Sterility, endotoxin, bioburden, mycoplasma and container closure testing to USP, Ph. Eur. and JP, with rapid methods when the clock matters.",
    answer="We run compendial sterility (USP &lt;71&gt;, Ph. Eur. 2.6.1), bacterial endotoxins by LAL and recombinant factor C, bioburden, microbial limits, mycoplasma and container closure integrity. Standard sterility reports in 14 days of incubation plus review; endotoxin in 2 to 3 days. Rapid methods are available for short-shelf-life products.",
    chips=[("14 d", "compendial sterility incubation"), ("2 to 3 d", "endotoxin turnaround"), ("ISO 5", "isolator sterility suites")],
    visual=V_PETRI, vchips=[("&lt;71&gt;", "Sterility"), ("&lt;85&gt;", "Endotoxins"), ("2.6.7", "Mycoplasma"), ("0 CFU", "Grade A target")],
    tests_h="Every microbiology release test, in one network.",
    tests=[("Sterility, membrane filtration", "USP <71>, Ph. Eur. 2.6.1, JP 4.06", "14 d + 2 d", "20 containers (typical)", "ISO 17025 target", "Product filtered through 0.45 µm membranes, rinsed to remove antimicrobial activity and incubated in FTM (30–35 °C) and SCDM (20–25 °C) for 14 days. Method suitability performed per product.", "Isolator, closed filtration units", ml("sterility-membrane-filtration")),
           ("Sterility, direct inoculation", "USP <71>, Ph. Eur. 2.6.1", "14 d + 2 d", "Per batch size table", "ISO 17025 target", "For products that cannot be filtered (oily, insoluble, devices). Product transferred directly into media and incubated 14 days.", "Isolator", ml("sterility-membrane-filtration")),
           ("Bacterial endotoxins, kinetic chromogenic LAL", "USP <85>, Ph. Eur. 2.6.14, JP 4.01", "2 to 3 d", "2 to 5 mL", "ISO 17025 target", "Photometric LAL with a five-point standard curve, positive product controls at the chosen dilution, and MVD calculated against the product limit.", "Kinetic plate readers", ml("bacterial-endotoxins-lal")),
           ("Bacterial endotoxins, gel-clot", "USP <85>, Ph. Eur. 2.6.14", "1 to 2 d", "2 mL", "ISO 17025 target", "Limit test or semi-quantitative assay where photometric methods suffer interference.", "Heating blocks", ml("bacterial-endotoxins-lal")),
           ("Recombinant factor C (rFC)", "Ph. Eur. 2.6.32, USP <86>", "2 to 3 d", "2 to 5 mL", "Validation per product", "Animal-free endotoxin detection with a fluorescent substrate. Not affected by glucans. Comparability against LAL documented per product.", "Fluorescence plate readers", ml("recombinant-factor-c")),
           ("Bioburden (TAMC, TYMC)", "USP <61>, Ph. Eur. 2.6.12", "5 to 7 d", "10 g or 10 mL", "ISO 17025 target", "Plate count, membrane filtration or MPN with recovery verified per product.", "Biosafety cabinets, incubators", ml("bioburden")),
           ("Specified microorganisms", "USP <62>, Ph. Eur. 2.6.13", "5 to 7 d", "10 g or 10 mL", "ISO 17025 target", "Absence of E. coli, Salmonella, P. aeruginosa, S. aureus, C. albicans, bile-tolerant Gram-negative bacteria.", "Selective media, MALDI-TOF ID", ml("bioburden")),
           ("Mycoplasma, culture method", "Ph. Eur. 2.6.7, USP <63>", "28 d", "10 mL + cells", "ISO 17025 target", "Agar and broth culture plus indicator cell culture, 28 days.", "Microaerophilic incubators", ml("mycoplasma-nat")),
           ("Mycoplasma, NAT (qPCR)", "Ph. Eur. 2.6.7, USP <63>", "1 to 2 d", "1 to 10 mL", "Validation per product", "Nucleic acid amplification validated for specificity and a detection limit of 10 CFU/mL as required by Ph. Eur.", "qPCR", ml("mycoplasma-nat")),
           ("Antimicrobial effectiveness", "USP <51>, Ph. Eur. 5.1.3", "28 d", "5 x 20 mL", "ISO 17025 target", "Challenge with five compendial organisms, log-reduction at defined intervals.", "Incubators", ""),
           ("Container closure integrity", "USP <1207>", "3 to 10 d", "30+ units", "Validation per container", "Deterministic methods first: vacuum decay, high-voltage leak detection, headspace analysis. Dye ingress only when justified.", "Vacuum decay, HVLD, laser headspace", ml("container-closure-integrity")),
           ("Microbial identification", "USP <1113>", "1 to 3 d", "Isolate", "ISO 17025 target", "MALDI-TOF MS identification with 16S rRNA sequencing for unresolved isolates.", "MALDI-TOF, sequencer", ""),
           ("Disinfectant efficacy", "EN 13697, USP <1072>", "2 to 4 wk", "Disinfectant + surfaces", "Project", "Surface challenge with environmental isolates on your actual materials.", "Coupons, incubators", "")],
    reg="Sterility, endotoxin and microbial limits are harmonised across USP, Ph. Eur. and JP for most tests; we report against the pharmacopoeia your dossier cites.",
    ins_h="Isolators, readers and identification, on one data system.",
    ins=([("lab-cleanroom-suit", "Sterility isolators", ["ISO 5 / Grade A interior", "VHP decontamination cycle", "Closed membrane filtration units"]),
          ("micro-petri-1", "Incubation and reading", ["30–35 °C and 20–25 °C rooms", "Daily reads logged in LIMS", "Photo of every plate at read"]),
          ("lab-plate-pink", "Kinetic LAL and rFC readers", ["Sensitivity to 0.005 EU/mL", "Five-point curves", "21 CFR Part 11 software"]),
          ("inst-pcr", "qPCR for mycoplasma", ["Validated to 10 CFU/mL", "Results in 1 to 2 days", "Internal controls per run"]),
          ("lab-microscope-close", "Identification", ["MALDI-TOF MS", "16S rRNA sequencing", "Isolate library per client"])], 68, "of planned sterility isolator hours"),
    tiers=(16, 14, 2),
    samp_l="Sterility counts are set by USP &lt;71&gt; Table 3 from batch size; we confirm the number in your quote.",
    samp=["Number of containers matches the compendial table for your batch size", "Samples labelled with product, batch, expiry and container count", "Stored and shipped at the labelled storage condition", "Method suitability already done, or ordered together", "Product limit (EU per mg or mL) stated for endotoxin", "Signed sample submission sheet in the box"],
    how_h="From cold box to sterility report.",
    how=[("Submit", "Order sterility, endotoxin and mycoplasma together. We check that method suitability exists for your product.", "lab-analyst-pc", "sealed"),
         ("Receive", "Containers counted and photographed; temperature logger read; samples moved straight into controlled storage.", "log-warehouse", "opened"),
         ("Test", "Filtration in the isolator; media incubated 14 days with reads logged and photographed. Endotoxin runs in parallel.", "micro-petri-2", "instrument"),
         ("Release", "Microbiology reviewer checks reads and controls; QA e-signs the certificate.", "lab-goggles", "reported")],
    chip=("14 d to 7 d", "Rapid sterility for a short-shelf-life product", "<p>An illustrative example: an ATP-bioluminescence rapid sterility method validated per Ph. Eur. 5.1.6 against the compendial test, cutting time-to-result for a hospital compounding client.</p>"),
    scope=[["Sterility testing", "USP <71>, Ph. Eur. 2.6.1", "ISO/IEC 17025"], ["Bacterial endotoxins", "USP <85>, Ph. Eur. 2.6.14", "ISO/IEC 17025"], ["Microbial limits", "USP <61>/<62>", "ISO/IEC 17025"], ["Mycoplasma", "Ph. Eur. 2.6.7", "ISO/IEC 17025, GMP"]],
    gal=GALLERY(["micro-petri-2", "lab-petri-hand", "lab-microscope-man"]),
    faq=[("How long does a sterility test take?", "<p>Fourteen days of incubation under USP &lt;71&gt; and Ph. Eur. 2.6.1, plus about two days for filtration and review. Rapid methods validated per Ph. Eur. 5.1.6 can cut this to days.</p>"),
         ("How many containers do you need for sterility?", "<p>It depends on batch size and fill volume, using the tables in USP &lt;71&gt;. For a parenteral batch of more than 500 containers the usual minimum is 20 containers (or 2% for some larger batches); we confirm the number before you ship.</p>"),
         ("What is method suitability and do I need it?", "<p>Yes. Method suitability shows that your product does not inhibit growth of the compendial organisms under test conditions. It is done once per product and repeated after formulation changes.</p>"),
         ("LAL or recombinant factor C?", "<p>Both detect endotoxin. rFC is animal-free and does not react to beta-glucans; it is in Ph. Eur. 2.6.32 and USP &lt;86&gt;. For an existing LAL-registered product a switch needs comparability data and a regulatory variation.</p>"),
         ("How do you set the endotoxin limit?", "<p>Limit = K/M. K is 5 EU/kg for most parenteral routes and 0.2 EU/kg for intrathecal; M is the maximum dose per kg per hour. Use the calculator on this page.</p>"),
         ("What is low endotoxin recovery?", "<p>Some biologic formulations with polysorbate and chelating buffers mask spiked endotoxin over time. We run hold-time recovery studies to show whether your product is affected.</p>"),
         ("Do you test mycoplasma by culture or NAT?", "<p>Both. Culture takes 28 days. A validated NAT method under Ph. Eur. 2.6.7 gives results in one to two days and is common for cell and gene therapy products.</p>"),
         ("What happens if a sterility test fails?", "<p>We notify you the same day, preserve the media and isolate, identify the organism, and run a laboratory investigation per USP &lt;1223&gt; and FDA's sterility guidance before any retest decision.</p>"),
         ("Can you test container closure integrity?", "<p>Yes, with deterministic methods preferred by USP &lt;1207&gt;: vacuum decay, high-voltage leak detection and laser headspace analysis.</p>"),
         ("Do you identify environmental isolates?", "<p>Yes, by MALDI-TOF MS, with 16S rRNA sequencing for organisms the library cannot resolve.</p>")],
    tool=("Signature tool", "Endotoxin Limit Calculator", "Enter dose and route; get the endotoxin limit, maximum valid dilution and a recommended method.", ENDO),
    guides_h="What experienced microbiologists want you to know.",
    guides=[("Rapid microbiological methods, explained", "<p>Rapid methods detect growth signals sooner: ATP bioluminescence, CO<sub>2</sub> monitoring in automated culture bottles, flow cytometry and solid-phase cytometry. Ph. Eur. 5.1.6 and USP &lt;1223&gt; describe validation: accuracy, precision, specificity, limit of detection and equivalence to the compendial method.</p><p>They make most sense for short-shelf-life products such as cell therapies and radiopharmaceuticals, and for in-process bioburden where a day matters.</p>", ""),
            ("Sterility test failure: investigation guide", "<p>A positive sterility test is presumed product failure until proven otherwise. Investigate the lab first: isolator environmental data, operator, media and controls. Identify the organism to species level and compare it with your environmental monitoring isolates.</p><p>An invalid test is declared only with clear evidence of a lab error, as FDA's aseptic processing guidance expects. Otherwise the batch fails.</p>", ""),
            ("LAL versus recombinant reagents", "<p>LAL comes from horseshoe crab blood and responds to endotoxin and, unless blocked, to beta-glucans. rFC uses a recombinant protein and a fluorescent signal and is glucan-blind.</p><p>Since Ph. Eur. 2.6.32 (2021) and USP &lt;86&gt;, rFC is a compendial option. The switch is a change with data: parallel testing on three or more lots.</p>", "/insights/endotoxin-lal-vs-recombinant.html")],
    band=BAND("lab-filtration", "Every plate photographed. Every read logged.", "Microbiology data is easy to lose and hard to defend. Ours sits in the same LIMS as every chemistry result.", BTN("See data integrity", "/quality/data-integrity.html")),
    related=["environmental-monitoring", "cell-gene-therapy-testing", "small-molecule-qc-release"],
    cta=("Sterility you can bank on.", "Tell us the product, batch size and deadline. We confirm the container count and method suitability status in your quote."),
))

# =====================================================================================
# 8. Environmental Monitoring and Cleanrooms
# =====================================================================================
EMB = ('<div class="sv2-em" data-sv2="em"><div class="sv2-in">'
       + "".join(f'<label><span>Grade {g} rooms</span><input type="number" min="0" max="40" value="{v}" data-g="{g}"></label>' for g, v in [("A", 2), ("B", 2), ("C", 3), ("D", 4)])
       + '<label><span>Typical room area (m²)</span><input type="number" min="1" max="1000" value="20" data-m="area"></label>'
       '<label><span>Operation</span><select data-m="op"><option value="op">In operation (dynamic)</option><option value="rest">At rest</option></select></label></div>'
       '<div class="sv2-emo" aria-live="polite"></div></div>'
       '<p class="cn">Limits from EU GMP Annex 1 (2022) Tables 1 and 6; minimum particle sampling locations from ISO 14644-1:2015 Table A.1. Frequencies are a suggested starting plan; your contamination control strategy sets the final plan.</p>')

build("environmental-monitoring", dict(
    lede="Viable and non-viable monitoring, water and gas testing, and cleanroom classification, designed around your contamination control strategy.",
    answer="We sample and test your cleanrooms, utilities and people: viable air, surfaces and gloves, non-viable particles, compressed gases, purified water and WFI. We classify rooms to ISO 14644-1 and set limits to EU GMP Annex 1 (2022). Trend reports show alert and action excursions every month, not only when an inspector asks.",
    chips=[("Annex 1", "2022 aligned programmes"), ("ISO 14644", "classification"), ("24 h", "excursion call-back target")],
    visual=V_HEPA, vchips=[("3,520", "/m³ ≥0.5 µm, Grade A"), ("<1 CFU", "Grade A action"), ("0.45 m/s", "UDAF guidance"), ("WFI", "≤0.25 EU/mL")],
    tests_h="Air, surfaces, people, water and gas.",
    tests=[("Active viable air sampling", "Annex 1, USP <1116>", "3 to 5 d", "On-site, 1 m³", "ISO 17025 target", "Impaction onto TSA, incubated per your validated regime; CFU/m³ against grade limits.", "Impaction air samplers", ml("bioburden")),
           ("Settle plates", "Annex 1, USP <1116>", "3 to 5 d", "90 mm plates", "ISO 17025 target", "Passive exposure up to 4 hours per plate; CFU/4 h.", "Incubators", ""),
           ("Contact plates and swabs", "Annex 1, USP <1116>", "3 to 5 d", "55 mm RODAC", "ISO 17025 target", "Surfaces and gowns after critical operations; neutralisers in media.", "Incubators", ""),
           ("Glove prints and gowning qualification", "Annex 1", "3 to 5 d", "Per operator", "ISO 17025 target", "Five-finger glove prints after interventions; gowning qualification programmes.", "Incubators", ""),
           ("Non-viable particle counts", "ISO 14644-1, Annex 1", "Same day", "On-site", "ISO 17025 target", "≥0.5 µm and ≥5 µm per m³ at rest and in operation.", "Calibrated particle counters", ""),
           ("Cleanroom classification", "ISO 14644-1:2015", "1 to 3 d", "On-site", "ISO 17025 target", "Sampling locations from Table A.1, 95% UCL no longer required.", "Particle counters", ""),
           ("Purified water and WFI: TOC", "USP <643>, Ph. Eur. 2.2.44", "1 to 2 d", "250 mL, TOC-clean vial", "ISO 17025 target", "TOC ≤500 ppb (USP).", "TOC analyser", ml("toc-conductivity-water")),
           ("Conductivity", "USP <645>, Ph. Eur.", "1 d", "250 mL", "ISO 17025 target", "Three-stage test for bulk water.", "Conductivity meter", ml("toc-conductivity-water")),
           ("WFI endotoxin", "USP <85>, Ph. Eur. 2.6.14", "2 d", "50 mL depyrogenated", "ISO 17025 target", "Limit 0.25 EU/mL.", "Kinetic LAL", ml("bacterial-endotoxins-lal")),
           ("Water microbial count", "USP <1231>, Ph. Eur.", "5 to 7 d", "100 to 250 mL", "ISO 17025 target", "Membrane filtration on R2A; WFI action ≤10 CFU/100 mL.", "Filtration manifolds", ml("bioburden")),
           ("Compressed gases", "ISO 8573, Annex 1", "3 to 5 d", "On-site", "ISO 17025 target", "Viable, particles, oil, moisture for product-contact air and nitrogen.", "Gas samplers", ""),
           ("Media fill support", "Annex 1, FDA aseptic guidance", "Project", "Your process", "GMP", "Incubation and reading of filled units; organism identification on any positive.", "Incubators, MALDI-TOF", "")],
    reg="Annex 1 (2022, in force since August 2023) is the reference for EU and PIC/S inspections; FDA's 2004 aseptic guidance and USP &lt;1116&gt; for the US; revised Schedule M in India.",
    ins_h="Calibrated samplers, a trending engine and people who go to your site.",
    ins=([("room-clean-2", "Cleanroom field team", ["Gowned to Grade B", "Site SOP training per client", "Sampling maps agreed in advance"]),
          ("room-clean-1", "Particle counters", ["28.3 L/min and 100 L/min", "ISO 21501-4 calibrated", "Data exported straight to LIMS"]),
          ("lab-cleanroom-suit", "Viable air samplers", ["Impaction, 1 m³ samples", "Validated physical efficiency", "Isolator-compatible heads"]),
          ("lab-flasks-pour", "Water laboratory", ["TOC, conductivity, endotoxin", "R2A membrane filtration", "Bottle prep certified clean"]),
          ("data-dashboard", "Trending", ["Alert/action per location", "Monthly trend reports", "Excursion alerts in the portal"])], 54, "of planned field-team days"),
    tiers=(7, 4, 1),
    samp_l="Most EM work happens at your site. For water and gas, we ship the right bottles and media to you.",
    samp=["Room map with grades and sampling points agreed", "Gowning and site access booked for our field team", "Media lots and neutralisers agreed for your disinfectants", "Water bottles pre-cleaned for TOC and depyrogenated for endotoxin", "Samples returned within the validated hold time", "Chain of custody form signed at handover"],
    how_h="From sampling map to trend report.",
    how=[("Plan", "We map rooms, grades and points from your contamination control strategy.", "room-clean-2", "sealed"),
         ("Sample", "Field team samples at rest or in operation; plates logged by barcode.", "lab-cleanroom-suit", "opened"),
         ("Incubate", "Plates incubated, read, photographed and isolates identified.", "micro-petri-1", "instrument"),
         ("Trend", "Results trended against alert and action levels; excursions flagged within 24 hours.", "data-dashboard", "reported")],
    chip=("3 excursions to 0", "Grade B trend turned round in one quarter", "<p>An illustrative example: trending showed recurring counts at one pass-through hatch; a cleaning change and a new sampling point fixed it within a quarter.</p>"),
    scope=[["Viable monitoring", "Annex 1, USP <1116>", "ISO/IEC 17025"], ["Cleanroom classification", "ISO 14644-1:2015", "ISO/IEC 17025"], ["Water testing", "USP <643>, <645>, <85>", "ISO/IEC 17025"]],
    gal=GALLERY(["room-clean-1", "lab-cleanroom-suit", "micro-petri-2"]),
    faq=[("What does Annex 1 require for Grade A monitoring?", "<p>Continuous non-viable particle monitoring for the full duration of critical processing, and viable monitoring (active air, settle plates, gloves) throughout. Any growth in Grade A should be investigated.</p>"),
         ("What are the Grade A to D particle limits?", "<p>Per Annex 1 Table 1 (≥0.5 µm per m³): Grade A 3,520 at rest and in operation; B 3,520 at rest and 352,000 in operation; C 352,000 at rest and 3,520,000 in operation; D 3,520,000 at rest.</p>"),
         ("How many locations do I need for ISO 14644-1 classification?", "<p>It depends on room area, from ISO 14644-1:2015 Table A.1: for example 6 locations up to 24 m² and 10 up to 52 m². The builder on this page calculates it.</p>"),
         ("Alert versus action levels: what is the difference?", "<p>Action levels come from Annex 1 limits; exceeding them needs investigation. Alert levels are set from your own historical data to warn of drift before you reach action levels.</p>"),
         ("Do you sample on site?", "<p>Yes. Our field team gowns into your cleanrooms, follows your SOPs and hands samples back on a signed chain of custody form.</p>"),
         ("How quickly will I know about an excursion?", "<p>Our target is a call within 24 hours of a read above the action level, with the isolate identified as soon as it grows.</p>"),
         ("Can you test purified water and WFI?", "<p>Yes: TOC (USP &lt;643&gt;), conductivity (&lt;645&gt;), endotoxin (≤0.25 EU/mL for WFI) and microbial count on R2A.</p>"),
         ("Do you support media fills?", "<p>We incubate and read media-fill units and identify any contaminant. Design and execution of the simulation remain your responsibility.</p>")],
    tool=("Signature tool", "EM Programme Builder", "Enter your room grades and size; get a starting sampling plan with limits and frequencies.", EMB),
    guides_h="Short guides for QA and production teams.",
    guides=[("Grade A to D requirements at a glance", "<p>Grade A is the critical zone: filling, open sterile product, stopper bowls. Grade B is its background for aseptic preparation. Grades C and D support less critical steps.</p><p>Annex 1 viable limits (Table 6): Grade A no growth; B 10 CFU/m³ air, 5 CFU/4 h settle, 5 CFU per contact plate and glove; C 100, 50 and 25; D 200, 100 and 50.</p>", ""),
            ("Excursion response playbook", "<p>Within an hour: confirm the read and photograph the plate. Same day: identify the organism and check the batch timeline. Within 72 hours: impact assessment on product made in that window.</p><p>Close with a CAPA only when the root cause is supported by data, not by habit.</p>", ""),
            ("Trending and alert/action limits", "<p>Set alert levels from 12 months of data, for example the 95th percentile per location. Review them yearly. Trend by location, organism and shift, not only by room.</p><p>Repeated Gram-positive cocci usually point at people. Spore-formers point at materials and cleaning.</p>", "")],
    band=BAND("room-clean-2", "Prove your cleanroom stays clean.", "Monthly trends, not inspection-week scrambles.", BTN("Request an EM proposal", "/request-quote.html?service=7")),
    related=["microbiology-sterility", "regulatory-data-integrity-support", "small-molecule-qc-release"],
    cta=("Your EM programme, designed in an afternoon.", "Send your room list and grades. We return a sampling plan, field schedule and price within one business day."),
))

# =====================================================================================
# 9. Extractables and Leachables
# =====================================================================================
ELS = ('<div class="sv2-el" data-sv2="el"><div class="sv2-in">'
       '<label><span>Container / closure</span><select data-l="c"><option value="2">Prefilled syringe (glass, elastomer plunger)</option><option value="2">Glass vial with rubber stopper</option><option value="3">Plastic bag (IV, multilayer film)</option>'
       '<option value="2">Plastic bottle (LDPE, HDPE)</option><option value="3">Inhaler (MDI, DPI components)</option><option value="1">Blister (PVC/PVDC, Alu-Alu)</option><option value="3">Single-use bioprocess system</option></select></label>'
       '<label><span>Dosage form</span><select data-l="p"><option value="3">Aqueous solution</option><option value="3">Solution with surfactant or co-solvent</option><option value="2">Suspension or emulsion</option><option value="1">Solid oral (tablet, capsule)</option><option value="1">Powder</option></select></label>'
       '<label><span>Route</span><select data-l="r"><option value="3">Inhalation</option><option value="3">Injection or intravitreal</option><option value="2">Ophthalmic or nasal</option><option value="2">Transdermal or topical</option><option value="1">Oral</option></select></label>'
       '<label><span>Daily dose volume (mL)</span><input type="number" min="0.01" step="any" value="1" data-l="v"></label></div>'
       '<div class="sv2-out" aria-live="polite"><span class="k">Risk</span><b data-l="risk">&nbsp;</b><span data-l="aet"></span><ul data-l="plan"></ul></div></div>'
       '<p class="cn">Risk follows the FDA 1999 container closure guidance matrix (route concern &times; likelihood of interaction). AET uses the PQRI safety concern threshold: 1.5 µg/day for parenterals, 0.15 µg/day for inhalation. General guidance, not a study protocol.</p>')

build("extractables-leachables", dict(
    lede="Extractables studies, leachables on stability and packaging compatibility, designed from a risk assessment and reported to an analytical evaluation threshold.",
    answer="We design and run extractables studies on your container, closure and processing materials, then monitor leachables in the product through stability. Methods cover volatiles (HS-GC-MS), semi-volatiles (GC-MS), non-volatiles (LC-HRMS) and elements (ICP-MS), reported to an AET derived from PQRI thresholds and USP &lt;1663&gt; and &lt;1664&gt;.",
    chips=[("4 to 12 wk", "typical E&L study"), ("AET", "driven reporting"), ("4 techniques", "orthogonal screen")],
    visual=V_VIAL, vchips=[("&lt;1663&gt;", "Extractables"), ("&lt;1664&gt;", "Leachables"), ("1.5 µg/d", "PQRI SCT"), ("ICP-MS", "Elements")],
    tests_h="Orthogonal methods, one report.",
    tests=[("Controlled extraction study", "USP <1663>, ISO 10993-18", "4 to 6 wk", "Components x3 lots", "Project", "Solvents of different polarity, exaggerated conditions, reflux or Soxhlet, with mass balance and blanks.", "Reflux, ASE, incubators", ml("extractables-gc-ms")),
           ("Volatiles, HS-GC-MS", "USP <1663>", "2 wk", "Components", "Project", "Headspace GC-MS for residual monomers and solvents.", "HS-GC-MS", ml("extractables-gc-ms")),
           ("Semi-volatiles, GC-MS", "USP <1663>", "2 wk", "Extracts", "Project", "Library search plus authentic standards for antioxidants, plasticisers, oligomers.", "GC-MS (EI)", ml("extractables-gc-ms")),
           ("Non-volatiles, LC-HRMS", "USP <1663>", "2 to 3 wk", "Extracts", "Project", "Accurate-mass LC-MS in positive and negative mode for additives and degradants.", "UHPLC-QTOF", ml("leachables-lc-ms")),
           ("Elemental extractables", "USP <232>/<233>, ICH Q3D", "1 to 2 wk", "Extracts", "ISO 17025 target", "ICP-MS for Q3D elements plus packaging elements (Si, B, Al, Zn).", "ICP-MS", ml("elemental-impurities-icp-ms")),
           ("Targeted leachables on stability", "USP <1664>, ICH Q1A", "Per pull", "Product at each pull", "Validation per product", "Validated targeted methods for compounds above the AET, tested at each stability time point.", "GC-MS, LC-MS/MS", ml("leachables-lc-ms")),
           ("Nitrosamines from packaging", "FDA NDSRI guidance, EMA Q&A", "1 to 2 wk", "Lidding, product", "Validation per product", "Nitrocellulose lidding and amine-containing inks can form nitrosamines; LC-MS/MS at ng/g levels.", "LC-MS/MS", ml("nitrosamines-lc-ms-ms")),
           ("Plastic components", "USP <661.1>, <661.2>", "2 to 3 wk", "Materials and systems", "ISO 17025 target", "Material characterisation and packaging system chemical assessment.", "FTIR, ICP-MS, UV", ml("ftir-identification")),
           ("Glass containers", "USP <660>, <1660>", "2 wk", "Vials", "ISO 17025 target", "Hydrolytic resistance and delamination propensity.", "Autoclave, ICP-OES", ""),
           ("Elastomeric closures", "USP <381>, Ph. Eur. 3.2.9", "2 wk", "Stoppers", "ISO 17025 target", "Physicochemical tests, fragmentation, self-sealing.", "Various", ""),
           ("Container closure integrity", "USP <1207>", "3 to 10 d", "30+ units", "Validation per container", "Deterministic leak tests through shelf life.", "Vacuum decay, HVLD", ml("container-closure-integrity")),
           ("Single-use system extractables", "BPOG, USP <665>", "4 to 8 wk", "Components", "Project", "Risk-based extractables for bioprocess bags, filters and tubing.", "GC-MS, LC-HRMS, ICP-MS", ml("extractables-gc-ms"))],
    reg="FDA's 1999 container closure guidance, EMA's guideline on plastic immediate packaging, USP &lt;1663&gt;/&lt;1664&gt;/&lt;665&gt; and PQRI thresholds frame every study we design.",
    ins_h="Four orthogonal techniques so nothing hides.",
    ins=([("inst-gc", "Headspace and GC-MS", ["EI libraries plus in-house standards", "Volatiles to semi-volatiles", "Dual-column confirmation"]),
          ("inst-lcms", "LC-HRMS", ["Accurate mass < 5 ppm", "Positive and negative ESI and APCI", "Structural elucidation workflow"]),
          ("inst-icp", "ICP-MS", ["All ICH Q3D elements", "Collision cell", "ppt detection"]),
          ("lab-vials-bw", "Simulation studies", ["Controlled temperature extraction", "Worst-case contact times", "Blanks and spiked recoveries"]),
          ("lab-analyst-pc", "Toxicology hand-off", ["Compound lists with confidence levels", "PDE inputs for your toxicologist", "AET reporting"])], 61, "of planned LC-HRMS capacity"),
    tiers=(30, 20, 10),
    samp_l="E&L studies start with materials. Send components from at least three lots where you can.",
    samp=["Bill of materials and supplier data for every component", "Components from up to three lots", "Drug product (or placebo) for simulation studies", "Dose, route, duration and patient population for the AET", "Stability protocol if leachables join stability pulls", "Supplier extractables data, if available"],
    how_h="From risk assessment to toxicology-ready report.",
    how=[("Assess", "We score each component by route, contact and duration, and agree the AET.", "docs-papers", "sealed"),
         ("Extract", "Controlled extractions with solvents that bracket your formulation.", "lab-vials-bw", "opened"),
         ("Analyse", "HS-GC-MS, GC-MS, LC-HRMS and ICP-MS screen every extract.", "inst-lcms", "instrument"),
         ("Report", "Compounds above the AET identified and quantified; targeted leachables methods follow.", "lab-analyst-pc", "reported")],
    chip=("4 to 1", "Leachables list trimmed before stability", "<p>An illustrative example: a sound extractables study and AET justification reduced a prefilled syringe programme from four targeted leachables methods to one.</p>"),
    scope=[["Elemental impurities", "USP <232>/<233>", "ISO/IEC 17025"], ["Plastic packaging", "USP <661.1>/<661.2>", "ISO/IEC 17025"], ["Leachables methods", "USP <1664>", "GMP, per product"]],
    gal=GALLERY(["lab-vials-bw", "inst-gc", "lab-glassware"]),
    faq=[("What is the difference between extractables and leachables?", "<p>Extractables are compounds that can be pulled out of a material under exaggerated conditions. Leachables are compounds that actually migrate into the drug product under normal conditions. Leachables are usually a subset of extractables.</p>"),
         ("What is the AET?", "<p>The analytical evaluation threshold is the concentration above which a compound must be identified and reported for toxicological assessment. It is derived from a safety threshold, such as the PQRI SCT of 1.5 µg/day for parenterals, and the dose.</p>"),
         ("Which products need full E&amp;L studies?", "<p>Inhalation and injectable products, especially liquids, carry the highest concern under FDA's 1999 guidance. Solid oral products in standard blisters usually need much less.</p>"),
         ("How long does an extractables study take?", "<p>Typically four to six weeks from component receipt to report, longer for complex single-use systems.</p>"),
         ("Do you identify unknown compounds?", "<p>Yes, with accurate-mass LC-HRMS, GC-MS libraries and authentic standards, reported with a confidence level (confirmed, confident, tentative).</p>"),
         ("Can supplier data replace my study?", "<p>Sometimes in part. Supplier data can support material selection and a risk assessment, but regulators expect product-specific leachables data for high-risk products.</p>"),
         ("Can packaging cause nitrosamines?", "<p>Yes. Nitrocellulose-based lidding foils and amine-containing inks have been linked to nitrosamines in blister products. We test packaging and product together.</p>"),
         ("Do you support biologics in prefilled syringes?", "<p>Yes: tungsten and silicone oil from syringe manufacture, plunger oligomers, and their effect on protein aggregation.</p>")],
    tool=("Signature tool", "E&amp;L Risk Screener", "Choose your container, product and route; see the risk level and a recommended study design.", ELS),
    guides_h="Packaging questions our scientists hear every week.",
    guides=[("Regulatory view on E&amp;L by region", "<p>US: FDA's 1999 container closure guidance and USP &lt;1663&gt;/&lt;1664&gt;, with &lt;661.1&gt;/&lt;661.2&gt; for plastics. EU: EMA guideline on plastic immediate packaging materials and Ph. Eur. 3.1 and 3.2. Inhalation products: PQRI OINDP recommendations with a 0.15 µg/day SCT.</p><p>India and ASEAN regulators generally accept studies designed to these references.</p>", ""),
            ("Nitrosamines from packaging", "<p>Nitrocellulose lacquer on aluminium lidding can release nitrogen oxides during heat sealing; amines in the product or inks can then nitrosate. Screen packaging as part of your nitrosamine risk assessment, not after.</p>", "/insights/nitrosamine-testing-2027.html"),
            ("Study design for biologics in prefilled syringes", "<p>Look at tungsten pins from barrel forming, silicone oil droplets, plunger stopper extractables and adhesive from staked needles. Pair leachables with sub-visible particle and aggregation data, because the risk for proteins is often physical, not only toxicological.</p>", "/insights/el-prefilled-syringes.html")],
    band=BAND("lab-glassware", "Know what your packaging puts in your product.", "", BTN("Screen my packaging", "/request-quote.html?service=8")),
    related=["stability-studies", "small-molecule-qc-release", "biologics-characterization-release"],
    cta=("Packaging risk, measured.", "Send your component list and dose. We return a risk-based study design and an AET within days."),
))

# =====================================================================================
# 10. Bioanalytical and Immunogenicity
# =====================================================================================
ADA = ('<div class="sv2-ada" data-sv2="ada"><div class="sv2-in">'
       '<label><span>Study samples</span><input type="number" min="10" max="20000" value="600" data-a="n"></label>'
       '<label><span>True ADA-positive rate (%)</span><input type="range" min="0" max="60" value="12" data-a="pos"><output data-a="poso">12%</output></label>'
       '<label><span>Screening false-positive rate</span><select data-a="fpr"><option value="5">5% (FDA recommended screening cut point)</option><option value="2">2%</option></select></label>'
       '<label><span>Confirmatory false-positive rate</span><select data-a="cfpr"><option value="1">1%</option><option value="0.1">0.1%</option></select></label></div>'
       '<ol class="sv2-tier" aria-live="polite">'
       + "".join(f'<li data-t="{k}"><b>{t}</b><span class="sv2-bar"><i></i></span><em>0</em><small>{d}</small></li>' for k, t, d in
                 [("all", "All samples", "Every study sample enters the screening assay"), ("scr", "Screen positive", "Signal above the screening cut point"),
                  ("con", "Confirmed positive", "Signal inhibited by excess drug above the confirmatory cut point"), ("tit", "Titred", "Serial dilution to the titre cut point"),
                  ("nab", "Tested for NAb", "Confirmed positives tested in a neutralising antibody assay")])
       + '</ol><p class="cn">Tiered approach per FDA guidance on immunogenicity testing of therapeutic protein products (2019) and EMA guideline EMEA/CHMP/BMWP/14327/2006 Rev. 1. Counts are modelled from your inputs, not study data.</p></div>')

build("bioanalytical-immunogenicity", dict(
    lede="LC-MS/MS and ligand-binding PK assays, tiered anti-drug antibody testing and neutralising antibody assays, validated to ICH M10.",
    answer="We develop, validate and run bioanalytical methods for clinical and non-clinical samples: LC-MS/MS PK assays for small molecules and peptides, ligand-binding PK for biologics, and tiered immunogenicity (screen, confirm, titre, NAb). Validation follows ICH M10; immunogenicity follows FDA's 2019 guidance.",
    chips=[("ICH M10", "validation"), ("4 tiers", "immunogenicity"), ("−80 °C", "monitored storage")],
    visual=V_LCMS, vchips=[("M10", "BMV"), ("pg/mL", "LLOQ range"), ("5%", "screen FPR"), ("SIL-IS", "internal standards")],
    tests_h="PK, immunogenicity and biomarkers.",
    tests=[("LC-MS/MS PK assay, small molecule", "ICH M10", "Validation 4 to 6 wk", "100 to 250 µL plasma", "GLP/GCP target", "Protein precipitation, SPE or LLE with stable-isotope internal standard; MRM detection.", "Triple quadrupole LC-MS/MS", ml("lc-ms-ms-pk-assay")),
           ("LC-MS/MS PK assay, peptides and oligonucleotides", "ICH M10", "6 to 8 wk", "100 µL", "GLP/GCP target", "Immunocapture or SPE enrichment with signature fragments.", "LC-MS/MS", ml("lc-ms-ms-pk-assay")),
           ("Ligand-binding PK (ELISA, ECL)", "ICH M10", "6 to 8 wk", "50 µL serum", "GLP/GCP target", "Sandwich assays with anti-idiotype reagents; parallelism assessed.", "ECL and plate readers", ""),
           ("ADA screening", "FDA 2019, EMA", "Per batch", "50 µL serum", "GLP/GCP target", "Bridging assay with acid dissociation for drug tolerance; statistically derived cut point.", "ECL platform", ml("ada-bridging-assay")),
           ("ADA confirmation", "FDA 2019, EMA", "Per batch", "50 µL", "GLP/GCP target", "Competitive inhibition with excess drug against a confirmatory cut point.", "ECL platform", ml("ada-bridging-assay")),
           ("ADA titre", "FDA 2019", "Per batch", "50 µL", "GLP/GCP target", "Serial dilution to the titre cut point.", "ECL platform", ml("ada-bridging-assay")),
           ("Neutralising antibody, cell-based", "FDA 2019, EMA", "Per batch", "100 µL", "GLP/GCP target", "Cell-based NAb for agonist or enzyme mechanisms.", "Cell culture, plate readers", ml("nab-cell-based-assay")),
           ("Neutralising antibody, competitive ligand-binding", "FDA 2019", "Per batch", "50 µL", "GLP/GCP target", "Non-cell CLB format when mechanism allows.", "ECL platform", ml("nab-cell-based-assay")),
           ("Biomarker assays", "ICH M10 (context), FDA BMV 2018", "Project", "Per assay", "Fit for purpose", "Context-of-use validation for exploratory and decision-making biomarkers.", "Various", ""),
           ("Cell-based potency support", "ICH Q6B", "Project", "Product", "GMP", "Shared cell culture capability with release potency assays.", "Cell culture", ml("cell-based-potency")),
           ("Incurred sample reanalysis", "ICH M10", "Per study", "Study samples", "GLP/GCP target", "ISR on up to 10% of samples (first 1,000) plus 5% thereafter.", "As method", ""),
           ("Long-term stability in matrix", "ICH M10", "Per time point", "QCs in matrix", "GLP/GCP target", "Covers the full storage period of study samples.", "−80 °C freezers", "")],
    reg="ICH M10 (adopted 2022) harmonises bioanalytical method validation for FDA, EMA, PMDA and CDSCO submissions.",
    ins_h="Mass spectrometers, ECL readers and freezers that never go quiet.",
    ins=([("inst-lcms", "Triple quadrupole LC-MS/MS", ["pg/mL sensitivity", "UHPLC front end", "Stable-isotope internal standards"]),
          ("lab-plate-pink", "Ligand-binding platforms", ["ECL and colorimetric readers", "Automated plate washers", "Liquid-handling robots"]),
          ("lab-pipette-vials", "Sample preparation", ["SPE, LLE and immunocapture", "96-well automation", "Barcoded chain of custody"]),
          ("lab-sample-rack", "Sample management", ["−80 °C with alarms", "Freeze-thaw tracking", "Courier dry-ice receipt"]),
          ("bio-cells-pink", "Cell-based NAb", ["Reporter gene and proliferation assays", "Cell banks qualified", "Drug-tolerance studies"])], 47, "of planned bioanalytical capacity"),
    tiers=(15, 8, 4),
    samp_l="Clinical samples arrive frozen on dry ice with a manifest that matches every tube.",
    samp=["Sample manifest matching tube labels exactly", "Shipped on dry ice with a temperature logger", "Collection anticoagulant and tube type stated", "Positive control antibody or reference standard supplied", "Study protocol and analysis plan shared", "Courier booked Monday to Wednesday to avoid weekend holds"],
    how_h="From freezer to final table.",
    how=[("Plan", "We agree the analysis plan, cut-point strategy and reporting format.", "docs-papers", "sealed"),
         ("Receive", "Dry-ice boxes checked, tubes reconciled against the manifest, stored at −80 °C.", "lab-sample-rack", "opened"),
         ("Analyse", "Runs with calibrators and QCs; accepted against M10 criteria.", "inst-lcms", "instrument"),
         ("Report", "Concentration tables, ISR, ADA status per subject and an audit-ready report.", "lab-analyst-pc", "reported")],
    chip=("3 wk", "ADA method validated in three weeks", "<p>An illustrative example: a bridging ADA assay with acid dissociation validated in three weeks, with drug tolerance shown at expected trough concentrations.</p>"),
    scope=[["Bioanalytical validation", "ICH M10", "GLP / GCP"], ["Immunogenicity", "FDA 2019 guidance", "GLP / GCP"], ["Sample management", "21 CFR Part 11", "GCP"]],
    gal=GALLERY(["lab-pipette-blue", "lab-tube-rack", "lab-automation"]),
    faq=[("What does ICH M10 cover?", "<p>Validation and study-sample analysis for chromatographic and ligand-binding assays measuring drugs and metabolites in biological matrices, including ISR, cross-validation and reporting.</p>"),
         ("What is a tiered immunogenicity approach?", "<p>Samples are screened; screen-positives are confirmed by drug inhibition; confirmed positives are titred and tested for neutralising activity. Each tier uses a statistically derived cut point.</p>"),
         ("How is the screening cut point set?", "<p>From drug-naive samples, usually 50 or more individuals, targeting a 5% false-positive rate so that true positives are not missed.</p>"),
         ("What is drug tolerance?", "<p>The drug concentration at which the assay still detects ADA. Acid dissociation and other pre-treatments improve it.</p>"),
         ("Do you run incurred sample reanalysis?", "<p>Yes: 10% of samples up to 1,000 and 5% beyond, as M10 requires. Two thirds must agree within 20% for chromatographic assays and 30% for ligand-binding assays.</p>"),
         ("LC-MS/MS or ligand binding for a biologic?", "<p>Ligand binding is the default for most proteins; LC-MS/MS with signature peptides helps when reagents are poor or specificity is critical.</p>"),
         ("How long are samples stored?", "<p>As your protocol and contract say, at −80 °C with alarmed monitoring. Long-term stability in matrix must cover the storage period.</p>"),
         ("Can you transfer a method from another lab?", "<p>Yes, with partial validation or cross-validation as M10 describes.</p>")],
    tool=("Signature tool", "ADA Tiered Testing Visualiser", "See how many samples flow through each tier from your study size and positive rate.", ADA),
    guides_h="Immunogenicity and bioanalysis, in plain words.",
    guides=[("Immunogenicity risk assessment, explained", "<p>Start with the molecule (sequence, aggregates, impurities), the patient (immune status, disease) and the treatment (route, frequency, duration). Higher risk drives earlier and more frequent ADA sampling and a NAb assay that reflects the mechanism.</p>", ""),
            ("ICH M10 key points", "<p>One guideline for chromatographic and ligand-binding assays. Full validation covers selectivity, specificity, matrix effect, calibration, accuracy and precision, carry-over, dilution integrity and stability. Accuracy acceptance: ±15% (±20% at LLOQ) for chromatography; ±20% (±25% at LLOQ and ULOQ) for ligand binding.</p>", ""),
            ("Bioanalytical method validation checklist", "<p>Reference standard with CoA. Blank matrix from at least six sources. Stable-isotope internal standard where possible. Stability: bench-top, freeze-thaw, long-term, stock solution, processed sample. A written plan before the first run.</p>", "")],
    band=BAND("lab-sample-rack", "Clear answers from complex samples.", "", BTN("Plan a study", "/book-a-call.html")),
    related=["biologics-characterization-release", "method-development-validation", "cell-gene-therapy-testing"],
    cta=("Clear answers from complex samples.", "Share your protocol and sample numbers. We propose a validation plan and timeline within two business days."),
))

# =====================================================================================
# 11. Reference Standards and Excipient Testing
# =====================================================================================
EXC = [
 ("Microcrystalline cellulose", "Microcrystalline Cellulose", "Cellulose, microcrystalline", "Microcrystalline Cellulose", "Identification, pH, conductivity, loss on drying, degree of polymerisation, bulk density, microbial limits"),
 ("Lactose monohydrate", "Lactose Monohydrate", "Lactose monohydrate", "Lactose Hydrate", "Identification (IR), clarity and colour, specific rotation, water (KF), protein and light-absorbing impurities, microbial limits"),
 ("Magnesium stearate", "Magnesium Stearate", "Magnesium stearate", "Magnesium Stearate", "Identification, acidity/alkalinity, cadmium, lead and nickel, loss on drying, fatty acid composition (GC), assay (Mg)"),
 ("Povidone", "Povidone", "Povidone", "Povidone", "Identification, K-value, aldehydes, peroxides, hydrazine, vinylpyrrolidinone, nitrogen content"),
 ("Croscarmellose sodium", "Croscarmellose Sodium", "Croscarmellose sodium", "Croscarmellose Sodium", "Identification, pH, sodium chloride and glycolate, settling volume, degree of substitution, loss on drying"),
 ("Sodium starch glycolate", "Sodium Starch Glycolate", "Sodium starch glycolate (type A / type B)", "Sodium Starch Glycolate", "Identification, pH, iron, sodium chloride and glycolate, loss on drying, assay (Na)"),
 ("Hypromellose", "Hypromellose", "Hypromellose", "Hypromellose", "Identification, viscosity, substitution type (methoxy, hydroxypropoxy by GC), loss on drying"),
 ("Mannitol", "Mannitol", "Mannitol", "D-Mannitol", "Identification, related substances (HPLC), reducing sugars, nickel, bacterial endotoxins for parenteral grade"),
 ("Sucrose", "Sucrose", "Sucrose", "Sucrose", "Identification, specific rotation, conductivity, dextrins, reducing sugars, sulfite, endotoxins for parenteral grade"),
 ("Polysorbate 80", "Polysorbate 80", "Polysorbate 80", "Polysorbate 80", "Identification, fatty acid composition, ethylene oxide and dioxan, peroxide value, acid and hydroxyl value, water"),
 ("Talc", "Talc", "Talc", "Talc", "Identification, absence of asbestos (XRD, microscopy), acid-soluble substances, lead and other elements, microbial limits"),
 ("Colloidal silicon dioxide", "Colloidal Silicon Dioxide", "Silica, colloidal anhydrous", "Light Anhydrous Silicic Acid", "Identification, pH, loss on ignition, assay (SiO2)"),
 ("Maize starch", "Corn Starch", "Maize starch", "Corn Starch", "Identification, pH, iron, oxidising substances, sulfur dioxide, loss on drying, microbial limits"),
 ("Glycerin", "Glycerin", "Glycerol", "Concentrated Glycerin", "Identification including diethylene glycol and ethylene glycol limit (GC), related substances, halogenated compounds, water"),
 ("Titanium dioxide", "Titanium Dioxide", "Titanium dioxide", "Titanium Oxide", "Identification, water-soluble substances, aluminium oxide and silica, elements, assay. Note: no longer authorised as a food additive in the EU (E171)"),
 ("Macrogol / PEG", "Polyethylene Glycol", "Macrogols", "Macrogol 400 / 4000 / 6000 (by grade)", "Identification, viscosity, average molecular mass, ethylene oxide and dioxan, ethylene glycol and diethylene glycol, formaldehyde"),
]
EXCJ = json.dumps([dict(n=a, us=b, eu=c, jp=d, t=e) for a, b, c, d, e in EXC])
XC = (f'<div class="sv2-xc" data-sv2="xc" data-x="{html.escape(EXCJ)}"><div class="sv2-in">'
      '<label><span>Excipient</span><input list="sv2-xl" data-x="q" placeholder="Start typing, e.g. lactose" autocomplete="off"><datalist id="sv2-xl">' + "".join(f"<option>{a}</option>" for a, *_ in EXC) + '</datalist></label>'
      '<label><span>Market</span><select data-x="m"><option value="us">United States (USP-NF)</option><option value="eu">Europe (Ph. Eur.)</option><option value="jp">Japan (JP)</option><option value="all">Global filing (all three)</option></select></label></div>'
      '<div class="sv2-xo" aria-live="polite"><p class="cn">Choose an excipient to see the monograph names and key tests.</p></div></div>'
      '<p class="cn">Monograph titles as published in USP-NF, Ph. Eur. and JP; tests are the key ones, not the full monograph. Many of these are harmonised through the Pharmacopoeial Discussion Group. '
      'Indian Pharmacopoeia titles often follow the same naming; we confirm the current edition for each order.</p>')

build("reference-standards-excipients", dict(
    lede="Compendial testing of excipients, APIs and reference standards to USP-NF, Ph. Eur., JP and IP, plus in-house standard qualification.",
    answer="We release raw materials and excipients against USP-NF, Ph. Eur., JP and IP monographs, qualify in-house and secondary reference standards against primary standards, and support supplier qualification with full and reduced testing. Identity by FTIR or Raman; purity by HPLC, GC and ICP-MS; water by Karl Fischer.",
    chips=[("4 pharmacopoeias", "USP-NF, Ph. Eur., JP, IP"), ("3 to 10 d", "typical release"), ("DEG/EG", "screening on glycerin")],
    visual=V_XRPD, vchips=[("FTIR", "Identity"), ("KF", "Water"), ("XRPD", "Form"), ("ICP-MS", "Q3D")],
    tests_h="Full monographs, reduced testing, and the risky tests that matter most.",
    tests=[("Full compendial monograph testing", "USP-NF, Ph. Eur., JP, IP", "5 to 10 d", "50 to 100 g", "ISO 17025 target", "Every test in the current monograph, reported against the edition you specify.", "Full QC suite", ""),
           ("Identity by FTIR", "USP <197>, Ph. Eur. 2.2.24", "1 to 2 d", "1 g", "ISO 17025 target", "ATR or KBr against a reference spectrum.", "FTIR", ml("ftir-identification")),
           ("Identity by Raman (container-through)", "USP <1120>, Ph. Eur. 2.2.48", "Same day", "Container", "Validation per material", "Handheld Raman for 100% container identity at receipt.", "Handheld Raman", ml("raman-identification")),
           ("Assay and related substances", "USP <621>, Ph. Eur. 2.2.46", "3 to 5 d", "5 g", "ISO 17025 target", "HPLC or UPLC to the monograph method.", "HPLC, UPLC", ml("hplc-assay-related-substances")),
           ("Water content, Karl Fischer", "USP <921>, Ph. Eur. 2.5.12", "1 to 2 d", "5 g", "ISO 17025 target", "Volumetric or coulometric KF.", "KF titrators", ml("water-content-karl-fischer")),
           ("Residual solvents", "USP <467>, ICH Q3C", "3 to 5 d", "2 g", "ISO 17025 target", "Headspace GC for Class 1, 2 and 3 solvents.", "HS-GC-FID", ml("residual-solvents-gc-hs")),
           ("Elemental impurities", "USP <232>/<233>, ICH Q3D", "3 to 5 d", "2 g", "ISO 17025 target", "Risk-based elemental testing by ICP-MS.", "ICP-MS", ml("elemental-impurities-icp-ms")),
           ("DEG and EG in glycerin and high-risk excipients", "USP Glycerin monograph, WHO alerts", "2 to 3 d", "10 mL", "ISO 17025 target", "GC limit test for diethylene glycol and ethylene glycol (0.10% each in USP).", "GC-FID", ""),
           ("Polymorph and crystallinity", "USP <941>, Ph. Eur. 2.9.33", "3 to 5 d", "1 g", "ISO 17025 target", "XRPD for form identity and amorphous content.", "XRPD", ml("xrpd-polymorph")),
           ("Particle size", "USP <429>, Ph. Eur. 2.9.31", "2 to 3 d", "10 g", "ISO 17025 target", "Laser diffraction with validated dispersion.", "Laser diffraction", ml("particle-size-laser-diffraction")),
           ("Microbial limits", "USP <61>/<62>", "5 to 7 d", "10 g", "ISO 17025 target", "TAMC, TYMC and specified organisms.", "Microbiology suite", ml("bioburden")),
           ("Reference standard qualification", "USP <11>, WHO TRS 943 Annex 3", "2 to 4 wk", "1 to 5 g", "GMP", "Identity, purity by mass balance or qNMR, water, residue on ignition, assigned content with uncertainty and retest date.", "HPLC, NMR, KF, TGA", ml("uplc-impurity-profiling"))],
    reg="Release against the pharmacopoeia your marketing authorisation cites; for multi-market products we test once against the strictest combined requirement where monographs differ.",
    ins_h="A full QC suite for the ingredients that go into everything.",
    ins=([("lab-glassware", "Wet chemistry", ["Titrations, limit tests, clarity and colour", "Calibrated volumetric glassware", "Second-person verification"]),
          ("inst-hplc", "HPLC and UPLC", ["Monograph methods as written", "Column inventory per monograph", "Empower-style audit trails"]),
          ("inst-gc", "GC and headspace GC", ["USP <467> procedures", "DEG/EG limit tests", "FID and MS detectors"]),
          ("inst-icp", "ICP-MS", ["ICH Q3D elements", "Microwave digestion", "USP <233> validated"]),
          ("lab-microscopes-row", "Physical testing", ["XRPD, laser diffraction", "Bulk and tapped density", "Microscopy"])], 58, "of planned QC chemistry capacity"),
    tiers=(10, 5, 2),
    samp_l="Tell us the monograph edition you release against; it changes the method.",
    samp=["Excipient name, grade and supplier lot number", "Pharmacopoeia and edition to test against", "At least 3x the quantity needed for one full test", "Supplier CoA included", "Stored as labelled (some grades are hygroscopic)", "Reduced-testing rationale, if you use one"],
    how_h="From warehouse sample to release CoA.",
    how=[("Submit", "Order full or reduced testing; tell us the edition.", "lab-analyst-pc", "sealed"),
         ("Receive", "Identity by Raman through the container where validated.", "log-warehouse", "opened"),
         ("Test", "Monograph tests run in parallel; out-of-specification results trigger a phase I investigation.", "lab-glassware", "instrument"),
         ("Release", "CoA lists every test, the edition and the result against the limit.", "lab-goggles", "reported")],
    chip=("1 lot stopped", "DEG found in a supplier's glycerin", "<p>An illustrative example of why the DEG/EG limit test matters: a lot that passed the supplier CoA failed our GC limit test and never reached manufacturing.</p>"),
    scope=[["Compendial excipient testing", "USP-NF, Ph. Eur.", "ISO/IEC 17025"], ["Elemental impurities", "USP <232>/<233>", "ISO/IEC 17025"], ["Reference standard qualification", "USP <11>", "GMP"]],
    gal=GALLERY(["pharma-capsules", "lab-flasks-pour", "pharma-tubes"]),
    faq=[("Do I need full monograph testing on every lot?", "<p>Not always. After supplier qualification, many companies use reduced testing (identity plus selected tests) with periodic full testing, justified by supplier data and audits. Regulators expect identity on every container for some materials.</p>"),
         ("Which pharmacopoeia should I test against?", "<p>The one cited in your marketing authorisation. For global products we can test against several and report each result against each limit.</p>"),
         ("Why test glycerin for DEG and EG?", "<p>Diethylene glycol contamination of glycerin and other excipients has caused deaths in several countries. USP requires a DEG and EG limit test in the Glycerin monograph identification, at 0.10% each.</p>"),
         ("Can you qualify a working reference standard?", "<p>Yes: identity, purity, water, residue, assigned content with uncertainty against a primary standard, and a retest date.</p>"),
         ("What is pharmacopoeial harmonisation?", "<p>The Pharmacopoeial Discussion Group (USP, Ph. Eur., JP, with IP joining in 2023) harmonises selected excipient monographs and general chapters so one test satisfies all three.</p>"),
         ("Can you test APIs too?", "<p>Yes, against compendial monographs or your specification, including related substances, residual solvents and elemental impurities.</p>"),
         ("Do you do identity on every container?", "<p>Yes, with handheld Raman through the bag or bottle where the method is validated for that material.</p>"),
         ("What if my supplier CoA and your result disagree?", "<p>We investigate our result first, then share data so you can raise it with the supplier.</p>")],
    tool=("Signature tool", "Excipient Compendial Checker", "Pick an excipient and market; see the monograph title and the key tests.", XC),
    guides_h="Why every ingredient deserves your attention.",
    guides=[("Why supplier audits are not enough", "<p>An audit shows a system on the day you visit. Testing shows the material in your hand. Use both: audits set your confidence, testing confirms each lot, and trending catches drift.</p>", ""),
            ("Counterfeit and adulterated excipient risks", "<p>Glycerin, propylene glycol and sorbitol solutions have been adulterated with DEG and EG. Heparin was adulterated with oversulphated chondroitin sulphate in 2008. High-value or high-volume liquid excipients deserve specific tests, not only identity.</p>", ""),
            ("Pharmacopoeial harmonisation explained", "<p>Harmonised monographs and chapters (such as &lt;61&gt;, &lt;62&gt;, dissolution and many excipients) mean one test result can support filings in the US, EU and Japan. Check the harmonisation status in each pharmacopoeia, because local additions can remain.</p>", "")],
    band=BAND("pharma-pills-mix", "Trust every ingredient.", "", BTN("Send a test list", "/request-quote.html?service=10")),
    related=["small-molecule-qc-release", "method-development-validation", "extractables-leachables"],
    cta=("Trust every ingredient.", "Send your excipient list and the pharmacopoeias you file against. We price full and reduced testing side by side."),
))

# =====================================================================================
# 12. Regulatory and Data Integrity Support
# =====================================================================================
_q = ["Every user on every instrument and LIMS has a unique login (no shared accounts).", "Audit trails are switched on and reviewed before results are approved.",
      "Manual integration is controlled by SOP and every instance is justified.", "Raw data, including aborted runs, is retained and reviewable.",
      "OOS results always trigger a documented Phase I lab investigation.", "System clocks cannot be changed by analysts.",
      "Data backup and restore have been tested in the last 12 months.", "A data integrity risk assessment covers every GxP computerised system."]
IRS = ('<div class="sv2-irs" data-sv2="irs"><ol class="sv2-qs">' + "".join(
    f'<li><p>{q}</p><div role="radiogroup" aria-label="Answer">' + "".join(f'<label><input type="radio" name="sv2q{i}" value="{v}"><span>{t}</span></label>' for v, t in [(2, "Yes"), (1, "Partly"), (0, "No")]) + '</div></li>' for i, q in enumerate(_q))
       + '</ol><div class="sv2-out" aria-live="polite"><span class="k">Readiness score</span><b data-i="s">Answer all 8</b><p data-i="t"></p>'
       '<a class="btn" href="/tools/inspection-readiness-score.html">Take the full 20-question assessment</a></div></div>'
       '<p class="cn">A short self-check, not an audit. Nothing you choose here leaves your browser.</p>')

build("regulatory-data-integrity-support", dict(
    lede="Mock inspections, ALCOA+ data integrity gap assessments, CTD Module 3 analytical sections and OOS investigation support, from people who have sat across the table from inspectors.",
    answer="We help QC labs and manufacturers prepare for and answer inspections: mock inspections, data integrity gap assessments against ALCOA+, CTD Module 3 analytical sections, responses to regulatory queries, and support on deviations and OOS investigations. Our advice is grounded in published FDA, MHRA, PIC/S and WHO guidance.",
    chips=[("ALCOA+", "gap assessments"), ("Module 3", "CTD authoring"), ("1 to 6 wk", "typical engagement")],
    visual=V_DOSS, vchips=[("PIC/S", "PI 041-1"), ("MHRA", "GxP DI 2018"), ("FDA", "DI Q&A 2018"), ("CTD", "Module 3")],
    tests_h="Engagements, not just tests.",
    tests=[("Mock inspection", "FDA, EMA, MHRA, CDSCO practice", "2 to 5 d on site", "Site access", "Project", "Inspector-style walkthrough of QC and QA with daily debriefs and a written findings report graded critical, major and other.", "Audit team", ""),
           ("Data integrity gap assessment", "PIC/S PI 041-1, MHRA 2018, FDA 2018", "1 to 3 wk", "Systems list, SOPs", "Project", "System-by-system review of access, audit trails, backups, review practice and culture against ALCOA+.", "Audit team", ""),
           ("Audit trail review programme", "FDA DI guidance 2018", "2 wk", "System exports", "Project", "Risk-based audit trail review SOP and training for reviewers.", "CDS, LIMS", ""),
           ("CTD Module 3 analytical sections", "ICH M4Q", "2 to 6 wk", "Methods, validation data", "Project", "3.2.S.4 and 3.2.P.5 sections: procedures, validation summaries, batch analyses, justification of specifications.", "Regulatory writers", ""),
           ("Response to regulatory queries", "FDA, EMA, CDSCO", "Per deadline", "Query letter", "Project", "Scientific response drafting, with new data generated in our labs if needed.", "Writers, labs", ""),
           ("OOS investigation support", "FDA OOS guidance 2022, MHRA", "Per case", "Data and records", "Project", "Phase I and Phase II investigations, root cause analysis, retest and resample justification.", "Senior analysts", ml("hplc-assay-related-substances")),
           ("Deviation and CAPA support", "ICH Q10", "Per case", "Records", "Project", "Root cause tools and effectiveness checks.", "QA team", ""),
           ("Method validation package review", "ICH Q2(R2), Q14", "1 to 2 wk", "Protocols and reports", "Project", "Gap review before submission.", "Method lifecycle team", ml("forced-degradation")),
           ("Tech transfer support", "WHO TRS 961 Annex 7", "4 to 8 wk", "Methods and specs", "Project", "Transfer protocols, comparative testing and reports.", "Labs", ""),
           ("Computerised system validation review", "GAMP 5 (2nd ed.), Annex 11, Part 11", "2 to 4 wk", "Validation records", "Project", "Risk-based review of CSV for CDS and LIMS.", "CSV specialists", ""),
           ("Training: data integrity for analysts", "PIC/S, WHO TRS 996 Annex 5", "1 d", "On site or remote", "Project", "Practical training with real chromatography examples.", "Trainers", "")],
    reg="Our checklists draw on FDA, MHRA, PIC/S, WHO and EU GMP Chapter 4 and Annex 11. We tailor to the regulator you expect next.",
    mid=SPLIT("docs-papers", H3("What an inspector actually looks at") + UL(["Audit trails on chromatography data systems, including deleted and reprocessed injections", "Who can change system time and delete data", "Orphan data: injections that never made it into a result", "Paper records issued and reconciled", "How OOS results were closed, and how often retests passed", "Training records against the SOPs people actually used"])),
    ins_h="Tools of the trade: people, checklists and data.",
    ins=([("biz-team-laptops", "Audit team", ["Former QC heads and QA leads", "Native-language interviews", "Daily debriefs"]),
          ("docs-papers", "Checklists", ["Mapped to PIC/S PI 041-1", "System-by-system", "Graded findings"]),
          ("lab-analyst-pc", "Data reviewers", ["Audit trail forensics", "CDS and LIMS expertise", "Sampling of real records"]),
          ("sec-servers", "IT and CSV", ["Backup and restore tests", "Access reviews", "GAMP 5 risk approach"]),
          ("pharma-team", "Trainers", ["Analyst and reviewer training", "Case-based", "Competency checks"])], 40, "of planned advisory days committed"),
    tiers=(20, 10, 5),
    samp_l="Before a mock inspection we ask for a short document pack.",
    samp=["Site master file or lab overview", "List of GxP computerised systems", "Key SOPs: data review, OOS, audit trail review", "Last two inspection reports and responses", "Organisation chart for QC and QA", "Named site contact for the visit"],
    how_h="From kick-off to closed findings.",
    how=[("Scope", "We agree the regulator, systems and products in scope.", "biz-team-laptops", "sealed"),
         ("Review", "Documents and data reviewed before arrival.", "docs-papers", "opened"),
         ("Inspect", "On-site mock inspection with daily debriefs.", "lab-team-three", "instrument"),
         ("Report", "Graded findings and a CAPA plan you can act on.", "lab-analyst-pc", "reported")],
    chip=("12 to 2", "Findings cut before a pre-approval inspection", "<p>An illustrative example: a mock inspection raised 12 findings; by the real inspection, the site had closed ten and had evidence-backed plans for two.</p>"),
    scope=[["Quality management", "ISO 9001", "Group roadmap"], ["Computerised systems", "Annex 11, Part 11", "Internal validation"], ["Audit programme", "ICH Q10", "Internal"]],
    gal=GALLERY(["lab-analyst-pc", "sec-servers", "biz-team-laptops"]),
    faq=[("What is ALCOA+?", "<p>Data should be Attributable, Legible, Contemporaneous, Original and Accurate, plus Complete, Consistent, Enduring and Available. It is the vocabulary regulators use for data integrity.</p>"),
         ("How long does a mock inspection take?", "<p>Two to five days on site for a QC laboratory, plus document review beforehand and a report within ten working days.</p>"),
         ("Will a mock inspection be the same as the real one?", "<p>No mock inspection can predict a real one. We use the same techniques and published expectations, and we tell you plainly what we find.</p>"),
         ("Can you write CTD Module 3 analytical sections?", "<p>Yes: 3.2.S.4 and 3.2.P.5 in particular, from your validation and batch data, written to ICH M4Q.</p>"),
         ("What are the most common data integrity findings?", "<p>Shared logins, disabled or unreviewed audit trails, uncontrolled manual integration, deleted or orphan data, and missing reconciliation of paper records.</p>"),
         ("Do you help with OOS investigations?", "<p>Yes, following FDA's OOS guidance (revised 2022): a Phase I laboratory investigation before any retest, then a full-scale Phase II if no lab error is confirmed.</p>"),
         ("Do you give regulatory advice?", "<p>We give technical and compliance support based on published guidance. Regulatory strategy decisions remain yours and your regulatory affairs team's.</p>"),
         ("Is our information kept confidential?", "<p>Yes, under a confidentiality agreement signed before any document is shared.</p>")],
    tool=("Signature tool", "Inspection Readiness Score (short version)", "Eight questions. An honest score in under two minutes.", IRS),
    guides_h="Inspection readiness, condensed.",
    guides=[("Top 10 data integrity findings and how to prevent them", "<p>1 shared accounts; 2 audit trails off; 3 audit trails not reviewed; 4 trial injections; 5 uncontrolled manual integration; 6 deleted data; 7 time changes; 8 uncontrolled blank forms; 9 backup never restored; 10 OOS invalidated without evidence. Each one has a technical fix and a behavioural one.</p>", "/insights/data-integrity-top-10-findings.html"),
            ("How to prepare for an FDA pre-approval inspection", "<p>FDA's PAI programme (CP 7346.832) checks readiness for commercial manufacture, conformance to the application and data integrity. Check that every number in Module 3 traces to raw data, that methods in the dossier match methods in use, and that people can explain their own data.</p>", ""),
            ("OOS investigation walkthrough", "<p>Stop. Preserve everything. Analyst and supervisor review the obvious: calculations, solutions, instrument, system suitability. If a lab error is proven, invalidate and retest. If not, Phase II widens to manufacturing. Never test into compliance.</p>", "")],
    band=BAND("docs-papers", "Be inspection-ready on any day.", "", BTN("Book a quality call", "/book-a-call.html")),
    related=["method-development-validation", "environmental-monitoring", "reference-standards-excipients"],
    cta=("Be inspection-ready on any day.", "Tell us which regulator and when. We propose a mock inspection or gap assessment within two business days."),
))
