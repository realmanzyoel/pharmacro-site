"""Labs: hub, ten planned lab pages, capabilities matrix (blueprint 4.7). All sites are planned; people and figures are illustrative."""
from ph import *

# slug -> (airport code, airport name, lat, lon, drive time, regulators [(body, what)], lab head (name, img), photos for the tour)
EXTRA = {
 "hyderabad": ("HYD", "Rajiv Gandhi International Airport", 17.24, 78.43, "about 45 minutes", "India", ("Dr Kavya Reddy", "sci-woman-2"),
               ["lab-corridor", "inst-hplc", "lab-pipette-vials", "inst-dissolution", "lab-analyst-pc"]),
 "mumbai": ("BOM", "Chhatrapati Shivaji Maharaj International Airport", 19.09, 72.87, "about 40 minutes", "India", ("Vikram Desai", "sci-man-4"),
            ["city-mumbai", "lab-bench-woman", "micro-petri-2", "pharma-blisters", "lab-sample-rack"]),
 "pune": ("PNQ", "Pune International Airport", 18.58, 73.92, "about 35 minutes", "India", ("Dr Meera Kulkarni", "sci-woman-6"),
          ["vax-vials", "lab-petri-hand", "micro-petri-1", "room-clean-1", "lab-microscope-woman"]),
 "bengaluru": ("BLR", "Kempegowda International Airport", 13.20, 77.71, "about 60 minutes", "India", ("Dr Arvind Rao", "sci-man-5"),
               ["lab-instrument-load", "inst-lcms", "lab-plate-pink", "bio-cells-pink", "lab-team-three"]),
 "singapore": ("SIN", "Singapore Changi Airport", 1.36, 103.99, "about 30 minutes", "Singapore", ("Dr Rachel Lim", "sci-woman-3"),
               ["city-singapore-night", "bio-cells-green", "lab-cleanroom-suit", "inst-pcr", "lab-microscope-close"]),
 "kuala-lumpur": ("KUL", "Kuala Lumpur International Airport", 2.75, 101.71, "about 55 minutes", "Malaysia", ("Ahmad Faiz", "sci-man-6"),
                  ["city-kl-aerial", "lab-glassware", "inst-gc", "lab-cylinders", "room-clean-2"]),
 "leiden": ("AMS", "Amsterdam Airport Schiphol", 52.31, 4.76, "about 25 minutes", "Netherlands", ("Dr Sanne de Vries", "sci-woman-7"),
            ["city-amsterdam", "lab-automation", "lab-vials-bw", "inst-lcms", "lab-filtration"]),
 "cambridge": ("STN", "London Stansted Airport (LHR for long-haul)", 51.89, 0.26, "about 35 minutes", "United Kingdom", ("Dr Oliver Hughes", "sci-man-3"),
               ["city-london", "bio-cells-green", "lab-seated-woman", "inst-pcr", "lab-microscopes-row"]),
 "dublin": ("DUB", "Dublin Airport", 53.42, -6.27, "about 25 minutes", "Ireland", ("Aoife Kelly", "sci-woman-5"),
            ["city-dublin", "micro-petri-1", "room-clean-1", "lab-goggles", "lab-flasks-pour"]),
 "new-jersey": ("EWR", "Newark Liberty International Airport", 40.69, -74.17, "about 60 minutes", "United States", ("Dr Michael Grant", "sci-man-2"),
                ["city-newyork", "lab-vials-bw", "vax-virus", "inst-icp", "lab-instrument-bench"]),
}
REGS_BY = {
 "India": [("CDSCO", "Central Drugs Standard Control Organisation: national regulator for drugs and approved testing laboratories."),
           ("State Licensing Authority", "Approval as a drug testing laboratory under the Drugs and Cosmetics Rules, 1945."),
           ("NABL", "ISO/IEC 17025:2017 accreditation body for Indian testing laboratories."), ("Revised Schedule M", "GMP expectations for Indian manufacturers that clients must meet.")],
 "Singapore": [("HSA", "Health Sciences Authority: GMP and therapeutic product regulator."), ("SAC-SINGLAS", "ISO/IEC 17025 accreditation in Singapore."), ("PIC/S", "HSA is a PIC/S member; GMP expectations align.")],
 "Malaysia": [("NPRA", "National Pharmaceutical Regulatory Agency: GMP inspections and product registration."), ("Standards Malaysia (SAMM)", "ISO/IEC 17025 accreditation."), ("ASEAN", "Zone IVb stability expectations for the region.")],
 "Netherlands": [("IGJ", "Health and Youth Care Inspectorate: GMP inspections for EU release testing."), ("RvA", "Dutch Accreditation Council for ISO/IEC 17025."), ("EMA / EU GMP", "EU GMP Part I, Annex 11 and Annex 15 apply.")],
 "United Kingdom": [("MHRA", "Medicines and Healthcare products Regulatory Agency: GMP and GLP inspections."), ("UKAS", "ISO/IEC 17025 accreditation."), ("UK GMP", "UK GMP follows the EU GMP guide as retained in UK law.")],
 "Ireland": [("HPRA", "Health Products Regulatory Authority: GMP inspections and manufacturing authorisations."), ("INAB", "Irish National Accreditation Board for ISO/IEC 17025."), ("EU GMP", "EU release testing for a large pharma manufacturing base.")],
 "United States": [("FDA", "Contract testing labs are subject to 21 CFR Parts 210 and 211 and FDA inspection."), ("A2LA / ANAB", "ISO/IEC 17025 accreditation bodies in the US."), ("DEA", "Registration needed to handle controlled-substance samples.")],
}
INSTR = {
 "small-molecule-qc-release": [("HPLC and UPLC systems", "inst-hplc", "Quaternary pumps, PDA and charged aerosol detection, 21 CFR Part 11 chromatography data system."),
                               ("Dissolution baths, USP apparatus 1 to 4", "inst-dissolution", "Six- and eight-vessel baths with automated sampling and online UV.")],
 "stability-studies": [("Walk-in stability chambers", "lab-corridor", "ICH long-term, intermediate and accelerated conditions including 30 °C / 75% RH, mapped and alarmed 24/7."),
                       ("Photostability cabinets", "lab-glassware", "ICH Q1B Option 2 light sources with calibrated lux and UV meters.")],
 "method-development-validation": [("LC-MS method development stack", "inst-lcms", "Single and triple quadrupole MS with column and solvent screening."),
                                   ("GC and GC-MS", "inst-gc", "Headspace and liquid injection for residual solvents and volatiles.")],
 "biologics-characterization-release": [("High-resolution LC-MS", "inst-lcms", "Intact, subunit and peptide mapping workflows."),
                                        ("Capillary electrophoresis", "lab-instrument-load", "CE-SDS and icIEF for size and charge variants.")],
 "mrna-vaccine-testing": [("Capillary electrophoresis for RNA", "lab-instrument-load", "Integrity and fragment analysis of mRNA."),
                          ("Dynamic light scattering", "lab-instrument-bench", "LNP size and PDI; plate-based fluorescence for encapsulation efficiency.")],
 "cell-gene-therapy-testing": [("Droplet digital PCR", "inst-pcr", "Vector genome titre and residual DNA with absolute quantitation."),
                               ("Flow cytometers", "bio-cells-green", "Multi-colour identity, purity and viability panels.")],
 "microbiology-sterility": [("Isolator for sterility testing", "room-clean-1", "Closed membrane filtration in a decontaminated isolator."),
                            ("Endotoxin readers", "lab-plate-pink", "Kinetic chromogenic, turbidimetric and recombinant factor C assays.")],
 "environmental-monitoring": [("Active air samplers and particle counters", "room-clean-2", "Viable and non-viable monitoring to ISO 14644 and EU GMP Annex 1."),
                              ("TOC and conductivity analysers", "lab-cylinders", "Purified water and WFI testing to USP <643> and <645>.")],
 "extractables-leachables": [("GC-MS and LC-MS for E&L", "inst-lcms", "Volatile, semi-volatile and non-volatile screening with library searching."),
                             ("ICP-MS", "inst-icp", "Elemental extractables and ICH Q3D elemental impurities.")],
 "bioanalytical-immunogenicity": [("Triple quadrupole LC-MS/MS", "inst-lcms", "Regulated PK assays validated to ICH M10."),
                                  ("Plate readers and immunoassay platforms", "lab-plate-pink", "ADA screening, confirmation and titre; neutralising antibody assays.")],
 "reference-standards-excipients": [("FTIR and Raman", "lab-glassware", "Raw material identity, including handheld Raman at receipt."),
                                    ("Karl Fischer titrators", "lab-flasks-pour", "Volumetric and coulometric water content.")],
 "regulatory-data-integrity-support": [("Validated LIMS and CDS", "data-dashboard", "One LIMS and one chromatography data system across the network.")],
}

def _labs_data():
    return [dict(s=l[0], c=l[1], co=l[2], r=l[3], ph=l[6], f=l[7], im=l[8]) for l in LABS]

def _route(slug):
    """Small SVG map: airport -> lab, a drawn route on a local grid."""
    l = LAB[slug]; e = EXTRA[slug]
    la, lo, ala, alo = l[4], l[5], e[2], e[3]
    mnx, mxx, mny, mxy = min(lo, alo), max(lo, alo), min(la, ala), max(la, ala)
    sp = max(mxx - mnx, mxy - mny) or .1
    def p(a, b): return 60 + (b - mnx) / sp * 280, 200 - (a - mny) / sp * 160
    x1, y1 = p(ala, alo); x2, y2 = p(la, lo)
    cx, cy = (x1 + x2) / 2 + 40, min(y1, y2) - 30
    grid = "".join(f'<path d="M{x},0V240"/>' for x in range(0, 401, 40)) + "".join(f'<path d="M0,{y}H400"/>' for y in range(0, 241, 40))
    return (f'<svg class="lb-route reveal" viewBox="0 0 400 240" role="img" aria-label="Route from {e[0]} airport to the {l[1]} lab">'
            f'<g class="lb-grid">{grid}</g><path class="lb-rt" pathLength="1" d="M{x1:.0f},{y1:.0f} Q{cx:.0f},{cy:.0f} {x2:.0f},{y2:.0f}"/>'
            f'<circle cx="{x1:.0f}" cy="{y1:.0f}" r="7" class="lb-ap"/><text x="{x1:.0f}" y="{y1 + 24:.0f}" text-anchor="middle">{e[0]}</text>'
            f'<circle cx="{x2:.0f}" cy="{y2:.0f}" r="8" class="lb-lab"/><text x="{x2:.0f}" y="{y2 - 16:.0f}" text-anchor="middle">PharmaCRO {l[1]}</text></svg>')

def _tour(slug):
    ims = EXTRA[slug][7]
    fr = "".join(f'<figure class="lb-tf{" on" if i == 0 else ""}"><img src="/img/{im}.jpg" alt="{alt(im)}" loading="lazy"><figcaption>{i + 1} / {len(ims)} &middot; {alt(im)}</figcaption></figure>' for i, im in enumerate(ims))
    return (f'<div class="lb-tour reveal" aria-roledescription="slideshow" aria-label="Photo tour">{fr}<div class="lb-tbar"><i></i></div>'
            f'<button type="button" class="lb-tp" aria-pressed="false">Pause tour</button></div>'
            f'<p class="cn">A 20-second photo tour stands in until we film each site. Photos are illustrative stock images, not this lab. {ILL("Illustrative")}</p>')

def _instruments(sp):
    items = [i for s in sp for i in INSTR.get(s, [])][:6]
    c = "".join(f'<details class="lb-inst reveal" style="--i:{k}"><summary><img src="/img/{im}.jpg" alt="" loading="lazy"><b>{n}</b><span>Show spec</span></summary><p>{d}</p>'
                f'<p class="lb-cap"><span>Planned capacity</span><b>{[2, 3, 4, 6][k % 4]} units</b> {ILL()}</p></details>' for k, (n, im, d) in enumerate(items))
    return f'<div class="lb-insts">{c}</div>'

def _team(slug):
    head = EXTRA[slug][6]
    people = [(head[0], "Lab head", head[1]), ("[QA head]", "Head of Quality Assurance", "sci-woman-1"), ("[Senior scientist]", "Senior Scientist, method development", "sci-man-1"),
              ("[Microbiology lead]", "Microbiology Lead", "sci-woman-4")]
    return PEOPLE([(n, r, im, "I want every client to be able to call the person who ran their sample.") for n, r, im in people])

def lab_page(l):
    s, city, country, region, la, lo, phase, focus, img, sp = l
    e = EXTRA[s]
    regs = REGS_BY[e[5]]
    certs = "".join(f'<div class="lb-cert"><b>{b}</b><span>{w}</span><small>Certificate number: [pending] &middot; Expiry: [pending] &middot; <a href="/quality/accreditations.html">Verify</a></small></div>' for b, w in regs[:3])
    news = [("Planned", f"{city} site selection and integration plan", "/news.html"), ("Hiring", f"Roles opening at {city}", "/careers/index.html"), ("Network", "Method transfer programme from the Hyderabad flagship", "/labs/capabilities-matrix.html")]
    body = (ANSWER(f"PharmaCRO {city} is a planned {region} site in the network, opening in {phase} of the plan. Its focus: {focus.lower()}. "
                   f"It will run the same SOPs, instruments and LIMS as every other PharmaCRO lab, so methods transfer in days and your results look the same wherever they are tested.")
            + KV([("City", f"{city}, {country}"), ("Region", region), ("Planned opening", f"{phase} of the company plan"), ("Years operating", f"Planned site {ILL('Not yet operating')}"),
                  ("Focus", focus), ("Lab head", f"{e[6][0]} {ILL('Illustrative')}"), ("Nearest airport", f"{e[0]}, {e[1]}")])
            + SH("Photo tour", f"Inside the {city} lab.") + _tour(s)
            + SH("Regulatory scope", f"Who oversees work in {country}.", "Results from this site are written to satisfy the local regulator and the regulators of the markets our clients ship to.")
            + T(["Body", "What it means for your samples"], [[b, w] for b, w in regs])
            + REGBADGES()
            + SH("Capabilities and instruments", "What runs here.", "Select an instrument to see its specification. Counts are planning figures.") + _instruments(sp)
            + SPLIT(e[7][1], H3("Specialities unique to this site") + TICKLIST([SVC[k][1] + ": " + SVC[k][7][0] for k in sp] + ["Overflow and method transfer from every other PharmaCRO lab"]), flip=True)
            + SH("Accreditations and inspection history", "What this site will hold, and what it holds today.",
                 "Plain words: as a planned site, this lab holds no accreditation and has no inspection record under PharmaCRO yet. Targets are shown below; certificates appear here with numbers and dates once issued.")
            + f'<div class="lb-certs">{certs}</div><p><a class="btn o" href="/quality/inspection-history.html">How we disclose inspection history</a></p>'
            + SH("Team", "The people who will run your samples.") + _team(s)
            + SH("Location and logistics", "Getting samples here.")
            + '<div class="two"><div>' + _route(s) + f'<p class="cn">From {e[0]}: {e[4]} by road. Map is schematic.</p></div><div>'
            + KV([("Address", f"[Street address], {city}, {country} {ILL('Placeholder')}"), ("Receiving hours", "Monday to Friday 08:00 to 20:00, Saturday 09:00 to 13:00, local time. Critical-tier samples by arrangement 24/7."),
                  ("Courier instructions", "Book through the portal or the quote email. Label every box with the sample ID and quote reference; keep the temperature logger inside the box."),
                  ("Cold chain", "2 to 8 °C, −20 °C, −80 °C and liquid nitrogen dry-shipper receipt, with temperature traces logged at intake."),
                  ("Customs help", "We prepare the commercial invoice wording, HS code guidance and import permits for biological samples where needed.")])
            + f'<p><a class="btn" href="/submit-samples.html">How to ship samples</a> <a class="btn o" href="/tools/lab-locator-shipping-planner.html">Shipping planner</a></p></div></div>'
            + SH("Local news and careers", f"What is happening in {city}.")
            + '<div class="lb-news">' + "".join(f'<a class="reveal" href="{u}"><small>{t}</small><b>{h}</b></a>' for t, h, u in news) + '</div>'
            + SH("Services offered here", f"Lead services at {city}.") + SVCGRID(only=sp, filters=False)
            + GALLERY(e[7][2:5])
            + SH("Questions", f"About the {city} lab.")
            + FAQS([(f"Is the {city} lab open?", f"<p>Not yet. {city} is a planned site in {phase} of the company plan. Until it opens, work for this region runs at the nearest operating PharmaCRO lab and the quote says exactly where.</p>"),
                    ("Will my results differ between labs?", "<p>They should not. Every site runs the same SOPs, the same instrument models and one LIMS, and methods are formally transferred with comparative testing before use.</p>"),
                    ("Can I audit this site?", "<p>Yes. Request an audit through <a href='/contact.html'>contact</a>; a quality lead confirms within 48 hours.</p>"),
                    ("Which regulators will this site work to?", f"<p>{', '.join(b for b, _ in regs)}, plus the expectations of the markets you ship to, such as FDA and EMA.</p>"),
                    ("Can you receive frozen samples?", "<p>Yes: 2 to 8 °C, −20 °C, −80 °C and dry-shipper receipt, with the temperature trace logged at intake.</p>")], f"faq-{s}"))
    page(f"labs/{s}", f"PharmaCRO {city}", f"A planned {region} lab: {focus.lower()}.", body, img=img, eyebrow=f"Labs &middot; {country}",
         chips=[(phase, "planned opening"), (region, "region"), (e[0], "nearest airport")], crumbs=[("Labs", "/labs/index.html")],
         cta=(f"Have samples bound for {city}?", "Tell us the product and tests. Until this site opens we will route them to the nearest operating lab and tell you where.", e[7][0]))

for _l in LABS: lab_page(_l)

# ---------- hub ----------
def _cards():
    c = "".join(f'<a class="lb-card reveal" href="/labs/{l[0]}.html" data-name="{l[1]}" data-ph="{["Year 1", "Year 2", "Year 2 to 3", "Year 3"].index(l[6])}" data-r="{l[3]}" style="--i:{i % 4}">'
                f'<img src="/img/{l[8]}.jpg" alt="{alt(l[8])}" loading="lazy"><div><p class="ey">{l[3]} &middot; planned {l[6]}</p><h3>{l[1]}, {l[2]}</h3><p>{l[7]}</p>'
                f'<ul>{"".join(f"<li>{SVC[k][1]}</li>" for k in l[9])}</ul><small>Lab head: {EXTRA[l[0]][6][0]} &middot; Current lead time: {5 + i % 4} days {ILL("Simulated")}</small></div></a>'
                for i, l in enumerate(LABS))
    rb = "".join(f'<button type="button" class="ch" data-lr="{r}" aria-pressed="false">{r}</button>' for r in ["India", "Southeast Asia", "Europe", "United States"])
    return (f'<div class="lb-ctl"><span>Sort</span><button type="button" class="ch" data-ls="name" aria-pressed="false">Name</button><button type="button" class="ch" data-ls="ph" aria-pressed="true">Opening</button>'
            f'<button type="button" class="ch" data-ls="r" aria-pressed="false">Region</button><span>Filter</span>{rb}</div><div class="lb-cards">{c}</div>')

page("labs/index", "Ten labs. One standard.",
     "A planned network of GMP testing labs across India, Southeast Asia, Europe and the United States, close to your plant and your regulator.",
     ANSWER("PharmaCRO is building ten pharmaceutical testing labs: four in India, two in Southeast Asia, three in Europe and one in the United States. Every site will run the same SOPs, "
            "instrument models and LIMS, so a method validated in one lab transfers to another in days, and you see every sample in one portal.")
     + MAP("labs-map", big=True)
     + SH("All labs", "Find the right site.", "Sort and filter the planned sites. Select a card for the lab page.") + _cards()
     + BAND("lab-corridor", "One SOP set. One instrument list. One LIMS.", "The network is only valuable if a result from Pune means the same as a result from Dublin. That is the standard every acquisition is integrated to.",
            BTN("See the capabilities matrix", "/labs/capabilities-matrix.html"))
     + SH("Network principles", "What makes ten labs behave like one.")
     + ICARDS([("doc", "Same SOPs", "One quality manual and one SOP set, translated where needed, controlled in one document system."),
               ("peak", "Same instruments", "A standard instrument list per service line, so methods do not need redevelopment when they move."),
               ("lock", "Same LIMS", "One LIMS and chromatography data system: one audit trail, one CoA format, one portal."),
               ("arrow", "Method transfer in days", "Comparative testing against pre-agreed criteria, run by the same method owner across sites."),
               ("truck", "Overflow by design", "If one lab is full, your samples can move to another with your approval and no change to the report."),
               ("shield", "One quality team", "QA reports into the Head of Quality, not into site management.")])
     + SH("Capabilities", "Which lab does what.", "A preview of the full matrix.") + SPLIT("lab-team-three", P("Each site has one or two centres of excellence and runs routine services that every client needs. The matrix shows planned capability by site and service.")
                                                                                        + P(BTN("Open the capabilities matrix", "/labs/capabilities-matrix.html")))
     + STRIP(["city-hyderabad", "city-mumbai", "city-pune", "city-bengaluru", "city-singapore", "city-kl", "city-leiden", "city-cambridge", "city-dublin", "city-newjersey"])
     + FAQS([("Are these labs operating today?", "<p>No. They are planned sites from the company plan, phased from Year 1 (India) to Year 3 (United States). Each lab page says so.</p>"),
             ("Will you buy existing labs or build new ones?", "<p>Mainly acquire accredited, founder-led labs and integrate them. See <a href='/partner-with-us.html'>Partner with us</a>.</p>"),
             ("Can I choose which lab tests my samples?", "<p>Yes. The quote names the lab; any change needs your approval.</p>")], "faq-labs"),
     img="lab-corridor", eyebrow="Labs", chips=[("10", "planned sites"), ("4", "regions"), ("1", "LIMS")],
     cta=("Close to your plant. Close to your regulator.", "Tell us where you manufacture and where you file. We will suggest the right lab and the fastest route."))

page("labs/capabilities-matrix", "Capabilities matrix",
     "Every planned lab against every service: centres of excellence, routine capability and work routed through the network.",
     ANSWER("The matrix shows, for each planned PharmaCRO lab, whether a service is a centre of excellence, offered routinely, available by transfer from another site, or not offered. "
            "Because every lab shares one LIMS and SOP set, a service marked as transfer can usually start within days.")
     + MATRIX()
     + SH("How to read it", "Four levels of capability.")
     + T(["Symbol", "Level", "What it means"], [['<i class="lv3"></i>', "Centre of excellence", "Method owners, method development and the deepest instrument capacity sit here."],
                                              ['<i class="lv2"></i>', "Offered", "Routine, validated capability at this site."],
                                              ['<i class="lv1"></i>', "Via network transfer", "Run at a sister site, or transferred here for your programme."],
                                              ['<i class="lv0"></i>', "Not offered", "Not planned at this site."]])
     + SH("How transfer works", "Validated once. Run anywhere.")
     + STEPLINE([("Transfer protocol", "The method owner writes acceptance criteria before any testing at the receiving site."),
                 ("Comparative testing", "Both sites test the same lots; results are compared against the pre-set criteria."),
                 ("Report and approval", "QA approves the transfer report; the method goes live in the shared LIMS."),
                 ("Ongoing equivalence", "Inter-site checks and shared control samples keep results aligned.")])
     + SPLIT("inst-hplc", H3("Need a capability not shown?") + P("Many services can be added to a site within weeks by transfer. Tell us the method and the volume.")
             + MAILFORM([("name", "Name", "text", True), ("email", "Work email", "email", True), ("lab", "Preferred lab", [l[1] for l in LABS], False), ("need", "Capability needed", "textarea", True)],
                        "Capability request", "Request a capability"))
     + f'<p class="cn">Planned capability {ILL("Planned network")}. Final scope is confirmed per site on the accreditation wall.</p>',
     img="lab-team-three", eyebrow="Labs", crumbs=[("Labs", "/labs/index.html")], chips=[("10 x 12", "labs by services"), ("4", "capability levels")])
