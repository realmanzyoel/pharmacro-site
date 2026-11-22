"""PharmaCRO client site: data, layout and interactive components.
Built on the Investor Labs design system (lib.py helpers + il.css/il.js), re-themed by assets/ph.css + ph.js.
Content modules do:  from ph import *   and call page(path, ...).
Write internal links root-absolute ("/services/stability-studies.html"); render() rewrites them relative so the site also works from file://.
Honesty rule (from the blueprint): every figure, accreditation, inspection outcome, person and client story is an illustrative
placeholder until Quality and Legal verify it. Mark them with ILL() / the global preview bar; never present them as verified.
"""
import os, re, html, json
from lib import *   # P, H2, H3, UL, OL, T, KV, GRID, FLOW, IMG, SPLIT, GALLERY, STRIP, BAND, MOSAIC, QUOTE, KPI, BARS, COLS, LINE, DONUT, RING, FUNNEL, TIMELINE, VS, PILLS, SECTION, CALL, BTN, alt, ALT

BRAND = "PharmaCRO"
TAG = "Pharmaceutical testing network"
MAIL = "contact@eliteleadgrow.com"  # every form opens the visitor's mail app addressed here (no backend yet)
ASOF = "21 November 2026"
# Phone numbers are fictional placeholders. Replace before launch.
PHONES = [("India", "+91 40 5550 0142", "+914055500142"), ("Singapore", "+65 5550 0142", "+6555500142"),
          ("Europe", "+31 20 555 0142", "+31205550142"), ("United States", "+1 (609) 555-0142", "+16095550142")]

def ILL(t="Illustrative"):
    """Small inline marker on any figure or claim that is a placeholder pending verification."""
    return f'<span class="ill" title="Placeholder until verified by Quality and Legal">{t}</span>'

# ---------- services ----------
# slug, name, short, headline, image, icon, TAT range, 3 key tests, lead scientist key, modalities, stages, hero-motion key
SERVICES = [
 ("small-molecule-qc-release", "Small Molecule QC and Release", "Release testing for tablets, capsules, injectables and APIs.", "Release batches with confidence.",
  "lab-pipette-vials", "tablet", "3 to 10 days", ["Assay and related substances (HPLC)", "Dissolution, all USP apparatus", "Nitrosamines and NDSRIs (LC-MS/MS)"], "ananya", ["small"], ["clinical", "commercial", "post"], "dissolve"),
 ("stability-studies", "Stability Studies", "ICH stability programmes in every climatic zone, I to IVb.", "Stability that holds up in every climate.",
  "lab-corridor", "clock", "Pull to report in 5 to 10 days", ["ICH long-term, intermediate, accelerated", "Photostability (ICH Q1B)", "Zone IVb (30 °C / 75% RH)"], "rahul", ["small", "bio", "mrna"], ["clinical", "commercial", "post"], "zones"),
 ("method-development-validation", "Method Development, Validation and Transfer", "HPLC, GC, LC-MS and dissolution methods that transfer first time.", "Methods that transfer first time.",
  "inst-hplc", "peak", "2 to 8 weeks", ["Method development (QbD, ICH Q14)", "Validation to ICH Q2(R2)", "Cross-lab method transfer"], "mei", ["small", "bio"], ["preclinical", "clinical", "commercial"], "peak"),
 ("biologics-characterization-release", "Biologics Characterization and Release", "Similarity and consistency for monoclonals, proteins and biosimilars.", "Prove similarity. Prove consistency.",
  "lab-instrument-load", "antibody", "5 to 15 days", ["SEC, CE-SDS and icIEF", "Peptide mapping and intact MS", "Cell-based potency"], "elena", ["bio"], ["preclinical", "clinical", "commercial"], "antibody"),
 ("mrna-vaccine-testing", "mRNA and Vaccine Testing", "Integrity, capping, poly(A), dsRNA and LNP characterisation.", "Specialist testing for the next generation of medicines.",
  "vax-vials", "helix", "5 to 12 days", ["mRNA integrity (CE, fragment analysis)", "5' capping and poly(A) tail length", "LNP size, PDI and encapsulation"], "kenji", ["mrna"], ["preclinical", "clinical", "commercial"], "lnp"),
 ("cell-gene-therapy-testing", "Cell and Gene Therapy Testing", "Release and characterisation for AAV, lentiviral and CAR-T products.", "Where every sample is irreplaceable.",
  "bio-cells-green", "capsid", "1 to 14 days", ["Vector genome titre (ddPCR)", "AAV empty/full ratio (AUC)", "Flow cytometry identity and purity"], "sara", ["cgt"], ["preclinical", "clinical", "commercial"], "capsid"),
 ("microbiology-sterility", "Microbiology and Sterility", "Sterility, endotoxin, bioburden and mycoplasma testing.", "Sterility you can bank on.",
  "micro-petri-1", "dish", "2 to 14 days", ["Sterility (USP <71>, Ph. Eur. 2.6.1)", "Bacterial endotoxins (LAL and recombinant)", "Mycoplasma (culture and NAT)"], "priya", ["small", "bio", "mrna", "cgt"], ["clinical", "commercial", "post"], "colonies"),
 ("environmental-monitoring", "Environmental Monitoring and Cleanrooms", "Viable and non-viable monitoring, water and gas testing.", "Prove your cleanroom stays clean.",
  "room-clean-2", "air", "1 to 7 days", ["Viable air and surface monitoring", "Purified water and WFI testing", "Cleanroom classification (ISO 14644)"], "tom", ["small", "bio", "mrna", "cgt"], ["commercial", "post"], "hepa"),
 ("extractables-leachables", "Extractables and Leachables", "E&L studies and packaging compatibility for every container type.", "Know what your packaging puts in your product.",
  "lab-vials-bw", "vial", "4 to 12 weeks", ["Extractables studies (GC-MS, LC-MS, ICP-MS)", "Leachables on stability", "USP <661>, <1663>, <1664>"], "lukas", ["small", "bio"], ["clinical", "commercial"], "migrate"),
 ("bioanalytical-immunogenicity", "Bioanalytical and Immunogenicity", "PK, ADA and NAb assays validated to ICH M10.", "Clear answers from complex samples.",
  "inst-lcms", "plasma", "1 to 6 weeks", ["LC-MS/MS PK assays", "ADA screening, confirmation and titre", "Neutralising antibody assays"], "james", ["small", "bio", "mrna", "cgt"], ["preclinical", "clinical"], "lcms"),
 ("reference-standards-excipients", "Reference Standards and Excipient Testing", "Compendial testing of excipients, APIs and reference standards.", "Trust every ingredient.",
  "lab-glassware", "crystal", "3 to 10 days", ["Compendial monograph testing (USP, EP, JP, IP)", "Reference standard qualification", "Raw material identity (FTIR, Raman)"], "ananya", ["small", "bio"], ["discovery", "clinical", "commercial"], "xrpd"),
 ("regulatory-data-integrity-support", "Regulatory and Data Integrity Support", "Mock inspections, ALCOA+ gap assessments and CTD Module 3 support.", "Be inspection-ready on any day.",
  "docs-papers", "shield", "1 to 6 weeks", ["Mock inspections and DI gap assessments", "CTD Module 3 analytical sections", "OOS and deviation investigation support"], "helen", ["small", "bio", "mrna", "cgt"], ["clinical", "commercial", "post"], "dossier"),
]
SVC = {s[0]: s for s in SERVICES}
def svc_url(slug): return f"/services/{slug}.html"

MODALITIES = [("small", "Generic or small molecule", "pharma-blisters"), ("bio", "Biosimilar or biologic", "lab-instrument-load"),
              ("mrna", "mRNA or vaccine", "vax-vials"), ("cgt", "Cell or gene therapy", "bio-cells-green"), ("unsure", "Not sure yet", "lab-goggles")]
STAGES = [("discovery", "Discovery", "Fit-for-purpose methods and early characterisation."), ("preclinical", "Preclinical", "GLP-aware characterisation and tox batch support."),
          ("clinical-phase-1-3", "Clinical (Phase 1 to 3)", "Phase-appropriate validation, release and stability."), ("commercial-release", "Commercial release", "Validated, fast, routine batch release."),
          ("post-approval-stability", "Post-approval and stability", "Ongoing stability, changes and lifecycle management.")]
STAGE_KEY = {"discovery": "discovery", "preclinical": "preclinical", "clinical": "clinical-phase-1-3", "commercial": "commercial-release", "post": "post-approval-stability"}

INDUSTRIES = [("generics", "Generics", "Tight margins and tight launch windows.", "pharma-blisters2"),
              ("biosimilars", "Biosimilars", "Proving similarity to a moving reference product.", "lab-instrument-load"),
              ("biotech-startups", "Biotech startups", "No internal lab, a small team and a board deadline.", "lab-team-three"),
              ("big-pharma", "Big pharma", "Overflow capacity and global consistency.", "lab-corridor"),
              ("cdmos", "CDMOs", "Your clients' timelines become your timelines.", "lab-automation"),
              ("vaccine-makers", "Vaccine makers", "High stakes, high volume, no margin for error.", "vax-vials"),
              ("api-manufacturers", "API manufacturers", "Impurity profiles every regulator will read.", "lab-flasks-pour"),
              ("excipient-packaging-suppliers", "Excipient and packaging suppliers", "Your customers' auditors are your auditors.", "pharma-capsules")]

# ---------- labs (planned network; locations come from the company plan, details are illustrative) ----------
# slug, city, country, region, lat, lon, phase ("Year 1"...), focus, image, specialties
LABS = [
 ("hyderabad", "Hyderabad", "India", "India", 17.39, 78.49, "Year 1", "Flagship: small molecule QC, stability, nitrosamines", "city-hyderabad", ["small-molecule-qc-release", "stability-studies", "method-development-validation", "reference-standards-excipients"]),
 ("mumbai", "Mumbai", "India", "India", 19.08, 72.88, "Year 1", "Small molecule QC, microbiology, export release", "city-mumbai2", ["small-molecule-qc-release", "microbiology-sterility", "environmental-monitoring"]),
 ("pune", "Pune", "India", "India", 18.52, 73.86, "Year 1", "Vaccines and microbiology", "city-pune", ["mrna-vaccine-testing", "microbiology-sterility", "stability-studies"]),
 ("bengaluru", "Bengaluru", "India", "India", 12.97, 77.59, "Year 1", "Biologics and bioanalytical", "city-bengaluru", ["biologics-characterization-release", "bioanalytical-immunogenicity", "method-development-validation"]),
 ("singapore", "Singapore", "Singapore", "Southeast Asia", 1.35, 103.82, "Year 2", "Biologics and cell and gene therapy hub for ASEAN", "city-singapore", ["biologics-characterization-release", "cell-gene-therapy-testing", "stability-studies"]),
 ("kuala-lumpur", "Kuala Lumpur", "Malaysia", "Southeast Asia", 3.14, 101.69, "Year 2", "Small molecule QC and Zone IVb stability", "city-kl", ["small-molecule-qc-release", "stability-studies", "environmental-monitoring"]),
 ("leiden", "Leiden", "Netherlands", "Europe", 52.16, 4.49, "Year 2 to 3", "EU release and biologics", "city-leiden", ["biologics-characterization-release", "extractables-leachables", "regulatory-data-integrity-support"]),
 ("cambridge", "Cambridge", "United Kingdom", "Europe", 52.21, 0.12, "Year 2 to 3", "Cell and gene therapy and bioanalytical", "city-cambridge", ["cell-gene-therapy-testing", "bioanalytical-immunogenicity", "method-development-validation"]),
 ("dublin", "Dublin", "Ireland", "Europe", 53.35, -6.26, "Year 2 to 3", "EU QC release and microbiology", "city-dublin", ["small-molecule-qc-release", "microbiology-sterility", "environmental-monitoring"]),
 ("new-jersey", "New Jersey", "United States", "United States", 40.35, -74.66, "Year 3", "US release, E&L and mRNA", "city-newjersey", ["extractables-leachables", "mrna-vaccine-testing", "small-molecule-qc-release"]),
]
LAB = {l[0]: l for l in LABS}
S_, LAT0_ = 2.7778, 80
MAP_W, MAP_H = 1000, round((LAT0_ + 58) * S_)
def xy(lat, lon): return round((lon + 180) * S_, 1), round((LAT0_ - lat) * S_, 1)
LAND = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "world.txt")).read()
LAND_MINI = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "world_mini.txt")).read()  # simplified for the nav menu

# ---------- people (illustrative profiles until the team is announced) ----------
SCI = {
 "ananya": ("Dr Ananya Rao", "Head of Small Molecule Analytics", "HPLC, dissolution and nitrosamine risk", "sci-woman-2", "Hyderabad"),
 "rahul": ("Rahul Mehta", "Stability Programme Lead", "ICH Q1 design and Zone IVb launches", "sci-man-4", "Mumbai"),
 "mei": ("Dr Mei Lin Tan", "Method Lifecycle Lead", "QbD development, ICH Q2(R2) and Q14", "sci-woman-3", "Singapore"),
 "elena": ("Dr Elena Novak", "Head of Biologics", "Biosimilar comparability and mass spectrometry", "sci-woman-7", "Leiden"),
 "kenji": ("Dr Kenji Sato", "mRNA and LNP Analytics Lead", "Capping, poly(A) and dsRNA methods", "sci-man-5", "Singapore"),
 "sara": ("Dr Sara Okafor", "Cell and Gene Therapy Lead", "ddPCR, AUC and flow cytometry release", "sci-woman-4", "Cambridge"),
 "priya": ("Priya Nair", "Head of Microbiology", "Sterility, endotoxin and rapid methods", "sci-woman-6", "Pune"),
 "tom": ("Tom Byrne", "Environmental Monitoring Lead", "Annex 1 contamination control strategies", "sci-man-1", "Dublin"),
 "lukas": ("Dr Lukas Weber", "E&L Programme Lead", "Extractables, leachables and packaging", "sci-man-3", "Leiden"),
 "james": ("Dr James Carter", "Bioanalytical Lead", "ICH M10 validation, PK and immunogenicity", "sci-man-2", "New Jersey"),
 "helen": ("Helen Murphy", "Head of Quality", "Data integrity, audits and inspection readiness", "sci-woman-5", "Dublin"),
 "arjun": ("Arjun Kapoor", "Head of Client Science", "Scoping calls and package design", "sci-man-6", "Bengaluru"),
}

# ---------- registry ----------
PAGES = {}  # path (no .html) -> dict

def page(path, title, lede, body, img=None, chips=None, eyebrow=None, hero="cine", desc=None, jsonld=None, cta=None, crumbs=None, hb=None, nav=None):
    """hero: "cine" (photo header), "plain" (text header), "bare" (body only).
    cta: (headline, text) for the closing quote band, False to omit. crumbs: [(label, path), ...] before this page.
    hb: hero buttons HTML (default: Request a quote + Talk to a scientist). nav: top-nav key to mark active."""
    PAGES[path] = dict(title=title, lede=lede, body=body, img=img, chips=chips or [], eyebrow=eyebrow, hero=hero, desc=desc,
                       jsonld=jsonld or [], cta=cta, crumbs=crumbs, hb=hb, nav=nav)

# ---------- icons (24px stroke) ----------
_IC = {
 "tablet": '<rect x="3" y="8" width="18" height="8" rx="4"/><path d="M12 8v8"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "peak": '<path d="M2 19h3l3-1 2-9 2 13 2-15 2 11 2-1h4"/>',
 "antibody": '<path d="M12 21v-8M12 13 6 7M12 13l6-6M6 7 3 4M6 7 9 4M18 7l-3-3M18 7l3-3"/>',
 "helix": '<path d="M7 3c0 6 10 6 10 12s-10 6-10 6M17 3c0 6-10 6-10 12M8 7h8M8 17h8"/>',
 "capsid": '<path d="M12 2 21 7v10l-9 5-9-5V7z"/><path d="M12 2v20M3 7l18 10M21 7 3 17"/>',
 "dish": '<ellipse cx="12" cy="13" rx="9" ry="5"/><circle cx="9" cy="13" r="1.2"/><circle cx="14" cy="12" r="1.6"/><circle cx="13" cy="15" r=".9"/>',
 "air": '<path d="M3 8h12a3 3 0 1 0-3-3M3 12h16a3 3 0 1 1-3 3M3 16h8"/>',
 "vial": '<path d="M9 2h6M10 2v5l-4 11a3 3 0 0 0 3 4h6a3 3 0 0 0 3-4L14 7V2"/><path d="M7.5 14h9"/>',
 "plasma": '<path d="M12 3s6 7 6 11a6 6 0 0 1-12 0c0-4 6-11 6-11z"/><path d="M9 15a3 3 0 0 0 3 3"/>',
 "crystal": '<path d="m12 2 7 6-3 13H8L5 8z"/><path d="M5 8h14M12 2 9 8l3 13 3-13z"/>',
 "shield": '<path d="M12 2 4 5v6c0 5 3.5 9 8 11 4.5-2 8-6 8-11V5z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
 "lock": '<rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
 "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
 "check": '<path d="m5 12 5 5 9-10"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "moon": '<path d="M20 14A8 8 0 1 1 10 4a7 7 0 0 0 10 10z"/>',
 "truck": '<path d="M2 6h11v10H2zM13 10h5l3 3v3h-8z"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
 "doc": '<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h6"/>',
 "people": '<circle cx="9" cy="8" r="3.5"/><path d="M2 21c0-4 3-6.5 7-6.5s7 2.5 7 6.5"/><circle cx="17.5" cy="9" r="2.5"/><path d="M17 14c3 0 5 2 5 5"/>',
 "spark": '<path d="M12 2v6M12 16v6M2 12h6M16 12h6M5 5l4 4M15 15l4 4M19 5l-4 4M9 15l-4 4"/>',
 "phone": '<path d="M5 3h4l2 5-3 2a12 12 0 0 0 6 6l2-3 5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2"/>',
 "pin": '<path d="M12 22s7-7 7-12a7 7 0 0 0-14 0c0 5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
 "flask": '<path d="M9 2h6M10 2v6L4 19a2 2 0 0 0 2 3h12a2 2 0 0 0 2-3l-6-11V2"/><path d="M7 15h10"/>',
 "gauge": '<path d="M4 18a8 8 0 1 1 16 0"/><path d="m12 18 4-6"/>',
 "leaf": '<path d="M5 19C5 9 11 4 20 4c0 9-5 15-15 15z"/><path d="M5 19 14 10"/>',
 "api": '<path d="m8 8-5 4 5 4M16 8l5 4-5 4M14 4l-4 16"/>',
}
def ICON(k, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{_IC.get(k, _IC["spark"])}</svg>'

PEAK = ('<svg class="peak" viewBox="0 0 40 24" aria-hidden="true"><path pathLength="1" d="M1 21h7c2 0 2.5-1 3.5-4l2.5-9c1-3.5 2.5-3.5 3.5 0l2.6 10c.8 3 1.6 3 3 3h3.2c1.2 0 1.6-1.2 2.2-3l.8-2.2c.5-1.4 1.4-1.4 1.9 0l.8 2.2c.6 1.8 1 3 2.2 3H39"/></svg>')

def SIG(cls=""):
    """Signature chromatogram line: draws itself when scrolled into view (divider, loader, progress)."""
    return (f'<div class="sig reveal {cls}" aria-hidden="true"><svg viewBox="0 0 1200 60" preserveAspectRatio="none"><path pathLength="1" d="M0 52H180c30 0 34-2 42-12l10-26c4-10 10-10 14 0l10 26c6 12 10 12 30 12H420c16 0 18-4 22-10l6-14c3-6 7-6 10 0l6 14c4 8 6 10 22 10H700c24 0 28-4 34-14l14-34c4-8 9-8 13 0l14 34c6 12 10 14 34 14H980c12 0 14-2 17-6l4-7c2-3 5-3 7 0l4 7c3 4 5 6 17 6H1200"/></svg></div>')

# ---------- navigation ----------
RES = [("Insights", "/insights/index.html", "Weekly articles by our scientists"), ("Method Library", "/method-library/index.html", "A public catalogue of test methods"),
       ("Regulatory Radar", "/regulatory-radar.html", "What FDA, EMA and CDSCO changes mean for testing"), ("Case studies", "/case-studies.html", "Problem, approach, result"),
       ("Webinars and events", "/webinars.html", "Live and on demand"), ("Whitepapers", "/whitepapers.html", "Deep guides you can keep"),
       ("Glossary", "/glossary.html", "Pharma testing terms in plain words"), ("Tools and calculators", "/tools/index.html", "Plan, estimate and check")]
COMPANY = [("About us", "/about/index.html", "Science you can sign your name to"), ("Leadership", "/about/leadership.html", "Who runs the network"),
           ("Our story", "/about/our-story.html", "Why we exist"), ("Sustainability", "/sustainability.html", "Greener analytical chemistry"),
           ("News", "/news.html", "Announcements and milestones"), ("Careers", "/careers/index.html", "Do the science medicines depend on"),
           ("Partner with us", "/partner-with-us.html", "For owners of GMP labs"), ("Investors", "/investors.html", "Thesis and data room access"),
           ("Contact", "/contact.html", "Every route to a human")]
QUAL = [("Quality overview", "/quality/index.html", "Inspection-ready, every day"), ("Accreditations", "/quality/accreditations.html", "Every certificate, scope and expiry"),
        ("Data integrity (ALCOA+)", "/quality/data-integrity.html", "How the LIMS enforces each principle"), ("Inspection history", "/quality/inspection-history.html", "Regulatory inspections in plain words"),
        ("Ethics and compliance", "/quality/ethics-and-compliance.html", "Code of conduct and speak-up line")]
TECH = [("Technology", "/technology/index.html", "One LIMS, one data standard"), ("Client portal", "/portal/index.html", "Watch your samples move"),
        ("API and integrations", "/technology/api-and-integrations.html", "REST API and webhooks"), ("Portal login", "/portal/login.html", "For existing clients")]

def _dd(label, href, items, key, cur, cols=1, extra=""):
    on = " on" if cur == key else ""
    li = "".join(f'<a href="{u}"><b>{t}</b><span>{d}</span></a>' for t, u, d in items)
    return (f'<div class="dd"><a href="{href}" class="ddt{on}" aria-haspopup="true">{label}</a>'
            f'<div class="ddm c{cols}"><div class="ddl">{li}</div>{extra}</div></div>')

def _mega(cur):
    sv = "".join(f'<a href="{svc_url(s)}" data-mm="{i}">{ICON(ic)}<b>{n}</b><span>{d}</span></a>' for i, (s, n, d, h, im, ic, tat, *_ ) in enumerate(SERVICES))
    st = "".join(f'<a href="/solutions/{k}.html"><b>{n}</b></a>' for k, n, _ in STAGES)
    ind = "".join(f'<a href="/industries/{k}.html"><b>{n}</b></a>' for k, n, _, _ in INDUSTRIES)
    data = json.dumps([dict(n=s[1], h=s[3], img=s[4], tat=s[6], t=s[7][0], u=svc_url(s[0])) for s in SERVICES])
    feat = (f'<div class="mm-f" data-mmdata="{html.escape(data)}"><img src="/img/biz-highfive.jpg" alt="" loading="lazy"><div><small class="mm-k">Featured case study</small>'
            f'<b class="mm-h">Biosimilar comparability, 14 weeks to 6</b><span class="mm-t">An illustrative example of a program run across two labs on one LIMS.</span>'
            f'<a class="btn sm" href="/case-studies.html">Read the story</a></div></div>')
    on = " on" if cur == "services" else ""
    return (f'<div class="dd mega"><a href="/services/index.html" class="ddt{on}" aria-haspopup="true">Services</a><div class="ddm mm">'
            f'<div class="mm-c mm-s"><p class="mm-hd">By service</p>{sv}<a class="all" href="/services/index.html">All services and bundles &rsaquo;</a></div>'
            f'<div class="mm-c"><p class="mm-hd">By stage</p>{st}<p class="mm-hd">By industry</p>{ind}</div>{feat}</div></div>')

def _labsdd(cur):
    pins = "".join(f'<a class="mp" href="/labs/{s}.html" style="left:{xy(la, lo)[0] / MAP_W * 100:.1f}%;top:{xy(la, lo)[1] / MAP_H * 100:.1f}%" data-c="{c}" data-f="{html.escape(f)}" data-p="{ph}"><i></i></a>'
                   for s, c, co, r, la, lo, ph, f, im, sp in LABS)
    on = " on" if cur == "labs" else ""
    return (f'<div class="dd"><a href="/labs/index.html" class="ddt{on}" aria-haspopup="true">Labs</a><div class="ddm lab-dd">'
            f'<div class="mini"><svg viewBox="0 0 {MAP_W} {MAP_H}" aria-hidden="true"><path d="{LAND_MINI}"/></svg>{pins}</div>'
            f'<div class="mini-i"><b class="mi-c">Hover a city</b><span class="mi-f">Ten planned sites across India, Southeast Asia, Europe and the US.</span><small class="mi-p"></small>'
            f'<a href="/labs/index.html">All labs and the map &rsaquo;</a><a href="/labs/capabilities-matrix.html">Capabilities matrix &rsaquo;</a></div></div></div>')

def header(path, cur):
    ind = [(n, f"/industries/{k}.html", d) for k, n, d, _ in INDUSTRIES]
    return (f'<a class="skip" href="#main">Skip to content</a>'
            f'<div class="pv"><div class="w"><span><b>Preview</b> PharmaCRO is assembling its lab network. Figures, accreditations, people and client stories shown are illustrative placeholders until verified.</span>'
            f'<a href="/terms.html#preview">How we label claims</a></div></div>'
            f'<nav class="top" aria-label="Main"><div class="w">'
            f'<a class="logo" href="/index.html" aria-label="{BRAND} home">{PEAK}<b>Pharma<em>CRO</em></b></a>'
            f'<div class="links">{_mega(cur)}{_dd("Industries", "/industries/index.html", ind, "industries", cur)}{_labsdd(cur)}'
            f'{_dd("Quality", "/quality/index.html", QUAL, "quality", cur)}{_dd("Technology", "/technology/index.html", TECH, "technology", cur)}'
            f'{_dd("Resources", "/insights/index.html", RES, "resources", cur, 2)}{_dd("Company", "/about/index.html", COMPANY, "company", cur, 2)}</div>'
            f'<div class="nr"><a class="stat" href="/status.html" title="Network status (demo data)"><i></i><span>Demo status &middot; avg TAT 4.2 d</span></a>'
            f'<button class="srch" type="button" aria-label="Search (press /)">{ICON("search")}<kbd>/</kbd></button>'
            f'<label class="reg"><span class="vh">Region</span><select data-region aria-label="Region"><option value="global">Global</option><option value="in">India &middot; CDSCO</option><option value="eu">Europe &middot; EMA</option><option value="us">US &middot; FDA</option><option value="apac">APAC &middot; PMDA, HSA</option></select></label>'
            f'<button class="thm" type="button" aria-label="Switch dark mode">{ICON("moon", "ic m")}{ICON("sun", "ic s")}</button>'
            f'<a class="ghost" href="/portal/index.html">{ICON("lock")}<span>Client portal</span></a>'
            f'<a class="cta" href="/request-quote.html">Request a quote</a>'
            f'<button class="burger" type="button" aria-expanded="false" aria-controls="mnav" aria-label="Menu"><i></i><i></i></button></div></div><div id="prog"></div>'
            f'<div class="mnav" id="mnav" hidden>{_mnav()}</div></nav>')

def _mnav():
    grp = [("Services", [(s[1], svc_url(s[0])) for s in SERVICES] + [("All services and bundles", "/services/index.html")]),
           ("Industries", [(n, f"/industries/{k}.html") for k, n, _, _ in INDUSTRIES]), ("Labs", [(l[1], f"/labs/{l[0]}.html") for l in LABS] + [("Map and all labs", "/labs/index.html")]),
           ("Quality", [(t, u) for t, u, _ in QUAL]), ("Technology", [(t, u) for t, u, _ in TECH]), ("Resources", [(t, u) for t, u, _ in RES]), ("Company", [(t, u) for t, u, _ in COMPANY])]
    g = "".join(f'<details><summary>{h}</summary>' + "".join(f'<a href="{u}">{t}</a>' for t, u in L) + '</details>' for h, L in grp)
    return g + '<p class="mn-b"><a class="btn" href="/request-quote.html">Request a quote</a> <a class="btn o" href="/portal/index.html">Client portal</a></p>'

def footer():
    tests = "".join(f"<option>{s[1]}</option>" for s in SERVICES)
    cols = [("Services", [(s[1], svc_url(s[0])) for s in SERVICES[:8]] + [("All services", "/services/index.html")]),
            ("Industries and labs", [(n, f"/industries/{k}.html") for k, n, _, _ in INDUSTRIES[:5]] + [("Lab map", "/labs/index.html"), ("Capabilities matrix", "/labs/capabilities-matrix.html")]),
            ("Resources", [(t, u) for t, u, _ in RES]),
            ("Company", [(t, u) for t, u, _ in COMPANY])]
    c = "".join(f'<div><h4>{h}</h4>' + "".join(f'<a href="{u}">{t}</a>' for t, u in L) + "</div>" for h, L in cols)
    badges = "".join(f'<span class="bdg" title="{t} (target scope, not yet held)">{ICON("shield")}{b}</span>' for b, t in
                     [("ISO/IEC 17025", "Testing laboratory accreditation"), ("GMP", "Good Manufacturing Practice"), ("ISO 9001", "Quality management"), ("Part 11", "21 CFR Part 11 aligned portal"), ("GLP", "Good Laboratory Practice"), ("ISO 27001", "Information security (roadmap)")])
    qcol = f'<div class="fq"><h4>Quality</h4>{badges}<a href="/quality/accreditations.html">Accreditation wall &rsaquo;</a></div>'
    ph = "".join(f'<a href="tel:{t}"><small>{r}</small>{n}</a>' for r, n, t in PHONES)
    legal = [("Privacy", "/privacy.html"), ("Terms", "/terms.html"), ("Cookies", "/cookies.html"), ("Accessibility", "/accessibility.html"), ("Whistleblowing", "/whistleblowing.html"),
             ("Modern slavery statement", "/modern-slavery-statement.html"), ("Sitemap", "/sitemap.html"), ("Status", "/status.html"), ("Support", "/support.html"), ("Image credits", "/terms.html#credits")]
    return (f'<footer class="pf"><div class="w">'
            f'<div class="fband"><div><p class="ey">Have a batch waiting?</p><h2>Tell us what it is. A scientist replies within 4 business hours.</h2></div>'
            f'<form class="mf fb-form" data-mail="{MAIL}" data-kind="Footer quote" novalidate><label><span>Work email</span><input name="email" type="email" autocomplete="email" required placeholder="you@company.com"></label>'
            f'<label><span>Test type</span><select name="test" required><option value="">Choose a service</option>{tests}<option>Not sure yet</option></select></label>'
            f'<button class="btn" type="submit">Get my quote</button><p class="mf-ok" hidden>Your email app has opened with the details. Press send and we will reply within 4 business hours.</p></form>'
            f'<div class="fph"><p class="ey">Call us now</p>{ph}<small>Placeholder numbers until launch.</small></div></div>'
            f'<div class="cols">{c}{qcol}</div>'
            f'<div class="fnews"><div><h3>The Regulatory Radar</h3><p>One email a week on FDA, EMA and CDSCO changes that affect testing. No spam, unsubscribe in one click.</p></div>'
            f'<form class="mf" data-mail="{MAIL}" data-kind="Regulatory Radar subscription" novalidate><label><span>Email</span><input name="email" type="email" required placeholder="you@company.com"></label><button class="btn o" type="submit">Subscribe</button>'
            f'<p class="mf-ok" hidden>Your email app has opened. Press send to subscribe.</p></form></div>'
            f'<div class="fcomp"><span>Accredited. Audited. Accountable. (Target standards, shown before accreditation is held.)</span><span>Data protection: GDPR, DPDP Act 2023 (India), PDPA (Singapore) aligned policies.</span><span>{ICON("lock")} Security: HTTPS, HSTS, encrypted forms</span></div>'
            f'<div class="flegal">{"".join(f"<a href={chr(34)}{u}{chr(34)}>{t}</a>" for t, u in legal)}</div>'
            f'<p class="fine">PharmaCRO is the working name of a planned pharmaceutical analytical testing network, part of the <a href="https://investorlabs.eliteleadgrow.com/pharma.html">Investor Labs</a> group. '
            f'Until launch, lab locations are planned sites, and figures, accreditations, inspection outcomes, people and case studies are illustrative placeholders. Nothing here is regulatory advice. '
            f'Photos are from Unsplash and Wikimedia Commons and do not show PharmaCRO facilities or staff.</p>'
            f'<p class="fine">&copy; 2026 {BRAND}. <button class="totop" type="button">{SIG()}<span>Back to top</span></button></p></div>'
            f'<div class="wm" aria-hidden="true"><span>PharmaCRO</span></div></footer>')

def floaters():
    tests = "".join(f"<option>{s[1]}</option>" for s in SERVICES)
    return (f'<aside class="qtab" aria-label="Quick quote"><button class="qt-b" type="button" aria-expanded="false">Get a quote in 90 seconds</button>'
            f'<form class="mf qt-f" data-mail="{MAIL}" data-kind="Quick quote" hidden novalidate><b>Quick quote</b><label><span>Name</span><input name="name" autocomplete="name" required></label>'
            f'<label><span>Work email</span><input name="email" type="email" autocomplete="email" required></label><label><span>Test type</span><select name="test" required><option value="">Choose</option>{tests}<option>Not sure yet</option></select></label>'
            f'<button class="btn" type="submit">Send</button><a href="/request-quote.html">Full quote form &rsaquo;</a><p class="mf-ok" hidden>Your email app has opened. Press send and a scientist replies within 4 business hours.</p></form></aside>'
            f'<div class="ask"><button class="ask-b" type="button" aria-expanded="false" aria-controls="askp">{ICON("chat")}<span>Ask the Lab</span></button>'
            f'<div class="ask-p" id="askp" hidden role="dialog" aria-label="Ask the Lab"><div class="ask-h"><b>Ask the Lab</b><small>Demo assistant. Answers only from pages on this site, always cites them, and never gives regulatory advice.</small><button type="button" class="ask-x" aria-label="Close">&times;</button></div>'
            f'<div class="ask-l" aria-live="polite"><p class="am bot">Hello. Ask me whether we can test something, for example <em>nitrosamine testing India</em> or <em>stability zone IVb</em>.</p></div>'
            f'<div class="ask-q"><button type="button">Can you test for nitrosamines?</button><button type="button">Zone IVb stability</button><button type="button">mRNA capping efficiency</button><button type="button">How fast is sterility?</button></div>'
            f'<form class="ask-f"><label class="vh" for="askin">Your question</label><input id="askin" placeholder="Can you test..." autocomplete="off"><button class="btn sm" type="submit">Ask</button></form></div></div>'
            f'<div class="srch-o" hidden role="dialog" aria-label="Search the site"><div class="so-in"><label class="so-l">{ICON("search")}<span class="vh">Search</span><input type="search" placeholder="Try: nitrosamine testing India, stability zone IVb, endotoxin limit" autocomplete="off"></label>'
            f'<div class="so-r" aria-live="polite"></div><p class="so-h">Press <kbd>/</kbd> anywhere to search. <kbd>Esc</kbd> to close.</p></div></div>'
            f'<div class="ck" hidden role="region" aria-label="Cookie choices"><p>We use only essential cookies and one local setting for your region and theme. Optional analytics stay off unless you say yes.</p>'
            f'<div><button class="btn sm" data-ck="all" type="button">Allow analytics</button> <button class="btn sm o" data-ck="ess" type="button">Essential only</button> <a href="/cookies.html">Details</a></div></div>')

# ---------- interactive components (behaviour in assets/ph.js) ----------
def WORDS(text, tag="h1", cls=""):
    """Masked word-by-word headline reveal (60 ms stagger)."""
    w = " ".join(f'<span class="wm-w"><span style="--i:{i}">{x}</span></span>' for i, x in enumerate(text.split()))
    return f'<{tag} class="words {cls}" aria-label="{html.escape(re.sub("<[^>]+>", "", text))}">{w}</{tag}>'

def EY(t): return f'<p class="ey">{t}</p>'

def SH(eyebrow, title, lede="", center=False):
    return f'<div class="sh2 reveal{" ctr" if center else ""}"><p class="ey">{eyebrow}</p><h2>{title}</h2>' + (f"<p>{lede}</p>" if lede else "") + "</div>"

def TRUST():
    items = [("ISO/IEC 17025", "Testing and calibration laboratories", "Target scope per site. Certificate numbers appear here once issued."),
             ("GMP compliant", "Good Manufacturing Practice", "Sites operated to EU and US GMP expectations. Status per site on the accreditation wall."),
             ("FDA-inspected sites", "US Food and Drug Administration", "Applies only to acquired sites with an FDA inspection record. None claimed yet."),
             ("EMA-recognised", "European Medicines Agency", "Target for EU sites. Not held yet."),
             ("CDSCO-licensed", "Central Drugs Standard Control Organisation, India", "Indian sites operate under state and CDSCO approvals where required."),
             ("ISO 9001", "Quality management systems", "Group quality system certification on the roadmap."),
             ("21 CFR Part 11", "Electronic records and signatures", "Portal designed to Part 11 principles; validation pending.")]
    row = "".join(f'<span class="tb" tabindex="0">{ICON("shield")}<b>{a}</b><em role="tooltip"><b>{b}</b>{c}</em></span>' for a, b, c in items)
    return (f'<div class="trust reveal"><div class="tr-m"><div>{row}{row.replace("tabindex=" + chr(34) + "0" + chr(34), "tabindex=" + chr(34) + "-1" + chr(34) + " aria-hidden=" + chr(34) + "true" + chr(34))}</div></div>'
            f'<p class="tr-n">Trusted by [X] of the top 50 pharma manufacturers {ILL("placeholder: replace with a verified claim")}</p></div>')

def SCICARD(key, compact=False):
    n, role, spec, im, city = SCI[key]
    first = n.replace("Dr ", "").split()[0]
    return (f'<div class="sci reveal{" cp" if compact else ""}"><img src="/img/{im}.jpg" alt="" loading="lazy"><div><b>{n}</b><span>{role}</span><small>{spec} &middot; {city}</small>'
            f'<a class="btn sm o" href="mailto:{MAIL}?subject={html.escape("Question for " + n)}">Ask {first}</a>{ILL("Illustrative profile")}</div></div>')

def CHIP(metric, title, text):
    """Case-study chip: a metric badge that expands into a short story."""
    return (f'<details class="chip reveal"><summary><b>{metric}</b><span>{title}</span></summary><div>{text}<p class="cn">{ILL("Illustrative case")} Real, approved case studies replace these at launch.</p>'
            f'<a href="/case-studies.html">More case studies &rsaquo;</a></div></details>')

def FAQS(items, id="faq"):
    """Answer-first accordion: one open at a time, deep-linkable (#faq-3), FAQPage JSON-LD."""
    d = "".join(f'<details class="acc reveal" id="{id}-{i + 1}"><summary>{q}<a class="dl" href="#{id}-{i + 1}" aria-label="Link to this question">#</a></summary><div>{a}</div></details>' for i, (q, a) in enumerate(items))
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": re.sub("<[^>]+>", "", q),
          "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in items]}
    return f'<div class="accs one" id="{id}">{d}</div><script type="application/ld+json">{json.dumps(ld)}</script>'

def CTA(h="Your next batch could clear in 48 hours.", t="Tell us the product, the tests and the date you need. A scientist replies within 4 business hours, and a typical quote takes one day.", img="lab-corridor"):
    tests = "".join(f"<option>{s[1]}</option>" for s in SERVICES)
    return (f'<section class="qband reveal" style="--bg:url(/img/{img}.jpg)"><canvas class="mol" aria-hidden="true"></canvas><div class="qb-in"><p class="ey">Get a quote</p><h2>{h}</h2><p>{t}</p>'
            f'<form class="mf qb-f" data-mail="{MAIL}" data-kind="Quote request" novalidate><label><span>Work email</span><input name="email" type="email" autocomplete="email" required></label>'
            f'<label><span>Test type</span><select name="test" required><option value="">Choose</option>{tests}<option>Not sure yet</option></select></label>'
            f'<label><span>Urgency</span><select name="urgency"><option>Standard</option><option>Priority</option><option>Critical (24 to 72 h)</option></select></label>'
            f'<button class="btn mag big" type="submit"><span>Get my quote</span><svg class="tick" viewBox="0 0 24 24" aria-hidden="true"><path pathLength="1" d="m5 12 5 5 9-10"/></svg></button>'
            f'<p class="mf-ok" hidden>Got it. Your email app has opened with the details; press send and a scientist will reply within 4 business hours.</p></form>'
            f'<p class="qb-s">Reply within 4 business hours. Typical quote in 1 day. <a href="/book-a-call.html">Or talk to a scientist &rsaquo;</a></p></div></section>')

def CRUMBS(crumbs, title):
    items = [("Home", "/index.html")] + list(crumbs or [])
    h = "".join(f'<a href="{u}">{t}</a><i>/</i>' for t, u in items) + f'<span aria-current="page">{re.sub("<[^>]+>", "", title)}</span>'
    return f'<nav class="crumbs" aria-label="Breadcrumb">{h}</nav>'

def VIAL(steps):
    """Sticky 'how it works': a vial travels along a drawn path and changes state. steps: (title, text, img, state)."""
    st = "".join(f'<div class="vj-s" data-i="{i}" data-st="{s}"><p class="ey">Step {i + 1}</p><h3>{t}</h3><p>{d}</p></div>' for i, (t, d, im, s) in enumerate(steps))
    ims = "".join(f'<img class="vj-im{" on" if i == 0 else ""}" src="/img/{im}.jpg" alt="{alt(im)}" loading="lazy">' for i, (t, d, im, s) in enumerate(steps))
    n = len(steps)
    marks = "".join(f'<circle cx="{40 + i * (520 / (n - 1)):.0f}" cy="{60 + (i % 2) * 40}" r="7" class="vj-m"/>' for i in range(n))
    pts = " ".join(f'{40 + i * (520 / (n - 1)):.0f},{60 + (i % 2) * 40}' for i in range(n))
    return (f'<div class="vj"><div class="vj-v"><div class="vj-ph">{ims}</div><svg class="vj-p" viewBox="0 0 600 160" aria-hidden="true"><polyline class="vj-tr" points="{pts}"/><polyline class="vj-fl" pathLength="1" points="{pts}"/>{marks}'
            f'<g class="vj-vial"><rect x="-9" y="-22" width="18" height="34" rx="5"/><rect class="cap" x="-11" y="-30" width="22" height="9" rx="2"/><rect class="liq" x="-7" y="-6" width="14" height="16" rx="3"/></g></svg>'
            f'<p class="vj-state">Sealed</p></div><div class="vj-st">{st}</div></div>')

def NUMBERS(items, asof=ASOF):
    """Metrics with count-up, a sparkline that draws in, and a hover definition. items: (value, label, definition, spark[list])."""
    out = []
    for i, (v, l, d, sp) in enumerate(items):
        m = re.match(r"^([^\d]*)(\d[\d,]*\.?\d*)(.*)$", v)
        if m:
            pre, num, suf = m.groups(); dec = len(num.split(".")[1]) if "." in num else 0
            b = f'<b class="cnt" data-to="{num.replace(",", "")}" data-dec="{dec}" data-pre="{html.escape(pre)}" data-suf="{html.escape(suf)}" data-comma="{1 if "," in num else 0}">{v}</b>'
        else: b = f"<b>{v}</b>"
        mx, mn = max(sp), min(sp)
        pts = " ".join(f"{j * (100 / (len(sp) - 1)):.1f},{28 - (x - mn) / ((mx - mn) or 1) * 24:.1f}" for j, x in enumerate(sp))
        out.append(f'<div class="num reveal" style="--i:{i}" tabindex="0">{b}<span>{l}</span><svg viewBox="0 0 100 30" preserveAspectRatio="none" aria-hidden="true"><polyline pathLength="1" points="{pts}"/></svg><em role="tooltip">{d}</em></div>')
    return f'<div class="nums">{"".join(out)}</div><p class="cn nums-n">Updated {asof}. {ILL("All figures are placeholders")} <a href="/quality/index.html#measure">How we measure</a>.</p>'

def SPLITPANELS(a, b):
    """Two large panels that split with a diagonal wipe on hover. a/b: (img, eyebrow, title, text, link, linktext, tone)."""
    def pn(x, k):
        im, e, t, d, l, lt, tone = x
        return f'<a class="spn {k} {tone}" href="{l}" style="--bg:url(/img/{im}.jpg)"><div><p class="ey">{e}</p><h3>{t}</h3><p>{d}</p><span class="btn">{lt}</span></div></a>'
    return f'<div class="spns reveal">{pn(a, "a")}{pn(b, "b")}</div>'

def STEPLINE(steps):
    """Steps joined by a line that draws and lights each step as you scroll. steps: (title, text)."""
    li = "".join(f'<li class="sl-i"><i>{i + 1}</i><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(steps))
    return f'<ol class="sline"><span class="sl-l" aria-hidden="true"><span></span></span>{li}</ol>'

def TICKLIST(items):
    return '<ul class="ticks tick-in">' + "".join(f'<li style="--i:{i}">{x}</li>' for i, x in enumerate(items)) + "</ul>"

def ICARDS(items, n=3):
    """Icon cards whose icon draws itself. items: (icon, title, text)."""
    return f'<div class="icards g{n}">' + "".join(f'<div class="icard reveal tilt" style="--i:{i}">{ICON(ic, "ic draw")}<h3>{t}</h3><p>{d}</p></div>' for i, (ic, t, d) in enumerate(items)) + "</div>"

def TESTS(rows, id="tests"):
    """Searchable/filterable test table; rows expand. rows: (method, standard, tat, sample, accreditation, summary, instruments, method_link or "")."""
    std = sorted({s.strip() for r in rows for s in re.split(r",|/", r[1]) if s.strip()})
    opts = "".join(f"<option>{s}</option>" for s in std)
    body = "".join(f'<details class="tt-r" data-s="{html.escape(r[1])}"><summary><span class="tt-m">{r[0]}</span><span>{r[1]}</span><span>{r[2]}</span><span>{r[3]}</span><span class="tt-a">{r[4]}</span></summary>'
                   f'<div><p>{r[5]}</p><p><b>Instruments:</b> {r[6]}</p>' + (f'<a href="{r[7]}">Full Method Library entry &rsaquo;</a>' if r[7] else "") + '</div></details>' for r in rows)
    return (f'<div class="tt" id="{id}"><div class="tt-f"><label><span class="vh">Search tests</span><input type="search" placeholder="Search {len(rows)} tests" data-tt="q"></label>'
            f'<label><span class="vh">Standard</span><select data-tt="s"><option value="">All standards</option>{opts}</select></label><span class="tt-c" aria-live="polite"></span></div>'
            f'<div class="tt-h"><span>Test and method</span><span>Standard</span><span>Typical TAT</span><span>Sample</span><span>Accreditation</span></div>{body}'
            f'<p class="nores" hidden>No test matches. <a href="/request-quote.html">Ask us anyway</a>: we run many non-listed methods.</p>'
            f'<p class="cn">Accreditation shows the target scope per method. {ILL("Placeholder")} Final scope is confirmed per site on the <a href="/quality/accreditations.html">accreditation wall</a>.</p></div>')

REGS = [("FDA", "us"), ("EMA", "eu"), ("CDSCO", "in"), ("PMDA", "apac"), ("WHO PQ", "global"), ("USP", "us"), ("Ph. Eur.", "eu"), ("JP", "apac"), ("IP", "in"), ("HSA", "apac"), ("MHRA", "eu"), ("ICH", "global")]
def REGBADGES(keys=None):
    r = [x for x in REGS if not keys or x[0] in keys]
    return ('<div class="regs reveal">' + "".join(f'<span class="rg" data-reg="{k}">{n}</span>' for n, k in r) +
            '<p class="cn">Badges for your region light up. Change region in the header.</p></div>')

def TIERS(days=(10, 5, 2)):
    """Turnaround tiers with a segmented control that shows the result date relative to today."""
    t = [("Standard", days[0], "1.0×", "Most release and stability work."), ("Priority", days[1], "1.5×", "Launch windows and investigations."), ("Critical", days[2], "2.0 to 2.5×", "Line stoppages and batch on hold: 24 to 72 hours.")]
    seg = "".join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" data-d="{d}" data-m="{m}" data-x="{html.escape(x)}">{n}</button>' for i, (n, d, m, x) in enumerate(t))
    return (f'<div class="tiers reveal"><div class="seg" role="tablist" aria-label="Turnaround tier">{seg}</div><div class="ti-o"><span class="k">Ship today, results by</span><b class="ti-d">&nbsp;</b>'
            f'<span class="ti-x"></span><span class="ti-m"></span></div><p class="cn">Indicative business days after sample receipt and acceptance. Price multipliers are guidance, confirmed in your quote. '
            f'If we miss the date, the fee for that test is credited {ILL("subject to commercial approval")}.</p></div>')

def CHECKRING(items, label="Sample checklist"):
    li = "".join(f'<li><label><input type="checkbox" data-cr> <span>{x}</span></label></li>' for x in items)
    return (f'<div class="cring reveal"><div class="cr-r"><svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="50" class="tr"/><circle cx="60" cy="60" r="50" class="cr-f" pathLength="100"/></svg><b>0%</b></div>'
            f'<div><h3>{label}</h3><ol class="cr-l">{li}</ol><a class="btn cr-u" aria-disabled="true" href="/submit-samples.html">Request a pre-filled shipping label</a>'
            f'<a class="cr-dl" href="/submit-samples.html#sheet">Download the sample submission sheet</a></div></div>')

def GANTT(rows, weeks=12, title="Indicative timeline"):
    """rows: (label, start_week, length_weeks). Bars draw left to right."""
    b = "".join(f'<div class="gt-r" style="--s:{s / weeks * 100:.2f}%;--w:{l / weeks * 100:.2f}%;--i:{i}"><span>{n}</span><i><u></u></i></div>' for i, (n, s, l) in enumerate(rows))
    ax = "".join(f"<span>{w}</span>" for w in range(0, weeks + 1, max(1, weeks // 6)))
    return f'<div class="gantt chart reveal"><h4>{title}</h4>{b}<div class="gt-ax">{ax}</div><p class="cn">Weeks from sample receipt. Illustrative; your plan is confirmed in the quote.</p></div>'

def MAP(id="labmap", big=False):
    """Interactive network map: pins pulse, hover card, filters, method-transfer arcs, nearest-lab finder."""
    grat = "".join(f'<path class="grat" d="M{(lon + 180) * S_:.0f},0V{MAP_H}"/>' for lon in range(-150, 181, 30)) + "".join(f'<path class="grat" d="M0,{(LAT0_ - lat) * S_:.0f}H1000"/>' for lat in range(60, -60, -30))
    data = json.dumps([dict(s=s, c=c, co=co, r=r, x=xy(la, lo)[0], y=xy(la, lo)[1], la=la, lo=lo, ph=ph, f=f, sp=[SVC[k][1] for k in sp], spk=sp) for s, c, co, r, la, lo, ph, f, im, sp in LABS])
    regs = "".join(f'<button type="button" class="ch" data-mr="{r}" aria-pressed="false">{r}</button>' for r in ["India", "Southeast Asia", "Europe", "United States"])
    svcs = "".join(f'<option value="{s[0]}">{s[1]}</option>' for s in SERVICES)
    return (f'<div class="lmap{" big" if big else ""}" id="{id}" data-labs="{html.escape(data)}"><div class="lm-ctl"><div class="lm-regs" role="group" aria-label="Filter by region">{regs}</div>'
            f'<label><span class="vh">Filter by service</span><select data-ms><option value="">All services</option>{svcs}</select></label>'
            f'<button type="button" class="ch" data-arcs aria-pressed="false">Show method transfer routes</button>'
            f'<form class="lm-near"><label><span class="vh">Your city</span><input placeholder="Find my nearest lab: type a city" list="{id}-cities"></label><button class="btn sm" type="submit">Find</button></form>'
            f'<datalist id="{id}-cities">{"".join(f"<option>{c}</option>" for c in CITIES)}</datalist></div>'
            f'<div class="lm-st"><svg class="lm-svg" viewBox="0 0 {MAP_W} {MAP_H}" role="img" aria-label="Map of planned PharmaCRO labs">{grat}<path class="land" d="{LAND}"/><g class="arcs"></g><g class="pins"></g></svg>'
            f'<div class="lm-card" aria-live="polite"><p class="ey">Planned network</p><h3>Ten labs. One standard.</h3><p>Hover or tap a pin for the city, focus, planned opening and services.</p></div></div>'
            f'<p class="cn">Locations are planned sites from the company plan; queue depth and next slot are simulated for the demo. {ILL("Planned network")}</p></div>'
            f'<script>window.PC_CITIES={json.dumps(CITIES, ensure_ascii=False)}</script>')

CITIES = {"Ahmedabad": (23.02, 72.57), "Baddi": (30.96, 76.79), "Chennai": (13.08, 80.27), "Delhi": (28.61, 77.21), "Goa": (15.3, 74.12), "Hyderabad": (17.39, 78.49),
          "Visakhapatnam": (17.69, 83.22), "Vadodara": (22.31, 73.18), "Kolkata": (22.57, 88.36), "Mumbai": (19.08, 72.88), "Bengaluru": (12.97, 77.59), "Pune": (18.52, 73.86),
          "Singapore": (1.35, 103.82), "Kuala Lumpur": (3.14, 101.69), "Jakarta": (-6.2, 106.85), "Bangkok": (13.75, 100.5), "Ho Chi Minh City": (10.82, 106.63), "Manila": (14.6, 120.98),
          "Shanghai": (31.23, 121.47), "Seoul": (37.57, 126.98), "Tokyo": (35.68, 139.69), "Sydney": (-33.87, 151.21), "Dubai": (25.2, 55.27),
          "London": (51.51, -0.13), "Dublin": (53.35, -6.26), "Cork": (51.9, -8.47), "Amsterdam": (52.37, 4.9), "Basel": (47.56, 7.59), "Copenhagen": (55.68, 12.57), "Frankfurt": (50.11, 8.68),
          "Paris": (48.86, 2.35), "Barcelona": (41.39, 2.17), "Milan": (45.46, 9.19), "Boston": (42.36, -71.06), "New York": (40.71, -74.01), "Philadelphia": (39.95, -75.17),
          "Raleigh": (35.78, -78.64), "San Diego": (32.72, -117.16), "San Francisco": (37.77, -122.42), "Toronto": (43.65, -79.38), "Puerto Rico": (18.22, -66.59), "São Paulo": (-23.55, -46.63)}

def PORTAL():
    """Scroll-scrubbed mock dashboard: statuses advance Received > In analysis > Under review > Released; toasts slide in; cursor tilts the device."""
    rows = [("PC-24-0918", "Metformin 500 mg tablets, B2291", "Assay, dissolution, RS"), ("PC-24-0919", "Adalimumab DS, Lot 77A", "SEC, CE-SDS, icIEF"),
            ("PC-24-0920", "mRNA-LNP, ENG-04", "Integrity, capping, EE%"), ("PC-24-0921", "WFI loop, Room 2B", "TOC, conductivity, endotoxin"),
            ("PC-24-0922", "Amoxicillin API, 24-118", "Nitrosamines (LC-MS/MS)")]
    r = "".join(f'<div class="pm-r" data-i="{i}"><span class="pm-id">{a}</span><span class="pm-n">{b}<small>{c}</small></span><span class="pm-s" data-st="0">Received</span><span class="pm-b"><i></i></span></div>' for i, (a, b, c) in enumerate(rows))
    return (f'<div class="pmock"><div class="pm-dev tiltd"><div class="pm-top"><span>{PEAK}<b>PharmaCRO Portal</b></span><span class="pm-u">QC Team &middot; Demo data</span></div>'
            f'<div class="pm-k"><div><small>In progress</small><b class="pm-k1">5</b></div><div><small>Released this week</small><b class="pm-k2">0</b></div><div><small>Avg TAT</small><b>4.2 d</b></div><div><small>OOS open</small><b>0</b></div></div>'
            f'<div class="pm-h"><span>Sample</span><span>Product and tests</span><span>Status</span><span>Progress</span></div>{r}'
            f'<div class="pm-toasts" aria-live="polite"></div></div><div class="pm-rail" aria-hidden="true"></div></div>')

def ALCOA():
    L = [("A", "Attributable", "Every action carries a unique user ID and an e-signature. Shared log-ins are blocked at the LIMS and on instruments.", "Analyst R.M. injected sequence SEQ-4471 at 09:42:11 IST."),
         ("L", "Legible", "Records are electronic, human-readable and retained in their original format, with no overwrite.", "Chromatograms stored as vendor raw data plus a rendered PDF."),
         ("C", "Contemporaneous", "Time stamps come from a network time server; manual time entry is disabled.", "Weighing at 10:03:27 auto-captured from the balance."),
         ("O", "Original", "The first capture is the record. Printouts are true copies with a hash.", "Raw data file hash recorded on the CoA."),
         ("A", "Accurate", "Calculations run in validated templates; manual transcription is avoided by direct instrument capture.", "Assay result calculated in a locked template v3.2."),
         ("C", "Complete", "All data, including repeats and aborted runs, stays visible to reviewers.", "Aborted injection 7 shown in the reviewer's audit trail."),
         ("C", "Consistent", "The same SOPs, sequence and audit-trail review apply at every lab.", "Audit trail reviewed before every result is approved."),
         ("E", "Enduring", "Records are kept on validated storage for the retention period plus one year.", "Retention: 10 years for release data, per client agreement."),
         ("A", "Available", "Records can be retrieved for an inspector within an hour.", "Retrieval drill: every quarter at every site.")]
    b = "".join(f'<button type="button" class="al-l" aria-pressed="{"true" if i == 0 else "false"}" data-i="{i}"><b>{a}</b><span>{n}</span></button>' for i, (a, n, c, e) in enumerate(L))
    p = "".join(f'<div class="al-p{" on" if i == 0 else ""}" data-i="{i}"><h3>{n}</h3><p><b>How our LIMS enforces it.</b> {c}</p><p class="al-e"><span>Example</span>{e}</p></div>' for i, (a, n, c, e) in enumerate(L))
    return f'<div class="alcoa reveal"><div class="al-s" role="group" aria-label="ALCOA+ principles">{b}</div>{p}<p class="cn">Designed controls {ILL("to be validated per site")}</p></div>'

def AUDIT():
    ev = [("09:42:11", "R. Mehta (Analyst)", "Result created", "Assay 99.2% LC, sequence SEQ-4471"), ("11:05:48", "System", "Audit trail checked", "No manual integrations, no aborted runs hidden"),
          ("13:20:02", "D. Iyer (Reviewer)", "Reviewed", "Peak integration and system suitability verified"), ("15:31:40", "QA, H. Murphy", "Approved", "E-signed. Meaning: approval of results"), ("15:31:41", "System", "Released", "CoA v1 generated, hash 9f3c...e21")]
    li = "".join(f'<li style="--i:{i}"><time>{t}</time><b>{w}</b><span>{a}</span><em>{d}</em></li>' for i, (t, w, a, d) in enumerate(ev))
    return f'<div class="audit reveal"><div class="au-shield">{ICON("shield", "ic big")}</div><ol>{li}</ol><p class="cn">Demo audit trail with sample data.</p></div>'

def RADAR(items, live=True):
    """items: (date, regulator, title, takeaway, tag)."""
    li = "".join(f'<li class="rd-i" style="--i:{i}" data-reg="{g}"><time>{d}</time><span class="rd-g">{g}</span><b>{t}</b><em>{k}</em><small>{tg}</small></li>' for i, (d, g, t, k, tg) in enumerate(items))
    return f'<ul class="radar{" live" if live else ""}">{li}</ul>'

def CASES(items):
    """Horizontal drag carousel; metric counts up when centred; click expands. items: (img, metric_num, metric_suffix, title, industry, service, problem, approach, result, quote)."""
    c = "".join(f'<article class="cs-c" tabindex="0" data-i="{i}"><img src="/img/{im}.jpg" alt="{alt(im)}" loading="lazy"><div><p class="ey">{ind} &middot; {sv}</p>'
                f'<b class="cs-m"><span class="cnt" data-to="{mn}" data-dec="0" data-pre="" data-suf="" data-comma="0">{mn}</span>{ms}</b><h3>{t}</h3>'
                f'<button class="btn sm o cs-x" type="button">Read the story</button></div>'
                f'<template><h2>{t}</h2><p class="ey">{ind} &middot; {sv}</p><h3>Problem</h3><p>{pr}</p><h3>Approach</h3><p>{ap}</p><h3>Result</h3><p>{rs}</p>{QUOTE(q, "Client QC lead (illustrative)")}'
                f'<p class="cn">{ILL("Illustrative case")} Real, approved case studies replace these at launch.</p><p><a class="btn" href="/request-quote.html">Start a similar project</a></p></template></article>'
                for i, (im, mn, ms, t, ind, sv, pr, ap, rs, q) in enumerate(items))
    return f'<div class="cases"><div class="cs-t">{c}</div><div class="cs-n"><button type="button" class="cs-p" aria-label="Previous">&larr;</button><button type="button" class="cs-nx" aria-label="Next">&rarr;</button></div></div><dialog class="cs-d"><button class="cs-cl" type="button" aria-label="Close">&times;</button><div class="cs-b"></div></dialog>'

def FLIPS(cards):
    """cards: (img, title, sub, back_img, back_html)."""
    c = "".join(f'<button class="flip reveal" style="--i:{i}" type="button" aria-pressed="false"><span class="fr"><img src="/img/{im}.jpg" alt="" loading="lazy"><b>{t}</b><em>{s}</em><small>Tap to see the instrument</small></span>'
                f'<span class="bk"><img src="/img/{bi}.jpg" alt="" loading="lazy">{b}</span></button>' for i, (im, t, s, bi, b) in enumerate(cards))
    return f'<div class="flips">{c}</div>'

def BUNDLES(items):
    """Stacked layers that fan out on hover. items: (name, text, [service slugs], weeks, link)."""
    c = "".join(f'<a class="bun reveal" href="{l}" style="--i:{i}"><div class="bu-st">' + "".join(f'<span style="--k:{k}">{SVC[s][1]}</span>' for k, s in enumerate(ss)) +
                f'</div><h3>{n}</h3><p>{t}</p><small>{w}</small></a>' for i, (n, t, ss, w, l) in enumerate(items))
    return f'<div class="buns">{c}</div>'

def MATRIX():
    """Labs x services capability matrix; hover highlights row and column."""
    head = "".join(f'<th scope="col"><a href="{svc_url(s[0])}">{s[1].replace(" and ", " &amp; ")}</a></th>' for s in SERVICES)
    rows = ""
    for l in LABS:
        cells = ""
        for j, s in enumerate(SERVICES):
            lvl = 3 if s[0] in l[9][:1] else 2 if s[0] in l[9] else (1 if (hash(l[0] + s[0]) % 5 == 0 or s[0] == "regulatory-data-integrity-support") else 0)
            lab = ["Not offered", "Via network transfer", "Offered", "Centre of excellence"][lvl]
            cells += f'<td data-c="{j}" title="{l[1]}: {lab}"><i class="lv{lvl}" aria-label="{lab}"></i></td>'
        rows += f'<tr><th scope="row"><a href="/labs/{l[0]}.html">{l[1]}</a><small>{l[6]}</small></th>{cells}</tr>'
    return (f'<div class="mtx reveal"><div class="tw"><table><thead><tr><th>Lab</th>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
            '<p class="lgd2"><span><i class="lv3"></i>Centre of excellence</span><span><i class="lv2"></i>Offered</span><span><i class="lv1"></i>Via network transfer</span><span><i class="lv0"></i>Not offered</span></p>'
            f'<p class="cn">Planned capability by site {ILL("Planned network")}. <button class="btn sm o" type="button" onclick="window.print()">Download as PDF</button></p></div>')

def RFQ():
    """The money flow: 4-step quote request (what, timing, you, confirm). Opens the visitor's email app with a reference number."""
    mod = "".join(f'<label class="pick"><input type="radio" name="modality" value="{n}"{" checked" if i == 0 else ""}><span>{n}</span></label>' for i, (k, n, im) in enumerate(MODALITIES))
    tests = "".join(f'<label class="pick sm"><input type="checkbox" name="tests" value="{s[1]}"><span>{ICON(s[5])}{s[1]}</span></label>' for s in SERVICES)
    countries = "".join(f"<option>{c}</option>" for c in ["India", "Singapore", "Malaysia", "Indonesia", "Thailand", "Vietnam", "Japan", "South Korea", "China", "Australia", "United Arab Emirates", "United Kingdom", "Ireland", "Netherlands", "Germany", "Switzerland", "France", "Spain", "Italy", "Denmark", "Belgium", "United States", "Canada", "Brazil", "Other"])
    return (f'<form class="rfq" data-mail="{MAIL}" novalidate><ol class="rq-p" aria-label="Progress"><li class="on">What</li><li>Timing</li><li>You</li><li>Confirm</li></ol>'
            f'<fieldset class="rq-s on" data-s="0"><legend>What do you need tested?</legend><p class="rq-h">Product type</p><div class="picks">{mod}</div>'
            f'<p class="rq-h">Services (choose any)</p><div class="picks">{tests}</div>'
            f'<label><span>Specific tests, methods or specification (optional)</span><textarea name="detail" rows="3" placeholder="e.g. USP assay, dissolution apparatus 2 at 50 rpm, NDSRI screen per FDA AI limits"></textarea></label>'
            f'<label class="up"><span>Attach a test list, spec or protocol (PDF, XLSX, DOCX)</span><input type="file" name="file" accept=".pdf,.xlsx,.xls,.docx,.doc"><small>Your email app cannot attach files automatically; we will remind you to attach it before sending.</small></label>'
            f'<p class="rq-sug" aria-live="polite"></p></fieldset>'
            f'<fieldset class="rq-s" data-s="1"><legend>When do you need results?</legend>{TIERS()}<label><span>Target date (optional)</span><input type="date" name="date"></label>'
            f'<label><span>Number of samples or batches</span><input type="number" name="n" min="1" value="1"></label></fieldset>'
            f'<fieldset class="rq-s" data-s="2"><legend>About you</legend><div class="rq-g"><label><span>Name</span><input name="name" autocomplete="name" required></label>'
            f'<label><span>Work email</span><input name="email" type="email" autocomplete="email" required></label><label><span>Company</span><input name="company" autocomplete="organization"></label>'
            f'<label><span>Role</span><select name="role"><option>QC / analytical</option><option>QA</option><option>Procurement</option><option>Regulatory affairs</option><option>R&amp;D / CMC</option><option>Founder / executive</option><option>Other</option></select></label>'
            f'<label><span>Phone (optional)</span><input name="phone" type="tel" autocomplete="tel"></label><label><span>Country</span><select name="country">{countries}</select></label></div>'
            f'<label class="chk"><input type="checkbox" name="existing"> <span>I am an existing client (we will link this to your portal account)</span></label></fieldset>'
            f'<fieldset class="rq-s" data-s="3"><legend>Check and send</legend><div class="rq-sum"></div>'
            f'<label class="chk"><input type="checkbox" name="consent" required> <span>I agree that PharmaCRO may contact me about this request. <a href="/privacy.html">Privacy policy</a>.</span></label>'
            f'<p class="cn">What happens next: a reference number is created now; a scientist replies within 4 business hours with questions or a quote; a typical quote takes one day.</p></fieldset>'
            f'<div class="rq-n"><button type="button" class="btn o rq-b" hidden>Back</button><button type="button" class="btn rq-x">Next</button><button type="submit" class="btn rq-go" hidden>Send my request</button></div>'
            f'<p class="rq-err" role="alert"></p><div class="rq-ok" hidden tabindex="-1"><svg class="tick big" viewBox="0 0 24 24" aria-hidden="true"><path pathLength="1" d="m5 12 5 5 9-10"/></svg>'
            f'<h3>Got it. A scientist will reply within 4 business hours.</h3><p>Your reference is <b class="rq-id"></b>. Your email app has opened with every detail filled in; press send. If you chose a file, attach it before sending.</p>'
            f'<p><a class="btn o" href="/book-a-call.html">Book a call with a scientist</a> <a class="btn o" href="/submit-samples.html">How to ship samples</a></p></div></form>')

def MAILFORM(fields, kind, button="Send", ok="Your email app has opened with the details. Press send and we will reply within one business day.", cls=""):
    """Generic form that opens the visitor's mail app. fields: (name, label, type|[options], required)."""
    f = ""
    for n, l, t, r in fields:
        req = " required" if r else ""
        if isinstance(t, list): f += f'<label><span>{l}</span><select name="{n}"{req}><option value="">Choose</option>{"".join(f"<option>{o}</option>" for o in t)}</select></label>'
        elif t == "textarea": f += f'<label><span>{l}</span><textarea name="{n}" rows="4"{req}></textarea></label>'
        elif t == "checkbox": f += f'<label class="chk"><input type="checkbox" name="{n}"{req}> <span>{l}</span></label>'
        else: f += f'<label><span>{l}</span><input name="{n}" type="{t}"{req}></label>'
    return f'<form class="mf card {cls}" data-mail="{MAIL}" data-kind="{html.escape(kind)}" novalidate>{f}<button class="btn" type="submit">{button}</button><p class="mf-ok" hidden>{ok}</p></form>'

def SVCGRID(only=None, filters=True):
    """Service cards with icon, promise, three tests, TAT and quote link; filter bar re-flows the grid."""
    cards = []
    for i, s in enumerate(SERVICES):
        if only and s[0] not in only: continue
        tests = "".join(f"<li>{t}</li>" for t in s[7])
        cards.append(f'<a class="svc tilt reveal" style="--i:{i % 6}" href="{svc_url(s[0])}" data-mod="{" ".join(s[9])}" data-stg="{" ".join(s[10])}" data-q="{html.escape((s[1] + " " + s[2] + " " + " ".join(s[7])).lower())}">'
                     f'<img src="/img/{s[4]}.jpg" alt="" loading="lazy"><div>{ICON(s[5])}<h3>{s[1]}</h3><p>{s[3]}</p><ul>{tests}</ul><small>{ICON("clock")} {s[6]}</small><em>Request a quote &rsaquo;</em></div></a>')
    fb = ""
    if filters:
        fb = ('<div class="sf" role="group" aria-label="Filter services"><span>Modality</span>' + "".join(f'<button type="button" class="ch" data-f="mod" data-v="{k}" aria-pressed="false">{n.split(" or ")[0]}</button>' for k, n, im in MODALITIES[:4]) +
              '<span>Stage</span>' + "".join(f'<button type="button" class="ch" data-f="stg" data-v="{k}" aria-pressed="false">{n}</button>' for k, n in [("discovery", "Discovery"), ("preclinical", "Preclinical"), ("clinical", "Clinical"), ("commercial", "Commercial"), ("post", "Post-approval")]) +
              '<button type="button" class="ch clr" data-f="clear">Clear</button></div>')
    return f'{fb}<div class="svcs">{"".join(cards)}</div><p class="nores sv-n" hidden>No service matches those filters. <a href="/book-a-call.html">Talk to a scientist</a>.</p>'

def ROUTER():
    """Home 'Who are you?' tiles that morph into a tailored mini test finder; choice is remembered site-wide."""
    t = "".join(f'<button class="rt" type="button" data-mod="{k}" style="--bg:url(/img/{im}.jpg)"><span><b>{n}</b><em>Show my tests &rsaquo;</em></span></button>' for k, n, im in MODALITIES)
    data = json.dumps({k: [dict(n=s[1], u=svc_url(s[0]), t=s[7][0], tat=s[6]) for s in SERVICES if k in s[9]] for k in ["small", "bio", "mrna", "cgt"]})
    return (f'<div class="router" data-r="{html.escape(data)}"><div class="rts" role="group" aria-label="What are you making?">{t}</div>'
            f'<div class="rt-o" hidden aria-live="polite"><div class="rt-h"><h3></h3><button type="button" class="btn sm o rt-back">Change</button></div><div class="rt-l"></div>'
            f'<p><a class="btn" href="/request-quote.html">Get a quote for these</a> <a class="btn o" href="/tools/test-finder.html">Use the full Test Finder</a></p></div></div>')

def CONSTELLATION():
    """Twelve service nodes on elliptical orbits; hover pulls forward, click opens a drawer."""
    n = len(SERVICES)
    nodes = "".join(f'<button class="cn-n" type="button" style="--a:{i / n * 360:.1f}deg;--r:{1 if i % 2 else .72}" data-i="{i}">{ICON(s[5])}<span>{s[1]}</span></button>' for i, s in enumerate(SERVICES))
    drawers = "".join(f'<template data-i="{i}"><p class="ey">{s[6]}</p><h3>{s[1]}</h3><p>{s[3]} {s[2]}</p><ul>{"".join(f"<li>{t}</li>" for t in s[7])}</ul>'
                      f'<p><a class="btn sm" href="/request-quote.html?service={i}">Request a quote</a> <a class="btn sm o" href="{svc_url(s[0])}">Service details</a></p></template>' for i, s in enumerate(SERVICES))
    return (f'<div class="const reveal"><div class="cn-o"><div class="cn-core">{PEAK}<b>One LIMS<br>One standard</b></div>{nodes}</div>{drawers}'
            f'<aside class="cn-d" hidden><button type="button" class="cn-x" aria-label="Close">&times;</button><div></div></aside></div>')

def CLOCK():
    """A large circular clock that sweeps as you scroll, tier cards, and our TAT vs a typical industry range."""
    return (f'<div class="tclock"><div class="tc-c reveal"><svg viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="88" class="tc-f"/>'
            + "".join(f'<line x1="100" y1="16" x2="100" y2="{24 if k % 3 else 30}" transform="rotate({k * 30} 100 100)" class="tc-t"/>' for k in range(12)) +
            f'<path class="tc-sw" d="M100 100L100 12A88 88 0 0 1 100 12Z"/><line class="tc-h" x1="100" y1="100" x2="100" y2="26"/><circle cx="100" cy="100" r="5"/></svg><b class="tc-l">48 h</b></div>'
            f'<div class="tc-r">{BARS("Typical release testing turnaround, business days", [("PharmaCRO Standard (target)", 7, "5 to 10", "var(--teal)"), ("PharmaCRO Priority (target)", 4, "3 to 5", "var(--teal)"), ("PharmaCRO Critical (target)", 2, "1 to 3", "var(--amb)"), ("Typical industry range", 18, "10 to 25", "#8b97a8")], "Bars show midpoints. Industry range is a general market observation, not a measured benchmark. Targets are illustrative.")}</div></div>')

def TATCALC():
    opts = "".join(f'<option value="{i}">{s[1]}</option>' for i, s in enumerate(SERVICES))
    return (f'<div class="tcalc reveal"><h3>Estimate my TAT</h3><div class="tq-in"><label><span>Ship date</span><input type="date" data-tq="d"></label><label><span>Service</span><select data-tq="s">{opts}</select></label>'
            f'<label><span>Tier</span><select data-tq="t"><option value="1">Standard</option><option value="0.55">Priority</option><option value="0.3">Critical</option></select></label></div>'
            f'<p class="tq-o" aria-live="polite"></p></div>')

def LIFECYCLE():
    st = [("Discovery", ["reference-standards-excipients", "method-development-validation"]), ("Development", ["method-development-validation", "biologics-characterization-release", "extractables-leachables"]),
          ("Clinical", ["small-molecule-qc-release", "stability-studies", "bioanalytical-immunogenicity", "mrna-vaccine-testing", "cell-gene-therapy-testing"]),
          ("Scale-up", ["method-development-validation", "environmental-monitoring", "extractables-leachables"]), ("Commercial", ["small-molecule-qc-release", "microbiology-sterility", "environmental-monitoring", "biologics-characterization-release"]),
          ("Post-approval", ["stability-studies", "regulatory-data-integrity-support", "reference-standards-excipients"])]
    cols = "".join(f'<div class="lc-c" data-i="{i}"><b>{n}</b>' + "".join(f'<a href="{svc_url(s)}">{SVC[s][1]}</a>' for s in ss) + "</div>" for i, (n, ss) in enumerate(st))
    return f'<div class="lcyc"><div class="lc-bar" aria-hidden="true"><i></i></div><div class="lc-g">{cols}</div></div>'

def COMPARE():
    rows = []
    for s in SERVICES:
        lab = ", ".join(l[1] for l in LABS if s[0] in l[9])
        samp = {"small-molecule-qc-release": "1 to 5 g or 20 units", "stability-studies": "Per pull schedule", "method-development-validation": "5 to 20 g",
                "biologics-characterization-release": "1 to 5 mg protein", "mrna-vaccine-testing": "100 to 500 µg RNA", "cell-gene-therapy-testing": "1 to 2 mL or 10⁶ cells",
                "microbiology-sterility": "20 containers (typical)", "environmental-monitoring": "On-site sampling", "extractables-leachables": "Packaging + product lots",
                "bioanalytical-immunogenicity": "100 to 250 µL plasma", "reference-standards-excipients": "10 to 50 g", "regulatory-data-integrity-support": "Documents"}[s[0]]
        tat = int(re.findall(r"\d+", s[6])[0])
        rows.append(f'<tr><td><a href="{svc_url(s[0])}">{s[1]}</a></td><td data-v="{tat}">{s[6]}</td><td>{samp}</td><td>FDA, EMA, CDSCO, PMDA</td><td>{lab}</td></tr>')
    return ('<div class="cmp reveal"><div class="tw"><table class="sort"><thead><tr><th><button type="button" data-k="0">Service</button></th><th><button type="button" data-k="1">Typical TAT</button></th>'
            '<th><button type="button" data-k="2">Sample need</button></th><th>Regulatory coverage</th><th><button type="button" data-k="4">Lead labs</button></th></tr></thead><tbody>' + "".join(rows) + '</tbody></table></div>'
            f'<p class="cn">Indicative. Sample needs depend on the specification. {ILL()}</p></div>')

def PEOPLE(keys):
    """Leadership grid: portraits desaturated until hover, then colour and an 'in their words' line."""
    return '<div class="ppl">' + "".join(f'<figure class="pp reveal" style="--i:{i}"><img src="/img/{im}.jpg" alt="Portrait for {n} (illustrative)" loading="lazy"><figcaption><b>{n}</b><span>{r}</span><em>&ldquo;{q}&rdquo;</em></figcaption></figure>'
                                         for i, (n, r, im, q) in enumerate(keys)) + f'</div><p class="cn">{ILL("Illustrative profiles")} Names and photos are placeholders until the team is announced.</p>'

def HSCROLL(items):
    """Horizontal timeline with a drawn connecting line; images reveal with a clip-path wipe. items: (year, title, text, img)."""
    li = "".join(f'<li class="hs-i reveal" style="--i:{i}"><img src="/img/{im}.jpg" alt="{alt(im)}" loading="lazy"><em>{y}</em><h3>{t}</h3><p>{d}</p></li>' for i, (y, t, d, im) in enumerate(items))
    return f'<div class="hscr"><ol>{li}</ol></div>'

def MASONRY(items):
    """Photo mosaic with hover captions and a lightbox. items: (img, caption)."""
    return '<div class="mas">' + "".join(f'<button type="button" class="ms-i reveal" style="--i:{i % 6}" data-cap="{html.escape(c)}"><img src="/img/{im}.jpg" alt="{alt(im)}" loading="lazy"><span>{c}</span></button>' for i, (im, c) in enumerate(items)) + '</div><dialog class="lbox"><button type="button" class="lb-x" aria-label="Close">&times;</button><img alt=""><p></p></dialog>'

def TOC():
    return '<nav class="toc" aria-label="On this page"><p class="ey">On this page</p><ol></ol></nav>'

def KEYTAKE(items):
    return '<div class="keyt reveal"><p class="ey">Key takeaways</p>' + UL(items) + "</div>"

def ANSWER(text):
    """Answer-first summary (first 40 to 60 words answer the question directly)."""
    return f'<div class="answer reveal"><p class="ey">The short answer</p><p>{text}</p></div>'

def AUTHOR(key, mins, date=ASOF):
    n, role, spec, im, city = SCI[key]
    return f'<div class="author"><img src="/img/{im}.jpg" alt="" loading="lazy"><div><b>{n}</b><span>{role} {ILL("Illustrative author")}</span><small>{mins} min read &middot; Updated {date} &middot; Scientific review pending</small></div></div>'

# ---------- render ----------
FONT = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">')
NAVKEY = [("services/", "services"), ("solutions/", "services"), ("industries/", "industries"), ("labs/", "labs"), ("quality/", "quality"), ("technology/", "technology"), ("portal/", "technology"),
          ("insights/", "resources"), ("method-library/", "resources"), ("tools/", "resources"), ("regulatory-radar", "resources"), ("case-studies", "resources"), ("webinars", "resources"),
          ("whitepapers", "resources"), ("glossary", "resources"), ("about/", "company"), ("careers/", "company"), ("sustainability", "company"), ("news", "company"), ("partner-with-us", "company"), ("investors", "company")]

def relativize(h, depth):
    pre = "../" * depth
    def f(m):
        a, u = m.group(1), m.group(2)
        if u == "" or u.endswith("/"): u += "index.html"
        return f'{a}="{pre}{u}"'
    h = re.sub(r'(href|src|action|data-src)="/(?!/)([^"]*)"', f, h)
    h = h.replace("--bg:url(/img/", "--bg:url(../img/")  # custom-property urls resolve against assets/site.css
    return h.replace("url(/img/", f"url({pre}img/")

ORG = {"@context": "https://schema.org", "@type": "Organization", "name": BRAND, "url": DOMAIN, "description": "A planned network of GMP pharmaceutical analytical testing laboratories.",
       "parentOrganization": {"@type": "Organization", "name": "Investor Labs", "url": "https://investorlabs.eliteleadgrow.com"}, "email": MAIL}

# ---------- photo band: pages with few images get an Investor Labs style mosaic ----------
MOSPOOL = [("inst-hplc", "Chromatography", "HPLC, UPLC and GC", "/method-library/index.html"), ("inst-lcms", "Mass spectrometry", "LC-MS/MS and HRMS", "/services/index.html"),
           ("lab-microscope-woman", "Microscopy", "Identity, particles, morphology", "/services/index.html"), ("vax-vials", "Vaccines and mRNA", "Release and stability", "/industries/index.html"),
           ("lab-cleanroom-suit", "Cleanroom", "Grade A to D discipline", "/quality/index.html"), ("bio-cells-pink", "Cell culture", "Potency and cell-based assays", "/industries/index.html"),
           ("lab-pipette-blue", "Bench work", "Precise, documented, reviewed", "/quality/data-integrity.html"), ("pharma-pills-mix", "Oral solids", "Generics and formulations", "/industries/index.html"),
           ("log-plane", "Cold chain", "Samples that arrive intact", "/submit-samples.html"), ("data-dash", "Live data", "Watch every sample in the portal", "/technology/index.html"),
           ("lab-team-three", "Our scientists", "Named, qualified, reachable", "/about/leadership.html"), ("inst-icp", "Elemental analysis", "ICP-MS to ICH Q3D", "/method-library/index.html"),
           ("micro-petri-2", "Microbiology", "Sterility and bioburden", "/services/index.html"), ("room-clean-1", "Controlled rooms", "Environmental monitoring", "/quality/index.html"),
           ("inst-dissolution", "Dissolution", "Profiles that predict performance", "/method-library/dissolution-testing.html"), ("lab-glassware", "Wet chemistry", "Classical methods, modern rigour", "/method-library/index.html"),
           ("city-singapore", "Singapore", "A planned APAC hub", "/labs/index.html"), ("city-hyderabad", "Hyderabad", "India's pharma capital", "/labs/index.html"),
           ("lab-automation", "Automation", "Robotics where it reduces error", "/technology/index.html"), ("bio-dna", "Molecular biology", "qPCR, ddPCR and sequencing", "/industries/index.html"),
           ("pharma-capsules", "Capsules", "Content uniformity and dissolution", "/industries/index.html"), ("lab-sample-rack", "Sample management", "Chain of custody from dock to CoA", "/submit-samples.html"),
           ("sec-servers", "Secure by design", "Encrypted, audited, backed up", "/technology/index.html"), ("pharma-scopes", "Optics", "Particles and polymorphs", "/services/index.html")]

def MOSBAND(path, hero_img, n=4):
    n = 8 if n == 8 else 4
    k = sum(ord(c) * (i + 3) for i, c in enumerate(path)) % len(MOSPOOL)
    out, i = [], 0
    while len(out) < n and i < len(MOSPOOL):
        im, t, d, u = MOSPOOL[(k + i * 5) % len(MOSPOOL)]; i += 1
        if im == hero_img or any(o[0] == im for o in out): continue
        out.append((im, t, d, u))
    tiles = "".join(f'<a href="{u}" class="reveal" style="--i:{j}"><img src="/img/{im}.jpg" alt="{ALT.get(im, t)}" loading="lazy"><span><b>{t}</b>{d}</span></a>' for j, (im, t, d, u) in enumerate(out))
    return f'<section class="mosband"><div class="mos">{tiles}</div></section>'

def render(path, d, v):
    depth = path.count("/")
    title = d["title"]
    cur = d["nav"] or next((k for p, k in NAVKEY if path.startswith(p)), "")
    hb = d["hb"] if d["hb"] is not None else ('<a class="btn big mag" href="/request-quote.html"><span>Get a quote in 90 seconds</span></a> <a class="btn o big" href="/book-a-call.html">Talk to a scientist</a>')
    crumbs = CRUMBS(d["crumbs"], title) if path not in ("index",) and d["hero"] != "bare" else ""
    if d["hero"] == "bare":
        top = ""
    elif d["hero"] == "plain":
        top = f'<header class="phx"><div class="w">{crumbs}<p class="ey">{d["eyebrow"] or BRAND}</p>{WORDS(title)}<p class="lede">{d["lede"]}</p>' + (f'<div class="hb">{hb}</div>' if hb else "") + '</div></header>'
    else:
        chips = d["chips"]
        hc = '<div class="hc">' + "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in chips[:3]) + "</div>" if chips else ""
        top = (f'<header class="cine pc" style="--bg:url(/img/{d["img"] or "lab-corridor"}.jpg)"><div class="cb"></div><div class="sp"></div>{hc}'
               f'<div class="cw">{crumbs}<p class="ey">{d["eyebrow"] or BRAND}</p>{WORDS(title)}<p class="lede">{d["lede"]}</p>' + (f'<div class="hb">{hb}</div>' if hb else "") + '</div></header>')
    cta = "" if d["cta"] is False else CTA(*(d["cta"] or ()))
    band = MOSBAND(path, d["img"], 8 if d["body"].count("<img") < 3 else 4) if (d["hero"] != "bare" and path not in ("404", "maintenance", "search", "portal/login") and d["body"].count("<img") < 5) else ""
    body = header(path, cur) + top + f'<main id="main"{"" if d["hero"] == "bare" and path == "index" else " class=w"}>{d["body"]}{band}</main>' + (f'<div class="w">{cta}</div>' if cta else "") + footer() + floaters()
    desc = html.escape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", d["desc"] or d["lede"] or title)).strip())[:300]
    t = html.escape(re.sub("<[^>]+>", "", title))
    full_t = f"{BRAND}: {TAG}" if path == "index" else f"{t} | {BRAND}"
    url = f'{DOMAIN}/{"" if path == "index" else path + ".html"}'
    lds = list(d["jsonld"])
    if path == "index": lds.append(ORG)
    if d["crumbs"] is not None or (path != "index" and d["hero"] != "bare"):
        items = [("Home", "/index.html")] + list(d["crumbs"] or []) + [(re.sub("<[^>]+>", "", title), "/" + path + ".html")]
        lds.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + u.replace("/index.html", "/")} for i, (n, u) in enumerate(items)]})
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j)}</script>' for j in lds)
    og = f'{DOMAIN}/img/{d["img"] or "lab-corridor"}.jpg'
    full = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{full_t}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">'
            f'<meta property="og:title" content="{t}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="{og}"><meta name="twitter:card" content="summary_large_image">'
            f'<meta name="theme-color" content="#ffffff"><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22%3E%3Crect width=%2232%22 height=%2232%22 rx=%228%22 fill=%22%230B1F3A%22/%3E%3Cpath d=%22M4 24h6l3-6 3-11 3 15 2-6h7%22 fill=%22none%22 stroke=%22%2300B8A9%22 stroke-width=%222.6%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/%3E%3C/svg%3E">'
            f'{FONT}<link rel="stylesheet" href="/assets/site.css?v={v}">{ld}'
            '<script>document.documentElement.classList.add("js");try{var t=new URLSearchParams(location.search).get("theme")||localStorage.getItem("pc-theme");if(t)document.documentElement.dataset.theme=t;var r=localStorage.getItem("pc-region");if(r)document.documentElement.dataset.region=r}catch(e){}</script></head>'
            f'<body class="pc p-{path.replace("/", "-")}" data-root="{"../" * depth}">{body}'
            f'<script src="/assets/site.js?v={v}" defer></script></body></html>')
    return relativize(full, depth)

# ---------- canonical URL map (every module links only to these; build.py checks) ----------
ARTICLES = ["nitrosamine-testing-2027", "stability-zone-ivb", "mrna-critical-quality-attributes", "method-transfer-failure", "biosimilar-analytical-similarity",
            "data-integrity-top-10-findings", "endotoxin-lal-vs-recombinant", "choosing-a-testing-partner", "cgt-release-testing", "el-prefilled-syringes",
            "cost-of-a-delayed-batch", "state-of-pharma-testing-2027"]
METHODS = ["hplc-assay-related-substances", "uplc-impurity-profiling", "dissolution-testing", "content-uniformity", "residual-solvents-gc-hs", "elemental-impurities-icp-ms",
           "nitrosamines-lc-ms-ms", "genotoxic-impurities", "xrpd-polymorph", "particle-size-laser-diffraction", "water-content-karl-fischer", "ftir-identification",
           "raman-identification", "ich-stability-storage", "photostability-q1b", "forced-degradation", "sec-hplc-aggregates", "ce-sds", "icief-charge-variants",
           "peptide-mapping-lc-ms", "intact-mass-ms", "glycan-profiling-hilic", "cell-based-potency", "hcp-elisa", "residual-dna-qpcr", "mrna-integrity-ce",
           "mrna-capping-lc-ms", "poly-a-tail-length", "dsrna-elisa", "lnp-size-pdi-dls", "encapsulation-efficiency-ribogreen", "ddpcr-vector-titre",
           "aav-empty-full-auc", "flow-cytometry-identity", "sterility-membrane-filtration", "bacterial-endotoxins-lal", "recombinant-factor-c", "mycoplasma-nat",
           "bioburden", "container-closure-integrity", "toc-conductivity-water", "extractables-gc-ms", "leachables-lc-ms", "lc-ms-ms-pk-assay", "ada-bridging-assay", "nab-cell-based-assay"]
TOOLS = [("test-finder", "Test Finder"), ("quote-estimator", "Instant Quote Estimator"), ("turnaround-calculator", "Turnaround Calculator"),
         ("stability-study-designer", "Stability Study Designer"), ("nitrosamine-risk-assessor", "Nitrosamine Risk Assessor"), ("endotoxin-limit-calculator", "Endotoxin Limit Calculator"),
         ("inspection-readiness-score", "Inspection Readiness Score"), ("lab-locator-shipping-planner", "Lab Locator and Shipping Planner"), ("method-search-compare", "Method Search and Compare"),
         ("regulatory-impact-checker", "Regulatory Impact Checker"), ("cost-of-delay-calculator", "Cost of Delay Calculator"), ("ask-the-lab", "Ask the Lab")]
ROLES = ["analytical-chemist-hyderabad", "microbiologist-pune", "qa-specialist-dublin", "biologics-scientist-bengaluru", "lab-manager-singapore", "client-scientist-new-jersey"]
PLANNED = (["index", "services/index", "services/bundles", "services/compare", "industries/index", "solutions/index", "labs/index", "labs/capabilities-matrix",
            "quality/index", "quality/accreditations", "quality/data-integrity", "quality/inspection-history", "quality/ethics-and-compliance",
            "technology/index", "technology/api-and-integrations", "portal/index", "portal/login", "insights/index", "method-library/index", "regulatory-radar",
            "case-studies", "webinars", "whitepapers", "glossary", "tools/index", "about/index", "about/leadership", "about/our-story", "sustainability", "news",
            "careers/index", "partner-with-us", "investors", "request-quote", "book-a-call", "submit-samples", "contact", "support", "status", "privacy", "terms",
            "cookies", "accessibility", "whistleblowing", "modern-slavery-statement", "sitemap", "search", "404", "maintenance"]
           + [f"services/{s[0]}" for s in SERVICES] + [f"industries/{k}" for k, *_ in INDUSTRIES] + [f"solutions/{k}" for k, *_ in STAGES]
           + [f"labs/{l[0]}" for l in LABS] + [f"insights/{a}" for a in ARTICLES] + [f"method-library/{m}" for m in METHODS]
           + [f"tools/{t}" for t, _ in TOOLS] + [f"careers/{r}" for r in ROLES])

# ---------- shared service-page parts (used by c_services.py and c_services2.py) ----------
def SVCHEAD(slug, visual, chips):
    """Service intro block (template section 1, under the photo hero): promise + TAT + lead scientist on the left;
    a dark panel on the right holding the service's own animated `visual` (SVG/HTML) with floating stat `chips` [(value, label)] orbiting it."""
    s = SVC[slug]; n, role, spec, im, city = SCI[s[8]]
    ch = "".join(f'<span class="svh-c" style="--k:{i}"><b>{a}</b>{b}</span>' for i, (a, b) in enumerate(chips))
    return (f'<section class="svh reveal"><div class="svh-t"><p class="ey">{s[1]}</p><h2>{s[3]}</h2><p class="lede">{s[2]}</p>'
            f'<p class="svh-tat">{ICON("clock")} Typical turnaround <b>{s[6]}</b></p>'
            f'<div class="svh-sci"><img src="/img/{im}.jpg" alt="" loading="lazy"><span><b>{n}</b>{role} {ILL("Illustrative")}</span></div>'
            f'<p class="hb"><a class="btn mag" href="/request-quote.html?service={SERVICES.index(s)}"><span>Request a quote</span></a> '
            f'<a class="btn o" href="mailto:{MAIL}?subject={html.escape("Question for " + n)}">Ask {n.replace("Dr ", "").split()[0]}</a></p></div>'
            f'<div class="svh-v"><div class="svh-vis">{visual}</div>{ch}</div></section>')

def RELATED(slugs, line="Customers who test this often also need:"):
    return SH("Related services", line) + SVCGRID(only=slugs, filters=False)
