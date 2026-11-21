"""Conversion, support and legal/utility pages. Blueprint 4.11 and 6. Imported last in the full build, so the sitemap sees every page."""
from ph import *
from img_meta import CREDITS

# ---------------- request a quote ----------------
rq_body = (
    '<div class="two"><div>' + RFQ() + '</div><div>'
    + SH("What happens next", "From your request to a signed quote.")
    + STEPLINE([("Instant", "A reference number and a summary email (from your own mail app) with everything you entered."),
                ("Within 4 business hours", "A named scientist replies with questions or a quote, routed to the nearest lab."),
                ("Usually within 1 day", "Your quote arrives with turnaround dates per tier and the MSA option."),
                ("When you accept", "We open your portal account and send the sample submission guide.")])
    + SCICARD("arjun")
    + '</div></div>'
    + SH("Questions", "Before you send.")
    + FAQS([("How long does the form take?", "<p>About 90 seconds. Only your name and email are required; everything else helps us quote faster.</p>"),
            ("Is the form sent automatically?", "<p>Not yet. During the preview it opens your email app with every detail filled in; you press send. A portal-based form replaces this at launch.</p>"),
            ("Can I attach a specification?", "<p>Yes. Choose the file so we know to expect it, then attach it to the email before sending.</p>"),
            ("What if I am not sure which tests I need?", "<p>Describe the product and the market. A scientist will propose a package, or <a href='/book-a-call.html'>book a call</a>.</p>"),
            ("Do you sign NDAs before quoting?", "<p>Yes. Ask in the details box and we will send our standard mutual NDA first.</p>"),
            ("What does the turnaround guarantee cover?", f"<p>If we miss the date promised in the quote, the fee for that test is credited. {ILL('Subject to commercial approval')}</p>")], "rq"))
page("request-quote", "Get a quote in 90 seconds.", "Four short steps. A scientist replies within 4 business hours with questions or a price.",
     rq_body, hero="plain", eyebrow="Request a quote", cta=False, hb="")

# ---------------- book a call ----------------
SPEC = [("small", "Small molecule", "ananya"), ("bio", "Biologics", "elena"), ("mrna", "mRNA and vaccines", "kenji"), ("cgt", "Cell and gene therapy", "sara"), ("reg", "Regulatory and quality", "helen")]
TZ = {"Hyderabad": ("Asia/Kolkata", "IST"), "Singapore": ("Asia/Singapore", "SGT"), "Leiden": ("Europe/Amsterdam", "CET"), "Cambridge": ("Europe/London", "UK"), "Dublin": ("Europe/Dublin", "Irish")}
book_body = (
    ANSWER("Pick a specialty and a time. You will talk to a scientist in that field for 30 minutes, not a salesperson. Afterwards you get a summary with a recommended package and a one-click quote.")
    + f'<div class="co-book" data-mail="{MAIL}"><div class="co-spec" role="group" aria-label="Specialty">'
    + "".join(f'<button type="button" class="co-sp" aria-pressed="{"true" if i == 0 else "false"}" data-n="{html.escape(SCI[k][0])}" data-tz="{TZ[SCI[k][4]][0]}" data-tzn="{SCI[k][4]}" data-spec="{n}">'
              f'<img src="/img/{SCI[k][3]}.jpg" alt="" loading="lazy"><b>{n}</b><span>{SCI[k][0]} &middot; {SCI[k][4]}</span></button>' for i, (key, n, k) in enumerate(SPEC))
    + '</div><div class="co-cal"><p class="co-tzl" aria-live="polite"></p><div class="co-grid" role="grid" aria-label="Available slots"></div></div>'
    + '<form class="co-pre" novalidate><h3>A few questions to make the call useful</h3><label><span>Name</span><input name="name" autocomplete="name" required></label>'
    + '<label><span>Work email</span><input name="email" type="email" autocomplete="email" required></label>'
    + '<label><span>Product and stage</span><input name="product" placeholder="e.g. biosimilar adalimumab, Phase 3" required></label>'
    + '<label><span>What would make this call a success?</span><textarea name="goal" rows="3"></textarea></label>'
    + '<p class="co-sel">No time selected yet.</p><button class="btn" type="submit">Request this time</button><p class="co-err" role="alert"></p>'
    + '<div class="co-ok" hidden tabindex="-1"><h3>Requested. Here is your prep checklist.</h3><ul><li>Your specification or test list</li><li>Target markets and regulators</li><li>Batch or sample numbers and timing</li></ul>'
    + '<p>Your email app has opened with the request; press send and the scientist confirms by reply. <a href="#" class="co-ics" download="pharmacro-call.ics">Add to calendar (.ics)</a></p></div></form></div>'
    + f'<p class="cn">Availability is simulated during the preview. {ILL("Demo calendar")}</p>')
page("book-a-call", "Talk to a scientist.", "Thirty minutes with a specialist in your molecule type. Pick a time that suits you.",
     book_body, img="lab-team-three", eyebrow="Book a call", cta=False, hb='<a class="btn big" href="#main">Pick a time</a>')

# ---------------- submit samples ----------------
sub_body = (
    ANSWER("After you accept a quote, register your samples here. You get a sample ID, a printable packing list and label previews, then choose a courier. "
           "We photograph and temperature-check every box on arrival and post a Received status within hours.")
    + f'<div class="co-wz" data-mail="{MAIL}"><ol class="co-dots" aria-label="Progress"><li class="on">Quote lines</li><li>Batch</li><li>Hazard and storage</li><li>Labels and courier</li></ol>'
    + '<fieldset class="co-ws on"><legend>Which quote lines are you sending?</legend><label><span>Quote reference</span><input name="quote" placeholder="e.g. Q-26-1142" required></label>'
    + '<div class="picks">' + "".join(f'<label class="pick sm"><input type="checkbox" name="line" value="{s[1]}"><span>{ICON(s[5])}{s[1]}</span></label>' for s in SERVICES) + '</div></fieldset>'
    + '<fieldset class="co-ws"><legend>Batch details</legend><div class="rq-g"><label><span>Product name</span><input name="product" required></label><label><span>Batch or lot number</span><input name="batch" required></label>'
    + '<label><span>Number of containers</span><input name="n" type="number" min="1" value="3" required></label><label><span>Manufacture date</span><input name="mfd" type="date"></label></div>'
    + '<label><span>CoA or protocol (optional)</span><input type="file" name="file" accept=".pdf,.docx,.xlsx"></label></fieldset>'
    + '<fieldset class="co-ws"><legend>Hazard and storage</legend><label><span>Storage condition</span><select name="storage" required><option value="">Choose</option><option>Ambient (15 to 25 °C)</option><option>Refrigerated (2 to 8 °C)</option><option>Frozen (−20 °C)</option><option>Ultra-low (−70 °C or below)</option></select></label>'
    + '<label><span>Hazard class</span><select name="hazard" required><option value="">Choose</option><option>Not hazardous</option><option>Potent compound (OEB 4 or 5)</option><option>Biological material (UN3373)</option><option>Flammable or toxic</option><option>Genetically modified organism</option></select></label>'
    + '<label class="chk"><input type="checkbox" name="sds" required> <span>I will include a safety data sheet or hazard statement in the box.</span></label></fieldset>'
    + '<fieldset class="co-ws"><legend>Labels, packing list and courier</legend><div class="co-out"></div>'
    + '<label><span>Courier option</span><select name="courier"><option>PharmaCRO-arranged cold-chain courier (recommended)</option><option>PharmaCRO-arranged ambient courier</option><option>I will arrange my own courier</option></select></label>'
    + '<p class="cn">Label codes are 2D-code-style previews for layout only; the real scannable labels are generated by the portal at launch.</p></fieldset>'
    + '<div class="co-an"><button type="button" class="btn o" data-wb hidden>Back</button><button type="button" class="btn" data-wn>Next</button><button type="button" class="btn" data-wp hidden>Print packing list</button><button type="button" class="btn o" data-wm hidden>Email this to the lab</button></div><p class="co-err" role="alert"></p></div>'
    + SH("Shipping and cold chain", "Get it here in the state you sent it.")
    + ICARDS([("truck", "Courier options", "Cold-chain couriers with data loggers on every refrigerated or frozen shipment; ambient lanes for stable products."),
              ("clock", "Receiving hours", "Monday to Friday 08:00 to 18:00 local time, Saturday by arrangement. Critical-tier samples are received around the clock."),
              ("doc", "Customs help", "Commercial invoice templates, HS code guidance and import permits for biological material, prepared with you.")])
    + SH("Exceptions", "If something is wrong when the box arrives.")
    + P("Damaged, out of temperature or missing paperwork? You get an alert with photos and the logger trace, and a one-click choice: proceed, hold or resend. Nothing is tested until you decide.")
    + f'<div class="box co-sheet" id="sheet"><h3>Sample submission sheet</h3><p>A spreadsheet template with one row per container: sample ID, product, batch, storage, tests and hazard.</p><button type="button" class="btn" data-csv>Download the sample submission sheet (.csv)</button></div>'
    + GALLERY(["log-warehouse", "log-plane", "lab-sample-rack"], ["Receipt and photo log", "Cold-chain lanes", "Into the LIMS within hours"]))
page("submit-samples", "Submit samples.", "Register samples, print labels and a packing list, and book a courier in a few minutes.",
     sub_body, img="log-warehouse", eyebrow="Submit samples", cta=False, hb='<a class="btn big" href="#main">Start the wizard</a> <a class="btn o big" href="#sheet">Download the sheet</a>')

# ---------------- contact ----------------
ROUTES = [("sales", "New work and quotes", [("name", "Name", "text", True), ("email", "Work email", "email", True), ("company", "Company", "text", False), ("msg", "What do you need tested?", "textarea", True)]),
          ("client", "Existing clients", [("name", "Name", "text", True), ("email", "Email", "email", True), ("sample", "Sample or project ID", "text", False), ("msg", "How can we help?", "textarea", True)]),
          ("careers", "Careers", [("name", "Name", "text", True), ("email", "Email", "email", True), ("msg", "Your question", "textarea", True)]),
          ("media", "Media", [("name", "Name", "text", True), ("email", "Email", "email", True), ("outlet", "Publication", "text", False), ("msg", "Your question", "textarea", True)]),
          ("partner", "Lab owners and partners", [("name", "Name", "text", True), ("reach", "Phone or email", "text", True), ("msg", "Tell us a little about your lab (optional)", "textarea", False)]),
          ("speak", "Whistleblowing", [("msg", "What would you like to report? You can stay anonymous.", "textarea", True), ("reach", "How to reach you (optional)", "text", False)])]
contact_body = (
    ANSWER("Choose who you need and the right form appears. Sales and existing clients get a scientist's reply within 4 business hours; everyone else within one business day.")
    + '<div class="co-routes" role="tablist" aria-label="Who do you need?">'
    + "".join(f'<button type="button" role="tab" class="ch" aria-selected="{"true" if i == 0 else "false"}" aria-pressed="{"true" if i == 0 else "false"}" data-rt="{k}">{t}</button>' for i, (k, t, f) in enumerate(ROUTES)) + "</div>"
    + "".join(f'<div class="co-rp" data-rp="{k}"{"" if i == 0 else " hidden"}>' + MAILFORM(f, f"Contact: {t}", "Send") + (f'<p class="cn">For full whistleblowing options see <a href="/whistleblowing.html">the speak-up page</a>.</p>' if k == "speak" else "") + "</div>"
              for i, (k, t, f) in enumerate(ROUTES))
    + SH("Regional teams", "Call the team nearest you.")
    + '<div class="co-reg">' + "".join(f'<div class="box reveal"><img src="/img/{im}.jpg" alt="" loading="lazy"><h3>{r}</h3><p><a href="tel:{t}">{n}</a></p><p class="cn">[Office address, {c}] {ILL("Placeholder")}</p></div>'
                                         for (r, n, t), im, c in zip(PHONES, ["city-hyderabad", "city-singapore", "city-amsterdam", "city-newyork"], ["Hyderabad", "Singapore", "Leiden", "New Jersey"])) + "</div>"
    + P(f"WhatsApp Business: [number at launch] {ILL('Placeholder')} &middot; Email: <a href='mailto:{MAIL}'>{MAIL}</a>")
    + SH("Callback", "Prefer that we call you?")
    + MAILFORM([("name", "Name", "text", True), ("phone", "Phone with country code", "tel", True), ("when", "Best time", ["Morning", "Midday", "Afternoon", "Evening"], True)], "Callback request", "Request a callback",
               "Your email app has opened. Press send and we will call at the time you chose, in your time zone.")
    + MAP("contact-map"))
page("contact", "Every route to a human.", "Sales, existing clients, careers, media, lab owners and whistleblowing: choose and we show the right form.",
     contact_body, img="biz-team-laptops", eyebrow="Contact", cta=False, hb="")

# ---------------- support ----------------
ARTS = [("How do I track a sample?", "Open the portal, or use the lookup on this page with your sample ID (format PC-YY-NNNN)."),
        ("Where is my CoA?", "Released CoAs are in the portal under Results. They are e-signed PDFs with a hash you can verify."),
        ("My samples arrived warm. What now?", "You will get an exception alert with the logger trace and photos. Choose proceed, hold or resend."),
        ("How do I add a colleague to the portal?", "Portal admins can invite users under Team; roles are QC, QA, procurement and read-only."),
        ("Can I get interim data?", "Yes, on request, watermarked 'not final' until QA approval."),
        ("What happens if there is an OOS result?", "The responsible scientist opens a thread with you the same day, and the investigation follows our OOS SOP."),
        ("How do I change a test after submission?", "Message the project scientist before analysis starts; changes after start may need a revised quote."),
        ("How do I request an audit?", "Choose a lab and dates; a quality lead confirms within 48 hours and opens a secure document exchange."),
        ("What file formats do you accept for specifications?", "PDF, DOCX and XLSX."),
        ("How are invoices sent?", "Through the portal and by email, referencing your PO and quote.")]
support_body = (
    ANSWER("Look up a sample, search the help articles or open a ticket. A person replies to tickets within 4 business hours for clients.")
    + '<div class="two"><div class="box"><h3>Sample status lookup</h3><form class="co-look"><label><span>Sample ID</span><input placeholder="e.g. PC-24-0918" autocomplete="off"></label><button class="btn" type="submit">Look up</button></form>'
    + '<div class="co-lr" aria-live="polite"></div><p class="cn">Demo with sample data. Try PC-24-0918 to PC-24-0922.</p></div>'
    + '<div class="box"><h3>Search help articles</h3><label><span class="vh">Search</span><input type="search" class="co-hs" placeholder="Try: CoA, warm, audit"></label>'
    + '<div class="co-hl">' + "".join(f'<details class="acc"><summary>{q}</summary><div><p>{a}</p></div></details>' for q, a in ARTS) + '</div><p class="nores co-hn" hidden>No article matches. Open a ticket below.</p></div></div>'
    + SH("Open a ticket", "A person reads every one.")
    + MAILFORM([("name", "Name", "text", True), ("email", "Email", "email", True), ("sample", "Sample or project ID (if any)", "text", False),
                ("prio", "Priority", ["Question", "Something is blocking a release", "Urgent: batch on hold"], True), ("msg", "What happened?", "textarea", True)], "Support ticket", "Open ticket",
               "Your email app has opened. Press send. Client tickets get a reply within 4 business hours; urgent ones by phone.")
    + f'<p>Prefer chat? Use <b>Ask the Lab</b> at the bottom right, or call {PHONES[0][1]}.</p>')
page("support", "Support", "Sample lookup, help articles and tickets read by people.", support_body, img="lab-analyst-pc", eyebrow="Support", cta=False, hb="")

# ---------------- status ----------------
status_body = (
    ANSWER("The network is pre-launch, so no lab is processing client samples yet. This page shows how status will be reported at launch: per lab, per courier lane, with maintenance and incident history.")
    + '<div class="co-stat">' + "".join(f'<div class="box co-sr"><i class="co-dot pre"></i><div><b>{l[1]}</b><span>{l[2]} &middot; planned {l[6]}</span></div><em>Pre-launch</em></div>' for l in LABS) + "</div>"
    + '<p class="co-legend"><span><i class="co-dot ok"></i>Operating</span><span><i class="co-dot amb"></i>Degraded or delays</span><span><i class="co-dot red"></i>Outage</span><span><i class="co-dot pre"></i>Pre-launch</span></p>'
    + SH("Courier lanes", "Delays we know about.") + T(["Lane", "Status", "Note"], [["India domestic cold chain", "Pre-launch", "Lanes contracted before the first site opens"], ["ASEAN to Singapore", "Pre-launch", "&mdash;"], ["EU to Leiden / Dublin", "Pre-launch", "&mdash;"], ["US to New Jersey", "Pre-launch", "&mdash;"]])
    + SH("Planned maintenance", "Scheduled in advance, announced 7 days ahead.") + P("None scheduled.")
    + SH("Incident history", "Every incident, with a plain-language cause.") + P("No incidents. History starts when the first lab goes live.")
    + MAILFORM([("email", "Email", "email", True)], "Status updates subscription", "Subscribe to status updates", "Your email app has opened. Press send to subscribe.")
    + f'<p class="cn">The header chip "Demo status &middot; avg TAT 4.2 d" uses demo data. {ILL("Demo")}</p>')
page("status", "Network status", "Lab operations, courier lanes, maintenance and incidents.", status_body, hero="plain", eyebrow="Status", cta=False, hb="")

# ---------------- legal ----------------
DRAFT = CALL("Draft pending legal review. This text describes our intended practice and will be finalised by counsel before launch.")
LEG = dict(hero="plain", eyebrow="Legal", cta=False, hb="")

page("privacy", "Privacy policy", "What we collect, why, and your rights.", DRAFT + P(
    "<b>Who we are.</b> PharmaCRO, a planned network of pharmaceutical testing laboratories and part of the Investor Labs group. Contact: " + f"<a href='mailto:{MAIL}'>{MAIL}</a>.",
    "<b>What we collect.</b> Only what you type into a form, which during the preview is sent by your own email app, not by this website. We do not run advertising trackers.",
    "<b>Local settings.</b> Your region, theme, cookie choice and the product type you chose are stored in your browser's local storage, never sent to us.",
    "<b>Why.</b> To answer your request, prepare quotes, run testing and meet regulatory record-keeping duties.",
    "<b>Lawful basis.</b> Contract, legitimate interests and legal obligation under GDPR, the UK GDPR, India's DPDP Act 2023 and Singapore's PDPA, as applicable.",
    "<b>Retention.</b> Enquiries for 24 months; client records for the period your contract and regulators require.",
    "<b>Your rights.</b> Access, correction, deletion, objection and portability. Email us; we reply within one month.",
    "<b>Transfers.</b> Where data moves between regions, we use standard contractual clauses or equivalent safeguards.",
    "<b>Candidates.</b> Applications are kept for 12 months unless you ask us to delete them sooner."), **LEG)

page("terms", "Terms of use", "The rules for using this website, how we label claims, and image credits.", DRAFT + P(
    "This website gives general information about planned services. It is not regulatory, legal or medical advice, and no contract is formed until a written quote is accepted.",
    "Quotes, turnaround commitments and fee credits apply only as written in a signed quote or master service agreement.")
    + f'<section id="preview">{H2("How we label claims")}' + P(
        "PharmaCRO is assembling its network. Until each item is verified by Quality and Legal, figures, accreditations, inspection outcomes, people, client names and case studies on this site are placeholders.",
        f"Placeholders carry a marker like this: {ILL()} Lab locations are planned sites from the company plan. Live-looking numbers (tickers, queues, status) are demo data.",
        "When a claim is verified, the marker is removed and the date of verification is shown next to it.") + "</section>"
    + f'<section id="credits">{H2("Image credits")}' + P("Photos are illustrative and do not show PharmaCRO facilities, staff or clients.")
    + T(["Image", "Author", "Licence", "Source"], [[n, html.escape(a), html.escape(l), f'<a href="{u}" rel="noopener">{"Unsplash" if "unsplash.com" in u else "Wikimedia Commons"}</a>'] for n, a, l, u, t in CREDITS]
        + [[n, "Unsplash contributor", "Unsplash Licence", '<a href="https://unsplash.com/" rel="noopener">Unsplash</a>'] for n in ["pharma-lab", "pharma-pipette", "pharma-chalk", "pharma-team", "pharma-plate", "pharma-scopes", "pharma-scope", "pharma-duo", "pharma-tubes", "data-laptop", "data-dash", "data-charts", "group-team", "corp-skyline"]])
    + "</section>", **LEG)

page("cookies", "Cookies", "We use essential storage only, unless you say yes to analytics.", DRAFT + T(["Name", "Type", "Purpose", "Kept"], [
    ["pc-ck", "Local storage", "Remembers your cookie choice", "Until cleared"], ["pc-theme", "Local storage", "Light or dark theme", "Until cleared"],
    ["pc-region", "Local storage", "Region for regulator references", "Until cleared"], ["pc-mod, pc-modn", "Local storage", "The product type you chose, to personalise pages", "Until cleared"],
    ["Analytics", "Off by default", "Privacy-first, aggregate page counts if you allow them", "13 months"]]) + P("Change your mind at any time by clearing site data in your browser."), **LEG)

page("accessibility", "Accessibility statement", "We aim for WCAG 2.2 AA across the site.", DRAFT + P(
    "<b>Our target.</b> WCAG 2.2 level AA: keyboard access to every control, visible focus, text contrast of at least 4.5:1, alt text on images, captions for video, and forms that announce errors.",
    "<b>Motion.</b> We honour your reduced-motion setting: animations become static or fade-only, and the home page motion has a pause button.",
    "<b>Known gaps.</b> Some interactive maps and charts have text alternatives that are less detailed than the visual. The orbiting services diagram becomes a simple list on small screens. We are working on both.",
    f"<b>Tell us.</b> If something does not work for you, email <a href='mailto:{MAIL}'>{MAIL}</a>. We reply within five business days and will provide the information another way."), **LEG)

page("whistleblowing", "Speak up", "Raise a concern safely, including anonymously.", DRAFT + P(
    "Anyone, inside or outside PharmaCRO, can report a concern about data integrity, safety, bribery, discrimination, modern slavery or any other wrongdoing.",
    "<b>Independent.</b> Reports go to the Head of Quality and an independent board member, not to the line management of the person concerned.",
    "<b>No retaliation.</b> Nobody is disadvantaged for raising a genuine concern. Retaliation is itself a disciplinary matter.",
    "<b>Anonymous.</b> You can leave the contact field empty. An independent hotline opens at launch.")
    + MAILFORM([("msg", "What would you like to report?", "textarea", True), ("site", "Which site, if any", ["Not site-specific"] + [l[1] for l in LABS], False), ("reach", "How to reach you (optional)", "text", False)],
               "Speak-up report", "Send report", "Your email app has opened. Press send. You can remove your name from the email before sending."), **LEG)

page("modern-slavery-statement", "Modern slavery statement", "How we prevent forced labour in our operations and supply chain.", DRAFT + P(
    "We do not tolerate modern slavery, forced labour or human trafficking anywhere in our business or supply chain.",
    "<b>Our supply chain.</b> Instruments, reagents, consumables, couriers, cleaning and security services. Higher-risk categories (cleaning, security, logistics) get supplier questionnaires and contract clauses.",
    "<b>Due diligence.</b> New suppliers sign our supplier code; acquired labs are reviewed during diligence and within the 100-day plan.",
    "<b>Training.</b> Managers and procurement staff are trained to recognise indicators.",
    "<b>Reporting.</b> Concerns go through the <a href='/whistleblowing.html'>speak-up line</a>. This statement will be approved by the board and reviewed yearly."), **LEG)

# ---------------- search, 404, maintenance ----------------
search_body = ('<div class="co-search"><label class="so-l box">' + ICON("search") + '<span class="vh">Search</span><input type="search" placeholder="Search services, methods, labs and articles" autocomplete="off" autofocus></label>'
               '<div class="co-sres so-r" aria-live="polite"></div></div>')
page("search", "Search", "Services, methods, labs, articles and tools.", search_body, hero="plain", eyebrow="Search", cta=False, hb="")

POP = [("Small molecule QC and release", "/services/small-molecule-qc-release.html"), ("Stability studies", "/services/stability-studies.html"), ("Method Library", "/method-library/index.html"),
       ("Test Finder", "/tools/test-finder.html"), ("Our labs", "/labs/index.html"), ("Request a quote", "/request-quote.html")]
page("404", "This page failed system suitability.", "Try the search, or head back home.",
     '<div class="co-search"><label class="so-l box">' + ICON("search") + '<span class="vh">Search</span><input type="search" placeholder="What were you looking for?" autocomplete="off"></label><div class="co-sres so-r" aria-live="polite"></div></div>'
     + SIG() + H2("Popular pages") + '<div class="co-pop">' + "".join(f'<a class="btn o" href="{u}">{t}</a>' for t, u in POP) + "</div>",
     hero="plain", eyebrow="Error 404", cta=False, hb='<a class="btn big" href="/index.html">Back home</a>')
page("maintenance", "We are calibrating.", "Back shortly. Samples and results are safe.",
     SIG() + P(f"Urgent? Call {PHONES[0][1]} (India), {PHONES[1][1]} (Singapore), {PHONES[2][1]} (Europe) or {PHONES[3][1]} (US).", "The client portal and your data are unaffected by website maintenance."),
     hero="plain", eyebrow="Maintenance", cta=False, hb="")

# ---------------- sitemap (last: lists everything registered so far) ----------------
GROUPS = [("Company", ("about/", "careers/", "sustainability", "news", "partner-with-us", "investors")), ("Services", ("services/",)), ("By stage", ("solutions/",)),
          ("Industries", ("industries/",)), ("Labs", ("labs/",)), ("Quality", ("quality/",)), ("Technology", ("technology/", "portal/")),
          ("Insights", ("insights/",)), ("Method Library", ("method-library/",)), ("Tools", ("tools/",)),
          ("Resources", ("regulatory-radar", "case-studies", "webinars", "whitepapers", "glossary")),
          ("Get in touch", ("request-quote", "book-a-call", "submit-samples", "contact", "support", "status")),
          ("Legal", ("privacy", "terms", "cookies", "accessibility", "whistleblowing", "modern-slavery-statement"))]
_pages = list(PAGES) + ["sitemap"]
_sm = ""
for g, pre in GROUPS:
    ps = [p for p in _pages if p.startswith(pre) and p != "sitemap"]
    if ps:
        _sm += f'<div class="box"><h3>{g} <small class="mono-v">{len(ps)}</small></h3><ul>' + "".join(f'<li><a href="/{p}.html">{re.sub("<[^>]+>", "", PAGES[p]["title"])}</a></li>' for p in ps) + "</ul></div>"
page("sitemap", "Sitemap", f"Every page on this site.", '<div class="co-sm">' + f'<div class="box"><h3>Home</h3><ul><li><a href="/index.html">Home</a></li></ul></div>' + _sm + "</div>",
     hero="plain", eyebrow="Sitemap", cta=False, hb="")
