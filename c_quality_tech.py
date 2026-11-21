"""Quality (blueprint 4.8) and Technology / Client portal (4.9). Certificates, inspections and security status are placeholders until verified."""
from ph import *

QC = [("Quality", "/quality/index.html")]
TC = [("Technology", "/technology/index.html")]

SHIELD = ('<div class="qx-shield" aria-hidden="true"><svg viewBox="0 0 240 240"><circle class="qx-ring" cx="120" cy="120" r="104" pathLength="1"/>'
          '<path class="qx-sh" pathLength="1" d="M120 34 56 58v52c0 44 28 78 64 96 36-18 64-52 64-96V58z"/><path class="qx-tk" pathLength="1" d="m90 122 22 22 40-46"/>'
          '<path class="qx-sl" pathLength="1" d="M0 200H60c10 0 12-2 15-10l5-14c2-5 5-5 7 0l5 14c3 8 5 10 15 10H150c8 0 10-4 13-14l6-24c2-6 5-6 7 0l6 24c3 10 5 14 13 14H240"/></svg></div>')

FLOW_Q = [("CAPA", "Every deviation, OOS and audit finding gets a root cause and a preventive action with an owner and a due date."),
          ("Change control", "Any change to a method, instrument, system or SOP is assessed for impact before it happens and verified after."),
          ("Training and competency", "Analysts are signed off per method by observed runs, not by reading the SOP."),
          ("Vendor qualification", "Suppliers of reagents, standards, couriers and software are qualified and re-assessed on a schedule."),
          ("Management review", "Quality metrics reviewed monthly by site and quarterly by the network leadership.")]

def qflow():
    n = "".join(f'<li class="qx-fn" style="--i:{i}"><i>{i + 1}</i><b>{t}</b><span>{d}</span></li>' for i, (t, d) in enumerate(FLOW_Q))
    return f'<ol class="qx-flow reveal">{n}</ol>'

VQP = ('<div class="qx-vqp reveal"><div class="qx-vr"><svg viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="50" class="tr"/><circle cx="60" cy="60" r="50" class="qx-vf" pathLength="100"/>'
       '<path class="qx-vt" pathLength="1" d="m42 62 13 13 25-28"/></svg></div><div><h3>Download the Vendor Qualification Pack</h3>'
       '<p>Quality manual summary, accreditation targets, SOP index, organisation chart and insurance summary. Enter your work email and the pack is sent to you; a quality lead follows up only if you ask.</p>'
       + MAILFORM([("email", "Work email", "email", True), ("company", "Company", "text", True), ("role", "Role", ["QA", "QC", "Procurement", "Regulatory", "Other"], False)],
                  "Vendor Qualification Pack request", "Request the pack", "Request sent from your email app. The pack is returned to that address; drafts are marked as pre-launch.", "qx-vform")
       + '</div></div>')

MEASURE = [("Turnaround time (TAT)", "Business days from sample receipt and acceptance (complete paperwork, correct condition) to CoA release in the portal."),
           ("On-time delivery", "Share of reports released on or before the date promised in the quote, all tiers, trailing 90 days."),
           ("Right-first-time", "Share of reports released without a correction or re-issue after release."),
           ("OOS rate", "Confirmed out-of-specification results per 1,000 reportable results, excluding laboratory error."),
           ("Laboratory error rate", "Invalidated results with an assignable laboratory root cause per 1,000 results."),
           ("Response time", "Business hours from a quote request or client query to a substantive reply from a scientist."),
           ("CAPA on time", "Share of corrective and preventive actions closed by their committed due date.")]

page("quality/index", "Inspection-ready, every day.", "How we protect the integrity of every result, and how you can check.",
     ANSWER("PharmaCRO's quality system is designed so every result can be defended in an inspection: ALCOA+ data integrity enforced by one LIMS, an independent QA review of every report, "
            "a full audit trail and one set of SOPs across every lab. Accreditations are targets until certificates are issued, and we label them that way.")
     + '<div class="two"><div>' + SHIELD + '</div><div>' + H2("Proof, not slogans.") + TICKLIST(["Independent QA review of every report before release", "Audit trail reviewed before every approval", "One SOP set, one LIMS, one CoA format", "Certificates shown with number, scope and expiry once issued", "Inspection outcomes disclosed in plain words"]) + '</div></div>'
     + SH("Accreditation wall", "Every certificate, scope and expiry, in one place.", "Today the wall shows target standards per site, clearly marked. Certificates replace the targets as they are issued.")
     + SPLIT("lab-goggles", P("ISO/IEC 17025:2017 for testing scope, GMP compliance for release testing, ISO 9001 for the group quality system and ISO/IEC 27001:2022 for information security are the planned standards.") + P(BTN("Open the accreditation wall", "/quality/accreditations.html")))
     + SH("Data integrity", "ALCOA+, enforced by the system rather than by memory.", "Choose a letter to see the control and an example.") + ALCOA()
     + SH("Audit trail", "Watch a result move from created to released.") + AUDIT()
     + SH("The quality system", "Five processes that keep a network consistent.") + qflow()
     + GALLERY(["lab-analyst-pc", "lab-team-three", "docs-papers"])
     + SH("Ethics and compliance", "How we behave when no one is checking.")
     + ICARDS([("doc", "Code of conduct", "One code for every employee and contractor, signed annually."), ("shield", "Anti-bribery", "Zero tolerance, gifts register and third-party due diligence."),
               ("people", "Speak up", "A confidential whistleblowing line with no retaliation."), ("check", "Conflicts", "Declared, reviewed and recorded.")], 4)
     + f'<p><a class="btn o" href="/quality/ethics-and-compliance.html">Ethics and compliance</a> <a class="btn o" href="/whistleblowing.html">Whistleblowing</a></p>'
     + VQP
     + f'<section id="measure">{SH("How we measure", "Definitions behind every number we publish.", "When a figure appears on this site it uses one of these definitions and carries the date it was measured.")}'
     + T(["Metric", "Definition"], [[a, b] for a, b in MEASURE]) + '</section>'
     + f'<section id="claims">{SH("How we label claims", "Placeholders are marked until they are verified.")}'
     + P(f"PharmaCRO is assembling its network. Until Quality and Legal verify a figure, accreditation, inspection outcome, person or client story, it carries a marker like this: {ILL()}. "
         "Planned lab locations are labelled as planned. Nothing marked this way should be relied on in a vendor assessment; ask us for the current verified position instead.")
     + P(BTN("Book a quality call", "/book-a-call.html")) + '</section>'
     + FAQS([("Can we audit you?", "<p>Yes. Choose a lab and dates through <a href='/contact.html'>contact</a>. A quality lead confirms within 48 hours and opens a secure document exchange.</p>"),
             ("Who reviews results?", "<p>An analyst creates the result, a second scientist reviews it, and QA approves it. No one approves their own data.</p>"),
             ("Do you hold ISO/IEC 17025 today?", "<p>Not as a network yet. Acquired labs bring their existing accreditations; the wall shows each one as it transfers or is issued.</p>")], "faq-q"),
     img="lab-goggles", eyebrow="Quality", chips=[("ALCOA+", "data integrity"), ("100%", "reports QA-reviewed (design)"), ("1", "SOP set")],
     cta=("Built to survive inspection.", "Ask for the Vendor Qualification Pack or book a call with our Head of Quality."))

# ---------- accreditations ----------
CERTS = []
for l in LABS:
    reg = {"India": "NABL", "Southeast Asia": "SAC-SINGLAS" if l[0] == "singapore" else "Standards Malaysia", "Europe": {"leiden": "RvA", "cambridge": "UKAS", "dublin": "INAB"}.get(l[0], ""), "United States": "A2LA / ANAB"}[l[3]]
    CERTS += [(l[1], "ISO/IEC 17025:2017", reg, "Testing scope: " + ", ".join(SVC[k][1] for k in l[9][:2])),
              (l[1], "GMP compliance", {"India": "CDSCO / State FDA", "Southeast Asia": "HSA" if l[0] == "singapore" else "NPRA", "Europe": {"leiden": "IGJ", "cambridge": "MHRA", "dublin": "HPRA"}.get(l[0], ""), "United States": "FDA"}[l[3]], "Quality control testing for medicinal products")]
CERTS += [("Network", "ISO 9001:2015", "Accredited certification body", "Group quality management system"), ("Network", "ISO/IEC 27001:2022", "Accredited certification body", "Portal, LIMS and client data")]

def wall():
    labs = sorted({c[0] for c in CERTS}); stds = sorted({c[1] for c in CERTS})
    f = ('<div class="qx-wf"><label><span class="vh">Lab</span><select data-wl><option value="">All labs</option>' + "".join(f"<option>{x}</option>" for x in labs) + '</select></label>'
         '<label><span class="vh">Standard</span><select data-ws><option value="">All standards</option>' + "".join(f"<option>{x}</option>" for x in stds) + '</select></label><span class="qx-wc" aria-live="polite"></span></div>')
    c = "".join(f'<button type="button" class="qx-cert reveal" data-l="{a}" data-s="{b}" aria-pressed="false" style="--i:{i % 4}"><span class="qx-cf">{ICON("shield")}<b>{b}</b><em>{a}</em><small>Issued by {who}</small>'
                f'<small class="mono">No. [pending] &middot; Expiry [pending]</small><i>Target</i></span><span class="qx-cb"><b>Scope</b><span>{sc}</span><small>Certificate PDF and verification link appear here once issued.</small></span></button>'
                for i, (a, b, who, sc) in enumerate(CERTS))
    return f'{f}<div class="qx-wall">{c}</div><p class="cn">All entries are targets {ILL("Not yet held")}. Select a card to see its scope.</p>'

page("quality/accreditations", "Accreditations", "Every certificate: scope, issuing body, number, expiry and a verification link, filterable by lab and standard.",
     ANSWER("This wall will list every PharmaCRO certificate with its scope, issuing body, number, expiry date, PDF and a link to verify it with the issuer. "
            "Today every entry is a target for a planned site and is marked as not yet held. Acquired labs' existing certificates are added as they transfer.")
     + wall()
     + SH("How to verify a certificate", "Never take our word for it.")
     + STEPLINE([("Find the number", "Each card shows the certificate number and the accreditation body."), ("Check the issuer's register", "NABL, UKAS, INAB, RvA, A2LA, ANAB and SAC publish searchable directories of accredited labs and scopes."),
                 ("Compare the scope", "Accreditation covers named methods only. Check your method is in scope."), ("Ask us", "If anything does not match, tell our Head of Quality.")])
     + SPLIT("docs-papers", H3("What accreditation does and does not mean") + P("ISO/IEC 17025:2017 confirms a lab is competent for the specific tests in its scope. It is not a GMP certificate, and GMP compliance for release testing is assessed by the medicines regulator through inspection.")),
     img="docs-papers", eyebrow="Quality", crumbs=QC, chips=[(str(len(CERTS)), "target certificates"), ("0", "held today")])

# ---------- data integrity ----------
DI_ROWS = [["Validation of systems", "21 CFR 11.10(a)", "Annex 11 §4", "LIMS and CDS validated with risk-based testing; re-validated on change"],
           ["Accurate and complete copies", "11.10(b)", "Annex 11 §8", "Human-readable and electronic copies with a hash"],
           ["Record protection and retention", "11.10(c)", "Annex 11 §7, §17", "Validated storage, backups tested, retention per agreement"],
           ["Access limited to authorised people", "11.10(d)", "Annex 11 §12", "Role-based access, MFA, no shared accounts"],
           ["Secure, time-stamped audit trail", "11.10(e)", "Annex 11 §9", "Who, what, when and why for every create, change and delete; cannot be switched off"],
           ["Operational and authority checks", "11.10(f), (g)", "Annex 11 §12", "Workflow enforces sequence; analysts cannot approve their own results"],
           ["Electronic signatures", "11.50, 11.70, 11.100 to 11.300", "Annex 11 §14", "Signature shows name, date, time and meaning; linked to the record"],
           ["Periodic review", "Guidance", "Annex 11 §11", "Systems and audit trails reviewed on a set schedule"]]
DETAIL = [("Attributable", "Unique log-ins on every instrument PC; badges or biometrics at shared benches."), ("Legible", "Records readable for the full retention period, including legacy formats."),
          ("Contemporaneous", "Network time; data captured directly from balances, pH meters and chromatography."), ("Original", "Raw data, not printouts, are the record; true copies are verified."),
          ("Accurate", "Locked calculation templates; manual integration only with a recorded reason and review."), ("Complete", "Repeats, aborted runs and invalidated results stay visible."),
          ("Consistent", "Same sequence of events and time stamps across sites."), ("Enduring", "Validated archive with restore tests."), ("Available", "Retrieval for an inspector within an hour.")]

page("quality/data-integrity", "Data integrity (ALCOA+)", "How our LIMS enforces each ALCOA+ principle, mapped to 21 CFR Part 11 and EU GMP Annex 11.",
     ANSWER("Data integrity means every result is attributable, legible, contemporaneous, original and accurate, and also complete, consistent, enduring and available. "
            "At PharmaCRO these principles are enforced by one validated LIMS and chromatography data system across every lab, not by memory, and are mapped to 21 CFR Part 11 and EU GMP Annex 11.")
     + ALCOA()
     + SH("Principle by principle", "The control behind each letter.") + T(["Principle", "Control"], [[a, b] for a, b in DETAIL])
     + SPLIT("lab-analyst-pc", H3("No orphan data") + P("Every injection, weighing and calculation is tied to a sample, a method version and a user. Data that is not linked to a sample is flagged for review, the most common source of findings in chromatography labs."))
     + SH("Regulatory mapping", "21 CFR Part 11 and EU GMP Annex 11, side by side.")
     + T(["Requirement", "21 CFR Part 11", "EU GMP Annex 11", "How it is met"], DI_ROWS)
     + f'<p class="cn">Design controls {ILL("Validation pending")}. Validation summaries are shared with auditors under NDA.</p>'
     + SH("Audit trail review", "Reviewed before every approval, not once a year.")
     + STEPLINE([("Analyst self-check", "The analyst confirms no unexplained changes before submitting."), ("Reviewer check", "A second scientist reviews the audit trail with the data, focusing on integrations, re-runs and deletions."),
                 ("QA approval", "QA confirms the review was done and e-signs with the meaning of the signature."), ("Periodic system review", "Quality reviews system-level audit trails (log-ins, configuration changes) on a schedule.")])
     + AUDIT()
     + GALLERY(["sec-servers", "data-dashboard", "lab-goggles"])
     + FAQS([("What is ALCOA+?", "<p>ALCOA stands for attributable, legible, contemporaneous, original and accurate. The plus adds complete, consistent, enduring and available. Regulators including FDA, MHRA and WHO use it to describe trustworthy data.</p>"),
             ("Is the portal Part 11 compliant?", "<p>It is designed to Part 11 and Annex 11 principles. Compliance also depends on validation and procedures, so we share validation evidence rather than a one-word claim.</p>"),
             ("Can analysts delete data?", "<p>No. Data can be invalidated with a reason and review, but never deleted.</p>")], "faq-di"),
     img="sec-servers", eyebrow="Quality", crumbs=QC, chips=[("9", "ALCOA+ principles"), ("Part 11", "and Annex 11 mapped")])

# ---------- inspection history ----------
TLI = [("At acquisition", "Disclosure review", "Each acquired lab's last three years of inspections reviewed in diligence.", "Planned"),
       ("100 days", "Gap closure", "Open observations closed or on a dated CAPA plan.", "Planned"),
       ("First inspection under PharmaCRO", "Regulator inspection", "Outcome published here in plain words.", "Pending"),
       ("Every inspection after", "Published within 30 days", "Date, body, scope and outcome added to the table.", "Policy")]

page("quality/inspection-history", "Inspection history", "Regulatory inspections in plain words: date, body, scope and outcome.",
     ANSWER("As a network still being assembled, PharmaCRO has no regulatory inspection history of its own yet. When labs join, their inspection records will be reviewed and disclosed here, "
            "and every inspection after that will be published with its date, body, scope and outcome in plain words.")
     + '<div class="qx-stmt reveal"><b>Current position</b><p>No PharmaCRO site has been inspected by a regulator under PharmaCRO ownership. No outcomes are claimed.</p></div>'
     + SH("The table we will publish", "Every inspection, in one table.")
     + T(["Date", "Lab", "Body", "Scope", "Outcome"], [["[date]", "[lab]", "[FDA / EMA member state / MHRA / CDSCO / HSA]", "[GMP / GLP / pre-approval]", "[No observations / observations, all closed]"]])
     + f'<p class="cn">Template {ILL("No entries yet")}. Outcomes are published only when legally approved; otherwise a summary statement is shown.</p>'
     + SH("Timeline", "How disclosure works as labs join.")
     + '<ol class="qx-tl">' + "".join(f'<li class="reveal" style="--i:{i}"><em>{a}</em><h3>{b}</h3><p>{c}</p><span class="qx-oc">{d}</span></li>' for i, (a, b, c, d) in enumerate(TLI)) + '</ol>'
     + SPLIT("lab-team-three", H3("Acquired labs") + P("Labs we acquire must have active accreditation and no major observations in the last three years. Their histories, including any observations and how they were closed, are disclosed here once the acquisition completes.")
             + P(BTN("Partner with us", "/partner-with-us.html", True)), flip=True),
     img="lab-team-three", eyebrow="Quality", crumbs=QC, chips=[("0", "inspections to date"), ("30 days", "publication target")])

# ---------- ethics ----------
ETH = [("Code of conduct", "<p>Honesty with data, respect for colleagues and clients, and compliance with the law in every country we work in. Every employee and contractor signs it each year, and managers are measured on it.</p>"),
       ("Anti-bribery and corruption", "<p>No bribes, kickbacks or facilitation payments, in any form or amount. Gifts and hospitality above a low threshold are registered and approved. Agents and intermediaries are screened before engagement. The policy follows the UK Bribery Act 2010, the US FCPA and India's Prevention of Corruption Act, 1988.</p>"),
       ("Whistleblowing and speak-up line", "<p>Anyone can report a concern confidentially and anonymously, including data integrity concerns. Reports go to an independent team, not the site involved. No one is penalised for a good-faith report. <a href='/whistleblowing.html'>How to report</a>.</p>"),
       ("Supplier code", "<p>Suppliers commit to the same standards: lawful employment, no forced or child labour, safe workplaces, environmental care and data protection. See our <a href='/modern-slavery-statement.html'>modern slavery statement</a>.</p>"),
       ("Conflicts of interest", "<p>Employees declare outside interests, family relationships with clients or suppliers, and investments that could influence decisions. Declarations are reviewed and recorded; scientists never test samples for a company they have an interest in.</p>"),
       ("Data protection", "<p>Client and personal data are handled under GDPR, India's DPDP Act 2023, Singapore's PDPA and US state laws as applicable. See the <a href='/privacy.html'>privacy notice</a>.</p>")]

page("quality/ethics-and-compliance", "Ethics and compliance", "Code of conduct, anti-bribery, speak-up line, supplier code and conflicts policy.",
     ANSWER("PharmaCRO runs on one code of conduct, a zero-tolerance anti-bribery policy, a confidential speak-up line, a supplier code and a conflicts-of-interest policy. "
            "They apply in every lab and every country, and data integrity concerns can be raised through the same confidential route.")
     + '<div class="accs one" id="eth">' + "".join(f'<details class="acc reveal" id="eth-{i + 1}"><summary>{q}</summary><div>{a}</div></details>' for i, (q, a) in enumerate(ETH)) + '</div>'
     + BAND("lab-goggles", "Every result has a name behind it.", "Ethics in a testing lab starts with the data. That is why the speak-up line covers data integrity first.", BTN("Report a concern", "/whistleblowing.html"))
     + f'<p class="cn">Policy summaries {ILL("Drafts pending legal review")}.</p>',
     img="biz-team-laptops", eyebrow="Quality", crumbs=QC, cta=False)

# ---------- technology ----------
TABS = [("Tracking", "Live sample tracking", "Status timeline for every sample: received, queued, in analysis, under review, approved, released, with owner and time stamp.",
         '<div class="qx-ui"><b>PC-24-0919 &middot; Adalimumab DS</b>' + "".join(f'<div class="qx-tlr{" on" if i < 4 else ""}"><i></i><span>{s}</span><small>{t}</small></div>' for i, (s, t) in enumerate([("Received", "08:14, photo + temp log"), ("Queued", "08:40"), ("In analysis", "10:02, analyst S. Iyer"), ("Under review", "16:30"), ("Released", "")])) + '</div>', [(30, 22), (70, 64)]),
        ("CoAs", "Instant e-signed CoAs", "Every CoA is e-signed by QA and versioned. Download one or a hundred, with raw data on request.",
         '<div class="qx-ui"><b>Certificates of analysis</b>' + "".join(f'<div class="qx-row"><span class="mono">{a}</span><span>{b}</span><span class="qx-ok">Signed</span></div>' for a, b in [("CoA-0918-v1", "Metformin B2291"), ("CoA-0917-v2", "Amoxicillin 24-118"), ("CoA-0915-v1", "WFI Room 2B")]) + '</div>', [(85, 30)]),
        ("Trends", "Trending and control charts", "Control charts across batches and stability tables with shelf-life regression, so drift is visible before it becomes an OOS.",
         '<div class="qx-ui"><b>Assay trend, 20 batches</b><svg viewBox="0 0 300 120" class="qx-cc"><path d="M0 30H300M0 90H300" class="lim"/><path d="M0 60H300" class="mean"/><polyline pathLength="1" points="0,62 15,55 30,66 45,58 60,61 75,52 90,64 105,57 120,59 135,48 150,63 165,60 180,55 195,67 210,58 225,61 240,50 255,63 270,57 285,60 300,54"/></svg><small>Mean 99.4% &middot; UCL 101.2% &middot; LCL 97.6%</small></div>', [(50, 40)]),
        ("Alerts", "Deviation and OOS notifications", "An OOS or deviation opens a thread with the responsible scientist, and you choose who is notified by email, SMS, Slack or Teams.",
         '<div class="qx-ui"><b>Notifications</b><div class="qx-al amb"><b>OOS investigation opened</b>PC-24-0922 &middot; NDSRI above limit in 1 of 3 batches. Phase 1 lab investigation started.</div><div class="qx-al"><b>Released</b>PC-24-0918 &middot; CoA ready.</div></div>', [(20, 45)]),
        ("Team", "Roles and approvals", "Roles for QC, QA, procurement and read-only, with approvals for quotes and protocol changes.",
         '<div class="qx-ui"><b>Users and permissions</b>' + "".join(f'<div class="qx-row"><span>{a}</span><span class="mono">{b}</span></div>' for a, b in [("QC lead", "Approve, download"), ("QA", "Review, sign-off"), ("Procurement", "Quotes, POs"), ("Auditor", "Read-only, 30 days")]) + '</div>', [(80, 55)])]

def tabs():
    b = "".join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" data-i="{i}">{t}</button>' for i, (t, *_) in enumerate(TABS))
    p = "".join(f'<div class="qx-tp{" on" if i == 0 else ""}" data-i="{i}" role="tabpanel"><div><h3>{h}</h3><p>{d}</p></div><div class="qx-mock">{ui}'
                + "".join(f'<span class="qx-hs" style="left:{x}%;top:{y}%" tabindex="0"><i></i><em>{h}</em></span>' for x, y in hs) + '</div></div>' for i, (t, h, d, ui, hs) in enumerate(TABS))
    return f'<div class="qx-tabs reveal"><div class="seg" role="tablist" aria-label="Portal features">{b}</div>{p}</div>'

SEC = [["Hosting region", "Marketing site on a global CDN; portal data hosted in-region (India, EU, US) for data residency"],
       ["Encryption", "TLS 1.2+ in transit; AES-256 at rest"], ["Identity", "SSO (SAML / OIDC) with your identity provider, MFA required, role-based access"],
       ["SOC 2 Type II", f"Roadmap {ILL('Not yet held')}"], ["ISO/IEC 27001:2022", f"Roadmap {ILL('Not yet held')}"],
       ["Backup and disaster recovery", "Daily encrypted backups, cross-zone replication, restore tested quarterly; target RPO 1 hour, RTO 8 hours"],
       ["Penetration testing", "Independent test before launch and annually"], ["Vulnerability disclosure", "Report security issues through <a href='/contact.html'>contact</a>; we acknowledge within two business days"]]

LOCK = ('<div class="qx-lock" aria-hidden="true"><svg viewBox="0 0 200 200"><g class="qx-rot"><circle cx="100" cy="100" r="88" pathLength="1"/></g>'
        '<path class="qx-shk" d="M72 92V70a28 28 0 0 1 56 0v22"/><rect x="58" y="90" width="84" height="66" rx="12"/><circle cx="100" cy="118" r="8"/><path d="M100 126v12"/></svg></div>')

page("technology/index", "Your lab results. Live.", "One portal across every lab. Track, review and download without sending an email.",
     ANSWER("PharmaCRO runs one LIMS and one client portal across every lab. You see each sample's live status, download e-signed CoAs, trend results across batches and get alerts on deviations, "
            "and your systems can connect through a REST API and webhooks. Records are designed to 21 CFR Part 11 and EU GMP Annex 11 principles.")
     + '<section class="dark-sec">' + SH("The portal", "Watch your samples move.", "Move your cursor over the device; scroll to watch statuses advance. Demo data.") + PORTAL() + '</section>'
     + SH("Portal features", "Everything you used to chase by email.") + tabs()
     + SH("Data integrity by design", "Security and compliance built into the system.")
     + '<div class="two"><div>' + LOCK + '</div><div>' + TICKLIST(["Electronic records and signatures to Part 11 and Annex 11 principles", "Immutable, time-stamped audit trail", "Role-based access and MFA", "Encryption in transit and at rest", "One validated system, so one validation package for auditors"]) + P(BTN("Data integrity in detail", "/quality/data-integrity.html", True)) + '</div></div>'
     + SH("API and integrations", "Connect your ERP, QMS and LIMS.")
     + SPLIT("data-dashboard", P("A REST API and webhooks push results, CoAs and status changes into your systems, and accept sample submissions from them.") + P(BTN("API and integrations", "/technology/api-and-integrations.html")))
     + SH("Security and privacy", "Clear answers for your IT and QA teams.") + T(["Area", "Position"], SEC)
     + GALLERY(["sec-servers", "data-laptop", "lab-analyst-pc"])
     + FAQS([("Is there a mobile app?", "<p>Yes, for status, notifications and CoA download. Approvals and e-signatures use the web portal.</p>"),
             ("Can we use our own identity provider?", "<p>Yes, through SAML or OIDC single sign-on.</p>"),
             ("Where is our data stored?", "<p>In the region you choose (India, EU or US) for portal records and data packages.</p>")], "faq-tech"),
     img="data-dashboard", eyebrow="Technology", chips=[("1", "LIMS across all labs"), ("Part 11", "aligned design"), ("API", "REST and webhooks")],
     cta=("See your own samples here.", "Request portal access with your first quote; every client gets it at no charge."))

# ---------- portal (marketing) ----------
def qr(seed):
    cells = "".join(f'<rect x="{x * 6}" y="{y * 6}" width="6" height="6"/>' for y in range(21) for x in range(21)
                    if (x < 7 and y < 7) or (x > 13 and y < 7) or (x < 7 and y > 13) or ((x * 7 + y * 13 + seed) % 5 < 2))
    return f'<svg class="qx-qr" viewBox="0 0 126 126" aria-hidden="true">{cells}</svg>'

SCOPE = [("Dashboard", "Sample counts by status, upcoming deadlines, alerts and a quick quote request.", "data-dashboard"),
         ("Sample submission wizard", "Select quote lines, enter batch details, upload a CoA or protocol, declare hazards and storage, then print QR labels and book a courier.", "log-warehouse"),
         ("Live tracking", "Timeline, location and named analyst for every sample.", "lab-analyst-pc"),
         ("Results and CoA centre", "E-signed CoAs with version history and bulk download.", "docs-papers"),
         ("Trending", "Control charts, stability tables and shelf-life regression.", "data-laptop"),
         ("Quotes and orders", "View, approve and e-sign quotes and MSAs; upload purchase orders.", "biz-team-laptops"),
         ("Documents", "Protocols, reports, certificates and invoices in one place.", "docs-papers"),
         ("Users and permissions", "Roles for QC, QA, procurement and read-only auditors.", "biz-meeting-1" if "biz-meeting-1" in ALT else "biz-highfive"),
         ("Messaging", "Threads with scientists tied to a sample or project.", "lab-team-three"),
         ("Notifications", "Email, SMS, Slack and Teams, per user and per event.", "data-dashboard")]

page("portal/index", "Client portal", "Watch your samples move in real time: submit, track, review and download in one place.",
     ANSWER("The PharmaCRO client portal lets you submit samples with QR labels, track each one live, download e-signed CoAs, trend results and approve quotes, across every lab in the network. "
            "It opens to clients at launch; this page shows the planned scope with demo data.")
     + '<section class="dark-sec">' + PORTAL() + '</section>'
     + SH("Submission wizard", "Labels and courier in two minutes.")
     + '<div class="qx-wiz reveal"><div class="qx-ws">' + "".join(f'<span class="{"on" if i < 3 else ""}">{i + 1}. {s}</span>' for i, s in enumerate(["Quote lines", "Batch details", "Hazard and storage", "Labels", "Courier"])) + '</div>'
     + '<div class="qx-wl">' + "".join(f'<div class="qx-lbl">{qr(i)}<div><b class="mono">PC-24-09{20 + i}</b><span>{p}</span><small>Store 2 to 8 °C &middot; Quote Q-5512</small></div></div>' for i, p in enumerate(["mRNA-LNP ENG-04 vial 1 of 3", "mRNA-LNP ENG-04 vial 2 of 3", "mRNA-LNP ENG-04 vial 3 of 3"])) + '</div>'
     + '<p class="cn">Demo labels. Real labels include a unique sample ID and a packing list PDF.</p></div>'
     + SH("Full scope", "Ten things the portal does.")
     + '<div class="qx-scope">' + "".join(f'<div class="qx-sc reveal" style="--i:{i % 4}"><img src="/img/{im}.jpg" alt="" loading="lazy"><div><small class="mono">{i + 1:02d}</small><h3>{t}</h3><p>{d}</p></div></div>' for i, (t, d, im) in enumerate(SCOPE)) + '</div>'
     + SH("Trending", "Spot drift before it becomes an OOS.")
     + LINE("Assay, % label claim, last 12 batches (demo)", [f"B{i}" for i in range(1, 13)], [("Assay", [99.1, 99.6, 98.9, 99.3, 99.8, 99.0, 98.7, 99.4, 99.2, 99.9, 99.1, 99.5])], "Demo data.", lambda v: f"{v:.1f}%")
     + SH("Empty state", "Where you start.")
     + '<div class="qx-empty reveal">' + ICON("vial", "ic big") + '<p>Nothing in progress yet. Ship your first samples and watch them move here.</p><a class="btn" href="/submit-samples.html">How to ship samples</a></div>'
     + STRIP(["lab-analyst-pc", "data-dashboard", "lab-sample-rack", "log-warehouse", "docs-papers", "lab-pipette-vials"])
     + FAQS([("When does the portal open?", "<p>At network launch. Until then quotes, reports and CoAs are sent by secure email.</p>"),
             ("Does it cost extra?", "<p>No. Every client gets portal access.</p>"),
             ("Can our auditors get access?", "<p>Yes, as time-limited read-only users.</p>")], "faq-portal"),
     img="data-laptop", eyebrow="Technology", crumbs=TC, chips=[("10", "modules"), ("Live", "status"), ("QR", "sample labels")],
     hb='<a class="btn big" href="/portal/login.html">Portal login</a> <a class="btn o big" href="/request-quote.html">Request access with a quote</a>')

# ---------- login ----------
page("portal/login", "Client portal login", "Sign in to track samples, download CoAs and approve quotes.",
     '<div class="qx-login"><form class="qx-lf" novalidate><a class="qx-st" href="/status.html"><i></i>System status: demo</a>'
     '<div class="qx-l1"><label><span>Work email</span><input type="email" name="email" autocomplete="username" required></label>'
     '<label><span>Password</span><input type="password" name="pw" autocomplete="current-password" required></label>'
     '<button class="btn big" type="submit">Sign in</button><button class="btn o" type="button" data-sso>Sign in with SSO</button></div>'
     '<div class="qx-l2" hidden><p>Enter the 6-digit code from your authenticator app.</p><div class="qx-otp">' + "".join('<input inputmode="numeric" maxlength="1" aria-label="Digit">' for _ in range(6)) + '</div>'
     '<button class="btn big" type="button" data-mfa>Verify</button></div>'
     '<div class="qx-l3" hidden>' + SIG() + '<h3>The client portal opens at launch.</h3><p>Nothing was sent or checked: this page is a preview. Until launch, quotes, reports and CoAs arrive by secure email.</p>'
     '<p><a class="btn" href="/request-quote.html">Request a quote</a> <a class="btn o" href="/portal/index.html">See what the portal does</a></p></div>'
     '<p class="qx-lk"><a href="/request-quote.html">Request access</a> &middot; <a href="/support.html">Support</a> &middot; <a href="/privacy.html">Privacy</a></p></form>'
     '<div class="qx-lim"><img src="/img/lab-analyst-pc.jpg" alt="An analyst reviewing data at a computer in a laboratory"></div></div>',
     hero="plain", eyebrow="Client portal", crumbs=[("Client portal", "/portal/index.html")], cta=False, hb="")

# ---------- API ----------
CODE = '''curl -X POST https://api.pharmacro.example/v1/samples \\
  -H "Authorization: Bearer $TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{
    "quote_id": "Q-5512",
    "product": "mRNA-LNP ENG-04",
    "batch": "ENG-04-2611",
    "storage": "2-8C",
    "tests": ["mrna-integrity-ce", "encapsulation-efficiency-ribogreen"]
  }\''''
RESP = '''HTTP/1.1 201 Created
{
  "sample_id": "PC-24-0920",
  "status": "awaiting_receipt",
  "label_pdf": "https://api.pharmacro.example/v1/samples/PC-24-0920/label.pdf",
  "promised_date": "2026-12-03"
}'''
EP = [["POST", "/v1/samples", "Register samples against a quote; returns IDs and label PDFs"], ["GET", "/v1/samples/{id}", "Status, timeline, analyst and location"],
      ["GET", "/v1/samples/{id}/results", "Released results with units and specification"], ["GET", "/v1/coas/{id}", "E-signed CoA PDF and hash"],
      ["GET", "/v1/quotes", "Quotes and their status"], ["POST", "/v1/webhooks", "Subscribe a URL to events"]]
EV = [["sample.received", "Samples logged at the lab, with photo and temperature trace link"], ["sample.status_changed", "Any move along the status timeline"],
      ["result.released", "Results approved by QA"], ["coa.issued", "CoA e-signed and available"], ["deviation.opened", "Deviation or OOS investigation opened"], ["quote.issued", "A new quote is ready to approve"]]

page("technology/api-and-integrations", "API and integrations", "A REST API and webhooks that connect PharmaCRO results to your ERP, QMS and LIMS.",
     ANSWER("The PharmaCRO API lets your systems register samples, read status and results, download e-signed CoAs and subscribe to webhook events such as result.released. "
            "It uses JSON over HTTPS with OAuth 2.0 tokens, and a sandbox with demo data is available before you connect production systems.")
     + '<div class="qx-api reveal"><div class="qx-code"><div class="qx-ch"><span>Request</span><button type="button" class="btn sm" data-send>Send request</button></div><pre><code class="qx-type" data-code="' + html.escape(CODE) + '"></code></pre></div>'
     + '<div class="qx-code"><div class="qx-ch"><span>Response</span><span class="qx-state" aria-live="polite">Waiting</span></div><pre><code class="qx-resp" data-code="' + html.escape(RESP) + '"></code></pre></div></div>'
     + f'<p class="cn">Simulated demo: nothing is sent. The host name is a placeholder {ILL("Sandbox at launch")}.</p>'
     + SH("Endpoints", "The core resources.") + T(["Method", "Path", "What it does"], [[f'<span class="mono">{a}</span>', f'<span class="mono">{b}</span>', c] for a, b, c in EP])
     + SH("Webhooks", "Events pushed to your systems.") + T(["Event", "When it fires"], [[f'<span class="mono">{a}</span>', b] for a, b in EV])
     + P("Webhook payloads are signed with an HMAC-SHA256 header so you can verify they came from us; failed deliveries retry with backoff for 24 hours.")
     + SH("Integrations", "Where results usually need to go.")
     + ICARDS([("api", "ERP", "Purchase orders and invoices to SAP, Oracle or Microsoft Dynamics through the API or file drop."),
               ("shield", "QMS", "Deviation and OOS events into Veeva Vault QMS, MasterControl or TrackWise."),
               ("flask", "LIMS", "Results into LabWare, LabVantage or STARLIMS, so your release decision uses one record."),
               ("chat", "Collaboration", "Status notifications into Slack and Microsoft Teams.")], 4)
     + SPLIT("sec-servers", H3("Sandbox") + P("A sandbox with demo samples, results and webhooks lets your team build and validate the integration before go-live. Ask for credentials with your first quote."), flip=True)
     + FAQS([("How do we authenticate?", "<p>OAuth 2.0 client credentials, with tokens scoped per integration and rotated on a schedule.</p>"),
             ("Are there rate limits?", "<p>Yes, generous per-client limits, returned in response headers.</p>"),
             ("Is the API validated?", "<p>It is part of the validated system. Your own validation of the integration remains your responsibility.</p>")], "faq-api"),
     img="sec-servers", eyebrow="Technology", crumbs=TC, chips=[("REST", "JSON over HTTPS"), ("6", "webhook events"), ("OAuth 2.0", "auth")])
