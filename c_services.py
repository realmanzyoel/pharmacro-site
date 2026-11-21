"""Services hub, bundles, compare, and service pages 1-6 (blueprint 4.3, 4.4, 4.5).
Behaviour for the local widgets (.sv1-*) lives in assets/m_services.js; styles in assets/m_services.css."""
from ph import *

CR = [("Services", "/services/index.html")]
def ML(slug): return f"/method-library/{slug}.html"
def AR(slug): return f"/insights/{slug}.html"
def J(o): return html.escape(json.dumps(o, ensure_ascii=False))

# ---------- local components ----------
def SLIDER(slides, gauge_pct, gauge_label, gauge_note):
    """Instrument image slider with spec overlays + an animated capacity gauge. slides: (img, name, [specs])."""
    s = "".join(f'<figure class="sv1-sl-i{" on" if i == 0 else ""}" data-i="{i}"><img src="/img/{im}.jpg" alt="{alt(im)}" loading="lazy">'
                f'<figcaption><b>{n}</b><ul>{"".join(f"<li>{x}</li>" for x in sp)}</ul></figcaption></figure>' for i, (im, n, sp) in enumerate(slides))
    dots = "".join(f'<button type="button" aria-label="Show {n}"{" aria-current=true" if i == 0 else ""} data-i="{i}"></button>' for i, (im, n, sp) in enumerate(slides))
    return (f'<div class="sv1-ins"><div class="sv1-sl" aria-roledescription="carousel" aria-label="Instruments">{s}'
            f'<div class="sv1-sl-n"><button type="button" class="sv1-p" aria-label="Previous instrument">&larr;</button><div class="sv1-d">{dots}</div><button type="button" class="sv1-n" aria-label="Next instrument">&rarr;</button></div></div>'
            f'<div class="sv1-g reveal" style="--p:{gauge_pct}"><svg viewBox="0 0 200 120" aria-hidden="true"><path class="sv1-gt" d="M20 110A80 80 0 0 1 180 110" pathLength="100"/><path class="sv1-gf" d="M20 110A80 80 0 0 1 180 110" pathLength="100"/></svg>'
            f'<b>{gauge_pct}%</b><span>{gauge_label}</span><p class="cn">{gauge_note} {ILL("Planned capacity")}</p></div></div>')

def GUIDES(items):
    """Standout content: short substantive guides. items: (title, html, link or '')."""
    return '<div class="sv1-gd">' + "".join(f'<article class="sv1-gi reveal" style="--i:{i}"><h3>{t}</h3>{b}' + (f'<p><a href="{l}">Read the full guide &rsaquo;</a></p>' if l else "") + '</article>'
                                          for i, (t, b, l) in enumerate(items)) + "</div>"

def TOOLBOX(eyebrow, title, lede, inner):
    return f'<section class="sv1-tool reveal">{EY(eyebrow)}<h2>{title}</h2><p class="lede">{lede}</p>{inner}</section>'

def svc_page(slug, lede, chips, visual, vchips, tests, regs_note, slides, gauge, samples, vial, proof, faqs, tool, guides, related, cta, img=None, extra_top="", extra_mid=""):
    s = SVC[slug]; idx = SERVICES.index(s); n = SCI[s[8]][0]
    hb = (f'<a class="btn big mag" href="/request-quote.html?service={idx}"><span>Request a quote</span></a> '
          f'<a class="btn o big" href="mailto:{MAIL}?subject={html.escape("Question for " + n)}">Ask {n.replace("Dr ", "").split()[0]}</a>')
    body = (ANSWER(lede[1]) + SVCHEAD(slug, visual, vchips) + extra_top
            + SH("What we test", f"{len(tests)} tests, each with its standard, turnaround and sample need.", "Search or filter by standard. Open any row for the method summary, instruments and the Method Library entry.")
            + TESTS(tests, id="t-" + slug)
            + SH("Regulatory coverage", "Written for the regulator who will read your file.", regs_note) + REGBADGES()
            + SH("Instruments and capability", "Named instruments. Real capacity.", "Every site runs the same platforms on the same software, so a method validated in one lab runs identically in the next.")
            + SLIDER(slides, *gauge)
            + SH("Turnaround tiers", "Pick a tier. See your date.", "Business days from sample receipt and acceptance.") + TIERS()
            + SH("Sample requirements", "Ship it right the first time.", "Tick each item as you prepare the shipment. When everything is ticked, the shipping label request unlocks.")
            + CHECKRING(samples, "Before you ship")
            + SH("How it works", "Four steps, one named owner at each.") + VIAL(vial)
            + extra_mid
            + SH("Proof", "Evidence, not adjectives.") + '<div class="two"><div>' + proof[0] + f'<p class="cn">Accreditation scope: {proof[1]} {ILL("Target scope")} Final scope per site on the <a href="/quality/accreditations.html">accreditation wall</a>.</p></div><div>' + SCICARD(s[8]) + QUOTE(proof[2], f"{n} {ILL('Illustrative')}") + '</div></div>'
            + tool
            + SH("Guides", "What our scientists get asked most.") + GUIDES(guides)
            + SH("FAQ", "Questions, answered first.") + FAQS(faqs, "faq")
            + RELATED(related))
    page(f"services/{slug}", s[1], lede[0], body, img=img or s[4], chips=chips, crumbs=CR, cta=cta, hb=hb,
         jsonld=[{"@context": "https://schema.org", "@type": "Service", "name": s[1], "serviceType": "Pharmaceutical analytical testing", "provider": {"@type": "Organization", "name": BRAND},
                  "description": re.sub("<[^>]+>", "", lede[1]), "areaServed": ["India", "Southeast Asia", "Europe", "United States"]}])

BUNDLE_DATA = [
 ("Biosimilar Comparability Program", "Analytical similarity against the reference product, from lot sourcing to a submission-ready report.",
  ["biologics-characterization-release", "bioanalytical-immunogenicity", "stability-studies", "method-development-validation"], "10 to 16 weeks", "biologics-characterization-release",
  "Biosimilar developers preparing an FDA 351(k) or EMA similarity package, and biologics makers proving comparability after a process change (ICH Q5E).",
  [("Reference lot sourcing and intake", 0, 2), ("Method qualification (charge, size, glycans, potency)", 1, 4), ("Side-by-side testing, 3+ lots each", 4, 6), ("Forced degradation comparison", 6, 4), ("Statistics and tiered evaluation", 10, 3), ("Report and data package", 12, 2)], 14,
  ["Attribute risk ranking and tier assignment", "Side-by-side data for 3 or more lots of each product", "Equivalence and quality-range analysis", "Forced degradation overlay", "CTD-ready report and raw data in the portal"], "USD 180,000 to 420,000"),
 ("Tech Transfer Package", "Move a method from your lab or another CRO into ours, with a protocol, comparative testing and a signed report.",
  ["method-development-validation", "small-molecule-qc-release", "regulatory-data-integrity-support"], "4 to 8 weeks", "method-development-validation",
  "Sponsors changing testing partner, CDMOs taking on a new product, and anyone adding a second site for supply security.",
  [("Gap review of the sending lab's method and history", 0, 1), ("Transfer protocol with acceptance criteria", 1, 1), ("Training runs and system suitability", 2, 1), ("Comparative testing (both labs, same lots)", 3, 2), ("Report, deviations and sign-off", 5, 1)], 8,
  ["Risk-based transfer plan (USP ⟨1224⟩)", "Pre-agreed acceptance criteria", "Comparative or covalidation data", "Signed transfer report", "Method entered in the LIMS for routine use"], "USD 12,000 to 45,000 per method"),
 ("Launch Readiness Package", "Everything a product needs analytically between process validation and first commercial release.",
  ["small-molecule-qc-release", "stability-studies", "microbiology-sterility", "regulatory-data-integrity-support"], "8 to 14 weeks", "small-molecule-qc-release",
  "Generic and specialty manufacturers in the last six months before a launch date, especially for a new market.",
  [("Specification and method readiness review", 0, 2), ("Validation gaps closed", 2, 4), ("PPQ batch release testing", 4, 3), ("Stability programme set up (commitment batches)", 5, 2), ("Mock pre-approval inspection", 8, 2), ("Release-ready sign-off", 10, 2)], 12,
  ["Specification and method gap report", "Validated release methods", "PPQ batch results", "Commitment stability started", "Mock inspection report with CAPA list"], "USD 60,000 to 180,000"),
 ("Annual Stability Programme", "A year of ICH stability across your portfolio at a fixed price per pull, with trending every quarter.",
  ["stability-studies", "small-molecule-qc-release", "method-development-validation"], "12 months, rolling", "stability-studies",
  "Commercial products with ongoing stability commitments, annual product reviews and post-approval changes.",
  [("Protocol harmonisation across products", 0, 4), ("Storage across all zones", 2, 50), ("Quarterly pulls and testing", 12, 40), ("Quarterly OOT trending", 13, 39), ("Annual summary for the APR/PQR", 48, 4)], 52,
  ["Harmonised protocols", "Chamber storage in every climatic zone", "Pull testing to a fixed calendar", "Quarterly trend reports with OOT flags", "Annual summary for product quality review"], "Fixed price per pull, from USD 450"),
 ("Nitrosamine Risk Package", "From risk assessment to confirmatory testing for nitrosamines and NDSRIs, at the acceptable intakes regulators now expect.",
  ["small-molecule-qc-release", "method-development-validation", "regulatory-data-integrity-support"], "3 to 8 weeks", "small-molecule-qc-release",
  "Marketing authorisation holders with outstanding risk assessments, and API and finished-product makers responding to a regulator query.",
  [("Risk assessment (API route, excipients, packaging)", 0, 1), ("Method development for the NDSRI", 1, 2), ("Validation to the required limit", 2, 2), ("Confirmatory testing of 3+ batches", 4, 2), ("Report for the regulator", 6, 1)], 8,
  ["Written risk assessment per FDA and EMA expectations", "Sensitive LC-MS/MS or GC-MS/MS method", "Validation down to the acceptable intake", "Batch results with confirmatory data", "Regulatory response support"], "USD 15,000 to 60,000 per product"),
]

# ---------- services hub ----------
def AVAIL():
    tz = {"Hyderabad": "Asia/Kolkata", "Mumbai": "Asia/Kolkata", "Pune": "Asia/Kolkata", "Bengaluru": "Asia/Kolkata", "Singapore": "Asia/Singapore", "Leiden": "Europe/Amsterdam",
          "Cambridge": "Europe/London", "Dublin": "Europe/Dublin", "New Jersey": "America/New_York"}
    keys = ["arjun", "ananya", "mei", "elena", "kenji", "sara", "james", "helen"]
    c = "".join(f'<a class="sv1-av reveal" style="--i:{i}" href="/book-a-call.html" data-tz="{tz[SCI[k][4]]}"><img src="/img/{SCI[k][3]}.jpg" alt="" loading="lazy"><i class="sv1-dot"></i>'
                f'<b>{SCI[k][0]}</b><span>{SCI[k][2]}</span><small class="sv1-lt">{SCI[k][4]}</small></a>' for i, k in enumerate(keys))
    return f'<div class="sv1-avs">{c}</div><p class="cn">Availability is simulated from each scientist\'s local office hours. {ILL("Illustrative profiles")}</p>'

hub = (ANSWER("PharmaCRO offers twelve analytical testing services that cover a medicine's whole life: small molecule release, stability, method development and validation, biologics, mRNA and vaccines, cell and gene therapy, microbiology, environmental monitoring, extractables and leachables, bioanalysis, excipients and reference standards, and regulatory support. Find yours in two clicks below.")
       + '<div class="sv1-q reveal"><label for="svq">What do you need tested?</label><div><input id="svq" type="search" data-svcq placeholder="Try: dissolution, dsRNA, AAV titre, endotoxin, zone IVb" autocomplete="off" list="svq-l">'
       + '<datalist id="svq-l">' + "".join(f"<option>{t}</option>" for s in SERVICES for t in s[7]) + '</datalist></div><p class="cn">Cards below filter as you type. Matching is done on service names, descriptions and key tests.</p></div>'
       + SH("The lifecycle", "From first batch to final release.", "Scroll and the highlight moves along the lifecycle; the services each stage needs light up.") + LIFECYCLE()
       + SH("All services", "Twelve services. One standard.", "Filter by modality or stage. Every card shows three key tests, the typical turnaround and a quote link.") + SVCGRID()
       + BAND("lab-corridor", "One portal, one data standard, every lab.", "Whichever service you order, results arrive the same way: e-signed, in the portal, with the raw data a click away.", '<a class="btn" href="/portal/index.html">See the portal</a>')
       + SH("Bundles", "Packaged programmes for the moments that matter.", "Hover a bundle to fan out the services inside it.")
       + BUNDLES([(b[0], b[1], b[2], b[3], "/services/bundles.html#b" + str(i + 1)) for i, b in enumerate(BUNDLE_DATA)])
       + SH("Compare services", "Turnaround, sample need and lead labs side by side.", "Click a column header to sort.") + COMPARE()
       + '<p><a class="btn o" href="/services/compare.html">Open the full comparison</a></p>'
       + GALLERY(["inst-hplc", "lab-instrument-load", "micro-petri-1", "vax-vials", "room-clean-2", "inst-lcms"],
                 ["Liquid chromatography for assay and impurities", "Automated sample handling for biologics", "Microbial colonies counted for bioburden", "Vaccine vials awaiting release", "A cleanroom ready for environmental monitoring", "LC-MS for bioanalysis and NDSRIs"])
       + SH("Not sure what you need?", "Talk to a scientist.", "Pick anyone who is online now. A 20-minute scoping call usually saves weeks of back and forth.")
       + AVAIL() + '<p><a class="btn" href="/book-a-call.html">Book a scoping call</a> <a class="btn o" href="/tools/test-finder.html">Use the Test Finder</a></p>')

page("services/index", "Every test your product needs, from first batch to final release.",
     "Twelve services across the whole product lifecycle, one portal and one data standard. Search, filter, compare, or ask a scientist.",
     hub, img="lab-corridor", chips=[("12", "services"), ("500+", "methods (target)"), ("1 LIMS", "across every lab")],
     cta=("Not sure what you need? Talk to a scientist.", "Describe your product and stage. We will tell you plainly which tests you need, which you do not, and what they cost."))

# ---------- bundles ----------
bb = ANSWER("Bundles package the testing a programme needs into one plan, one price and one timeline. There are five: Biosimilar Comparability, Tech Transfer, Launch Readiness, Annual Stability and Nitrosamine Risk. Each lists who it is for, the services inside it, an indicative Gantt chart, deliverables and price guidance.")
bb += BUNDLES([(b[0], b[1], b[2], b[3], f"#b{i + 1}") for i, b in enumerate(BUNDLE_DATA)])
imgs = ["lab-instrument-load", "lab-team-three", "pharma-blisters2", "lab-corridor", "inst-lcms"]
for i, (n, t, ss, w, lead, who, gantt, tot, deliv, price) in enumerate(BUNDLE_DATA):
    idx = SERVICES.index(SVC[lead])
    bb += (f'<section class="sv1-bd" id="b{i + 1}">' + SH(f"Bundle {i + 1} of 5 &middot; {w}", n, t)
           + SPLIT(imgs[i], H3("Who it is for") + P(who) + H3("Services inside") + UL([f'<a href="{svc_url(s)}">{SVC[s][1]}</a>' for s in ss])
                   + H3("Indicative price") + P(f"{price} {ILL('Price guidance only')}") + f'<p><a class="btn" href="/request-quote.html?service={idx}">Request this package</a></p>', flip=bool(i % 2))
           + '<div class="two"><div>' + GANTT(gantt, tot, f"{n}: indicative timeline") + '</div><div class="box">' + H3("Deliverables") + TICKLIST(deliv) + '</div></div></section>')
bb += FAQS([("Can I change what is inside a bundle?", "<p>Yes. Bundles are starting points. A scientist adjusts the scope on the scoping call and the quote shows exactly what changed.</p>"),
            ("Is the bundle price fixed?", "<p>The quote is fixed once the scope is agreed. The ranges on this page are guidance until then, and depend on the number of lots, methods and markets.</p>"),
            ("Do bundles run across several labs?", "<p>Often. All labs run the same SOPs and LIMS, so one project lead and one report cover the whole bundle.</p>"),
            ("What if a result is out of specification?", "<p>We stop, notify you within one business day and open a Phase I laboratory investigation. The timeline in the portal updates so you see the impact.</p>")], "bfaq")
page("services/bundles", "Bundles", "Five packaged programmes, each with one plan, one timeline and one price.", bb, img="lab-team-three",
     chips=[("5", "bundles"), ("3 to 16 wk", "typical duration"), ("1", "project lead")], crumbs=CR,
     cta=("Want a bundle shaped to your programme?", "Tell us the product and the milestone. We will send a scoped plan and a fixed quote."))

# ---------- compare ----------
cb = (ANSWER("This table compares all twelve services on typical turnaround, sample need, regulatory coverage and the labs that lead them. Sort any column. Turnaround is in business days from receipt; sample needs are typical and depend on your specification. Use the guidance below to see which services your modality and stage usually need.")
      + COMPARE()
      + SH("How to read it", "Four columns, four questions.")
      + ICARDS([("clock", "Typical TAT", "Business days from sample receipt and acceptance to an approved report, at the Standard tier. Priority and Critical tiers shorten it."),
                ("vial", "Sample need", "A typical amount for a full specification. Compendial tests with large sample sizes, such as sterility, need more."),
                ("globe", "Regulatory coverage", "The regulators whose expectations the methods are written to. Pharmacopoeia chapters are cited per test on each service page."),
                ("pin", "Lead labs", "Sites planned as centres for that service. Any lab can receive your samples; work routes to the lead lab on the same LIMS.")], 4)
      + SH("Guidance by modality", "What products like yours usually need.")
      + T(["Modality", "Development", "Clinical", "Commercial"],
          [["Small molecule", "Method development, reference standards", "Release, stability, nitrosamine risk", "Release, stability, microbiology, EM"],
           ["Biologic or biosimilar", "Characterisation, method development", "Release, stability, bioanalytical, immunogenicity", "Release, stability, comparability after changes"],
           ["mRNA or vaccine", "Characterisation (cap, poly(A), LNP)", "Release, stability, sterility, endotoxin", "Release, stability, E&L for the container"],
           ["Cell or gene therapy", "Titre and empty/full method development", "Rapid release, potency, safety", "Release, comparability, stability"]])
      + SH("Guidance by stage", "Rigour that matches the phase.")
      + GRID([("Phase 1", "Methods fit for purpose and qualified, not fully validated. Stability supports the clinical shelf life.", "/solutions/clinical-phase-1-3.html", "Clinical stage"),
              ("Phase 3", "Methods validated to ICH Q2(R2) before pivotal batches. Specifications tighten.", "/solutions/clinical-phase-1-3.html", "Clinical stage"),
              ("Commercial", "Validated methods, registered specifications, routine release and ongoing stability.", "/solutions/commercial-release.html", "Commercial release")])
      + FAQS([("Why do turnaround ranges vary so much?", "<p>Incubation-based tests set the floor: sterility needs 14 days of incubation, and microbial limits need 3 to 5. Chemical tests can be done in days.</p>"),
              ("Can I combine services in one shipment?", "<p>Yes. One shipment and one sample submission form can cover several services; we split aliquots at receipt.</p>"),
              ("Are prices in the table?", f"<p>No. Use the <a href='/tools/quote-estimator.html'>Instant Quote Estimator</a> for a price band, or request a quote for a fixed price.</p>"),
              ("Which lab will test my samples?", "<p>Usually the lead lab for the service closest to you. The quote names the lab, and the portal shows it once samples arrive.</p>")], "cfaq"))
page("services/compare", "Compare services", "All twelve services side by side: turnaround, sample need, regulatory coverage and lead labs.", cb, img="data-dashboard",
     chips=[("12", "services compared"), ("4", "criteria"), ("Sortable", "columns")], crumbs=CR, hero="plain")


# =====================================================================================
# Service pages 1-6
# =====================================================================================
A17 = "17025 target"

# ---------- hero visuals ----------
V_DISSOLVE = ('<svg class="sv1-v sv1-dis" viewBox="0 0 360 240" role="img" aria-label="A tablet dissolving while its dissolution curve plots itself">'
              '<path class="ax" d="M44 204H344M44 204V24"/>' + "".join(f'<path class="gd" d="M44 {204 - k * 36}H344"/>' for k in range(1, 5))
              + "".join(f'<text x="{44 + m * 5:.0f}" y="222">{m}</text>' for m in (0, 10, 20, 30, 45, 60)) + '<text x="300" y="236">minutes</text><text x="8" y="30">%</text>'
              + "".join(f'<text x="18" y="{208 - k * 36}">{k * 25}</text>' for k in range(1, 5))
              + '<path class="cur" pathLength="1" d="M44 204C64 120 84 84 104 70S164 52 194 49 284 46 344 45"/>'
              + "".join(f'<circle class="pt" cx="{x}" cy="{y}" r="4" style="--k:{i}"/>' for i, (x, y) in enumerate([(69, 128), (94, 82), (119, 64), (144, 56), (194, 49), (269, 46), (344, 45)]))
              + '<g class="tab"><ellipse cx="270" cy="120" rx="34" ry="15"/><path d="M236 120v8c0 8 15 15 34 15s34-7 34-15v-8"/></g>'
              + "".join(f'<circle class="pc" cx="{250 + (i * 13) % 44}" cy="140" r="{1.5 + i % 3}" style="--k:{i}"/>' for i in range(10))
              + '<text class="q" x="190" y="38">Q = 80% at 30 min</text></svg>')

_ZP = [("I", 58, 15, "21 °C / 45% RH"), ("I", 54, -3, "21 °C / 45% RH"), ("II", 40, -98, "25 °C / 60% RH"), ("II", 36, 139, "25 °C / 60% RH"), ("II", 44, 9, "25 °C / 60% RH"),
       ("III", 24, 10, "30 °C / 35% RH"), ("III", 28, 50, "30 °C / 35% RH"), ("IVa", 22, -79, "30 °C / 65% RH"), ("IVb", 20, 78, "30 °C / 75% RH"), ("IVb", 3, 105, "30 °C / 75% RH"), ("IVb", -12, -50, "30 °C / 75% RH")]
_ZC = {"I": "#7fb3ff", "II": "#7fe7dc", "III": "#F2A900", "IVa": "#ff9f6b", "IVb": "#ff5f7a"}
V_ZONES = ('<svg class="sv1-v sv1-zn" viewBox="0 0 1000 430" role="img" aria-label="World map with stability chambers glowing in their ICH climatic zone colours as time advances">'
           f'<path class="land" d="{LAND}"/>'
           + "".join(f'<g class="zc" style="--c:{_ZC[z]};--k:{i}"><circle cx="{xy(la, lo)[0]}" cy="{xy(la, lo)[1]}" r="26" class="h"/><circle cx="{xy(la, lo)[0]}" cy="{xy(la, lo)[1]}" r="8"/>'
                     f'<text x="{xy(la, lo)[0] + 14}" y="{xy(la, lo)[1] - 10}">{z}</text></g>' for i, (z, la, lo, c) in enumerate(_ZP))
           + '<rect class="tt" x="40" y="400" width="920" height="6" rx="3"/><rect class="tf" x="40" y="400" width="920" height="6" rx="3"/>'
           + "".join(f'<text class="tm" x="{40 + m / 36 * 920:.0f}" y="426">{m}m</text>' for m in (0, 3, 6, 9, 12, 18, 24, 36)) + '</svg>')

V_PEAK = ('<svg class="sv1-v sv1-pk" viewBox="0 0 360 240" role="img" aria-label="A chromatogram peak pair sharpening as the method is optimised">'
          '<path class="ax" d="M30 200H340"/>'
          '<path class="p p1" d="M30 200H90C120 200 130 90 165 90S190 120 200 110 220 95 250 200H340"/>'
          '<path class="p p2" d="M30 200H110C130 200 135 70 152 70S168 190 180 190 196 80 210 80 226 200 240 200H340"/>'
          '<path class="p p3" d="M30 200H120C134 200 138 40 148 40S160 200 168 200H182C192 200 196 56 206 56S218 200 226 200H340"/>'
          '<text class="l1" x="230" y="40">Rs 0.9</text><text class="l2" x="230" y="40">Rs 1.6</text><text class="l3" x="230" y="40">Rs 2.8</text>'
          '<text class="sm" x="30" y="226">Gradient, pH and temperature tuned by DoE (ICH Q14)</text></svg>')

V_AB = ('<div class="sv1-ab3" role="img" aria-label="An antibody rotating with its quality attributes highlighted"><svg class="sv1-v sv1-ab" viewBox="0 0 360 260">'
        '<g class="y"><path d="M180 250V150"/><path d="M168 250V150"/><path d="M174 150L100 70"/><path d="M174 150L248 70"/><path d="M162 150L96 84"/><path d="M186 150L252 84"/>'
        '<path d="M100 70L72 30"/><path d="M248 70L276 30"/><path d="M96 84L58 52"/><path d="M252 84L290 52"/></g>'
        + "".join(f'<g class="hs" style="--k:{i}"><circle cx="{x}" cy="{y}" r="7"/><text x="{x + (12 if x > 180 else -12)}" y="{y + 4}" text-anchor="{"start" if x > 180 else "end"}">{t}</text></g>'
                  for i, (x, y, t) in enumerate([(174, 214, "N297 glycans"), (78, 40, "CDR oxidation"), (270, 40, "Deamidation"), (174, 150, "Hinge clipping"), (120, 92, "Charge variants"), (240, 110, "Aggregation")]))
        + '</svg></div>')

_LNP = "".join(f'<circle class="lp" cx="{180 + 92 * math.cos(a / 28 * 6.2832):.1f}" cy="{125 + 92 * math.sin(a / 28 * 6.2832):.1f}" r="7" style="--k:{a}"/>' for a in range(28))
V_LNP = ('<svg class="sv1-v sv1-ln" viewBox="0 0 360 250" role="img" aria-label="An mRNA strand folding and being wrapped in a lipid nanoparticle">'
         '<circle class="core" cx="180" cy="125" r="80"/>'
         '<path class="rna" pathLength="1" d="M110 130c10-30 25 30 35 0s25 30 35 0 25 30 35 0 25 30 35 0"/>'
         '<circle class="cap" cx="110" cy="130" r="6"/><path class="pa" d="M250 130h22"/>' + _LNP
         + '<text x="16" y="24">5′ cap</text><text x="282" y="236">poly(A)</text><text class="ee" x="180" y="240" text-anchor="middle">EE 94% · 82 nm · PDI 0.11</text></svg>')

_tri = []
for i in range(6):
    a1, a2 = i * 60 - 90, i * 60 - 30
    p = f"180,120 {180 + 86 * math.cos(math.radians(a1)):.1f},{120 + 86 * math.sin(math.radians(a1)):.1f} {180 + 86 * math.cos(math.radians(a2)):.1f},{120 + 86 * math.sin(math.radians(a2)):.1f}"
    dx, dy = 70 * math.cos(math.radians(a1 + 30)), 70 * math.sin(math.radians(a1 + 30))
    _tri.append(f'<polygon class="tri" points="{p}" style="--k:{i};--dx:{dx:.0f}px;--dy:{dy:.0f}px"/>')
V_AAV = ('<svg class="sv1-v sv1-aav" viewBox="0 0 360 250" role="img" aria-label="An AAV capsid assembling from its subunits and filling with a genome">'
         + "".join(_tri) + '<path class="gen" pathLength="1" d="M150 130c10-20 20 20 30 0s20 20 30 0"/><circle class="fill" cx="180" cy="120" r="40"/>'
         '<text x="180" y="236" text-anchor="middle" class="lab">Full capsid · 4.7 kb genome</text></svg>')

# ---------- tools ----------
MK = {"US": "United States (USP)", "EU": "Europe (Ph. Eur.)", "IN": "India (IP)", "JP": "Japan (JP)"}
BT = {  # test: (name, {market: reference}, business days)
 "desc": ("Description and appearance", {"US": "Monograph", "EU": "Monograph", "IN": "IP monograph", "JP": "Monograph"}, 1),
 "id": ("Identification (IR and HPLC retention time)", {"US": "⟨197⟩, ⟨621⟩", "EU": "2.2.24, 2.2.29", "IN": "IP monograph", "JP": "2.25, 2.01"}, 2),
 "assay": ("Assay (HPLC)", {"US": "Monograph, ⟨621⟩", "EU": "Monograph, 2.2.29", "IN": "IP monograph", "JP": "Monograph, 2.01"}, 3),
 "rs": ("Related substances (HPLC)", {"US": "Monograph, ICH Q3B", "EU": "Monograph, 2.2.29, ICH Q3B", "IN": "IP monograph, ICH Q3B", "JP": "Monograph, ICH Q3B"}, 3),
 "diss": ("Dissolution", {"US": "⟨711⟩", "EU": "2.9.3", "IN": "IP dissolution test", "JP": "6.10"}, 4),
 "drel": ("Drug release (multi-stage)", {"US": "⟨724⟩", "EU": "2.9.3", "IN": "IP dissolution test", "JP": "6.10"}, 6),
 "udu": ("Uniformity of dosage units", {"US": "⟨905⟩", "EU": "2.9.40", "IN": "IP uniformity test", "JP": "6.02"}, 3),
 "water": ("Water content (Karl Fischer)", {"US": "⟨921⟩", "EU": "2.5.12", "IN": "IP water determination", "JP": "2.48"}, 1),
 "rsolv": ("Residual solvents (GC-HS)", {"US": "⟨467⟩", "EU": "5.4, 2.4.24", "IN": "ICH Q3C", "JP": "2.46"}, 3),
 "ei": ("Elemental impurities (ICP-MS, if risk requires)", {"US": "⟨232⟩, ⟨233⟩", "EU": "5.20, 2.4.20", "IN": "ICH Q3D", "JP": "ICH Q3D"}, 5),
 "micro": ("Microbial enumeration and specified organisms", {"US": "⟨61⟩, ⟨62⟩", "EU": "2.6.12, 2.6.13", "IN": "IP microbial tests", "JP": "4.05"}, 6),
 "nitro": ("Nitrosamines and NDSRIs (if risk identified)", {"US": "⟨1469⟩, FDA AI limits", "EU": "EMA Art. 5(3) AI limits", "IN": "CDSCO, risk-based", "JP": "MHLW, risk-based"}, 6),
 "ph": ("pH", {"US": "⟨791⟩", "EU": "2.2.3", "IN": "IP pH", "JP": "2.54"}, 1),
 "dvol": ("Deliverable volume", {"US": "⟨698⟩", "EU": "Monograph", "IN": "IP monograph", "JP": "Monograph"}, 1),
 "ster": ("Sterility (membrane filtration)", {"US": "⟨71⟩", "EU": "2.6.1", "IN": "IP sterility test", "JP": "4.06"}, 14),
 "endo": ("Bacterial endotoxins", {"US": "⟨85⟩", "EU": "2.6.14", "IN": "IP endotoxin test", "JP": "4.01"}, 2),
 "subvis": ("Sub-visible particles", {"US": "⟨788⟩", "EU": "2.9.19", "IN": "IP particulate matter", "JP": "6.07"}, 2),
 "vis": ("Visible particles", {"US": "⟨790⟩", "EU": "2.9.20", "IN": "IP monograph", "JP": "6.06"}, 1),
 "cvol": ("Extractable volume", {"US": "⟨697⟩", "EU": "2.9.17", "IN": "IP monograph", "JP": "6.05"}, 1),
 "fill": ("Minimum fill", {"US": "⟨755⟩", "EU": "Monograph", "IN": "IP monograph", "JP": "Monograph"}, 1),
 "ivrt": ("In vitro release test (semisolid)", {"US": "⟨1724⟩", "EU": "EMA quality of topical products guideline", "IN": "Risk-based", "JP": "Risk-based"}, 7),
}
BF = {"Immediate-release tablet": ["desc", "id", "assay", "rs", "diss", "udu", "water", "rsolv", "ei", "micro", "nitro"],
      "Modified-release tablet": ["desc", "id", "assay", "rs", "drel", "udu", "water", "micro", "nitro"],
      "Hard capsule": ["desc", "id", "assay", "rs", "diss", "udu", "water", "micro", "nitro"],
      "Oral solution": ["desc", "id", "assay", "rs", "ph", "dvol", "micro", "nitro"],
      "Solution for injection": ["desc", "id", "assay", "rs", "ph", "ster", "endo", "subvis", "vis", "cvol", "ei"],
      "Topical cream": ["desc", "id", "assay", "rs", "fill", "micro", "ivrt"]}
TOOL_BRP = TOOLBOX("Signature tool", "Batch Release Planner", "Pick a dosage form and a market. The planner lists the compendial release tests, the chapter that governs each, and an estimated turnaround.",
    f'<div class="sv1-brp" data-t="{J({k: [v[0], v[1], v[2]] for k, v in BT.items()})}" data-f="{J(BF)}" data-mk="{J(MK)}"><div class="sv1-row">'
    f'<label><span>Dosage form</span><select data-b="f">{"".join(f"<option>{k}</option>" for k in BF)}</select></label>'
    f'<label><span>Market</span><select data-b="m">{"".join(f"<option value={k}>{v}</option>" for k, v in MK.items())}</select></label></div><div class="sv1-out" aria-live="polite"></div>'
    f'<p class="cn">General guidance from the pharmacopoeias. Your registered specification always governs. IP chapters are cited by test name. Tests run in parallel; turnaround is the longest test plus two days for QA review.</p>'
    f'<p><a class="btn" href="/request-quote.html?service=0">Send this plan to a scientist</a></p></div>')

TOOL_SD = TOOLBOX("Signature tool", "Stability Study Designer (mini)", "Choose zones, packs and duration. You get the ICH pull schedule, the sample count and a cost range.",
    '<div class="sv1-sd"><div class="sv1-row"><fieldset class="sv1-zs"><legend>Long-term condition (choose the zones you will market in)</legend>'
    + "".join(f'<label class="chk"><input type="checkbox" value="{z}" data-c="{c}"{" checked" if z in ("II", "IVb") else ""}> <span>Zone {z}: {c}</span></label>'
              for z, c in [("I/II", "25 °C / 60% RH"), ("II", "25 °C / 60% RH"), ("III", "30 °C / 35% RH"), ("IVa", "30 °C / 65% RH"), ("IVb", "30 °C / 75% RH")][1:]) +
    '</fieldset><div class="sv1-col"><label><span>Shelf life to support</span><select data-s="dur"><option value="24">24 months</option><option value="36" selected>36 months</option><option value="60">60 months</option></select></label>'
    '<label><span>Packaging configurations <output data-o="pk">2</output></span><input type="range" min="1" max="4" value="2" data-s="pk"></label>'
    '<label><span>Units tested per pull <output data-o="u">30</output></span><input type="range" min="10" max="120" step="5" value="30" data-s="u"></label>'
    '<label class="chk"><input type="checkbox" data-s="ph" checked> <span>Include photostability (ICH Q1B)</span></label></div></div>'
    '<div class="sv1-out" aria-live="polite"></div><p class="cn">Three primary batches, as ICH Q1A(R2) expects. Intermediate 30 °C / 65% RH is added automatically when long-term is 25 °C / 60% RH, and is tested only if accelerated shows significant change. '
    f'Cost range is indicative {ILL("Illustrative price")}.</p><p><a class="btn" href="/tools/stability-study-designer.html">Open the full designer</a> <a class="btn o" href="/request-quote.html?service=1">Quote this study</a></p></div>')

VW = {"Identification": [["Specificity / selectivity"], 1],
      "Assay (content or potency)": [["Specificity / selectivity", "Range: response (linearity or calibration model)", "Accuracy", "Precision: repeatability", "Precision: intermediate precision", "Robustness (from development, ICH Q14)"], 3],
      "Impurities, quantitative": [["Specificity / selectivity", "Range: response (linearity)", "Range: lower range limit (quantitation limit)", "Accuracy", "Precision: repeatability", "Precision: intermediate precision", "Robustness (from development, ICH Q14)"], 4],
      "Impurities, limit test": [["Specificity / selectivity", "Range: lower range limit (detection limit)", "Robustness (from development, ICH Q14)"], 2],
      "Dissolution (assay finish)": [["Specificity / selectivity (placebo and media)", "Range: response across 20% below to 20% above the specified range", "Accuracy", "Precision: repeatability", "Precision: intermediate precision", "Filter and solution stability", "Robustness (from development, ICH Q14)"], 3],
      "Residual solvents (GC)": [["Specificity / selectivity", "Range: response (linearity)", "Range: lower range limit (quantitation limit)", "Accuracy", "Precision: repeatability", "Precision: intermediate precision", "Robustness (from development, ICH Q14)"], 3]}
TOOL_VW = TOOLBOX("Signature tool", "Validation Wizard", "Choose the method type. The wizard lists the ICH Q2(R2) performance characteristics to demonstrate and estimates the timeline.",
    f'<div class="sv1-vw" data-v="{J(VW)}"><div class="sv1-chs" role="group" aria-label="Method type">' + "".join(f'<button type="button" class="ch" aria-pressed="{"true" if i == 1 else "false"}">{k}</button>' for i, k in enumerate(VW))
    + '</div><div class="sv1-out" aria-live="polite"></div><p class="cn">Based on ICH Q2(R2) (adopted November 2023) and ICH Q14. Validation is preceded by a written protocol with acceptance criteria and followed by a signed report.</p>'
    '<p><a class="btn" href="/request-quote.html?service=2">Quote this validation</a></p></div>')

BS = [("SEC monomer purity", "%", 97.0, 100.0, 98.2, 99.4, 98.9), ("HMW species (SEC)", "%", 0, 3, 0.6, 1.8, 1.1), ("Acidic variants (icIEF)", "%", 10, 35, 18, 26, 24.5),
      ("G0F glycan", "%", 20, 50, 30, 42, 37), ("Afucosylated glycans", "%", 1, 12, 4.5, 8.0, 6.2), ("Relative potency (cell-based)", "%", 70, 130, 85, 115, 101)]
TOOL_BS = TOOLBOX("Signature tool", "Biosimilar Similarity Explorer", "Each bar is the reference product's quality range across lots. Drag the slider to place your biosimilar's mean and see whether it sits inside.",
    '<div class="sv1-bs">' + "".join(f'<div class="sv1-bsr" data-lo="{lo}" data-hi="{hi}" data-a="{a}" data-b="{b}"><div class="sv1-bsh"><b>{n}</b><span>Reference range {lo_}–{hi_}{u}</span><output>{v}{u}</output></div>'
                                     f'<div class="sv1-bsb"><i class="rng"></i><i class="mk"></i></div><label class="vh" for="bs{i}">{n}</label><input id="bs{i}" type="range" min="{a}" max="{b}" step="0.1" value="{v}"></div>'
                                     for i, (n, u, a, b, lo, hi, v) in enumerate(BS) for lo_, hi_ in [(lo, hi)])
    + '<p class="sv1-bss" aria-live="polite"></p><p class="cn">Illustrative numbers, not any real product. A real assessment ranks attributes by risk and uses equivalence testing (Tier 1) for the most critical ones, quality ranges (Tier 2) and visual comparison (Tier 3) for the rest.</p>'
    '<p><a class="btn" href="/request-quote.html?service=3">Plan a similarity study</a></p></div>')

QA = {"cap": ("5′ cap", "Capping efficiency", "RNase H cleavage then LC-MS of the 5′ fragment", "Cap 1 vs Cap 0 vs uncapped quantified; typical target above 90% capped.", "/method-library/mrna-capping-lc-ms.html"),
      "utr": ("5′ and 3′ UTRs", "Identity and sequence integrity", "Sanger or NGS sequencing; RT-PCR identity", "Confirms the designed sequence and the absence of variants.", ""),
      "cds": ("Coding sequence", "Integrity (full-length RNA)", "Capillary gel electrophoresis, fragment analysis", "Percent intact mRNA; fragments indicate hydrolysis.", "/method-library/mrna-integrity-ce.html"),
      "pa": ("Poly(A) tail", "Tail length and distribution", "RNase T1 digestion then LC-MS", "Mean length and heterogeneity; affects stability and translation.", "/method-library/poly-a-tail-length.html"),
      "ds": ("dsRNA impurity", "Residual double-stranded RNA", "J2 antibody ELISA or dot blot", "dsRNA from IVT drives innate immune response; reported in ng per µg RNA.", "/method-library/dsrna-elisa.html"),
      "dna": ("DNA template", "Residual linearised plasmid", "qPCR", "Template left after DNase digestion, in ng per dose.", "/method-library/residual-dna-qpcr.html"),
      "ion": ("Ionisable lipid", "Lipid identity, content and purity", "HPLC with charged aerosol detection", "Each of the four lipids assayed; lipid-related impurities profiled.", ""),
      "peg": ("PEG-lipid", "PEG-lipid content", "HPLC-CAD", "Controls particle size and circulation; also screened for degradants.", ""),
      "lnp": ("LNP particle", "Size, PDI and encapsulation", "DLS for size and PDI; RiboGreen for encapsulation efficiency", "Typical targets: 60 to 100 nm, PDI below 0.2, EE above 90%.", "/method-library/lnp-size-pdi-dls.html"),
      "pot": ("Expressed protein", "Potency", "In vitro translation or cell-based expression", "Measures that the mRNA makes the intended protein.", "/method-library/cell-based-potency.html")}
QM = ('<svg class="sv1-qm" viewBox="0 0 640 300" aria-label="Diagram of an mRNA-LNP product. Select a part to see the test.">'
      '<circle class="lnpb" cx="470" cy="150" r="120"/>'
      + "".join(f'<circle cx="{470 + 120 * math.cos(a / 36 * 6.2832):.1f}" cy="{150 + 120 * math.sin(a / 36 * 6.2832):.1f}" r="6" class="lipd"/>' for a in range(36)) +
      '<g class="sv1-qk" data-k="cap" tabindex="0" role="button"><circle cx="40" cy="80" r="16"/><text x="40" y="120" text-anchor="middle">5′ cap</text></g>'
      '<g class="sv1-qk" data-k="utr" tabindex="0" role="button"><rect x="58" y="70" width="44" height="20" rx="6"/><text x="80" y="58" text-anchor="middle">UTR</text></g>'
      '<g class="sv1-qk" data-k="cds" tabindex="0" role="button"><rect x="104" y="70" width="150" height="20" rx="6"/><text x="179" y="58" text-anchor="middle">Coding sequence</text></g>'
      '<g class="sv1-qk" data-k="utr" tabindex="0" role="button"><rect x="256" y="70" width="34" height="20" rx="6"/></g>'
      '<g class="sv1-qk" data-k="pa" tabindex="0" role="button"><path d="M292 80h50" stroke-width="10"/><text x="317" y="58" text-anchor="middle">poly(A)</text></g>'
      '<g class="sv1-qk" data-k="ds" tabindex="0" role="button"><path d="M60 190q20-20 40 0t40 0M60 202q20-20 40 0t40 0"/><text x="100" y="236" text-anchor="middle">dsRNA</text></g>'
      '<g class="sv1-qk" data-k="dna" tabindex="0" role="button"><circle cx="230" cy="196" r="26"/><circle cx="230" cy="196" r="18"/><text x="230" y="244" text-anchor="middle">DNA template</text></g>'
      '<g class="sv1-qk" data-k="ion" tabindex="0" role="button"><circle cx="420" cy="110" r="14"/><text x="420" y="88" text-anchor="middle">Ionisable lipid</text></g>'
      '<g class="sv1-qk" data-k="peg" tabindex="0" role="button"><path d="M555 70l30-30M560 76l30-30"/><text x="590" y="30" text-anchor="middle">PEG-lipid</text></g>'
      '<g class="sv1-qk" data-k="lnp" tabindex="0" role="button"><path d="M430 165q20-20 40 0t40 0 40 0" /><text x="470" y="205" text-anchor="middle">Encapsulated mRNA</text></g>'
      '<g class="sv1-qk" data-k="pot" tabindex="0" role="button"><rect x="420" y="232" width="100" height="22" rx="11"/><text x="470" y="247" text-anchor="middle">Potency</text></g></svg>')
TOOL_QA = TOOLBOX("Signature tool", "mRNA Quality Attribute Map", "Select any part of the mRNA-LNP product to see the critical quality attribute, the method and what we report.",
    f'<div class="sv1-qa" data-q="{J(QA)}"><div class="sv1-qa-m">{QM}</div><div class="sv1-qa-p" aria-live="polite"><p class="ey">Select a component</p><h3>Ten attributes, one product</h3><p>The map covers the RNA, its impurities and the lipid nanoparticle that delivers it.</p></div></div>'
    '<p class="cn">Targets shown are typical published ranges, not specifications. Your product\'s acceptance criteria come from your development data.</p>')

CG = {"AAV": [("Vector genome titre", "ddPCR", "2 days"), ("Capsid titre", "ELISA", "2 days"), ("Empty/full ratio", "AUC or mass photometry", "3 days"), ("Infectious titre", "TCID50 with qPCR", "10 days"),
              ("Identity", "Sequencing, restriction digest", "5 days"), ("Purity", "SDS-PAGE / CE-SDS (VP1:VP2:VP3)", "3 days"), ("Replication-competent AAV", "Cell-based amplification and qPCR", "21 days"),
              ("Residual host cell DNA and protein", "qPCR, ELISA", "3 days"), ("Sterility", "Membrane filtration (⟨71⟩, 2.6.1)", "14 days"), ("Endotoxin", "LAL or rFC", "1 day"), ("Potency", "Transgene expression or activity", "7 to 14 days")],
      "Lentiviral vector": [("Physical titre", "p24 ELISA", "2 days"), ("Functional titre", "Transduction with ddPCR or flow", "7 days"), ("Replication-competent lentivirus", "Cell-based co-culture and p24", "28 days or more"),
                            ("Identity", "Sequencing", "5 days"), ("Residual plasmid and host DNA", "qPCR", "3 days"), ("Residual benzonase", "ELISA", "2 days"), ("Sterility", "Membrane filtration", "14 days"),
                            ("Mycoplasma", "NAT (Ph. Eur. 2.6.7)", "1 day"), ("Endotoxin", "LAL or rFC", "1 day")],
      "CAR-T (autologous)": [("Identity and CAR expression", "Flow cytometry", "Same day"), ("Viability and cell count", "7-AAD flow or image cytometry", "Same day"), ("Vector copy number", "ddPCR", "1 day"),
                             ("Potency", "Cytotoxicity or IFN-γ release", "1 to 3 days"), ("Sterility", "Rapid (Ph. Eur. 2.6.27) with 14-day confirmation", "Day 7 interim"), ("Mycoplasma", "NAT (Ph. Eur. 2.6.7)", "Same day"),
                             ("Endotoxin", "LAL or rFC", "Same day"), ("Replication-competent virus", "Tested on vector lot; on product if required", "Vector lot release")]}
TOOL_CG = TOOLBOX("Signature tool", "CGT Release Test Matrix", "Choose the product type. The matrix lists the release tests regulators expect and how long each takes.",
    f'<div class="sv1-cg" data-c="{J(CG)}"><div class="sv1-chs" role="group" aria-label="Product type">' + "".join(f'<button type="button" class="ch" aria-pressed="{"true" if i == 0 else "false"}">{k}</button>' for i, k in enumerate(CG))
    + '</div><div class="sv1-out" aria-live="polite"></div><p class="cn">General expectations from FDA CMC guidance for human gene therapy INDs (2020), Ph. Eur. 2.6.27 and 5.14, and EMA ATMP guidelines. The release panel for your product is agreed with your regulator.</p>'
    '<p><a class="btn" href="/request-quote.html?service=5">Plan my release panel</a></p></div>')

# ---------- 1. Small molecule QC ----------
svc_page("small-molecule-qc-release",
 ("Compendial and custom release testing for tablets, capsules, liquids, injectables and APIs, from assay to nitrosamines.",
  "Small molecule QC and release covers every test a batch needs before it ships: identification, assay and related substances by HPLC, dissolution in all USP apparatus, content uniformity, residual solvents, elemental impurities by ICP-MS, nitrosamines and NDSRIs by LC-MS/MS, polymorph, particle size and water. Typical turnaround is 3 to 10 business days."),
 [("3 to 10 d", "typical release TAT"), ("11", "core release tests"), ("ng/g", "NDSRI sensitivity")],
 V_DISSOLVE, [("Q=80%", "at 30 min"), ("6", "vessels per run"), ("0.03 ppm", "typical NDMA LOQ"), ("24 h", "Critical tier")],
 [("Assay and related substances (HPLC/UPLC)", "USP ⟨621⟩, Ph. Eur. 2.2.29, ICH Q3B", "3 to 5 days", "2 g or 20 units", A17, "Stability-indicating reversed-phase methods with UV or PDA detection; peak purity on every run.", "UHPLC with PDA, CDS with audit trail", ML("hplc-assay-related-substances")),
  ("Impurity profiling and unknown identification", "ICH Q3A, ICH Q3B", "5 to 10 days", "1 g", A17, "UPLC impurity profiles; unknowns above the identification threshold characterised by LC-HRMS.", "UPLC-PDA, Q-TOF", ML("uplc-impurity-profiling")),
  ("Dissolution, apparatus 1 to 4", "USP ⟨711⟩, Ph. Eur. 2.9.3, JP 6.10", "3 to 5 days", "12 to 24 units", A17, "Basket, paddle, reciprocating cylinder and flow-through cell; profiles and single-point release.", "Six- and eight-vessel baths, autosamplers, fibre optic UV", ML("dissolution-testing")),
  ("Uniformity of dosage units", "USP ⟨905⟩, Ph. Eur. 2.9.40", "2 to 3 days", "30 units", A17, "Content uniformity or weight variation by the harmonised procedure, L1 and L2 stages.", "UHPLC, analytical balances", ML("content-uniformity")),
  ("Residual solvents (GC headspace)", "USP ⟨467⟩, ICH Q3C", "3 days", "1 g", A17, "Class 1, 2 and 3 solvents by static headspace GC-FID, with procedure A, B and C logic.", "GC-FID with headspace sampler", ML("residual-solvents-gc-hs")),
  ("Elemental impurities (ICP-MS)", "USP ⟨232⟩, USP ⟨233⟩, ICH Q3D", "5 days", "1 g", A17, "All 24 ICH Q3D elements by risk class after closed-vessel microwave digestion.", "ICP-MS with collision cell, microwave digester", ML("elemental-impurities-icp-ms")),
  ("Nitrosamines and NDSRIs (LC-MS/MS)", "USP ⟨1469⟩, FDA guidance, EMA Art. 5(3)", "5 to 7 days", "2 g", A17, "Small nitrosamines and drug-substance-related nitrosamines down to the acceptable intake, with confirmation by HRMS on request.", "Triple quadrupole LC-MS/MS, GC-MS/MS", ML("nitrosamines-lc-ms-ms")),
  ("Mutagenic impurities", "ICH M7", "7 to 10 days", "2 g", A17, "Trace analysis of alkyl halides, sulfonate esters and other alerting structures at TTC-based limits.", "GC-MS, LC-MS/MS", ML("genotoxic-impurities")),
  ("Polymorph identification (XRPD)", "USP ⟨941⟩, Ph. Eur. 2.9.33", "3 days", "500 mg", A17, "Form identification and detection of unwanted forms in API and, where possible, in tablets.", "Powder X-ray diffractometer", ML("xrpd-polymorph")),
  ("Particle size (laser diffraction)", "USP ⟨429⟩, Ph. Eur. 2.9.31", "2 days", "5 g", A17, "D10, D50, D90 by wet or dry dispersion with method-specific dispersion validation.", "Laser diffraction analyser", ML("particle-size-laser-diffraction")),
  ("Water content (Karl Fischer)", "USP ⟨921⟩, Ph. Eur. 2.5.12", "1 day", "1 g", A17, "Volumetric or coulometric KF; oven transfer for hygroscopic or reactive samples.", "Volumetric and coulometric titrators", ML("water-content-karl-fischer")),
  ("Identification (FTIR, UV, HPLC)", "USP ⟨197⟩, Ph. Eur. 2.2.24", "1 to 2 days", "200 mg", A17, "IR by ATR or KBr against the reference standard; HPLC retention time match.", "FTIR with ATR, UV-Vis", ML("ftir-identification"))],
 "Methods are written to USP, Ph. Eur., JP and IP expectations, and reports are formatted for FDA, EMA, CDSCO and PMDA submissions and inspections.",
 [("inst-hplc", "UHPLC with PDA", ["Up to 1,300 bar", "PDA 190 to 800 nm", "Validated CDS with audit trail", "24 systems planned at the flagship"]),
  ("inst-dissolution", "Dissolution baths", ["USP apparatus 1, 2, 3 and 4", "Automated sampling", "Fibre optic UV for real-time profiles", "Mechanical calibration per ASTM E2503"]),
  ("inst-icp", "ICP-MS", ["24 ICH Q3D elements", "Collision/reaction cell", "Microwave closed-vessel digestion", "Sub-µg/g limits"]),
  ("inst-lcms", "Triple quadrupole LC-MS/MS", ["NDSRIs at ng/g", "MRM with qualifier ions", "HRMS confirmation available", "Shared method library across sites"]),
  ("inst-gc", "GC with headspace", ["USP ⟨467⟩ residual solvents", "FID and MS detection", "120-vial autosampler", "Nitrosamines by GC-MS/MS"])],
 (72, "of planned flagship HPLC capacity booked in a typical week", "Capacity planning model for the Hyderabad flagship."),
 ["Quantity: twice the full specification, plus retains (typically 2 g API or 60 units)", "Primary packaging intact and labelled with batch, product and expiry", "Storage condition stated; temperature logger for 2 to 8 °C", "Certificate of analysis or specification attached", "Hazard declaration (cytotoxic, potent, controlled substance)", "Signed sample submission sheet with the quote number"],
 [("Submit", "Send the specification. We confirm the methods, the tier and the date before you ship.", "lab-analyst-pc", "sealed"),
  ("Receive", "Samples photographed and logged within 4 hours of arrival; retains split and stored.", "lab-sample-rack", "opened"),
  ("Test", "A named analyst runs assay, impurities and dissolution in parallel on qualified systems.", "inst-hplc", "instrument"),
  ("Release", "Second-person review, QA approval, e-signed CoA and full chromatograms in the portal.", "lab-goggles", "reported")],
 (CHIP("TAT 21 → 6 days", "Release testing for a generic metformin line", "<p>A generic maker moved release testing for three strengths to a single lab with one LIMS template; release time fell from 21 to 6 business days.</p>"),
  "assay, related substances, dissolution, uniformity, residual solvents, elemental impurities and nitrosamines by the methods listed.",
  "Most failed releases are not chemistry problems. They are paperwork, sample and method-version problems. We remove those first."),
 [("What is included in standard release testing?", "<p>Everything in your registered specification. Typically identification, assay, related substances, dissolution or disintegration, uniformity of dosage units, water and microbial quality, plus risk-based residual solvents, elemental impurities and nitrosamines.</p>"),
  ("How fast can you release a batch?", "<p>Standard is 3 to 10 business days. Priority roughly halves that. Critical starts within hours of receipt and can release in 24 to 72 hours when the methods are already transferred.</p>"),
  ("Do you test to my in-house method or the pharmacopoeia?", "<p>Either. Compendial methods are verified under USP ⟨1226⟩; your in-house methods are transferred under USP ⟨1224⟩ before routine use.</p>"),
  ("Can you test nitrosamines down to the FDA acceptable intake?", "<p>Yes. Our LC-MS/MS methods are developed to reach a limit of quantitation at or below 30% of the acceptable intake-based limit, which is what regulators usually ask for in confirmatory testing.</p>"),
  ("What happens if a result is out of specification?", "<p>We follow the FDA OOS guidance: a Phase I laboratory investigation, notification within one business day, and no retesting into compliance.</p>"),
  ("Which dissolution apparatus do you run?", "<p>USP apparatus 1 (basket), 2 (paddle), 3 (reciprocating cylinder) and 4 (flow-through cell), with automated sampling and media degassing.</p>"),
  ("Do you test APIs as well as finished products?", "<p>Yes. API release follows the monograph or your specification, including polymorph, particle size and residual solvents.</p>"),
  ("Can you handle controlled or highly potent substances?", "<p>Planned sites will hold the licences and containment needed. Tell us at quote stage so the receiving lab is confirmed before you ship.</p>"),
  ("How do I get the raw data?", "<p>Chromatograms, sequences and audit trails are in the portal with the CoA. Native CDS files are available on request.</p>"),
  ("Do you support Indian Schedule M and export markets together?", "<p>Yes. Reports can reference IP, USP and Ph. Eur. in one package when a batch is released for several markets.</p>")],
 TOOL_BRP,
 [("Nitrosamine Testing Hub", "<p>FDA's NDSRI guidance (August 2023, updated since) assigns acceptable intakes by predicted potency category, from 26.5 to 1,500 ng/day. EMA uses the same CPCA approach. The work runs in three steps: a risk assessment of the API route, excipients and packaging; confirmatory testing when a risk is found; and changes to the process or specification if a result exceeds the limit.</p>"
   "<p class='sv1-dl'><b>Deadline tracker:</b> FDA asked for confirmatory testing and any changes by 1 August 2025. Check your market's current expectation before relying on any date.</p>", AR("nitrosamine-testing-2027")),
  ("Dissolution troubleshooting", "<ol><li>Low and variable results? Check deaeration and coning under the paddle first.</li><li>Rising results over time? Check filter adsorption and solution stability.</li><li>Capsules sticking? Use sinkers described in the method, and record them.</li><li>Cross-linked gelatin? USP ⟨711⟩ allows enzymes in the medium.</li></ol>", ""),
  ("Setting specifications for a new generic", "<p>Start from the reference listed drug's labelled strength and the pharmacopoeial monograph. Impurity limits follow ICH Q3B thresholds by maximum daily dose. Dissolution acceptance usually comes from the RLD profile and the FDA dissolution database.</p>", ""),
  ("Common OOS root causes", "<p>In our scientists' experience the usual causes are sample preparation (incomplete extraction, wrong dilution), integration choices, expired or mislabelled standards, and instrument suitability drifting within limits. Each has a preventive control in our SOPs.</p>", AR("data-integrity-top-10-findings"))],
 ["stability-studies", "method-development-validation", "microbiology-sterility"],
 ("Ready to release? So are we.", "Send the specification and the batch count. You get the test list, the date and the price in one reply."),
 extra_top=SPLIT("pharma-blisters", H3("Every dosage form") + P("Immediate- and modified-release tablets, hard and soft capsules, oral solutions and suspensions, injectables, creams and APIs. One method library, validated once and run at every site.")
                 + TICKLIST(["Same methods and templates at every lab", "Second-person review on every result", "Raw data and audit trail with every CoA"]))
           + STRIP(["pharma-blisters2", "pharma-capsules", "inst-hplc", "lab-pipette-vials", "pharma-pills-mix", "inst-dissolution", "lab-cylinders"]))

# ---------- 2. Stability ----------
svc_page("stability-studies",
 ("ICH stability programmes in every climatic zone, I to IVb, with pull testing, trending and shelf-life support.",
  "Stability studies show how a product's quality changes over time under temperature, humidity and light. We store and test to ICH Q1A(R2) to Q1E and Q5C: long-term, intermediate and accelerated conditions in every climatic zone including Zone IVb (30 °C/75% RH), photostability, in-use, freeze-thaw and shipping studies, with trending and shelf-life estimation."),
 [("I to IVb", "climatic zones"), ("±2 °C / ±5% RH", "chamber tolerance"), ("5 to 10 d", "pull to report")],
 V_ZONES, [("40/75", "accelerated"), ("30/75", "Zone IVb"), ("36 m", "typical programme"), ("24/7", "chamber monitoring")],
 [("Long-term storage and testing", "ICH Q1A(R2)", "5 to 10 days per pull", "Per protocol", A17, "25 °C/60% RH or 30 °C/65% RH; pulls at 0, 3, 6, 9, 12, 18, 24 months then annually.", "Walk-in and reach-in chambers, continuous monitoring", ML("ich-stability-storage")),
  ("Intermediate storage", "ICH Q1A(R2)", "5 to 10 days per pull", "Per protocol", A17, "30 °C/65% RH, required when accelerated shows significant change and long-term is 25 °C/60% RH.", "Reach-in chambers", ML("ich-stability-storage")),
  ("Accelerated storage", "ICH Q1A(R2)", "5 to 10 days per pull", "Per protocol", A17, "40 °C/75% RH for six months with pulls at 0, 3 and 6 months as a minimum.", "Reach-in chambers", ML("ich-stability-storage")),
  ("Zone IVb storage", "ICH Q1A(R2), WHO TRS 1010 Annex 10", "5 to 10 days per pull", "Per protocol", A17, "30 °C/75% RH for hot and very humid markets including India and ASEAN.", "Walk-in chambers", ML("ich-stability-storage")),
  ("Refrigerated and frozen storage", "ICH Q1A(R2), ICH Q5C", "5 to 10 days per pull", "Per protocol", A17, "5 °C ± 3 °C and −20 °C or colder, with 25 °C accelerated for refrigerated products.", "Pharmacy fridges, freezers, −80 °C", ML("ich-stability-storage")),
  ("Photostability", "ICH Q1B", "7 to 10 days", "Units plus dark controls", A17, "Option 1 or 2 exposure: at least 1.2 million lux hours visible and 200 Wh/m² near UV.", "Photostability cabinet with calibrated sensors", ML("photostability-q1b")),
  ("Forced degradation", "ICH Q1A(R2), ICH Q2(R2)", "2 to 3 weeks", "2 to 5 g", A17, "Acid, base, oxidation, heat, humidity and light stress to prove methods are stability-indicating.", "UHPLC-PDA, LC-MS", ML("forced-degradation")),
  ("Bracketing and matrixing designs", "ICH Q1D", "Protocol in 1 week", "Reduced sets", A17, "Reduced designs for multiple strengths and pack sizes, justified statistically.", "Protocol design and LIMS scheduling", ""),
  ("Data evaluation and shelf-life", "ICH Q1E", "1 week", "Data sets", A17, "Regression with 95% confidence limits, poolability testing and extrapolation limits.", "Validated statistics templates", ""),
  ("In-use stability", "EMA CPMP/QWP/2934/99", "Per study", "Opened containers", A17, "Simulated use after first opening or reconstitution, including microbial challenge where relevant.", "Chambers, microbiology lab", ""),
  ("Freeze-thaw and temperature cycling", "ICH Q1A(R2)", "2 to 4 weeks", "Per protocol", A17, "Cycling between storage extremes to support labelling and shipping excursions.", "Programmable chambers", ""),
  ("Shipping and excursion studies", "USP ⟨1079⟩", "2 to 6 weeks", "Packed shippers", A17, "Real or simulated lane profiles to justify excursion allowances.", "Thermal profiles, data loggers", "")],
 "Protocols are written to ICH Q1A(R2) to Q1E and Q5C, WHO's stability guideline for Zone IVb markets, and regional variations for FDA, EMA, CDSCO and PMDA. ICH is consolidating these into one revised Q1 guideline; we track the draft.",
 [("lab-corridor", "Walk-in stability chambers", ["25/60, 30/65, 30/75 and 40/75", "±2 °C and ±5% RH", "Dual monitoring with alarms to on-call staff", "Mapping per season"]),
  ("room-clean-1", "Reach-in and photostability cabinets", ["Option 1 and 2 light sources", "Calibrated lux and UV sensors", "Dark controls in the same cabinet"]),
  ("lab-sample-rack", "Sample management", ["Barcode per container", "LIMS-scheduled pulls", "Pull window ± 7 days for monthly points"]),
  ("data-dashboard", "Live chamber dashboard", ["Temperature and humidity every minute", "Excursion alerts in the portal", "Anonymised preview below"])],
 (64, "of planned walk-in chamber space allocated", "Chamber capacity model across Hyderabad, Mumbai and Kuala Lumpur."),
 ["Three primary batches, at least pilot scale, in the final container closure", "Enough units for every pull plus 20% spare (the designer below calculates it)", "Signed stability protocol or our template approved", "Initial (T0) release data or samples for T0 testing", "Storage condition on arrival stated on the shipment", "Validated stability-indicating methods, or a plan to transfer them"],
 [("Submit", "Agree the protocol: conditions, pulls, tests and packs, scheduled in the LIMS.", "docs-papers", "sealed"),
  ("Receive", "Samples labelled per container, loaded into qualified chambers the same day.", "lab-corridor", "opened"),
  ("Test", "Pulls on schedule; testing on validated stability-indicating methods.", "inst-hplc", "instrument"),
  ("Release", "Each time point reported with trend charts and out-of-trend flags.", "data-dashboard", "reported")],
 (CHIP("Zone IVb in 1 protocol", "An Indian generic maker added ASEAN markets", "<p>One harmonised protocol covered 25/60, 30/75 and 40/75 for three strengths, cutting the number of pulls by a third through matrixing under ICH Q1D.</p>"),
  "storage and pull testing under ICH Q1A(R2), photostability under ICH Q1B and statistical evaluation under ICH Q1E.",
  "A stability programme is a promise you make for three years. Design it like you will have to defend every pull."),
 [("Which conditions do I need for India and ASEAN?", "<p>Long-term at 30 °C/75% RH (Zone IVb) plus accelerated at 40 °C/75% RH. Products also sold in Zone II markets often add 25 °C/60% RH.</p>"),
  ("How many batches does ICH require?", "<p>At least three primary batches for registration, two of which at least pilot scale, manufactured by a process that simulates the final one.</p>"),
  ("What counts as significant change at accelerated?", "<p>For a drug product: a 5% change in assay from initial, any degradant over its acceptance criterion, failure of appearance or physical attributes, pH, or dissolution for 12 units.</p>"),
  ("How long before I can file?", "<p>ICH expects 12 months of long-term and 6 months of accelerated data at submission for most new products; some regions accept less for generics.</p>"),
  ("Can you extrapolate shelf-life?", "<p>Within ICH Q1E limits: typically up to twice the long-term data, and not more than 12 months beyond it, when data show little change and statistics support it.</p>"),
  ("How are chamber excursions handled?", "<p>Chambers are monitored every minute. An excursion triggers an alert, an impact assessment and a notification in your portal, with the temperature trace attached.</p>"),
  ("Do you run stability for biologics?", "<p>Yes, under ICH Q5C, usually at 5 °C long-term with 25 °C accelerated and −20 °C or −70 °C for drug substance.</p>"),
  ("What is bracketing?", "<p>Testing only the extremes of a design factor, such as the smallest and largest strength, on the assumption the middle behaves in between. ICH Q1D sets when it is acceptable.</p>"),
  ("Can I see my chamber data?", "<p>Yes. The portal shows live and historical conditions for the chambers holding your samples.</p>")],
 TOOL_SD,
 [("Zone IVb for India and ASEAN launches", "<p>India and ASEAN countries require long-term data at 30 °C/75% RH. Products developed only at 25/60 often fail here on moisture-driven degradation or dissolution slowdown. Test the commercial pack early, and consider desiccants or Alu-Alu blisters before the registration batches.</p>", AR("stability-zone-ivb")),
  ("Stability protocol template library", "<p>Our templates cover new drug products, generics, APIs, biologics and post-approval changes. Each lists conditions, pull points, tests, acceptance criteria and the statistics plan, ready for your QA to adapt.</p>", ""),
  ("Handling an out-of-trend result", "<p>OOT is not OOS. Confirm the data first, check the method and the time point against regression prediction intervals, then decide whether a deeper investigation is needed. Document the rule you use before the study starts.</p>", ""),
  ("Live chamber dashboard", "<p>Every chamber reports temperature and humidity every minute. The portal shows your samples' chambers, the last 30 days of data and any excursion with its impact assessment.</p>" + IMG("data-dashboard", "Anonymised preview of a chamber dashboard (illustrative)"), "")],
 ["small-molecule-qc-release", "method-development-validation", "extractables-leachables"],
 ("Your stability programme, designed in minutes.", "Tell us the markets, the packs and the shelf life you need. We will send a protocol draft and a fixed price per pull."),
 extra_top=SPLIT("lab-corridor", H3("Climatic zones at a glance") + T(["Zone", "Climate", "Long-term condition"], [["I", "Temperate", "21 °C / 45% RH"], ["II", "Subtropical, possibly humid", "25 °C / 60% RH"], ["III", "Hot, dry", "30 °C / 35% RH"], ["IVa", "Hot, humid", "30 °C / 65% RH"], ["IVb", "Hot, very humid", "30 °C / 75% RH"]])
                 + P("Conditions follow the WHO stability guideline. Check the WHO list for each market's assigned zone."), flip=True))

# ---------- 3. Method development ----------
svc_page("method-development-validation",
 ("HPLC, UPLC, GC, LC-MS and dissolution methods developed with QbD, validated to ICH Q2(R2) and transferred between labs first time.",
  "Method development, validation and transfer creates the analytical procedures your specification depends on. We develop HPLC, UPLC, GC, LC-MS and dissolution methods using QbD and ICH Q14, validate them to ICH Q2(R2) and USP ⟨1225⟩, verify compendial methods to USP ⟨1226⟩ and transfer methods between labs under USP ⟨1224⟩, typically in 2 to 8 weeks."),
 [("2 to 8 wk", "typical project"), ("ICH Q2(R2)", "validation standard"), ("1 SOP set", "for transfers")],
 V_PEAK, [("Rs ≥ 2.0", "critical pair target"), ("DoE", "robustness"), ("Q14", "lifecycle"), ("⟨1224⟩", "transfer")],
 [("HPLC and UPLC method development", "ICH Q14", "2 to 4 weeks", "5 to 20 g", A17, "Column and pH screening, DoE optimisation, stability-indicating by forced degradation.", "UHPLC with column and solvent switching", ML("hplc-assay-related-substances")),
  ("GC method development", "ICH Q14, USP ⟨467⟩", "2 to 3 weeks", "5 g", A17, "Headspace and direct-injection methods for solvents and volatile impurities.", "GC-FID, GC-MS", ML("residual-solvents-gc-hs")),
  ("LC-MS method development", "ICH Q14", "3 to 6 weeks", "2 to 5 g", A17, "Trace impurity, NDSRI and identification methods on triple quadrupole and HRMS.", "LC-MS/MS, Q-TOF", ML("nitrosamines-lc-ms-ms")),
  ("Dissolution method development", "USP ⟨1092⟩", "3 to 6 weeks", "100+ units", A17, "Solubility, sink conditions, apparatus and speed selection, discriminating power.", "Dissolution baths, fibre optics", ML("dissolution-testing")),
  ("Validation: assay", "ICH Q2(R2), USP ⟨1225⟩", "2 to 3 weeks", "5 g", A17, "Specificity, response, accuracy, repeatability, intermediate precision.", "UHPLC", ""),
  ("Validation: impurities", "ICH Q2(R2), USP ⟨1225⟩", "3 to 4 weeks", "5 g plus impurity standards", A17, "Adds quantitation limit and accuracy at reporting threshold levels.", "UHPLC, LC-MS", ""),
  ("Verification of compendial methods", "USP ⟨1226⟩", "1 to 2 weeks", "2 g", A17, "Demonstrates the monograph method works for your product in our lab.", "As per monograph", ""),
  ("Method transfer", "USP ⟨1224⟩", "2 to 4 weeks", "Same lots at both labs", A17, "Comparative testing, covalidation or waiver, with pre-agreed criteria.", "Same platforms at every site", ""),
  ("Robustness by design of experiments", "ICH Q14", "1 to 2 weeks", "1 g", A17, "Multivariate study of pH, temperature, flow and gradient to define the operable region.", "DoE software, UHPLC", ""),
  ("Forced degradation", "ICH Q1A(R2), ICH Q2(R2)", "2 to 3 weeks", "2 to 5 g", A17, "Proves specificity and supports the stability-indicating claim.", "UHPLC-PDA, LC-MS", ML("forced-degradation")),
  ("Cleaning validation methods", "EU GMP Annex 15", "2 weeks", "API and swabs", A17, "Swab and rinse recovery with HPLC or TOC finishes.", "UHPLC, TOC analyser", ML("toc-conductivity-water")),
  ("Analytical procedure lifecycle", "USP ⟨1220⟩, ICH Q14", "Ongoing", "Data sets", A17, "Analytical target profile, continued performance verification and change management.", "LIMS trending", "")],
 "Development follows ICH Q14; validation follows ICH Q2(R2) (adopted 2023), USP ⟨1225⟩ and ⟨1226⟩; transfer follows USP ⟨1224⟩. Reports slot into CTD section 3.2.P.5.3 and 3.2.S.4.3.",
 [("inst-hplc", "Method development UHPLC", ["Six-column switching", "Quaternary pumps", "Automated pH and solvent screening"]),
  ("inst-lcms", "LC-MS for specificity", ["Peak purity beyond PDA", "Unknowns identified by HRMS"]),
  ("lab-analyst-pc", "DoE and statistics", ["Design space modelling", "Validated calculation templates", "Method operable design region reports"]),
  ("lab-team-three", "Transfer team", ["Same SOPs at every site", "Paired analysts for training runs", "Acceptance criteria agreed up front"])],
 (58, "of planned method development capacity booked", "Development and validation capacity across Hyderabad, Bengaluru and Singapore."),
 ["Drug substance and product samples (5 to 20 g API typical)", "Impurity and reference standards, with CoAs", "Any existing method, validation report and history", "Specification and target limits (the analytical target profile)", "Placebo or excipient blend for specificity", "Known stability or degradation information"],
 [("Submit", "Agree the analytical target profile: what the method must measure, how well and over what range.", "docs-papers", "sealed"),
  ("Receive", "Standards and samples logged; feasibility runs start within days.", "lab-glassware", "opened"),
  ("Test", "Screening, DoE optimisation, forced degradation, then a written validation protocol.", "inst-hplc", "instrument"),
  ("Release", "Signed validation report and the method entered into the LIMS for routine use anywhere in the network.", "lab-analyst-pc", "reported")],
 (CHIP("Transfer in 9 days", "A stability method moved from a client lab to Singapore", "<p>With the same column, the same CDS template and a pre-agreed comparative protocol, transfer was complete in 9 business days instead of the 6 weeks planned.</p>"),
  "method development, validation to ICH Q2(R2) and transfer to USP ⟨1224⟩ for chromatographic, dissolution and spectroscopic methods.",
  "A method that only works in the lab that wrote it is not finished. We develop for the second lab from day one."),
 [("What changed with ICH Q2(R2)?", "<p>It covers more techniques, including multivariate and spectroscopic methods, replaces 'linearity' with 'response' within the range, and links validation to development data under ICH Q14.</p>"),
  ("Do I need ICH Q14's enhanced approach?", "<p>No. The minimal approach is still acceptable. The enhanced approach earns flexibility for post-approval changes when you define an analytical target profile and a proven operable region.</p>"),
  ("How long does validation take?", "<p>Typically 2 to 4 weeks after the protocol is approved, depending on the number of parameters and impurity levels.</p>"),
  ("Validation, verification or transfer: which do I need?", "<p>New non-compendial methods need validation. Compendial methods need verification under USP ⟨1226⟩. Moving a validated method to a new lab needs a transfer under USP ⟨1224⟩.</p>"),
  ("Why do method transfers fail?", "<p>Usually unstated method details: column history, dwell volume, integration rules, sample preparation steps that live in one analyst's head. Our transfer gap review captures them before the first injection.</p>"),
  ("Can you develop phase-appropriate methods?", "<p>Yes. Phase 1 methods are qualified and fit for purpose; full validation comes before pivotal batches.</p>"),
  ("What is an analytical target profile?", "<p>A short statement of what a method must measure, in what range and with what accuracy and precision. It drives every development choice under ICH Q14.</p>"),
  ("Do you write the CTD sections?", "<p>We provide the validation summary in CTD format, and our regulatory team can draft section 3.2.P.5 on request.</p>")],
 TOOL_VW,
 [("QbD analytical development", "<p>Define the analytical target profile, identify method parameters with risk assessment, study them with DoE, and set a control strategy. The result is a method that holds up when columns, analysts or labs change.</p>", ""),
  ("Method transfer checklist", "<ul><li>Method version and change history</li><li>Column brand, chemistry, lot history</li><li>System dwell volume and detector settings</li><li>Integration events, written down</li><li>Sample and standard preparation, step by step</li><li>Acceptance criteria agreed before data</li></ul><p><a href='/submit-samples.html#sheet'>Download the checklist</a> with the sample sheet.</p>", ""),
  ("Why 40 percent of transfers fail", f"<p>Our planning figure {ILL('Illustrative')} reflects what scientists across the industry report informally: many first-attempt transfers need rework. Nearly every cause is preventable with a gap review and pre-agreed criteria.</p>", AR("method-transfer-failure")),
  ("Lifecycle management under ICH Q14", "<p>After validation the method enters continued performance verification: system suitability trends, control samples and periodic review. Changes inside an approved operable region need no new validation.</p>", "")],
 ["small-molecule-qc-release", "stability-studies", "regulatory-data-integrity-support"],
 ("Let's make your next method transfer boring (in a good way).", "Send the method and the history. We return a gap review and a fixed price for transfer within two days."),
 extra_top=GALLERY(["inst-hplc", "lab-analyst-pc", "lab-glassware"], ["Liquid chromatography for development", "Modelling robustness data", "Clean glassware for standard preparation"]))

# ---------- 4. Biologics ----------
svc_page("biologics-characterization-release",
 ("Characterisation, comparability and release testing for monoclonal antibodies, recombinant proteins and biosimilars.",
  "Biologics characterisation and release proves a protein product is what it should be, batch after batch. We measure size variants by SEC and CE-SDS, charge variants by icIEF, structure by peptide mapping and intact mass spectrometry, glycans, potency in cell-based and binding assays, and process impurities such as host cell protein, residual DNA and Protein A."),
 [("5 to 15 d", "release TAT"), ("13", "core methods"), ("3 tiers", "similarity statistics")],
 V_AB, [("98.9%", "SEC monomer"), ("±1 Da", "intact mass"), ("<1 ppm", "HCP (LOQ range)"), ("85–115%", "potency range")],
 [("Size variants (SEC-HPLC)", "Ph. Eur. 2.2.30, ICH Q6B", "2 to 3 days", "200 µg", A17, "Monomer, aggregates and fragments; SEC-MALS for absolute molar mass.", "UHPLC with UV and MALS", ML("sec-hplc-aggregates")),
  ("CE-SDS, reduced and non-reduced", "USP ⟨129⟩, ICH Q6B", "2 to 3 days", "200 µg", A17, "Purity, light and heavy chains, non-glycosylated heavy chain.", "Capillary electrophoresis with UV", ML("ce-sds")),
  ("Charge variants (icIEF)", "Ph. Eur. 2.2.54, ICH Q6B", "2 to 3 days", "100 µg", A17, "Acidic, main and basic species with pI markers.", "Imaged capillary IEF", ML("icief-charge-variants")),
  ("Peptide mapping (LC-MS)", "Ph. Eur. 2.2.55, ICH Q6B", "5 to 10 days", "500 µg", A17, "Sequence coverage, oxidation, deamidation and other modifications quantified.", "UHPLC with HRMS", ML("peptide-mapping-lc-ms")),
  ("Intact and subunit mass", "ICH Q6B", "3 to 5 days", "100 µg", A17, "Glycoform profile and mass confirmation at intact and IdeS/reduced level.", "Q-TOF", ML("intact-mass-ms")),
  ("Glycan profiling", "USP ⟨212⟩, Ph. Eur. 2.2.59", "5 to 7 days", "300 µg", A17, "Released N-glycans labelled and separated by HILIC with fluorescence and MS.", "HILIC-FLR-MS", ML("glycan-profiling-hilic")),
  ("Cell-based potency", "USP ⟨1032⟩, USP ⟨1034⟩", "7 to 14 days", "1 mg", A17, "Parallel-line or 4PL relative potency against the reference standard.", "Plate readers, cell culture suite", ML("cell-based-potency")),
  ("Binding assays (ELISA, SPR)", "ICH Q6B", "3 to 7 days", "500 µg", A17, "Target and Fc-receptor binding, including FcγRIIIa and FcRn.", "SPR, plate readers", ""),
  ("Host cell protein (ELISA)", "USP ⟨1132⟩", "3 to 5 days", "500 µg", A17, "Generic or process-specific ELISA; MS-based HCP identification on request.", "Plate readers, LC-MS", ML("hcp-elisa")),
  ("Residual host cell DNA (qPCR)", "USP ⟨509⟩", "3 days", "200 µg", A17, "CHO or E. coli DNA quantified against a reference curve.", "qPCR", ML("residual-dna-qpcr")),
  ("Residual Protein A", "ICH Q6B", "2 to 3 days", "200 µg", A17, "Leached Protein A by ELISA.", "Plate readers", ""),
  ("Sub-visible particles", "USP ⟨787⟩, USP ⟨788⟩", "2 days", "5 mL", A17, "Light obscuration and flow imaging for protein particles.", "LO and flow imaging", ""),
  ("Higher-order structure", "ICH Q6B, ICH Q5E", "5 to 10 days", "2 mg", A17, "Circular dichroism, DSC and FTIR for comparability.", "CD, DSC, FTIR", "")],
 "Release and characterisation follow ICH Q6B, comparability follows ICH Q5E, and biosimilar similarity packages follow FDA and EMA biosimilar quality guidance.",
 [("lab-instrument-load", "Automated sample handling", ["Plate preparation for potency", "Barcode tracking"]),
  ("inst-lcms", "High-resolution MS", ["Intact, subunit and peptide level", "Sub-ppm mass accuracy"]),
  ("lab-automation", "Capillary electrophoresis and icIEF", ["CE-SDS and icIEF on one platform family", "Same templates at every site"]),
  ("lab-microscope-close", "Cell culture suite", ["Potency assays", "Mycoplasma-free master cell banks"])],
 (61, "of planned biologics capacity booked", "Biologics capacity across Bengaluru, Singapore and Leiden."),
 ["Drug substance or product: 2 to 10 mg depending on panel", "Reference standard and lot history", "Storage at the labelled temperature, shipped with a logger", "Formulation buffer or placebo for blanks", "Specification and any client-specific methods", "For biosimilars: reference product lots with purchase records"],
 [("Submit", "Agree the panel: release, characterisation or a full similarity package.", "docs-papers", "sealed"),
  ("Receive", "Cold-chain receipt checked against the logger; aliquots frozen per method.", "lab-tube-rack", "opened"),
  ("Test", "Size, charge, mass and potency run in parallel on qualified platforms.", "lab-instrument-load", "instrument"),
  ("Release", "QA-approved report, statistics for comparability, raw data in the portal.", "lab-analyst-pc", "reported")],
 (CHIP("14 → 6 weeks", "Biosimilar comparability package", "<p>Charge, size, glycan and potency methods ran in parallel at two labs on one LIMS, with acceptance criteria agreed before the first injection.</p>"),
  "size and charge variants, peptide mapping, intact mass, glycans, potency and process impurities.",
  "Similarity is a statistical argument, not a single chromatogram."),
 [("What does a biosimilar analytical similarity package include?", "<p>Primary structure, higher-order structure, glycans, size and charge variants, biological activity and process impurities, on multiple lots of both products, evaluated with risk-based statistics.</p>"),
  ("How many reference lots do I need?", "<p>Regulators expect enough to understand the reference product's variability. Ten or more lots for critical attributes is common; your agency's feedback decides.</p>"),
  ("What are the similarity tiers?", "<p>Attributes are ranked by risk. Tier 1 uses equivalence testing, Tier 2 quality ranges, Tier 3 visual comparison. FDA has since moved towards quality-range approaches for many attributes.</p>"),
  ("Do you develop potency assays?", "<p>Yes, cell-based and binding, designed and validated to USP ⟨1032⟩ to ⟨1034⟩.</p>"),
  ("Can you run comparability after a process change?", "<p>Yes, under ICH Q5E: pre- and post-change lots side by side with forced degradation where relevant.</p>"),
  ("How do you handle frozen drug substance?", "<p>Shipped on dry ice with a logger, received at −70 °C or colder, aliquoted once to avoid freeze-thaw cycles.</p>"),
  ("Which HCP assay do you use?", "<p>A commercial generic assay for early phases, or your process-specific assay transferred to us. MS-based HCP identification supports risk assessment.</p>"),
  ("Can you test biologics in prefilled syringes?", "<p>Yes, including sub-visible particles and silicone oil droplets by flow imaging, and E&L with our E&L team.</p>")],
 TOOL_BS,
 [("Comparability study design", "<p>Define the change, the attributes it could affect, the lots, the methods and the acceptance criteria before testing. ICH Q5E expects that order.</p>", ""),
  ("Analytical similarity explained", "<p>Similarity means no clinically meaningful differences, shown first through extensive analytics. The stronger the analytical data, the smaller the clinical programme that follows.</p>", AR("biosimilar-analytical-similarity")),
  ("Glycosylation and why it matters", "<p>Afucosylation raises FcγRIIIa binding and ADCC; high mannose shortens half-life; sialylation affects inflammation. Glycan control is usually a critical quality attribute for antibodies.</p>", ""),
  ("Choosing a potency assay", "<p>The assay should reflect the mechanism of action. For an ADCC-dependent antibody, binding alone is not enough; a reporter or primary-cell ADCC assay is expected.</p>", "")],
 ["bioanalytical-immunogenicity", "stability-studies", "method-development-validation"],
 ("Specialist hands for specialist molecules.", "Tell us the molecule, the phase and the question. We will propose a panel and a timeline within two days."),
 extra_top=GALLERY(["lab-instrument-load", "inst-lcms", "lab-microscope-close"], ["Loading samples for analysis", "Mass spectrometry for structure", "Cell culture for potency"]))

# ---------- 5. mRNA ----------
svc_page("mrna-vaccine-testing",
 ("Release and characterisation for mRNA therapeutics, LNP formulations and vaccines.",
  "mRNA and vaccine testing measures the attributes that decide whether an mRNA medicine works: RNA integrity, 5′ capping efficiency, poly(A) tail length, residual dsRNA and DNA template, lipid nanoparticle size, PDI and encapsulation efficiency, lipid identity and purity, in vitro expression potency, endotoxin and sterility, plus antigen assays for conventional vaccines."),
 [("5 to 12 d", "release TAT"), ("10", "critical attributes mapped"), ("−80 °C", "sample handling")],
 V_LNP, [("94%", "EE (example)"), ("82 nm", "size (example)"), (">90%", "capped (typical)"), ("PDI 0.11", "example")],
 [("mRNA integrity", "WHO mRNA guidance (2022)", "2 to 3 days", "10 µg RNA", A17, "Capillary gel electrophoresis or fragment analyser; % full-length mRNA.", "CE, fragment analyser", ML("mrna-integrity-ce")),
  ("5′ capping efficiency", "WHO mRNA guidance (2022), USP mRNA draft guidelines", "5 to 7 days", "50 µg RNA", A17, "RNase H-directed cleavage then LC-MS quantification of capped species.", "LC-HRMS", ML("mrna-capping-lc-ms")),
  ("Poly(A) tail length", "USP mRNA draft guidelines", "5 to 7 days", "50 µg RNA", A17, "RNase T1 digestion and LC-MS for length and distribution.", "LC-HRMS", ML("poly-a-tail-length")),
  ("Residual dsRNA", "WHO mRNA guidance (2022)", "3 days", "20 µg RNA", A17, "J2 antibody ELISA or dot blot.", "Plate readers", ML("dsrna-elisa")),
  ("Residual DNA template", "WHO mRNA guidance (2022)", "3 days", "20 µg RNA", A17, "qPCR against the linearised plasmid sequence.", "qPCR", ML("residual-dna-qpcr")),
  ("Identity by sequencing", "WHO mRNA guidance (2022)", "5 to 10 days", "10 µg RNA", A17, "RT-PCR and Sanger or NGS sequence confirmation.", "Sequencers", ""),
  ("LNP size and PDI", "ISO 22412", "1 day", "100 µL", A17, "Dynamic light scattering; Z-average and polydispersity index.", "DLS", ML("lnp-size-pdi-dls")),
  ("Encapsulation efficiency", "WHO mRNA guidance (2022)", "1 to 2 days", "100 µL", A17, "RiboGreen fluorescence with and without detergent.", "Plate readers", ML("encapsulation-efficiency-ribogreen")),
  ("Lipid identity, content and purity", "ICH Q6A principles", "3 to 5 days", "200 µL", A17, "HPLC with charged aerosol detection for all four lipids and degradants.", "HPLC-CAD", ""),
  ("In vitro expression potency", "WHO mRNA guidance (2022)", "5 to 7 days", "50 µg RNA", A17, "Transfection of cells and protein detection by flow or ELISA.", "Cell culture, flow cytometry", ML("cell-based-potency")),
  ("Bacterial endotoxins", "USP ⟨85⟩, Ph. Eur. 2.6.14", "1 day", "1 mL", A17, "Kinetic chromogenic LAL or recombinant factor C.", "Kinetic plate readers", ML("bacterial-endotoxins-lal")),
  ("Sterility", "USP ⟨71⟩, Ph. Eur. 2.6.1", "14 days", "Per USP ⟨71⟩ table", A17, "Membrane filtration in an isolator.", "Isolator, incubators", ML("sterility-membrane-filtration")),
  ("Residual ethanol", "ICH Q3C, USP ⟨467⟩", "2 days", "1 mL", A17, "GC headspace for solvent left from LNP formation.", "GC-FID headspace", ML("residual-solvents-gc-hs"))],
 "Methods follow WHO guidance on mRNA vaccines (2022), the USP draft guidelines for mRNA quality, and FDA and EMA expectations for vaccines and nucleic acid products.",
 [("vax-vials", "Ultra-cold storage", ["−80 °C freezers with remote alarms", "Dry-ice receipt and logging"]),
  ("inst-lcms", "LC-HRMS for cap and tail", ["Oligonucleotide workflows", "Intact and fragment level"]),
  ("lab-plate-pink", "Plate-based assays", ["RiboGreen EE", "dsRNA ELISA", "Expression potency"]),
  ("inst-pcr", "qPCR and ddPCR", ["Residual DNA template", "Identity by RT-PCR"])],
 (49, "of planned mRNA analytics capacity booked", "Capacity model for Pune, Singapore and New Jersey."),
 ["RNA: 100 to 500 µg per full release panel", "LNP product: at least 2 mL per lot", "Ship on dry ice with a temperature logger", "Sequence and construct map (under NDA)", "Reference material or previous lot", "Lipid composition and molar ratios"],
 [("Submit", "Map your CQAs to methods and agree the panel.", "docs-papers", "sealed"),
  ("Receive", "Dry-ice receipt; aliquots made once under RNase-free conditions.", "vax-vials", "opened"),
  ("Test", "RNA and LNP methods in parallel on dedicated RNase-free benches.", "inst-lcms", "instrument"),
  ("Release", "Integrated CoA covering RNA, LNP and safety tests.", "lab-goggles", "reported")],
 (CHIP("5 labs → 1", "An mRNA developer consolidated its release panel", "<p>Cap, tail, integrity, EE and safety testing moved from five vendors to one network with one CoA, removing two weeks of coordination per lot.</p>"),
  "integrity, capping, tail length, dsRNA, residual DNA, LNP size, PDI, EE, endotoxin and sterility.",
  "Most mRNA failures show up in the cap long before potency."),
 [("What are the critical quality attributes of an mRNA product?", "<p>Identity, integrity, capping, poly(A) tail, dsRNA and DNA template impurities, LNP size, PDI and encapsulation, lipid content, potency, and safety tests such as endotoxin and sterility.</p>"),
  ("Why does dsRNA matter?", "<p>Double-stranded RNA formed during in vitro transcription activates innate immune sensors, which can reduce protein expression and cause reactogenicity.</p>"),
  ("How is capping efficiency measured?", "<p>A probe directs RNase H to cut near the 5′ end; the short fragment is analysed by LC-MS to quantify Cap 1, Cap 0 and uncapped species.</p>"),
  ("What encapsulation efficiency is typical?", "<p>Published processes commonly report above 90%. Your acceptance criterion comes from your clinical lots.</p>"),
  ("Can you test self-amplifying RNA?", "<p>Yes. Longer constructs need adapted integrity and sequencing methods; tell us the length at quote stage.</p>"),
  ("How do you prevent RNase contamination?", "<p>Dedicated benches, RNase-free consumables, routine surface checks and separate pipettes for RNA work.</p>"),
  ("Do you test conventional vaccines too?", "<p>Yes: antigen content, adjuvant content, potency assays and safety tests, depending on the product.</p>"),
  ("How should mRNA samples be shipped?", "<p>Usually on dry ice at −70 °C or colder, with a logger. We book the courier and track the shipment.</p>")],
 TOOL_QA,
 [("Critical quality attributes of mRNA therapeutics", "<p>Start from the product: the RNA, its impurities and the LNP. Each attribute links to safety or efficacy, and each needs a method with known capability.</p>", AR("mrna-critical-quality-attributes")),
  ("Why dsRNA matters and how it is measured", "<p>The J2 antibody recognises double-stranded regions of 40 base pairs or more. ELISA gives a number; dot blot gives a quick check. Purification by cellulose or HPLC reduces it.</p>", ""),
  ("Scaling analytics from clinical to commercial", "<p>Clinical methods are often research methods. Before commercial filing they need validation, transfer and robust reference materials. Plan this 12 to 18 months ahead.</p>", ""),
  ("Cold-chain handling for mRNA samples", "<p>Freeze once, aliquot once, log everything. Repeated freeze-thaw changes LNP size and EE, which can look like a stability failure.</p>", "")],
 ["microbiology-sterility", "stability-studies", "extractables-leachables"],
 ("Specialist testing for the next generation of medicines.", "Send your CQA list. A specialist replies within 4 business hours with a panel and a date."),
 extra_top=GALLERY(["vax-vials", "bio-dna", "vax-virus"], ["Vaccine vials awaiting release", "Nucleic acids are the product", "Viral antigens for conventional vaccines"]))

# ---------- 6. CGT ----------
svc_page("cell-gene-therapy-testing",
 ("Release and characterisation for AAV and lentiviral vectors, CAR-T and other cell therapies, with rapid methods for fresh products.",
  "Cell and gene therapy testing proves identity, purity, potency and safety for products where every sample is irreplaceable. We measure vector genome titre by ddPCR, AAV empty/full ratio by AUC and mass photometry, replication-competent virus, flow cytometry identity and purity, potency, rapid sterility, mycoplasma by NAT, endotoxin and residual host cell DNA."),
 [("Same day", "rapid release tests"), ("3 products", "AAV, LV, CAR-T"), ("Day 7", "interim sterility")],
 V_AAV, [("1.2e13", "vg/mL (example)"), ("82%", "full capsids"), ("48 h", "CAR-T release"), ("ddPCR", "titre")],
 [("Vector genome titre", "USP ⟨1047⟩, FDA CMC gene therapy guidance (2020)", "2 days", "50 µL", A17, "ddPCR against transgene or ITR with DNase pre-treatment.", "Droplet digital PCR", ML("ddpcr-vector-titre")),
  ("AAV empty/full ratio", "USP ⟨1047⟩", "3 days", "400 µL", A17, "Analytical ultracentrifugation; mass photometry as an orthogonal fast method.", "AUC, mass photometer", ML("aav-empty-full-auc")),
  ("Capsid titre", "USP ⟨1047⟩", "2 days", "50 µL", A17, "Serotype-specific ELISA.", "Plate readers", ""),
  ("Infectious titre", "USP ⟨1047⟩", "10 days", "100 µL", A17, "TCID50 with qPCR readout.", "Cell culture, qPCR", ""),
  ("Replication-competent virus", "FDA CMC gene therapy guidance (2020)", "21 to 28+ days", "Per guidance", A17, "RCA for AAV, RCL for lentiviral vectors by cell-based amplification.", "BSL-2 cell culture", ""),
  ("Identity and purity (flow cytometry)", "Ph. Eur. 2.7.24", "Same day", "1e6 cells", A17, "CD3, CAR expression and phenotype panels.", "Spectral flow cytometers", ML("flow-cytometry-identity")),
  ("Viability and cell count", "Ph. Eur. 2.7.29", "Same day", "1e5 cells", A17, "7-AAD flow or image cytometry.", "Flow, image cytometers", ""),
  ("Vector copy number", "FDA CMC gene therapy guidance (2020)", "1 day", "1e6 cells", A17, "ddPCR per diploid genome.", "ddPCR", ML("ddpcr-vector-titre")),
  ("Potency", "FDA potency guidance for CGT products", "1 to 14 days", "Varies", A17, "Cytotoxicity, IFN-γ release or transgene activity, matched to mechanism.", "Plate readers, flow", ML("cell-based-potency")),
  ("Sterility (rapid and compendial)", "USP ⟨71⟩, Ph. Eur. 2.6.27", "Day 7 interim, 14 days final", "Per product", A17, "Automated growth-based rapid method with compendial confirmation.", "Isolator, automated culture", ML("sterility-membrane-filtration")),
  ("Mycoplasma (NAT)", "Ph. Eur. 2.6.7", "Same day", "Per product", A17, "Validated nucleic acid amplification replacing 28-day culture.", "qPCR", ML("mycoplasma-nat")),
  ("Bacterial endotoxins", "USP ⟨85⟩, Ph. Eur. 2.6.14", "Same day", "100 µL", A17, "LAL or recombinant factor C.", "Kinetic plate readers", ML("bacterial-endotoxins-lal")),
  ("Residual host cell DNA", "USP ⟨509⟩", "3 days", "100 µL", A17, "HEK293 or other host DNA by qPCR.", "qPCR", ML("residual-dna-qpcr"))],
 "Testing follows FDA guidance for human gene therapy INDs (2020), Ph. Eur. 5.14 and 2.6.27, USP ⟨1046⟩ and ⟨1047⟩, and EMA ATMP guidelines.",
 [("inst-pcr", "ddPCR and qPCR", ["Vector genome titre", "Vector copy number", "Residual DNA"]),
  ("bio-cells-green", "Flow cytometry", ["Spectral panels", "Same-day identity and viability"]),
  ("lab-cleanroom-suit", "Isolators for rapid sterility", ["Grade A environment", "Automated culture with day-7 interim"]),
  ("lab-microscope-woman", "BSL-2 cell culture", ["RCA and RCL assays", "Potency assays"])],
 (44, "of planned CGT capacity booked", "Capacity model for Singapore and Cambridge."),
 ["Sample volumes agreed per test: CGT samples are small, so plan them together", "Fresh products: courier booked before collection; time from collection recorded", "Frozen vector: dry ice with logger", "Chain of identity documents for patient-specific products", "Reference vector or cell lot", "Biosafety declaration (BSL level, vector type)"],
 [("Submit", "Agree the panel and the sample budget per lot; book the courier slot.", "docs-papers", "sealed"),
  ("Receive", "Chain-of-identity check, immediate split to each test in a biosafety cabinet.", "lab-cleanroom-suit", "opened"),
  ("Test", "Rapid tests run first; long assays continue after interim release data.", "inst-pcr", "instrument"),
  ("Release", "Interim and final CoAs, both e-signed, with clear 'not final' marking on interim data.", "lab-goggles", "reported")],
 (CHIP("Release in 48 h", "Autologous CAR-T inside a 72-hour window", "<p>Rapid sterility, flow identity and potency ran in parallel with a dedicated evening shift, leaving a full day for logistics.</p>"),
  "vector titre, empty/full, identity, viability, potency, rapid sterility, mycoplasma NAT and endotoxin.",
  "When the sample is a patient's own cells, there is no second chance. Plan every microlitre."),
 [("Which release tests does an AAV product need?", "<p>Typically vector genome titre, capsid titre and empty/full ratio, identity, purity, infectious titre or potency, replication-competent AAV, residual impurities, sterility, mycoplasma and endotoxin.</p>"),
  ("How fast can you release an autologous product?", "<p>Same-day identity, viability, endotoxin and mycoplasma NAT; potency in 1 to 3 days; rapid sterility with an interim result around day 7.</p>"),
  ("Is mycoplasma NAT accepted instead of culture?", "<p>Ph. Eur. 2.6.7 allows validated NAT methods as an alternative, and regulators accept them for short shelf-life products when validated.</p>"),
  ("AUC or mass photometry for empty/full?", "<p>AUC is the reference method. Mass photometry is faster and uses less sample, and works well as an orthogonal or in-process method.</p>"),
  ("How much sample do you need?", "<p>It depends on the panel. We build a sample budget with you so every microlitre is assigned before collection.</p>"),
  ("How do you protect chain of identity?", "<p>Two-person verification at receipt, barcode labels from your system where possible, and no relabelling.</p>"),
  ("Do you run replication-competent virus assays?", "<p>Yes, for AAV and lentiviral vectors, in BSL-2 facilities. They take 3 to 4 weeks or more, so they run on the vector lot.</p>"),
  ("Can you help design a potency assay?", "<p>Yes. FDA expects potency to reflect the mechanism of action; we develop and qualify assays with you.</p>")],
 TOOL_CG,
 [("Autologous versus allogeneic release", "<p>Autologous products are one batch per patient with tiny samples and hours to spare. Allogeneic products are larger batches tested more like biologics. The release strategy differs: rapid methods matter most for autologous.</p>", AR("cgt-release-testing")),
  ("Why timing matters for fresh products", "<p>Cells lose viability by the hour. Results that arrive after infusion are not release results; they are follow-up. Design the panel around the infusion window.</p>", ""),
  ("Regulatory expectations by region", "<p>FDA uses IND CMC guidance and potency guidance; EMA treats CGT as ATMPs with GMP for ATMPs; India's CDSCO regulates under the New Drugs and Clinical Trials Rules 2019. Methods are shared; expectations on timing and validation differ.</p>", ""),
  ("Sample budgeting", "<p>List every test, its volume and replicates, add 20% for repeats, and compare against what the process can spare. Then decide which tests move to the vector lot.</p>", "")],
 ["microbiology-sterility", "bioanalytical-immunogenicity", "biologics-characterization-release"],
 ("Where every sample is irreplaceable.", "Tell us the product type and the infusion window. We will propose a release panel and a sample budget."),
 extra_top=GALLERY(["bio-cells-green", "lab-cleanroom-suit", "bio-cells-pink"], ["Cells under fluorescence microscopy", "Aseptic work in a cleanroom", "Stained nuclei in cultured cells"]))
