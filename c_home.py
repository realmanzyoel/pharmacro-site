"""Home page: the 15 sections of blueprint 4.1."""
from ph import *

CHROM = ('<svg class="chrom" viewBox="0 0 300 120" preserveAspectRatio="none" aria-hidden="true"><path class="c0" d="M0 110H300"/>'
         '<path class="c1" pathLength="1" d="M0 108H40c8 0 9-2 12-10l6-40c2-10 5-10 7 0l6 40c3 8 4 10 12 10H120c6 0 7-1 9-6l4-22c1-6 3-6 4 0l4 22c2 5 3 6 9 6H190c8 0 9-3 12-14l7-72c2-12 5-12 7 0l7 72c3 11 4 14 12 14H300"/>'
         '<text x="57" y="50">API</text><text x="128" y="78">Imp. A</text><text x="200" y="22">Main</text></svg>')

SLIDES = ["pharma-lab", "inst-lcms", "lab-microscope-woman", "vax-vials", "lab-cleanroom-suit", "city-singapore-night"]
HERO = ('<header class="cine big">' + "".join(f'<div class="sl" style="background-image:url(/img/{n}.jpg);animation-delay:{i * 6}s"></div>' for i, n in enumerate(SLIDES))
        + '<canvas id="net"></canvas><div class="au"></div><div class="sp"></div><div class="cw"><p class="ey">PharmaCRO &middot; Pharmaceutical analytical testing network</p>'
        '<h1>Every batch. Every standard. <span class="shim">Every market.</span></h1>'
        '<p class="lede">One accredited network of pharmaceutical testing labs. Faster results, inspection-ready data, one portal.</p>'
        '<div class="hb"><a class="btn" href="/request-quote.html">Get a quote in 90 seconds</a> <a class="btn o" href="/tools/test-finder.html">Find the right test</a></div>'
        '<p class="tag">Small molecules. Biologics. mRNA. Cell and gene therapy. One standard.</p></div><span class="scrollcue"></span></header>')

MOS = ('<div class="mos m5">' + "".join(f'<a href="{u}" class="reveal" style="--i:{i}"><img src="/img/{im}.jpg" alt="{ALT.get(im, "")}" loading="lazy"><span><b>{t}</b>{d}</span></a>' for i, (im, t, d, u) in enumerate([
    ("inst-hplc", "Small molecule QC", "Assay, impurities, dissolution and release", "/services/index.html"),
    ("vax-vials", "mRNA and vaccines", "Capping, integrity, LNP and potency", "/industries/index.html"),
    ("bio-cells-green", "Cell and gene therapy", "Vector titre, identity and release", "/industries/index.html"),
    ("micro-petri-1", "Microbiology", "Sterility, endotoxin, environmental monitoring", "/services/index.html"),
    ("pharma-lab", "The lab network", "Ten planned sites, one standard", "/labs/index.html")])) + '</div>')
KPIS = ('<div class="kpis">' + "".join(f'<div class="kpi reveal" style="--i:{i}"><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate([
    ("10", "planned lab sites across four regions"), ("46", "published methods in the public library"), ("4.2 days", "demo average turnaround (placeholder)"), ("48 h", "fastest priority release, once live")])) + '</div>')

NETWORK = (SH("One network, every test", "A single standard across every lab.",
              "Method transfer between our labs takes days, not months, because every lab runs the same SOPs, the same instruments and the same LIMS.", center=True)
           + CONSTELLATION()
           + P("Hover a service to pull it forward; select it to see the key tests, typical turnaround and a quote button."))

MAPSEC = (SH("Global lab map", "Close to your plant. Close to your regulator.",
             "Ten planned sites across India, Southeast Asia, Europe and the United States, each serving its regulator's expectations and its region's climate zone.")
          + MAP("home-map"))

HOW = (SH("How it works", "From your dock to an e-signed CoA, in four steps.", "Every step has a promise and an owner you can name.")
       + VIAL([("Submit", "Send a quote request or open the portal. Context from the page you were on carries straight into the form, and a scientist replies within 4 business hours.", "lab-analyst-pc", "sealed"),
               ("Receive", "A cold-chain courier collects. When the box arrives we photograph the samples, log the temperature trace and post a receipt to your portal within hours.", "log-warehouse", "opened"),
               ("Test", "A named analyst runs your samples on a qualified instrument. You see live status: queued, in analysis, under review.", "inst-hplc", "instrument"),
               ("Release", "An independent QA reviewer approves the data, the CoA is e-signed, and the full data package lands in the portal with a query desk for questions.", "lab-goggles", "reported")]))

NUMS = (SH("Numbers that matter", "The figures we will publish, and how we will measure them.", "Every number on this page is a placeholder until it is verified and dated.")
        + NUMBERS([("1.2M", "tests per year", "Count of reportable results released across all sites in the trailing 12 months.", [3, 4, 4, 5, 6, 7, 8]),
                   ("30", "accredited labs", "Sites holding ISO/IEC 17025 for at least one method in scope at the date shown.", [6, 9, 12, 16, 20, 26, 30]),
                   ("14", "countries", "Countries with at least one operating PharmaCRO laboratory.", [3, 4, 6, 8, 10, 12, 14]),
                   ("98.6%", "on-time delivery", "Share of reports issued on or before the date promised in the quote, all tiers, trailing 90 days.", [94, 95, 96, 96.5, 97.8, 98.1, 98.6]),
                   ("0", "repeat critical observations", "Critical regulatory observations repeated at the same site at the next inspection.", [2, 1, 1, 0, 0, 0, 0])]))

TAT = (SH("Turnaround promise", "Know your date before you ship.",
          "Three tiers, one rule: if we miss the date, the fee for that test is credited.")
       + CLOCK() + TIERS() + TATCALC())

PORT = ('<section class="dark-sec"><div class="pin2"><div>' + EY("Client portal") + H2("Watch your samples move in real time.")
        + TICKLIST(["Live sample tracking with a status timeline", "Instant e-signed CoA download", "Trend and control charts across batches", "Full audit trail and team permissions", "API and webhooks into your ERP, QMS or LIMS"])
        + '<p><a class="btn" href="/portal/index.html">See the portal</a></p></div>' + PORTAL() + '</div></section>')

SCIENCE = (SH("Science depth", "Specialist hands for specialist molecules.", "Three of the hardest questions we answer, and who answers them.")
           + FLIPS([("vax-vials", "mRNA and LNP characterisation", "Capping, poly(A), dsRNA, encapsulation efficiency", "inst-lcms",
                     f"<b>Ion-pair RP LC-MS</b><span>5' cap and tail heterogeneity at intact and fragment level. Capillary electrophoresis for integrity; dye-binding for EE%.</span><em>&ldquo;Most mRNA failures show up in the cap long before potency.&rdquo; {SCI['kenji'][0]}</em>"),
                    ("lab-instrument-load", "Biologics comparability", "Charge, size, glycans, potency", "lab-automation",
                     f"<b>icIEF, CE-SDS, HILIC glycans</b><span>Side-by-side with the reference product across multiple lots, with acceptance ranges set before the data.</span><em>&ldquo;Similarity is a statistical argument, not a single chromatogram.&rdquo; {SCI['elena'][0]}</em>"),
                    ("pharma-blisters", "Nitrosamines and elemental impurities", "NDSRIs, ICH Q3D", "inst-icp",
                     f"<b>LC-MS/MS and ICP-MS</b><span>Low ng/g limits for NDSRIs against current acceptable intakes; all 24 ICH Q3D elements by risk class.</span><em>&ldquo;Start with the risk assessment; the method follows.&rdquo; {SCI['ananya'][0]}</em>")])
           + '<p style="margin-top:18px"><a class="btn o" href="/method-library/index.html">Browse the Method Library</a> <span class="cn">Growing towards 500+ methods.</span></p>'
           + '<div class="scis">' + SCICARD("kenji") + SCICARD("elena") + SCICARD("ananya") + '</div>')

CASESEC = (SH("Case studies", "Problems we are built to solve.", "Three illustrative stories with a hero metric each. Drag, swipe or use the arrows.")
           + CASES([("lab-instrument-load", 6, " weeks", "Biosimilar developer cut a comparability study from 14 weeks to 6", "Biosimilars", "Biologics characterization",
                     "A mid-size biosimilar developer needed a full analytical similarity package for an EMA filing, against three reference lots bought in two markets.",
                     "We ran charge, size, glycan and potency methods in parallel across two labs on the same LIMS, with acceptance criteria agreed before the first injection.",
                     "Package delivered in 6 weeks instead of the 14 originally quoted elsewhere, with one consolidated report and raw data in the portal.",
                     "We got one report, one reviewer and one set of raw data. That is what made the timeline possible."),
                    ("pharma-blisters2", 21, " days saved", "Generic launch cleared nitrosamine testing 21 days early", "Generics", "Small molecule QC",
                     "A generic manufacturer found a nitrosamine risk in a sartan formulation six weeks before a US launch date.",
                     "Risk assessment in 48 hours, a validated LC-MS/MS NDSRI method transferred from the flagship lab, and Critical-tier testing of three registration batches.",
                     "Results released 21 days before the deadline; the launch went ahead on schedule.",
                     "The risk assessment came back before we had finished writing the purchase order."),
                    ("bio-cells-green", 48, " hours", "Autologous CAR-T release in 48 hours with rapid sterility", "Cell and gene therapy", "CGT testing",
                     "A cell therapy company needed release results inside a 72-hour vein-to-vein window.",
                     "Rapid microbial methods, flow identity and potency run in parallel with a dedicated evening shift.",
                     "Release data in 48 hours, leaving a full day for logistics.",
                     "For our patients the clock matters more than anything else.")]))

QUALITY = ('<section class="dark-sec">' + SH("Quality and data integrity", "Built to survive inspection.",
                                            "Short claims, each with the evidence beside it.")
           + '<div class="two"><div>' + FAQS([("ALCOA+ controls", "<p>Every result is attributable, legible, contemporaneous, original and accurate, plus complete, consistent, enduring and available. <a href='/quality/data-integrity.html'>See exactly how the LIMS enforces each one</a>.</p>"),
                                               ("Full audit trail", "<p>Every create, change and approval is logged with user, time and reason, and reviewed before a result is approved.</p>"),
                                               ("21 CFR Part 11 aligned portal", "<p>Electronic records and signatures designed to Part 11 and EU Annex 11 principles. Validation evidence is available to auditors.</p>"),
                                               ("Independent QA review of every report", "<p>No analyst approves their own data. QA reviewers sit outside the testing team's reporting line.</p>"),
                                               ("Inspection record", f"<p>Zero data integrity findings in the last [X] inspections. {ILL('Verify before publishing')} <a href='/quality/inspection-history.html'>Inspection history</a>.</p>")], "q")
           + '</div><div>' + AUDIT() + '</div></div></section>')

INSIGHTS = (SH("Insights and Regulatory Radar", "What changed this week, and what it means for testing.")
            + '<div class="two"><div>' + MOSAIC([("pharma-blisters", "Nitrosamine testing in 2027: what regulators now expect", "Regulatory &middot; 9 min read", "/insights/nitrosamine-testing-2027.html"),
                                                 ("lab-corridor", "Stability zones explained: Zone IVb for India and ASEAN", "Methods &middot; 8 min read", "/insights/stability-zone-ivb.html"),
                                                 ("vax-vials", "mRNA critical quality attributes: the complete guide", "mRNA and vaccines &middot; 12 min read", "/insights/mrna-critical-quality-attributes.html")])
            + '</div><div>' + RADAR([("18 Nov 2026", "FDA", "Updated acceptable intake limits for NDSRIs", "Re-check any product whose NDSRI limit was set from the older potency category.", "Small molecule QC"),
                                     ("12 Nov 2026", "EMA", "Annex 1 contamination control strategy reminders", "Expect inspectors to ask how EM trending feeds your CCS.", "Environmental monitoring"),
                                     ("06 Nov 2026", "CDSCO", "Revised Schedule M compliance for MSMEs", "Smaller Indian manufacturers need documented QC capacity, in-house or outsourced.", "Generics"),
                                     ("29 Oct 2026", "ICH", "Q2(R2) and Q14 training materials", "Lifecycle validation is now the default expectation for new methods.", "Method validation")])
            + f'<p><a class="btn o" href="/regulatory-radar.html">Open the Regulatory Radar</a></p><p class="cn">{ILL("Sample feed")} Items summarise public regulator announcements; check the source before acting.</p></div></div>')

JOIN = (SH("Join the network", "Two ways to build this with us.")
        + SPLITPANELS(("biz-highfive", "For lab owners", "Own a GMP lab? Let us talk.", "We partner with founder-led labs. You keep your standards. We bring scale, systems and a bigger future for your team. Confidential, always.", "/partner-with-us.html", "Start a confidential conversation", "warm"),
                      ("lab-smile", "Careers", "Build your career in pharma science.", "Training budgets, instrument exposure, a clear ladder from analyst to site head, and pay you can see before you apply.", "/careers/index.html", "See open roles", "cool")))

body = (HERO + '<div class="w">' + MOS + KPIS + TRUST()
        + SH("Who are you?", "Tell us what you are making.", "Choose one and we will show the tests that matter for it. We remember your choice as you browse.")
        + ROUTER() + NETWORK + SIG() + MAPSEC + HOW + NUMS + TAT + PORT + SCIENCE + CASESEC + QUALITY + INSIGHTS + JOIN + '</div>')

page("index", "Every batch. Every standard. Every market.", "One accredited network of pharmaceutical testing labs. Faster results, inspection-ready data, one portal.",
     body, hero="bare", img="lab-corridor",
     desc="PharmaCRO is a planned network of GMP pharmaceutical analytical testing labs across India, Southeast Asia, Europe and the US: small molecule QC, stability, biologics, mRNA, cell and gene therapy, microbiology and more.",
     cta=("Your next batch could clear in 48 hours.", "Tell us the product, the tests and the date. A scientist replies within 4 business hours; a typical quote takes one day."))
