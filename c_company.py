"""Company pages: about, leadership, story, sustainability, news, careers (+ roles), partner with us, investors. Blueprint 4.2 and 4.11."""
from ph import *

CO = [("About us", "/about/index.html")]

# ---------------- about ----------------
VALUES = [("01", "Data is sacred.", "Every result is attributable, reviewed and kept. Nobody approves their own data, and nobody is asked to make a deadline by bending a number."),
          ("02", "Speed with rigour.", "We are fast because the system is the same everywhere, not because a step was skipped. If speed and integrity conflict, integrity wins."),
          ("03", "Respect the lab.", "We buy labs that are already good. We keep what made them good: their people, their client relationships, often their name."),
          ("04", "Be reachable.", "Every client has a named scientist. Every email gets a human reply within four business hours. Every phone call reaches someone who can help.")]
VALS = '<div class="co-vals">' + "".join(f'<div class="co-val reveal" style="--i:{i}"><b>{n}</b><h3>{t}</h3><p>{d}</p></div>' for i, (n, t, d) in enumerate(VALUES)) + "</div>"

MILESTONES = [("Year 1", "First lab joins the network", "A GMP-accredited small molecule QC lab in Hyderabad becomes the flagship and the template for every lab after it.", "city-hyderabad"),
              ("Year 1", "One LIMS, one SOP set", "The shared laboratory information system and harmonised SOPs go live at the first sites.", "lab-analyst-pc"),
              ("Year 1", "Four Indian sites", "Mumbai, Pune and Bengaluru join, adding microbiology, vaccines and biologics.", "city-mumbai2"),
              ("Year 2", "Southeast Asia", "Singapore and Kuala Lumpur open the ASEAN hub, with Zone IVb stability capacity.", "city-singapore"),
              ("Year 2", "First biologics centre", "Biosimilar comparability and mass spectrometry move from one lab to a network capability.", "lab-instrument-load"),
              ("Year 2 to 3", "Europe", "Leiden, Cambridge and Dublin bring EU release, cell and gene therapy and bioanalysis.", "city-leiden"),
              ("Year 3", "United States and mRNA", "A New Jersey site adds US release, E&amp;L and a dedicated mRNA and LNP analytics capability.", "city-newjersey")]

DAY = [("07:45", "Arrive, check the instrument log book and the overnight sequence on HPLC 4."), ("08:15", "Stand-up with the lab manager: today's Critical-tier samples come first."),
       ("09:00", "Weigh standards and samples; the balance writes straight into the LIMS."), ("11:30", "Review system suitability. Resolution 2.4, tailing 1.1: the run continues."),
       ("13:00", "Lunch, then a 30-minute training block on the new dissolution SOP."), ("14:00", "Peer review of a colleague's data, including the audit trail."),
       ("16:30", "A client scientist calls about an unexpected peak. Ten minutes on the phone saves a week of email."), ("17:30", "Hand over the evening sequence. Results go to QA in the morning.")]

about_body = (
    ANSWER("PharmaCRO is a planned network of GMP pharmaceutical analytical testing laboratories across India, Southeast Asia, Europe and the United States. "
           "We bring good independent labs into one standard, one LIMS and one portal, so clients get fast results they can defend in an inspection.")
    + SPLIT("lab-team-three", H2("Why we exist") + P(
        "The pharmaceutical testing market is fragmented, slow and inconsistent. Thousands of small accredited labs do excellent work, but each runs its own systems, its own report format and its own idea of a turnaround time.",
        "A QC director who needs release, stability and biologics work often manages three vendors, three portals and three audit programmes.",
        "We are bringing great independent labs into one standard without erasing what made them great.") + f'<p><a href="/about/our-story.html">Read our story &rsaquo;</a></p>')
    + SH("Milestones", "From one lab to a network.", "The plan, step by step. These are planned milestones, not achievements yet.")
    + HSCROLL(MILESTONES) + f'<p class="cn">{ILL("Planned milestones")} Timing follows the company plan and may change.</p>'
    + SH("What we believe", "Four values, each with a behaviour you can check.")
    + VALS
    + BAND("lab-corridor", "Science you can sign your name to.", "Every report we issue has a named analyst, a named reviewer and a named approver behind it.", BTN("Meet the leadership", "/about/leadership.html"))
    + SH("By the numbers", "What the network is planned to look like.")
    + NUMBERS([("30", "labs targeted by Year 3", "Planned portfolio size from the company plan (28 to 35 labs).", [1, 4, 8, 14, 20, 26, 30]),
               ("900", "scientists and analysts", "Planned headcount across all sites at Year 3 scale.", [60, 150, 280, 420, 600, 760, 900]),
               ("1,500", "qualified instruments", "Chromatography, mass spectrometry, microbiology and stability chambers across the network.", [90, 250, 480, 700, 950, 1200, 1500]),
               ("1.2M", "tests per year", "Reportable results released per year at planned scale.", [1, 2, 3, 5, 7, 9, 12]),
               ("14", "countries", "Countries with at least one PharmaCRO laboratory at planned scale.", [1, 1, 2, 4, 7, 10, 14])])
    + SH("Our labs, our people", "Real benches, real people, one standard.", "Select a photo to enlarge it.")
    + MASONRY([("lab-bench-woman", "A bright bench in a QC lab"), ("inst-hplc", "HPLC systems running an overnight sequence"), ("lab-microscope-woman", "Microbiology reading plates"),
               ("lab-team-three", "Method transfer review between two sites"), ("lab-pipette-vials", "Sample preparation for assay"), ("room-clean-2", "A cleanroom before environmental monitoring"),
               ("lab-smile", "An analyst between runs"), ("inst-lcms", "LC-MS for nitrosamine screening"), ("lab-goggles", "Safety first, every day"),
               ("lab-plate-pink", "Plate-based potency assay"), ("lab-corridor", "A long instrument lab"), ("micro-petri-1", "Colonies on agar after incubation")])
    + f'<p class="cn">Stock photography for illustration. {ILL("Not our facilities yet")}</p>'
    + SH("A day in the life", "An analyst's day in Hyderabad.", "Composite and illustrative, built from how well-run QC labs actually work.")
    + '<div class="two"><div>' + TIMELINE([(t, "", d) for t, d in DAY]) + '</div><div>' + IMG("lab-analyst-pc", "Most of the day is careful, quiet work. That is the point.") + SCICARD("ananya") + '</div></div>'
    + SH("Next step", "Three ways to work with us.")
    + GRID([("Request a quote", "Tell us the product and the tests. A scientist replies within 4 business hours.", "/request-quote.html", "Get a quote"),
            ("See careers", "Analysts, microbiologists, QA and lab managers across four regions.", "/careers/index.html", "Open roles"),
            ("Partner with us", "Own a GMP lab? Start a confidential conversation.", "/partner-with-us.html", "Talk to us")]))

page("about/index", "Science you can sign your name to.",
     "We are a network of pharmaceutical testing labs with one standard, one team ethic and one promise: results you can defend.",
     about_body, img="lab-team-three", eyebrow="About PharmaCRO", nav="company",
     chips=[("1", "standard"), ("10", "planned sites"), ("4", "regions")])

# ---------------- leadership ----------------
LEAD = [("Ravi Shankar", "Operating Partner and Chief Executive", "lead-1", "Our job is to make thirty labs feel like one, without making any of them feel smaller.",
         "Twenty years in pharmaceutical services, most recently running a multi-site contract testing business. Started as a QC analyst; still reads chromatograms on Fridays.", "MSc Analytical Chemistry; MBA"),
        ("Claire Dubois", "Chief Financial Officer", "lead-2", "Discipline on price is how we keep our promise on quality.",
         "Finance leader across healthcare services buy-and-build platforms. Built integration playbooks for more than twenty acquisitions.", "Chartered Accountant (ACA)"),
        ("Dr Anjali Verma", "Chief Scientific Officer", "lead-4", "A method should transfer like a recipe, not like a rumour.",
         "Analytical scientist with a background in biologics characterisation and method lifecycle management under ICH Q14. Author on method transfer and comparability.", "PhD Pharmaceutical Analysis"),
        ("Helen Murphy", "Head of Quality", "sci-woman-5", "Inspection-ready is not an event. It is a Tuesday.",
         "Quality leader with experience of FDA, EMA and HPRA inspections at contract laboratories. Designs data integrity programmes that analysts can actually follow.", "BSc Microbiology; Qualified Person training"),
        ("Daniel Lee", "Head of Technology", "lead-5", "One LIMS, one data model, no spreadsheets in the critical path.",
         "Built validated laboratory software and client portals. Responsible for the LIMS, the portal and computerised system validation.", "BEng Computer Systems; GAMP 5 practitioner"),
        ("Samuel Owusu", "Head of Partnerships", "lead-3", "Every lab owner deserves a straight answer and a fair process.",
         "Leads conversations with lab founders. Background in healthcare M&amp;A and post-merger integration.", "MA Economics")]

lead_body = (
    ANSWER("PharmaCRO is led by an operating team with backgrounds in contract testing, quality, laboratory software and acquisitions. "
           "Each lab keeps its own lab head; the group team sets one standard and supports every site.")
    + PEOPLE([(n, r, im, q) for n, r, im, q, b, c in LEAD])
    + SH("Bios", "Experience and credentials.")
    + '<div class="co-bios">' + "".join(f'<div class="box reveal"><img src="/img/{im}.jpg" alt="" loading="lazy"><div><h3>{n}</h3><p class="mono-v">{r}</p><p>{b}</p><p class="cn">{c}</p></div></div>' for n, r, im, q, b, c in LEAD) + "</div>"
    + f'<p class="cn">{ILL("Illustrative profiles")} Names, photos, bios and credentials are placeholders until the leadership team is announced.</p>'
    + SH("Governance", "How decisions are made.")
    + GRID([("Board", "An independent chair and investor representatives oversee strategy, acquisitions and risk.", "", ""),
            ("Quality reports independently", "The Head of Quality reports to the CEO and has a direct line to the board. Quality can stop a release; nobody can overrule that.", "/quality/index.html", "Quality"),
            ("Lab heads", "Every site keeps a lab head accountable for its people, clients and inspections.", "/labs/index.html", "Our labs"),
            ("Speak up", "Anyone can raise a concern confidentially, including anonymously.", "/whistleblowing.html", "Whistleblowing")])
    + IMG("biz-team-laptops", "Group functions exist to make the labs' work easier, not to add layers."))

page("about/leadership", "The people accountable for every result.", "An operating team from contract testing, quality, laboratory software and acquisitions.",
     lead_body, img="biz-team-laptops", eyebrow="Leadership", crumbs=CO, nav="company")

# ---------------- our story ----------------
story_body = (
    ANSWER("We started PharmaCRO because pharmaceutical testing is essential, regulated and badly fragmented. Good labs are small and isolated; clients juggle many vendors. "
           "A network with one standard can be faster and more defensible than any single lab.")
    + SPLIT("lab-vial-dark", H2("The problem we kept seeing") + P(
        "A generic manufacturer sends release testing to one lab, stability to another and microbiology to a third. Each has a different report, a different portal and a different turnaround. When an inspector asks a question, three vendors have to answer it.",
        "Meanwhile, the owners of those labs work hard to keep accreditation, buy instruments and keep their best analysts. Many are approaching retirement with no clear succession plan."))
    + SPLIT("lab-team-three", H2("What we decided to do") + P(
        "Bring those labs together. Not by replacing them, but by giving them one LIMS, one set of SOPs, one quality system and one portal.",
        "Then a method validated in Hyderabad can run in Singapore next week, and a client sees every result in one place."), flip=True)
    + QUOTE("We are not trying to build the biggest lab. We are trying to build the most dependable network.", "Founding team (illustrative)")
    + SH("The journey", "How the network is planned to grow.")
    + HSCROLL(MILESTONES)
    + SH("What we will never do", "Three lines we will not cross.")
    + ICARDS([("shield", "Trade integrity for speed", "No turnaround promise justifies a shortcut on data integrity."),
              ("people", "Strip a lab of its identity", "Where it helps clients and staff, a lab keeps its name and its team."),
              ("doc", "Publish an unverified claim", "Every figure on this site is labelled until Quality and Legal verify it.")])
    + GALLERY(["city-hyderabad", "city-singapore", "city-leiden"], ["India first", "Then Southeast Asia", "Then Europe and the US"])
    + f'<p class="cn">{ILL("Planned journey")}</p>')

page("about/our-story", "Why we exist.", "Testing is essential, regulated and fragmented. We are bringing great independent labs into one standard.",
     story_body, img="lab-vial-dark", eyebrow="Our story", crumbs=CO, nav="company")

# ---------------- sustainability ----------------
sus_body = (
    ANSWER("Analytical labs use a lot of solvent, power and packaging. Our plan is to cut all three with green analytical chemistry: smaller columns and faster runs, "
           "solvent recycling, efficient stability chambers and reusable cold-chain packaging, reported against targets every year.")
    + ICARDS([("flask", "Less solvent per result", "Moving HPLC methods to UHPLC with smaller columns typically cuts mobile phase use substantially per injection. We will re-validate where needed under ICH Q14 lifecycle principles."),
              ("leaf", "Recycle and replace", "Acetonitrile recovery where it is safe and validated; substituting greener solvents in sample preparation where methods allow."),
              ("gauge", "Smarter chambers and freezers", "Stability chambers and ultra-low freezers run around the clock. Right-sizing, door discipline and heat recovery reduce their load."),
              ("truck", "Reusable cold-chain boxes", "Validated reusable shippers for routine courier lanes, collected on the next pick-up."),
              ("doc", "Paper out of the critical path", "Electronic records, e-signatures and portal delivery replace printed data packages."),
              ("people", "Safer labs", "Solvent reduction is also exposure reduction for the analysts who handle them every day.")])
    + BARS("Planned reduction targets by Year 3, against each lab's first full year", [("Solvent per reportable result", 30, "-30%"), ("Electricity per instrument hour", 20, "-20%"),
                                                                                       ("Single-use shipping boxes", 60, "-60%"), ("Printed pages", 90, "-90%")],
           "Targets are illustrative and will be set per site after a baseline year.")
    + SPLIT("lab-glassware", H2("Measured, not marketed") + P("We will publish a yearly sustainability note with each site's baseline, the changes made and the results, including where we missed.",
                                                              "Method changes for sustainability go through change control and client notification like any other change.") + ILL("Targets"))
    + STRIP(["lab-flasks-pour", "lab-glassware", "room-clean-1", "log-warehouse", "lab-cylinders"]))

page("sustainability", "Greener analytical chemistry.", "Less solvent, less energy and less packaging per result, measured site by site.",
     sus_body, img="lab-glassware", eyebrow="Sustainability", crumbs=CO, nav="company")

# ---------------- news ----------------
NEWS = [("21 Nov 2026", "Company", "PharmaCRO publishes its client website preview", "The preview shows the planned services, labs and quality approach. Figures are labelled until verified.", "lab-corridor"),
        ("14 Nov 2026", "Quality", "Group data integrity standard drafted", "A single ALCOA+ standard covering every planned site, ready for adoption as labs join.", "lab-analyst-pc"),
        ("03 Nov 2026", "Network", "India launch sites confirmed in the plan", "Hyderabad, Mumbai, Pune and Bengaluru form the first planned cluster.", "city-hyderabad"),
        ("20 Oct 2026", "Technology", "LIMS and portal design complete", "One data model for samples, methods, results and certificates across every lab.", "data-dashboard"),
        ("02 Oct 2026", "People", "Leadership roles defined", "Quality, technology and partnerships leads will report to the operating partner.", "biz-team-laptops")]
news_body = (
    '<div class="co-news">' + "".join(f'<article class="box reveal" style="--i:{i}"><img src="/img/{im}.jpg" alt="" loading="lazy"><div><p class="ey">{d} &middot; {c}</p><h3>{t}</h3><p>{x}</p></div></article>'
                                      for i, (d, c, t, x, im) in enumerate(NEWS)) + "</div>"
    + f'<p class="cn">{ILL("Illustrative announcements")} News items are placeholders until each announcement is approved.</p>'
    + SH("Press", "For journalists.", "Press enquiries reach a person within one business day.")
    + MAILFORM([("name", "Name", "text", True), ("email", "Email", "email", True), ("outlet", "Publication", "text", False), ("q", "Your question", "textarea", True)], "Press enquiry", "Send to the press team"))

page("news", "News", "Announcements and milestones from the network.", news_body, hero="plain", eyebrow="Company", nav="company")

# ---------------- careers ----------------
# slug, title, city, region, function, level, image, summary, day, requirements
ROLE = {
 "analytical-chemist-hyderabad": ("Analytical Chemist, HPLC", "Hyderabad", "India", "Analytical", "Analyst", "lab-pipette-vials",
    "Run assay, related substances and dissolution testing for small molecule release and stability.",
    ["Prepare standards and samples to SOP", "Run and monitor HPLC and dissolution sequences", "Process and peer-review chromatographic data", "Write clear, review-ready records"],
    ["MSc or BPharm/MPharm in chemistry or pharmaceutical sciences", "1 to 4 years of HPLC experience in a GMP lab", "Working knowledge of USP and IP general chapters", "Care for detail and data integrity"]),
 "microbiologist-pune": ("Microbiologist, Sterility and Endotoxin", "Pune", "India", "Microbiology", "Analyst", "micro-petri-2",
    "Perform sterility, endotoxin, bioburden and environmental monitoring testing for vaccines and injectables.",
    ["Sterility by membrane filtration in isolators", "LAL and recombinant factor C endotoxin assays", "Environmental monitoring sampling and trending", "Media preparation and growth promotion"],
    ["MSc Microbiology", "1 to 5 years in a GMP microbiology lab", "Aseptic technique and gowning qualification", "Familiarity with EU GMP Annex 1"]),
 "qa-specialist-dublin": ("QA Specialist, Data Integrity", "Dublin", "Ireland", "Quality", "Senior", "docs-papers",
    "Review data, audit trails and investigations, and help each site stay inspection-ready every day.",
    ["Review analytical data packages and audit trails", "Lead OOS and deviation investigation reviews", "Host client audits and support regulatory inspections", "Train analysts on ALCOA+ in practice"],
    ["Degree in a life science", "4+ years in QA for a GMP laboratory", "Experience with HPRA, EMA or FDA inspections", "Strong writing and calm under questioning"]),
 "biologics-scientist-bengaluru": ("Scientist, Biologics Characterisation", "Bengaluru", "India", "Biologics", "Scientist", "lab-instrument-load",
    "Develop and run charge, size, glycan and mass spectrometry methods for biosimilar comparability.",
    ["Run SEC, CE-SDS and icIEF", "Peptide mapping and intact mass by LC-MS", "Design comparability studies with clients", "Write method development reports"],
    ["PhD or MSc in biochemistry or analytical chemistry", "3+ years in protein analytics", "Hands-on LC-MS experience", "Clear communication with client scientists"]),
 "lab-manager-singapore": ("Lab Manager", "Singapore", "Singapore", "Operations", "Manager", "city-singapore",
    "Lead a growing biologics and stability lab: people, capacity, clients and inspections.",
    ["Plan capacity and turnaround across teams", "Coach analysts and scientists", "Own the site's quality metrics with QA", "Be the senior face of the lab for clients"],
    ["Degree in a relevant science", "8+ years in GMP laboratories, 3+ leading teams", "Experience of HSA or other regulator inspections", "Commercial awareness"]),
 "client-scientist-new-jersey": ("Client Scientist", "New Jersey", "United States", "Client science", "Senior", "biz-highfive",
    "Turn client questions into the right testing package, and stay with the project until the CoA is signed.",
    ["Scope projects with QC, CMC and regulatory teams", "Design test packages and timelines", "Coordinate across labs on one LIMS", "Explain results in plain language"],
    ["MSc or PhD in analytical sciences", "5+ years in a CRO or pharma QC/CMC role", "Broad knowledge of small molecules and biologics", "Enjoy talking to people"]),
}
assert set(ROLE) == set(ROLES)

LADDER = [("Analyst", "Run methods to SOP, learn instruments, build habits that survive inspection.", "₹4 to 7 L", "S$45 to 60k", "€38 to 48k", "$58 to 72k"),
          ("Senior Analyst", "Own complex methods, train new analysts, first peer reviewer.", "₹7 to 11 L", "S$58 to 75k", "€45 to 56k", "$70 to 86k"),
          ("Scientist", "Develop and validate methods, design studies, talk to clients.", "₹11 to 18 L", "S$72 to 95k", "€52 to 68k", "$85 to 110k"),
          ("Senior Scientist", "Lead technical areas, solve hard problems, mentor scientists.", "₹18 to 28 L", "S$90 to 120k", "€65 to 85k", "$105 to 140k"),
          ("Lab Manager", "Run a lab: people, capacity, quality metrics and clients.", "₹28 to 45 L", "S$115 to 150k", "€80 to 105k", "$130 to 170k"),
          ("Site Head", "Lead a site, its inspections and its growth.", "₹45 L+", "S$150k+", "€100k+", "$165k+")]
ladder = ('<div class="co-lad"><div class="co-lad-r" role="group" aria-label="Region for salary bands">'
          + "".join(f'<button type="button" class="ch" data-lr="{i}" aria-pressed="{"true" if i == 0 else "false"}">{r}</button>' for i, r in enumerate(["India", "Singapore", "Europe", "United States"]))
          + '</div><ol>' + "".join(f'<li class="co-step reveal" style="--i:{i}"><i>{i + 1}</i><div><h3>{t}</h3><p>{d}</p><b class="co-pay" data-p="{html.escape(json.dumps([a, b, c, e]))}">{a}</b></div></li>'
                                     for i, (t, d, a, b, c, e) in enumerate(LADDER)) + "</ol>"
          + f'<p class="cn">Annual base salary bands. {ILL("Illustrative bands")} Final bands are published with each role once approved.</p></div>')

roles_list = ('<div class="co-rf" role="group" aria-label="Filter roles">'
              + '<label><span>Location</span><select data-rf="loc"><option value="">All</option>' + "".join(f"<option>{c}</option>" for c in sorted({r[1] for r in ROLE.values()})) + "</select></label>"
              + '<label><span>Function</span><select data-rf="fn"><option value="">All</option>' + "".join(f"<option>{c}</option>" for c in sorted({r[3] for r in ROLE.values()})) + "</select></label>"
              + '<label><span>Level</span><select data-rf="lv"><option value="">All</option>' + "".join(f"<option>{c}</option>" for c in sorted({r[4] for r in ROLE.values()})) + "</select></label>"
              + '<span class="co-rc" aria-live="polite"></span></div><div class="co-roles">'
              + "".join(f'<a class="co-role reveal" href="/careers/{s}.html" data-loc="{r[1]}" data-fn="{r[3]}" data-lv="{r[4]}"><img src="/img/{r[5]}.jpg" alt="" loading="lazy"><div><h3>{r[0]}</h3><p>{r[6]}</p>'
                        f'<small>{ICON("pin")} {r[1]}, {r[2]} &middot; {r[3]} &middot; {r[4]}</small></div></a>' for s, r in ROLE.items())
              + '</div><p class="nores co-rn" hidden>No roles match. Join the talent network below and we will tell you when one opens.</p>')

apply_form = (f'<form class="co-apply" data-mail="{MAIL}" novalidate><ol class="co-dots" aria-label="Progress"><li class="on">You</li><li>Questions</li><li>Video</li><li>Send</li></ol>'
              '<fieldset class="co-as on"><legend>About you</legend><label><span>Name</span><input name="name" autocomplete="name" required></label>'
              '<label><span>Email</span><input name="email" type="email" autocomplete="email" required></label>'
              '<label><span>LinkedIn profile or CV link</span><input name="cv" type="url" placeholder="https://"></label>'
              '<label><span>Role</span><select name="role" required><option value="">Choose</option>' + "".join(f"<option>{r[0]}, {r[1]}</option>" for r in ROLE.values()) + '<option>Talent network (no specific role)</option></select></label></fieldset>'
              '<fieldset class="co-as"><legend>Three short questions</legend><label><span>Which instruments or techniques have you used most?</span><textarea name="q1" rows="2" required></textarea></label>'
              '<label><span>Tell us about a result you questioned and what you did.</span><textarea name="q2" rows="3" required></textarea></label>'
              '<label><span>When could you start?</span><input name="q3" required></label></fieldset>'
              '<fieldset class="co-as"><legend>Optional video intro</legend><p>If you like, record a 60-second hello and paste a link (Loom, Drive, YouTube unlisted). It is optional and never counts against you.</p>'
              '<label><span>Video link</span><input name="video" type="url" placeholder="https://"></label></fieldset>'
              '<fieldset class="co-as"><legend>Check and send</legend><p>Your email app will open with your answers. Attach your CV if you did not share a link. You will get a status update by email at every stage, and you can withdraw with one reply.</p>'
              '<label class="chk"><input type="checkbox" name="consent" required> <span>I agree that PharmaCRO may keep my application for 12 months. <a href="/privacy.html">Privacy</a>.</span></label></fieldset>'
              '<div class="co-an"><button type="button" class="btn o" data-ab hidden>Back</button><button type="button" class="btn" data-an>Next</button><button type="submit" class="btn" data-ag hidden>Send application</button></div>'
              '<p class="co-err" role="alert"></p><div class="co-ok" hidden tabindex="-1"><h3>Thank you. That took courage and time.</h3><p>Your email app has opened with your application. Press send, and a real person from the lab will reply within five business days.</p></div></form>')

careers_body = (
    ANSWER("We hire analysts, microbiologists, QA specialists, scientists and lab managers across India, Southeast Asia, Europe and the US. "
           "Expect real training, real instruments, a visible career ladder and pay bands published before you apply.")
    + SH("Why join", "The things good scientists ask about first.")
    + ICARDS([("flask", "Instrument exposure", "HPLC, LC-MS, ICP-MS, CE, flow cytometry and more, across a network, not one bench."),
              ("doc", "Training budget", "A yearly learning budget per person, plus internal certification on every method you run."),
              ("people", "Mentoring", "Every analyst has a named mentor one level up and a review twice a year."),
              ("gauge", "A clear ladder", "Six steps from analyst to site head, with what each step needs written down."),
              ("shield", "Safety", "Solvent reduction, proper extraction and a culture where stopping work is praised."),
              ("globe", "Relocation support", "Move between sites in four regions, with help on visas and housing where needed.")], 3)
    + f'<p class="cn">{ILL("Planned benefits")}</p>'
    + GALLERY(["lab-smile", "lab-microscope-woman2", "lab-team-three"], ["Analysts", "Microbiology", "Method transfer review"])
    + SH("Career paths", "From analyst to site head.", "Scroll to build the ladder; choose a region to see salary bands.") + ladder
    + SH("Open roles", "Find your next bench.") + roles_list
    + BAND("lab-bench-woman", "Do the science medicines depend on.", "Every batch you release reaches a patient.")
    + '<div class="two" id="apply"><div>' + SH("Apply", "Apply in under three minutes.") + apply_form + '</div><div>'
    + SH("Not ready yet?", "Join the talent network.") + MAILFORM([("name", "Name", "text", True), ("email", "Email", "email", True), ("area", "Area of interest", ["Analytical chemistry", "Microbiology", "Biologics", "Quality", "Operations", "Client science"], True)], "Talent network", "Join the network", "Your email app has opened. Press send and we will tell you when a matching role opens.")
    + SH("Refer a friend", "Know someone great?") + MAILFORM([("you", "Your name", "text", True), ("friend", "Their name", "text", True), ("contact", "Their email or LinkedIn", "text", True), ("why", "Why they would be good", "textarea", False)], "Employee referral", "Send referral", "Your email app has opened. Press send. Referral bonuses are paid after the new colleague's probation.")
    + '</div></div>')

page("careers/index", "Do the science that medicines depend on.", "Analysts, scientists, QA and lab managers across four regions, with training, a clear ladder and published pay bands.",
     careers_body, img="lab-smile", eyebrow="Careers", nav="company", cta=False,
     chips=[("6", "open roles (illustrative)"), ("4", "regions"), ("6", "career steps")],
     hb='<a class="btn big" href="#apply">Apply in 3 minutes</a> <a class="btn o big" href="#main">See open roles</a>')

for s, (t, city, country, fn, lv, im, summ, day, req) in ROLE.items():
    ld = {"@context": "https://schema.org", "@type": "JobPosting", "title": t, "description": f"Illustrative role at a planned PharmaCRO laboratory. {summ}",
          "datePosted": "2026-11-21", "employmentType": "FULL_TIME", "hiringOrganization": {"@type": "Organization", "name": BRAND, "sameAs": DOMAIN},
          "jobLocation": {"@type": "Place", "address": {"@type": "PostalAddress", "addressLocality": city, "addressCountry": country}}}
    body = (ANSWER(f"{summ} This is a {lv.lower()}-level {fn.lower()} role at our planned {city} lab. {ILL('Illustrative role')}")
            + '<div class="two"><div>' + H2("What you will do") + TICKLIST(day) + H2("What you bring") + TICKLIST(req)
            + H2("What we offer") + UL(["Published salary band before interview", "Yearly training budget and method certifications", "A named mentor", "Health cover and paid leave in line with local practice", "Relocation support between sites"])
            + '</div><div>' + IMG(im, f"{city}: illustrative photo")
            + H3("A day in this role") + TIMELINE([("Morning", "", day[0]), ("Midday", "", day[1]), ("Afternoon", "", day[2]), ("End of day", "", day[3])]) + '</div></div>'
            + SH("Apply", "Apply in under three minutes.", "Your email app opens with your details; attach your CV and press send.")
            + MAILFORM([("name", "Name", "text", True), ("email", "Email", "email", True), ("cv", "LinkedIn or CV link", "url", False), ("why", "Why this role, in two or three lines", "textarea", True),
                        ("consent", "I agree that PharmaCRO may keep my application for 12 months.", "checkbox", True)], f"Application: {t}, {city}", "Send application",
                       "Your email app has opened. Press send and a person from the lab replies within five business days.")
            + f'<p><a href="/careers/index.html">&lsaquo; All roles</a></p>')
    page(f"careers/{s}", t, f"{city}, {country} &middot; {fn} &middot; {lv}", body, img=im, eyebrow="Careers", crumbs=[("Careers", "/careers/index.html")], nav="company",
         jsonld=[ld], cta=False, hb='<a class="btn big" href="#main">Read the role</a>')

# ---------------- partner with us ----------------
partner_form = (f'<form class="co-pf" data-mail="{MAIL}" novalidate><div class="co-pbar"><i></i></div><div class="co-pv"><div class="co-pt">'
                '<fieldset class="co-ps"><legend>1 of 3 &middot; About you</legend><label><span>Your name</span><input name="name" autocomplete="name" required></label>'
                '<label><span>Lab name</span><input name="lab" required></label><label><span>City</span><input name="city" required></label></fieldset>'
                '<fieldset class="co-ps"><legend>2 of 3 &middot; Your lab</legend><label><span>Main services</span><textarea name="services" rows="3" placeholder="e.g. small molecule QC, stability, microbiology" required></textarea></label>'
                '<label><span>Approximate annual revenue (optional)</span><select name="revenue"><option value="">Prefer not to say</option><option>Under $1M</option><option>$1M to $3M</option><option>$3M to $8M</option><option>Over $8M</option></select></label></fieldset>'
                '<fieldset class="co-ps"><legend>3 of 3 &middot; How to reach you</legend><label><span>Preferred contact</span><select name="contact" required><option value="">Choose</option><option>Phone call</option><option>Email</option><option>Video call</option><option>In person</option></select></label>'
                '<label><span>Phone or email</span><input name="reach" required></label><p class="cn">Your enquiry goes to two senior people only. For extra privacy, ask for our PGP key in your first email.</p></fieldset>'
                '</div></div><div class="co-an"><button type="button" class="btn o" data-pb hidden>Back</button><button type="button" class="btn" data-pn>Next</button><button type="submit" class="btn" data-pg hidden>Start a confidential conversation</button></div>'
                '<p class="co-err" role="alert"></p><div class="co-ok" hidden tabindex="-1"><h3>Thank you. This stays between us.</h3><p>Your email app has opened. Press send and one of two senior people will acknowledge within one business day. No automated marketing, ever.</p></div></form>')

partner_body = (
    ANSWER("We partner with founder-led, GMP-accredited pharmaceutical testing labs. Owners get a fair valuation and a clear process; staff and clients get continuity; "
           "the lab gets the network's systems, instruments and clients. A typical process takes three to six months.")
    + SPLIT("lab-smile", H2("We know what you built") + P("Accreditation that took years. Clients who trust your signature. Analysts you trained yourself.",
                                                            "We are not here to replace that. We are here to give it a bigger future, and to give you choices about yours."))
    + SH("What we offer", "Four promises.")
    + ICARDS([("gauge", "Fair valuation, clear process", "We explain how we value a lab, and we put the terms in writing early."),
              ("people", "Continuity for staff and clients", "Your team stays. Your clients keep their contacts. Where it helps, your lab keeps its name."),
              ("globe", "The network behind you", "Shared LIMS, portal, instruments, method transfer and clients from across four regions."),
              ("spark", "Retention and earn-out options", "Structures that reward you and your key people for the growth you help create.")], 2)
    + SH("What we look for", "Five signs of a great fit.")
    + '<div class="two"><div>' + TICKLIST(["GMP accredited (ISO/IEC 17025 and/or a GMP inspection history)", "EBITDA margin of 15 percent or higher", "Revenue of $1 million to $8 million a year",
                                           "A clean inspection history over the last three years", "A strong team that wants to stay"]) + '</div><div>' + IMG("lab-team-three", "") + '</div></div>'
    + SH("How it works", "Five steps, three to six months.")
    + STEPLINE([("Confidential call", "An hour with a senior person. No documents needed. We listen first."),
                ("NDA", "Signed online in minutes, before any information is shared."),
                ("Information exchange", "A short request list shared in a secure room, at your pace."),
                ("Offer and diligence", "A written offer, then focused diligence on quality, finance and people."),
                ("Close and integrate", "A 100-day plan agreed with you: LIMS, SOPs and portal, without disrupting clients.")])
    + SH("Owner stories", "In their own words.")
    + '<div class="co-quotes" aria-live="polite">' + "".join(f'<div class="co-q{" on" if i == 0 else ""}">{QUOTE(q, w)}</div>' for i, (q, w) in enumerate([
        ("This space is reserved for owners who have joined the network. We will not invent their words.", "Owner stories appear once real partnerships close"),
        ("When they do, you will be able to call them yourself. Ask us for an introduction.", "Our promise"),
        ("Until then, the best evidence is how we treat you in the first conversation.", "The partnerships team")])) + "</div>"
    + f'<p class="cn">{ILL("No owner stories yet")}</p>'
    + SH("Start a confidential conversation", "Three short steps.") + '<div class="two"><div>' + partner_form + '</div><div>' + IMG("biz-highfive", "Discreet, human follow-up. Never automated marketing.") + '</div></div>')

page("partner-with-us", "You built a great lab. Let's make it greater.",
     "We partner with founder-led pharmaceutical labs. You keep your standards. We bring scale, systems and a bigger future for your team.",
     partner_body, img="lab-smile", eyebrow="For lab owners", nav="company", cta=False,
     hb='<a class="btn big" href="#main">How it works</a> <a class="btn o big" href="mailto:' + MAIL + '?subject=Confidential%20conversation">Email us confidentially</a>')

# ---------------- investors ----------------
inv_body = (
    ANSWER("PharmaCRO plans to acquire small GMP-accredited testing labs, run them on one LIMS and one quality system, and grow them into a full-menu network. "
           "Testing is required by regulators for every batch, so demand is recurring. Eligible investors can request access to the data room through Investor Labs.")
    + SH("The thesis", "Three sentences.")
    + OL(["Pharmaceutical analytical testing is non-discretionary: every batch, every facility and every reformulation needs it.",
          "The market is fragmented into many small accredited labs with no scale, no shared technology and limited succession options.",
          "A network with one standard can serve multinational clients that single labs cannot, and improve margins through shared systems."])
    + SPLIT("pharma-team", H2("The market") + P("The company cites global pharmaceutical analytical testing outsourcing of about $8 billion today, with an estimate of $15 billion by 2030. "
                                                   "These are company-cited figures, not independent forecasts.") + ILL("Company estimate"))
    + SH("Access flow", "How data room access works.")
    + STEPLINE([("Request", "Submit a request through Investor Labs."), ("KYC and eligibility", "Identity and investor eligibility checks for your jurisdiction."),
                ("NDA", "E-signed non-disclosure agreement."), ("Approval", "The team approves access and assigns a contact."), ("MFA login", "Secure, watermarked viewing with an activity log.")])
    + SH("In the data room", "What approved investors can see.")
    + GRID([("Investor memorandum", "The full plan, assumptions and risks.", "", ""), ("Financial model", "Operating build by lab and region.", "", ""),
            ("KPIs and reports", "Quarterly reporting once operations begin.", "", ""), ("Q&amp;A log", "Questions and answers with response times.", "", "")])
    + '<p><a class="btn big" href="https://investorlabs.eliteleadgrow.com/inv-request.html">Request access via Investor Labs</a> <a class="btn o big" href="https://investorlabs.eliteleadgrow.com/pharma.html">Read the PharmaCRO overview</a></p>'
    + CALL("This page is not an offer of securities or a solicitation of any offer. Access to investment materials is limited to verified, eligible investors in jurisdictions where it is legally permitted. "
           "Forward-looking statements are plans, not forecasts, and actual results may differ materially. No return, valuation or performance is promised."))

page("investors", "Investors", "The thesis, the market and how to request data room access.", inv_body, img="corp-skyline", eyebrow="Investors", nav="company", cta=False,
     hb='<a class="btn big" href="https://investorlabs.eliteleadgrow.com/inv-request.html">Request access</a>')
