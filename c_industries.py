"""Industries hub, eight segment pages, solutions-by-stage hub and five stage pages (blueprint 4.6).
Local components: PAINS (split-screen scroll reveal), TILES (expanding segment tiles), MATCHER, MINIDELAY. Behaviour in assets/m_industries.js."""
from ph import *

SIDX = {s[0]: i for i, s in enumerate(SERVICES)}
TOOLN = dict(TOOLS)
IC = [("Industries", "/industries/index.html")]
SC = [("Solutions by stage", "/solutions/index.html")]

def PAINS(items):
    """items: (pain, detail, service_slug, solution, proof). Pain on the left fades to the answer on the right as you scroll."""
    rows = "".join(
        f'<div class="ind-pr"><div class="ind-pn"><span class="ind-k">Pain {i + 1}</span><h3>{p}</h3><p>{d}</p></div>'
        f'<div class="ind-so"><span class="ind-k">Our answer &middot; <a href="{svc_url(s)}">{SVC[s][1]}</a></span><p>{so}</p><small>{ICON("check")} {pr} {ILL()}</small></div></div>'
        for i, (p, d, s, so, pr) in enumerate(items))
    return f'<div class="ind-pains">{rows}</div>'

def PACKAGE(name, text, slugs, rows, weeks, main):
    comp = "".join(f'<li><a href="{svc_url(s)}">{ICON(SVC[s][5])}{SVC[s][1]}</a></li>' for s in slugs)
    return (f'<div class="ind-pkg reveal"><div><p class="ey">Recommended package</p><h3>{name}</h3><p>{text}</p><ul class="ind-comp">{comp}</ul>'
            f'<p><a class="btn" href="/request-quote.html?service={SIDX[main]}">Request this package</a> <a class="btn o" href="/services/bundles.html">All bundles</a></p></div>'
            f'<div>{GANTT(rows, weeks, name + ": indicative timeline")}</div></div>')

def MINIDELAY(value=250000):
    """Cost of delay mini calculator (the full tool lives at /tools/cost-of-delay-calculator.html)."""
    return (f'<div class="ind-cod reveal" data-v="{value}"><h3>What does a day of testing delay cost you?</h3>'
            f'<div class="ind-cod-in"><label><span>Value of the batch or launch per day (USD)</span><input type="number" min="0" step="1000" value="{value}" data-cod="v"></label>'
            f'<label><span>Your current testing turnaround (business days)</span><input type="number" min="1" max="120" value="20" data-cod="a"></label>'
            f'<label><span>Target turnaround (business days)</span><input type="number" min="1" max="120" value="7" data-cod="b"></label></div>'
            f'<p class="ind-cod-o" aria-live="polite"></p><p class="cn">Simple arithmetic: days saved x value per day. Your own finance team should set the daily value. '
            f'<a href="/tools/cost-of-delay-calculator.html">Open the full Cost of Delay Calculator</a>.</p></div>')

# ---------------------------------------------------------------- segments
IND = {
"generics": dict(
  chips=[("3 to 10 d", "release testing"), ("NDSRI", "risk assessment in 48 h"), ("CDSCO, FDA, EMA", "markets served")],
  answer="Generic manufacturers need fast, cheap, defensible release testing and a clean answer on nitrosamines before every launch. PharmaCRO runs compendial release, dissolution, stability and NDSRI testing on one LIMS, so methods transfer between labs in days and your launch date does not depend on a single instrument.",
  pains=[("Tight margins and tight launch windows.", "A day-one generic launch can be worth more than the whole year's testing budget. A late CoA costs real money.", "small-molecule-qc-release",
          "Guaranteed turnaround tiers with the date shown before you ship, and Critical-tier capacity reserved for launch batches.", "Launch batch released 21 days early in an illustrative case."),
         ("Nitrosamines keep moving.", "Acceptable intake limits for NDSRIs have been revised as data arrives. A product cleared last year may need another look.", "small-molecule-qc-release",
          "A 48-hour risk assessment, then validated LC-MS/MS methods at limits matched to the current acceptable intake.", "LC-MS/MS NDSRI methods at low ng/g limits."),
         ("Dissolution is where filings stall.", "Profile comparisons, f2 calculations and discriminating media are a common source of deficiency letters.", "method-development-validation",
          "Dissolution method development and comparative profiles designed to be discriminating from day one.", "All USP apparatus 1 to 4 in the network."),
         ("Zone IVb stability for India and ASEAN.", "Hot, humid markets need 30 °C / 75% RH data, and chamber space is scarce.", "stability-studies",
          "ICH programmes in every climatic zone with one pull schedule and one report format across labs.", "Zone IVb chambers planned at Indian and Malaysian sites."),
         ("Revised Schedule M raises the bar.", "Smaller Indian manufacturers must show documented, capable QC, in-house or outsourced.", "regulatory-data-integrity-support",
          "Outsourced QC under a quality agreement, plus a data integrity gap assessment of your own lab.", "Quality agreement template ready on request.")],
  pkg=("Generic Launch Readiness Package", "Everything a generic needs between exhibit batch and launch: release, dissolution profiles, nitrosamine clearance and stability set-up.",
       ["small-molecule-qc-release", "method-development-validation", "stability-studies", "microbiology-sterility"],
       [("NDSRI risk assessment", 0, 1), ("Method verification or transfer", 0, 2), ("Comparative dissolution (f2)", 1, 3), ("Exhibit batch release", 2, 2), ("Stability set-up and T0", 3, 2), ("Launch batch release (Priority)", 8, 1)], 10, "small-molecule-qc-release"),
  case=("21 days early", "Sartan launch cleared nitrosamine testing ahead of schedule", "<p>A generic manufacturer found a nitrosamine risk six weeks before a US launch. Risk assessment in 48 hours, a transferred LC-MS/MS method and Critical-tier testing of three batches released results 21 days before the deadline.</p>"),
  tool="nitrosamine-risk-assessor", mini="delay", delay=180000,
  reg=["<b>United States.</b> ANDAs need full CMC data, including dissolution comparisons and a nitrosamine risk assessment under FDA guidance on nitrosamine impurities and its NDSRI acceptable-intake recommendations.",
       "<b>Europe.</b> Generic applications under Article 10 of Directive 2001/83/EC rely on bioequivalence; the EMA nitrosamine Q&amp;A sets the risk assessment and testing expectations.",
       "<b>India.</b> The revised Schedule M (notified December 2023) brings Indian GMP closer to WHO standards and expects documented quality control capability, including for MSMEs.",
       "<b>WHO prequalification.</b> Products for donor-funded markets follow WHO PQ requirements, including Zone IVb stability where relevant."],
  svcs=["small-molecule-qc-release", "stability-studies", "method-development-validation", "reference-standards-excipients", "microbiology-sterility", "regulatory-data-integrity-support"],
  faqs=[("How fast can you release a generic batch?", "<p>Typical release testing takes 3 to 10 business days on Standard, 3 to 5 on Priority, and 1 to 3 on Critical. You see the date before you ship.</p>"),
        ("Do you test nitrosamines and NDSRIs?", "<p>Yes. We start with a risk assessment, then use LC-MS/MS methods with limits matched to the current acceptable intake for each impurity.</p>"),
        ("Can you take over a method from our in-house lab?", "<p>Yes. We verify compendial methods and transfer validated in-house methods with a written protocol and acceptance criteria agreed before testing.</p>"),
        ("Do you support f2 dissolution comparisons?", "<p>Yes. We run comparative profiles in multiple media and calculate f2, with bootstrap analysis when variability is high.</p>"),
        ("Can you run Zone IVb stability?", "<p>Yes, at 30 °C / 75% RH alongside Zone II conditions, with one pull schedule across sites.</p>"),
        ("Do you sign quality agreements?", "<p>Yes. Every client gets a quality agreement that sets out responsibilities for OOS, deviations, change control and data retention.</p>"),
        ("What does release testing cost?", "<p>It depends on the monograph and tier. The <a href='/tools/quote-estimator.html'>Instant Quote Estimator</a> gives an indicative band in a minute.</p>")],
  sci="ananya", split="pharma-pills-mix", gal=["inst-dissolution", "inst-hplc", "lab-corridor"], band="pharma-blisters2"),

"biosimilars": dict(
  chips=[("2 labs", "one comparability report"), ("ICH Q5E", "comparability logic"), ("15+", "orthogonal methods")],
  answer="Biosimilar developers must show their molecule is highly similar to a reference product that itself drifts lot to lot. PharmaCRO runs charge, size, glycan, structure and potency methods side by side across lots, with acceptance ranges set before data arrives, and delivers one analytical similarity report.",
  pains=[("The reference product moves.", "Reference lots bought in different markets and years vary. Your ranges must reflect that, or the argument fails.", "biologics-characterization-release",
          "Multiple reference lots tested together, with quality ranges agreed before your lots are run.", "Similarity ranges built from three or more reference lots."),
         ("Too many methods, too many vendors.", "Charge in one lab, glycans in another, potency in a third. Reconciling them takes weeks.", "biologics-characterization-release",
          "One programme across two labs on one LIMS, with one reviewer and one report.", "Comparability study cut from 14 weeks to 6 in an illustrative case."),
         ("Potency is the hardest assay.", "Cell-based potency assays are variable and slow to qualify.", "biologics-characterization-release",
          "Cell-based and binding potency assays qualified for your mechanism of action.", "Mechanism-matched potency panels."),
         ("Immunogenicity must match too.", "Regulators expect comparable immunogenicity data in the clinical programme.", "bioanalytical-immunogenicity",
          "Tiered ADA and NAb assays validated to ICH M10 principles for both products.", "Tiered ADA screen, confirm and titre.")],
  pkg=("Biosimilar Comparability Program", "A complete analytical similarity package: primary structure, higher-order structure, charge, size, glycans, potency and immunogenicity methods.",
       ["biologics-characterization-release", "bioanalytical-immunogenicity", "method-development-validation", "stability-studies"],
       [("Reference lot sourcing and range setting", 0, 2), ("Primary structure and intact MS", 1, 3), ("Charge and size variants", 1, 4), ("Glycan profiling", 2, 3), ("Potency and binding", 2, 5), ("Statistical similarity report", 6, 2)], 8, "biologics-characterization-release"),
  case=("14 to 6 weeks", "Biosimilar developer shortened an EMA similarity package", "<p>Charge, size, glycan and potency methods ran in parallel across two labs on the same LIMS, against three reference lots from two markets, with criteria agreed before the first injection.</p>"),
  tool="test-finder", mini="tat",
  reg=["<b>Europe.</b> The EMA guideline on similar biological medicinal products and its quality guideline set the analytical comparability expectations.",
       "<b>United States.</b> FDA reviews 351(k) applications on the totality of evidence; its guidance on comparative analytical assessment describes a risk-ranked, tiered approach.",
       "<b>Comparability after changes.</b> ICH Q5E sets the logic for showing a manufacturing change has not affected quality.",
       "<b>India.</b> CDSCO and the Department of Biotechnology publish Similar Biologics guidelines covering quality comparability."],
  svcs=["biologics-characterization-release", "bioanalytical-immunogenicity", "method-development-validation", "stability-studies", "microbiology-sterility"],
  faqs=[("How many reference lots do we need?", "<p>Enough to describe the reference product's variability. Many programmes test 6 to 10 or more over time; we start with what you have and plan the rest.</p>"),
        ("Do you use a tiered statistical approach?", "<p>Yes. Attributes are risk-ranked; the most critical get equivalence testing, others quality ranges or visual comparison.</p>"),
        ("Which mass spectrometry do you run?", "<p>Intact and subunit mass, peptide mapping with LC-MS/MS and released glycan analysis.</p>"),
        ("Can you develop our potency assay?", "<p>Yes. We develop and qualify cell-based or binding assays that reflect the mechanism of action.</p>"),
        ("Do you support FDA and EMA filings?", "<p>We provide data and reports formatted for CTD Module 3. Regulatory strategy stays with your team.</p>"),
        ("Can you handle post-approval comparability?", "<p>Yes, under ICH Q5E, for site moves, scale changes and process updates.</p>")],
  sci="elena", split="lab-instrument-load", gal=["inst-lcms", "lab-automation", "bio-cells-pink"], band="lab-instrument-bench"),

"biotech-startups": dict(
  chips=[("1 call", "to scope your programme"), ("Phase-appropriate", "rigour"), ("0", "internal lab needed")],
  answer="Early biotechs usually have no internal lab, a small team and a board deadline. PharmaCRO gives you a scientist to talk to, phase-appropriate packages that do not over-validate, and one portal for every result, so you can generate IND or IMPD quality data without building a QC department.",
  pains=[("No lab, no QC team.", "You have a molecule and a CMO, but nobody to own analytical work.", "method-development-validation",
          "A named client scientist who scopes the work, writes the plan and stays with you through Phase 1.", "Scoping call within 48 hours."),
         ("Every pound counts.", "Full ICH validation in Phase 1 burns cash you need for the clinic.", "method-development-validation",
          "Phase-appropriate methods: qualified for Phase 1, validated before Phase 3 and commercial.", "Phase 1 packages priced for seed-stage budgets."),
         ("The board wants a date.", "Missing an IND date can mean missing a financing milestone.", "stability-studies",
          "A Gantt plan before you sign, with release and stability started in parallel.", "Indicative timelines shown on every quote."),
         ("Investors and partners will audit you.", "Due diligence asks how your data was generated.", "regulatory-data-integrity-support",
          "ALCOA+ controls, audit trails and inspection-ready data from the first sample.", "Data packages ready for partner diligence.")],
  pkg=("IND/IMPD Starter Package", "Method qualification, Phase 1 release of drug substance and drug product, and the first stability timepoints.",
       ["method-development-validation", "small-molecule-qc-release", "stability-studies", "microbiology-sterility"],
       [("Scoping call and plan", 0, 1), ("Method development", 0, 4), ("Method qualification (phase-appropriate)", 3, 3), ("DS and DP release", 6, 2), ("Stability set-up, T0 to T3 months", 7, 13)], 20, "method-development-validation"),
  case=("6 weeks", "Seed-stage biotech reached first-in-human release in six weeks", "<p>A two-person CMC team needed qualified methods and Phase 1 release for an IND. A single plan covered development, qualification and release, with stability started the same week.</p>"),
  tool="test-finder", mini="tat",
  reg=["<b>Phase-appropriate GMP.</b> FDA guidance on CGMP for Phase 1 investigational drugs and EU guidance on IMP quality accept that methods are qualified, not fully validated, early on.",
       "<b>United States.</b> INDs need CMC information sufficient to assure identity, quality, purity and strength for the proposed trial.",
       "<b>Europe.</b> IMPDs follow the EMA guideline on quality documentation for investigational medicinal products in clinical trials.",
       "<b>Later phases.</b> Methods are validated to ICH Q2(R2) before pivotal trials and commercial release."],
  svcs=["method-development-validation", "small-molecule-qc-release", "biologics-characterization-release", "stability-studies", "regulatory-data-integrity-support"],
  faqs=[("Do we need fully validated methods for Phase 1?", "<p>Usually not. Methods should be scientifically sound and qualified; full ICH Q2(R2) validation comes before pivotal trials.</p>"),
        ("Can you work with our CMO?", "<p>Yes. We receive samples from your CMO and share results with them through the portal, with your permission.</p>"),
        ("Will one person own our programme?", "<p>Yes. You get a named client scientist from the first call.</p>"),
        ("How do you price small programmes?", "<p>Per test or per package, with fixed-price Phase 1 packages where scope is clear.</p>"),
        ("Can you help write the CMC section?", "<p>We write the analytical sections of Module 3 from our data. Regulatory strategy remains your decision.</p>"),
        ("Is our data owned by us?", "<p>Yes. You own your data and can export raw files and reports at any time.</p>")],
  sci="arjun", split="lab-team-three", gal=["lab-bench-woman", "lab-pipette-blue", "biz-team-laptops"], band="lab-smile"),

"big-pharma": dict(
  chips=[("10", "planned sites"), ("1", "LIMS and data standard"), ("MSA", "terms ready")],
  answer="Large pharmaceutical companies use PharmaCRO for overflow capacity, regional release and specialist methods without adding vendor risk. One master service agreement, one quality agreement and one data standard cover every lab, so a method qualified once can run in India, Singapore, Europe or the US.",
  pains=[("Internal QC is full.", "Peaks in demand, site transfers and new launches outrun internal capacity.", "small-molecule-qc-release",
          "Reserved capacity under an MSA, with committed monthly volumes and service levels.", "Monthly service reviews with named owners."),
         ("Every vendor is an audit.", "Qualifying many small labs costs procurement and QA time.", "regulatory-data-integrity-support",
          "One quality system across the network, so one audit programme covers every site.", "Vendor qualification pack available on request."),
         ("Global products, regional regulators.", "Release in India, the EU and the US each brings its own expectations.", "stability-studies",
          "Regional labs close to your plants and regulators, all on the same SOPs.", "Labs planned across four regions."),
         ("Data must flow into your systems.", "Emailed PDFs do not fit a modern QMS or LIMS.", "regulatory-data-integrity-support",
          "REST API and webhooks into your LIMS, QMS and ERP, with Part 11 aligned records.", "API documented for integration teams.")],
  pkg=("Global Overflow and Release Programme", "Reserved capacity for routine release and stability across regions, with method transfer handled once.",
       ["small-molecule-qc-release", "stability-studies", "method-development-validation", "microbiology-sterility", "environmental-monitoring"],
       [("MSA and quality agreement", 0, 3), ("Method transfer to hub lab", 2, 4), ("Network rollout to regional labs", 5, 3), ("Routine release under SLA", 7, 5), ("Quarterly business review", 11, 1)], 12, "small-molecule-qc-release"),
  case=("1 audit", "Global manufacturer qualified a network instead of five labs", "<p>A multinational used one audit programme and one quality agreement to cover several regional sites, then moved overflow release across them as demand shifted.</p>"),
  tool="cost-of-delay-calculator", mini="delay", delay=500000,
  reg=["<b>Outsourced activities.</b> EU GMP Chapter 7 and FDA 21 CFR 211 require written agreements and oversight of contract laboratories.",
       "<b>Data integrity.</b> FDA, MHRA, WHO and PIC/S guidance all expect ALCOA+ controls at contract labs as at your own sites.",
       "<b>Electronic records.</b> 21 CFR Part 11 and EU GMP Annex 11 govern electronic records and signatures in shared systems.",
       "<b>Methods.</b> USP &lt;1224&gt; describes approaches to transfer of analytical procedures between sites."],
  svcs=["small-molecule-qc-release", "stability-studies", "biologics-characterization-release", "microbiology-sterility", "environmental-monitoring", "regulatory-data-integrity-support"],
  faqs=[("Can you work under our MSA template?", "<p>Yes. We can work from your paper or ours, with a separate quality agreement.</p>"),
        ("Can we audit you?", "<p>Yes. Book an audit through the portal; a quality lead confirms within 48 hours.</p>"),
        ("Do you integrate with our LIMS?", "<p>Yes, through a REST API and webhooks. See <a href='/technology/api-and-integrations.html'>API and integrations</a>.</p>"),
        ("How do you transfer methods across sites?", "<p>Once, with a protocol, then network-wide on shared SOPs and instruments.</p>"),
        ("Can you reserve capacity?", "<p>Yes, with committed monthly volumes under an MSA.</p>"),
        ("Who is our single point of contact?", "<p>A named account scientist and a quality lead.</p>")],
  sci="helen", split="lab-corridor", gal=["lab-automation", "data-dashboard", "biz-team-laptops"], band="corp-skyline"),

"cdmos": dict(
  chips=[("White-label", "reports on request"), ("Priority", "tier for client batches"), ("Shared portal", "access for your clients")],
  answer="CDMOs carry their clients' timelines. PharmaCRO adds release, stability and specialist testing capacity behind your own QC, with reports that can go straight to your client, shared portal access and turnaround tiers that protect batch dates you have already promised.",
  pains=[("Your clients' deadlines are your deadlines.", "A late test result becomes your late delivery.", "small-molecule-qc-release",
          "Priority and Critical tiers with dates shown before samples ship.", "Turnaround promise with fee credit if missed."),
         ("Specialist methods you do not own.", "Clients ask for mass spectrometry, E&amp;L or mRNA assays you cannot justify buying.", "extractables-leachables",
          "Specialist methods from the network, delivered under your quality agreement.", "Full menu from small molecule to cell and gene therapy."),
         ("Tech transfer never ends.", "Every new client brings new methods.", "method-development-validation",
          "Method transfer and verification with protocols your clients can approve.", "Transfer protocols templated across labs."),
         ("Your cleanrooms are always being watched.", "Annex 1 raised expectations for environmental monitoring.", "environmental-monitoring",
          "EM, water and gas testing with trending built in.", "Trend reports aligned to your contamination control strategy.")],
  pkg=("Tech Transfer Package", "Method transfer, comparative testing and first batch release for a new client product.",
       ["method-development-validation", "small-molecule-qc-release", "extractables-leachables", "environmental-monitoring"],
       [("Method review and gap check", 0, 1), ("Transfer protocol approval", 1, 1), ("Comparative testing", 2, 3), ("Transfer report", 5, 1), ("First batch release", 6, 2)], 8, "method-development-validation"),
  case=("2 days", "CDMO protected a client ship date with Critical-tier release", "<p>An equipment failure took a CDMO's HPLC capacity offline the week of a client shipment. Samples were released on the Critical tier within two days.</p>"),
  tool="cost-of-delay-calculator", mini="delay", delay=120000,
  reg=["<b>Quality agreements.</b> FDA guidance on contract manufacturing arrangements and EU GMP Chapter 7 expect clear written responsibilities in every chain.",
       "<b>Contamination control.</b> EU GMP Annex 1 (revised 2022, in force since August 2023) requires a documented contamination control strategy for sterile manufacturing.",
       "<b>Method transfer.</b> USP &lt;1224&gt; and WHO guidance describe comparative testing, co-validation and waivers.",
       "<b>Extractables and leachables.</b> USP &lt;1663&gt; and &lt;1664&gt; set the framework for packaging assessments."],
  svcs=["method-development-validation", "small-molecule-qc-release", "extractables-leachables", "environmental-monitoring", "microbiology-sterility", "stability-studies"],
  faqs=[("Can reports go directly to our client?", "<p>Yes, with your permission, through shared portal access.</p>"),
        ("Do you offer white-label reports?", "<p>On request, provided the testing lab remains identifiable for regulatory purposes.</p>"),
        ("How quickly can you take an urgent batch?", "<p>Critical tier: 24 to 72 hours for many routine tests, subject to method availability.</p>"),
        ("Do you support Annex 1 environmental monitoring?", "<p>Yes. Viable and non-viable monitoring, water and gas testing, and trend reports.</p>"),
        ("Can you hold reserved capacity for us?", "<p>Yes, under an MSA with committed volumes.</p>"),
        ("Who signs the CoA?", "<p>Our QA approves our results; your QP or QA releases the product.</p>")],
  sci="arjun", split="lab-automation", gal=["room-clean-1", "lab-instrument-bench", "log-warehouse"], band="room-clean-2"),

"vaccine-makers": dict(
  chips=[("mRNA + LNP", "attribute coverage"), ("Rapid", "sterility options"), ("Cold chain", "handled end to end")],
  answer="Vaccine makers test high volumes under high stakes, often with cold-chain samples and short release windows. PharmaCRO covers antigen, mRNA and lipid nanoparticle attributes, sterility and endotoxin, with cold-chain receipt logged on arrival and potency methods built for your platform.",
  pains=[("Release windows are short.", "Campaign batches must move from fill to distribution fast.", "microbiology-sterility",
          "Parallel testing plans and rapid microbiological methods where they are validated for your product.", "Release plans built backwards from the ship date."),
         ("mRNA attributes are new to most labs.", "Capping, poly(A), dsRNA and encapsulation need specialist methods.", "mrna-vaccine-testing",
          "A full mRNA-LNP attribute panel run by a specialist team.", "Integrity, capping, poly(A), dsRNA, EE% and lipid identity."),
         ("Cold-chain samples are fragile.", "A temperature excursion can void a sample and cost weeks.", "mrna-vaccine-testing",
          "Temperature traces logged on receipt, with a one-click choice to proceed, hold or resend.", "Receipt photo and temperature log within hours."),
         ("WHO prequalification is exacting.", "Products for global programmes need WHO PQ-ready data.", "stability-studies",
          "Stability and release data formatted for WHO PQ dossiers, including Zone IVb conditions.", "Zone IVb chambers planned.")],
  pkg=("Vaccine Release Programme", "Lot release testing for antigen or mRNA-LNP products, including sterility, endotoxin and stability.",
       ["mrna-vaccine-testing", "microbiology-sterility", "stability-studies", "environmental-monitoring"],
       [("Method transfer and qualification", 0, 4), ("Identity, integrity and potency", 4, 2), ("Sterility and endotoxin", 4, 2), ("Release report", 6, 1), ("Stability pulls", 6, 6)], 12, "mrna-vaccine-testing"),
  case=("5 attributes", "mRNA developer consolidated five vendors into one panel", "<p>An mRNA developer was sending integrity, capping, poly(A), dsRNA and EE% to different labs. One panel on one LIMS gave one report and consistent trending.</p>"),
  tool="endotoxin-limit-calculator", mini="tat",
  reg=["<b>WHO.</b> WHO prequalification of vaccines and WHO guidance on mRNA vaccine quality set expectations for global supply.",
       "<b>Europe.</b> Official Control Authority Batch Release (OCABR) applies to many vaccines in the EU, on top of the manufacturer's own testing.",
       "<b>United States.</b> Biologics are licensed by FDA CBER; lot release protocols may be required.",
       "<b>India.</b> Vaccine lots are tested and released through the Central Drugs Laboratory, Kasauli, under CDSCO."],
  svcs=["mrna-vaccine-testing", "microbiology-sterility", "stability-studies", "biologics-characterization-release", "environmental-monitoring"],
  faqs=[("Which mRNA attributes do you test?", "<p>Integrity, 5' capping, poly(A) tail length, residual dsRNA, residual DNA template, LNP size, PDI, encapsulation efficiency and lipid identity and purity.</p>"),
        ("Do you offer rapid sterility?", "<p>Where a rapid method is validated for your product. Compendial sterility remains the reference.</p>"),
        ("How do you handle cold-chain samples?", "<p>We log the temperature trace on receipt and alert you to any excursion with a choice to proceed, hold or resend.</p>"),
        ("Can you support WHO PQ dossiers?", "<p>Yes, with data formatted for WHO PQ including Zone IVb stability.</p>"),
        ("Do you test endotoxin with recombinant reagents?", "<p>Yes, both LAL and recombinant factor C, validated for your product.</p>"),
        ("Can you develop a potency assay?", "<p>Yes, including in vitro translation for mRNA and antigen ELISA for protein vaccines.</p>")],
  sci="kenji", split="vax-vials", gal=["vax-virus", "lab-cleanroom-suit", "log-plane"], band="lab-cleanroom-suit"),

"api-manufacturers": dict(
  chips=[("ICH Q3A, Q3D", "impurity coverage"), ("Q3C", "residual solvents"), ("DMF", "ready data")],
  answer="API manufacturers sell impurity profiles as much as molecules. Every customer and regulator reads your related substances, residual solvents, elemental impurities and nitrosamine data. PharmaCRO runs those methods to ICH limits, with data packages ready for your Drug Master File and your customers' audits.",
  pains=[("Every customer audits your impurities.", "Each formulator asks for the same data in a slightly different format.", "small-molecule-qc-release",
          "One impurity package in a standard format, shared through the portal.", "Shared data packages with access control."),
         ("Nitrosamines start in the process.", "Reagents, solvents and recovered materials can generate nitrosamines.", "small-molecule-qc-release",
          "Process risk assessment plus LC-MS/MS or GC-MS confirmatory testing.", "Risk assessment in 48 hours."),
         ("Polymorphs decide performance.", "A form change can alter dissolution and stability.", "reference-standards-excipients",
          "XRPD, DSC and particle size methods to control solid form.", "XRPD form screening on request."),
         ("Genotoxic impurities need trace methods.", "ICH M7 limits demand ppm-level sensitivity.", "method-development-validation",
          "Trace methods developed and validated to M7 thresholds.", "GC-MS and LC-MS/MS trace methods.")],
  pkg=("API Impurity and DMF Package", "Related substances, residual solvents, elemental impurities, nitrosamines and solid form for a Drug Master File.",
       ["small-molecule-qc-release", "method-development-validation", "reference-standards-excipients", "stability-studies"],
       [("Impurity risk assessment (Q3A, M7, nitrosamines)", 0, 1), ("Method development and validation", 1, 4), ("Batch analysis, three batches", 4, 2), ("Solid form (XRPD)", 4, 1), ("Stability set-up", 6, 2)], 8, "small-molecule-qc-release"),
  case=("3 batches", "API maker filed a DMF update after an M7 review", "<p>A process change introduced a potential mutagenic impurity. A trace LC-MS/MS method was developed and validated, and three batches tested for the DMF amendment.</p>"),
  tool="nitrosamine-risk-assessor", mini="delay", delay=60000,
  reg=["<b>Impurities.</b> ICH Q3A covers impurities in new drug substances, Q3C residual solvents, Q3D elemental impurities and M7 mutagenic impurities.",
       "<b>GMP for APIs.</b> ICH Q7 sets GMP for active pharmaceutical ingredients, including laboratory controls.",
       "<b>Master files.</b> FDA Type II DMFs and the European ASMF and CEP procedures (EDQM) rely on robust analytical data.",
       "<b>India.</b> API exporters follow CDSCO requirements plus the importing country's rules."],
  svcs=["small-molecule-qc-release", "method-development-validation", "reference-standards-excipients", "stability-studies", "regulatory-data-integrity-support"],
  faqs=[("Do you test all ICH Q3D elements?", "<p>Yes, by ICP-MS, based on your risk assessment and the route of administration.</p>"),
        ("Can you develop ICH M7 trace methods?", "<p>Yes, with LC-MS/MS or GC-MS at the thresholds your assessment requires.</p>"),
        ("Do you run residual solvents?", "<p>Yes, by headspace GC to USP &lt;467&gt; and ICH Q3C.</p>"),
        ("Can you support a CEP application?", "<p>We generate the analytical data and reports; submission stays with you.</p>"),
        ("Do you characterise polymorphs?", "<p>Yes, with XRPD and supporting thermal methods.</p>"),
        ("Can customers see our results directly?", "<p>Yes, through controlled portal sharing you approve.</p>")],
  sci="ananya", split="lab-flasks-pour", gal=["inst-gc", "inst-icp", "lab-glassware"], band="lab-cylinders"),

"excipient-packaging-suppliers": dict(
  chips=[("USP, EP, JP", "monographs"), ("USP <661>", "packaging"), ("E&L", "studies")],
  answer="Excipient and packaging suppliers are audited by every customer's QA. PharmaCRO tests excipients against USP, Ph. Eur., JP and IP monographs, qualifies packaging to USP <661> and runs extractables studies, so you can hand customers one trusted data set instead of answering the same questions again.",
  pains=[("Your customers' auditors are your auditors.", "Each pharmaceutical customer asks for its own data and certificates.", "reference-standards-excipients",
          "Independent compendial testing with certificates your customers recognise.", "Monograph testing across USP, EP, JP and IP."),
         ("Harmonised monographs still differ.", "A test that passes USP may need extra work for EP or JP.", "reference-standards-excipients",
          "Multi-compendial testing in one run where monographs allow.", "Pharmacopoeial Discussion Group texts tracked."),
         ("Packaging must prove it is safe.", "Glass, polymers and elastomers each have their own chapter.", "extractables-leachables",
          "USP &lt;660&gt;, &lt;661.1&gt; and &lt;661.2&gt; testing and extractables profiles.", "Extractables by GC-MS, LC-MS and ICP-MS."),
         ("Adulteration is a real risk.", "Glycerin and propylene glycol contamination incidents have caused deaths.", "reference-standards-excipients",
          "Identity and DEG/EG testing on every lot you choose.", "DEG/EG limit tests per current monographs.")],
  pkg=("Supplier Qualification Package", "Compendial testing, packaging qualification and an extractables profile your customers can rely on.",
       ["reference-standards-excipients", "extractables-leachables", "microbiology-sterility"],
       [("Monograph testing (USP, EP, JP)", 0, 2), ("Microbial limits", 0, 2), ("USP <661> packaging tests", 1, 3), ("Extractables profile", 2, 6), ("Summary report for customers", 8, 1)], 9, "reference-standards-excipients"),
  case=("1 data set", "Excipient supplier answered 12 customer questionnaires with one report", "<p>A supplier used one multi-compendial testing report and one extractables profile to respond to a year of customer audit requests.</p>"),
  tool="method-search-compare", mini="tat",
  reg=["<b>Excipients.</b> IPEC-PQG GMP guidance and EU guidelines on risk assessment for excipients shape what customers expect.",
       "<b>Packaging.</b> USP &lt;660&gt; (glass), &lt;661.1&gt; and &lt;661.2&gt; (plastics) and &lt;381&gt; (elastomeric closures) define packaging tests; &lt;1663&gt; and &lt;1664&gt; cover E&amp;L.",
       "<b>Contamination.</b> USP and Ph. Eur. include DEG and EG limit tests for at-risk excipients such as glycerin and propylene glycol.",
       "<b>Harmonisation.</b> The Pharmacopoeial Discussion Group (USP, Ph. Eur., JP, with IP joining in 2023) harmonises key monographs."],
  svcs=["reference-standards-excipients", "extractables-leachables", "microbiology-sterility", "small-molecule-qc-release"],
  faqs=[("Which pharmacopoeias do you test to?", "<p>USP-NF, Ph. Eur., JP and IP, plus customer-specific specifications.</p>"),
        ("Do you test for DEG and EG?", "<p>Yes, by GC per the current monographs.</p>"),
        ("Can you test packaging components?", "<p>Yes: glass, plastics and elastomers to the relevant USP chapters, plus container closure integrity.</p>"),
        ("Do you run extractables studies?", "<p>Yes, with controlled extraction and GC-MS, LC-MS and ICP-MS analysis.</p>"),
        ("Can your report go to our customers?", "<p>Yes, through the portal or as a signed PDF.</p>"),
        ("Do you qualify reference standards?", "<p>Yes, including in-house working standards against primary standards.</p>")],
  sci="lukas", split="pharma-capsules", gal=["lab-vials-bw", "lab-glassware", "inst-gc"], band="pharma-tubes"),
}

def ind_page(key, name, line, img):
    D = IND[key]
    pkg = D["pkg"]
    mini = MINIDELAY(D["delay"]) if D["mini"] == "delay" else TATCALC()
    others = [(im, n, l, f"/industries/{k}.html") for k, n, l, im in INDUSTRIES if k != key][:4]
    body = (ANSWER(D["answer"])
            + SPLIT(D["split"], H2(line) + P(D["answer"].split(". ")[0] + ".") + TICKLIST([SVC[s][1] for s in D["svcs"][:4]]) + SCICARD(D["sci"], True))
            + SH("Pain points", "What gets in the way, and what we do about it.", "Scroll: each problem fades into our answer.")
            + PAINS(D["pains"])
            + SH("Package", "One plan for the whole job.", "One quote, one timeline, one portal.")
            + PACKAGE(*pkg)
            + GALLERY(D["gal"])
            + SH("Story and tools", "Proof, and a tool to plan with.")
            + '<div class="two"><div>' + CHIP(*D["case"]) + P(f'Most used tool for {name.lower()}: <a href="/tools/{D["tool"]}.html">{TOOLN[D["tool"]]}</a>.') + SCICARD(D["sci"]) + '</div><div>' + mini + '</div></div>'
            + BAND(D["band"], "Regulators read your data. We write it to be read.", "The rules that shape testing for " + name.lower() + ", in plain words.")
            + SH("Regulatory context", "What your regulators expect.", "General information, not regulatory advice. Check the current text before acting.")
            + '<div class="ind-reg">' + "".join(f'<p class="reveal">{r}</p>' for r in D["reg"]) + '</div>' + REGBADGES()
            + SH("Services", f"The services {name.lower()} use most.") + SVCGRID(only=D["svcs"], filters=False)
            + SH("FAQ", "Questions we hear from " + name.lower() + ".") + FAQS(D["faqs"], "faq-" + key)
            + SH("Other industries", "See how we work with others.") + MOSAIC(others))
    page(f"industries/{key}", name, line + " " + D["answer"].split(". ")[0] + ".", body, img=img, chips=D["chips"], eyebrow="Industries",
         crumbs=IC, cta=(f"{pkg[0]}: get a quote for your next batch.", "Tell us the product and the date. A scientist replies within 4 business hours with a plan and a price.", img))

for k, n, l, im in INDUSTRIES:
    ind_page(k, n, l, im)

# ---------------------------------------------------------------- hub
def TILES():
    t = "".join(f'<button class="ind-t reveal" type="button" style="--i:{i};--bg:url(/img/{im}.jpg)" data-k="{k}" aria-controls="ind-pv"><span><b>{n}</b><em>{l}</em></span></button>' for i, (k, n, l, im) in enumerate(INDUSTRIES))
    tp = "".join(f'<template data-k="{k}"><img src="/img/{im}.jpg" alt="{alt(im)}"><div><p class="ey">Industry</p><h3>{n}</h3><p class="ind-pl">{l}</p><p>{IND[k]["answer"]}</p>'
                 f'<ul>{"".join(f"<li>{SVC[s][1]}</li>" for s in IND[k]["svcs"][:4])}</ul><p class="ind-pk">Recommended: <b>{IND[k]["pkg"][0]}</b></p>'
                 f'<p><a class="btn" href="/industries/{k}.html">Open the {n.lower()} page</a> <button type="button" class="btn o ind-close">Back to all</button></p></div></template>' for k, n, l, im in INDUSTRIES)
    return f'<div class="ind-tiles"><div class="ind-tg">{t}</div><div class="ind-pv" id="ind-pv" hidden tabindex="-1"></div>{tp}</div>'

def MATCHER():
    a = [("small", "Small-molecule medicines or APIs"), ("bio", "Biologics or biosimilars"), ("vax", "Vaccines or mRNA"), ("ing", "Excipients or packaging")]
    b = [("mfr", "A manufacturer with my own QC lab"), ("nolab", "A developer with no internal lab"), ("cdmo", "A contract manufacturer"), ("global", "A global company with many sites"), ("api", "A supplier of active ingredients")]
    sel = lambda n, o: f'<select data-m="{n}"><option value="">Choose</option>' + "".join(f'<option value="{k}">{t}</option>' for k, t in o) + "</select>"
    names = json.dumps({k: n for k, n, _, _ in INDUSTRIES})
    return (f'<div class="ind-match reveal" data-n="{html.escape(names)}"><h3>Which are you?</h3><div class="ind-m-in"><label><span>We make</span>{sel("a", a)}</label>'
            f'<label><span>We are</span>{sel("b", b)}</label></div><p class="ind-m-o" aria-live="polite">Choose both to see your page.</p></div>')

cmp_rows = [[f'<a href="/industries/{k}.html">{n}</a>', l, IND[k]["pkg"][0], SVC[IND[k]["pkg"][5]][1], TOOLN[IND[k]["tool"]]] for k, n, l, im in INDUSTRIES]
hub = (ANSWER("PharmaCRO serves eight kinds of medicine makers and their suppliers. Each faces a different pressure: launch windows for generics, similarity for biosimilars, cash for startups, capacity for big pharma, client deadlines for CDMOs, release windows for vaccines, impurities for APIs and audits for suppliers. Pick yours to see the package built for it.")
       + SH("Segments", "Choose your industry.", "Select a tile to preview it here, then open the full page.")
       + TILES()
       + '<div class="two" style="margin-top:40px"><div>' + MATCHER() + '</div><div>' + IMG("lab-team-three", "One network, eight ways of working.") + '</div></div>'
       + SH("Compare", "Eight segments side by side.")
       + T(["Industry", "Main pressure", "Recommended package", "Lead service", "Most used tool"], cmp_rows)
       + STRIP([im for _, _, _, im in INDUSTRIES] + ["lab-corridor", "inst-hplc"])
       + SH("By stage", "Or start from where your product is.", "Testing needs change from discovery to post-approval.")
       + MOSAIC([("lab-microscope-close", n, d, f"/solutions/{k}.html") for k, n, d in STAGES])
       + FAQS([("Do you work with companies outside these eight segments?", "<p>Yes. Medical device makers with drug components, nutraceutical companies with pharmaceutical claims and academic groups also use us. <a href='/book-a-call.html'>Talk to a scientist</a>.</p>"),
               ("Is the testing different by industry?", "<p>The methods are often the same. What changes is the package, the turnaround tier and the regulatory context.</p>"),
               ("Can one company use several packages?", "<p>Yes. Many clients combine release, stability and specialist work under one MSA.</p>")], "faq-ind"))
page("industries/index", "Built around how you make medicines.", "Eight kinds of medicine makers, eight sets of pressures. See the package and tools built for yours.", hub,
     img="lab-team-three", eyebrow="Industries", chips=[("8", "segments served"), ("12", "service lines"), ("1", "portal for all")],
     cta=("Tell us what you make. We will tell you what to test.", "A scientist replies within 4 business hours with a recommended package and a price."))

# ---------------------------------------------------------------- stages
ST = {
"discovery": dict(
  img="lab-microscope-close", rig="Discovery methods are fit for purpose, not validated. The aim is reliable enough data to choose a candidate.",
  ans="At discovery, testing answers one question: is this candidate worth developing? You need identity, purity, early stability and solid-form data that are quick and scientifically sound, not validated to ICH Q2(R2). PharmaCRO runs fit-for-purpose methods fast, and designs them so they can grow into validated methods later.",
  tests=["Identity and purity screens (LC-MS, NMR by partner)", "Early forced degradation", "Solid form screening (XRPD)", "Solubility and early dissolution", "Reference standard characterisation"],
  gantt=[("Candidate identity and purity", 0, 1), ("Forced degradation screen", 1, 2), ("Solid form screen", 1, 2), ("Reference material characterisation", 2, 2)], wk=5,
  deliv=["Short technical report per candidate", "Raw data in the portal", "Method notes that feed later development"],
  rows=[["Identity and purity", "5 to 20 mg", "3 to 5 days"], ["Forced degradation", "50 to 100 mg", "1 to 2 weeks"], ["XRPD form screen", "20 to 50 mg", "3 to 7 days"]],
  svcs=["reference-standards-excipients", "method-development-validation", "small-molecule-qc-release"],
  faqs=[("Do discovery methods need validation?", "<p>No. They should be scientifically sound and documented, so they can be developed further.</p>"),
        ("How little material can you work with?", "<p>Often a few milligrams for identity and purity; more for degradation and form studies.</p>"),
        ("Will discovery data be used in a filing?", "<p>Usually as supporting information. Pivotal data comes from qualified or validated methods later.</p>")]),
"preclinical": dict(
  img="lab-bench-woman", rig="Preclinical methods are qualified: shown to be suitable for the tox batch, but not fully validated.",
  ans="Preclinical testing supports the toxicology batch and the first stability data. Methods are qualified rather than fully validated, and the batch used in GLP toxicology studies must be characterised well enough to link it to clinical material later. PharmaCRO qualifies methods, releases tox batches and starts stability early.",
  tests=["Method development and qualification", "Tox batch characterisation and release", "Dose formulation analysis support", "Early stability (accelerated and long-term)", "Biologics: primary structure, charge and size"],
  gantt=[("Method development", 0, 3), ("Method qualification", 2, 2), ("Tox batch release", 4, 1), ("Stability T0 to T3 months", 4, 13)], wk=17,
  deliv=["Qualification reports", "Tox batch certificate of analysis", "Stability protocol and early timepoints"],
  rows=[["Tox batch release (small molecule)", "1 to 5 g", "5 to 10 days"], ["Biologic characterisation panel", "5 to 10 mg", "2 to 3 weeks"], ["Stability per timepoint", "Per protocol", "5 to 10 days after pull"]],
  svcs=["method-development-validation", "biologics-characterization-release", "stability-studies", "bioanalytical-immunogenicity"],
  faqs=[("Are your labs GLP-certified?", "<p>Our planned network operates to GMP; GLP status will be shown per site when held. Many tox batch characterisations are done under GMP and referenced by the GLP study.</p>"),
        ("Why characterise the tox batch carefully?", "<p>The impurity profile of the tox batch qualifies the impurities you may see in clinical batches.</p>"),
        ("When should stability start?", "<p>As soon as the tox batch is made, so you have data before the first clinical batch.</p>")]),
"clinical-phase-1-3": dict(
  img="lab-pipette-blue", rig="Phase 1 methods: fit for purpose, not fully validated. Methods are validated to ICH Q2(R2) before pivotal (Phase 3) and commercial use.",
  ans="Clinical-stage testing grows with the programme. In Phase 1, qualified methods release clinical batches and support an IND or IMPD. By Phase 3, methods should be validated to ICH Q2(R2), specifications tightened and stability running on registration batches. PharmaCRO plans that progression from the start.",
  tests=["Clinical batch release (DS and DP)", "ICH stability on clinical and registration batches", "Method validation before Phase 3", "Bioanalytical PK and immunogenicity", "Specification setting support"],
  gantt=[("Phase 1 release", 0, 2), ("Phase 1 stability", 1, 10), ("Method validation", 6, 6), ("Phase 3 registration batch release", 12, 2), ("Registration stability", 13, 11)], wk=24,
  deliv=["CoAs for each clinical batch", "Validation reports to ICH Q2(R2)", "Stability reports for the dossier", "Analytical sections for CTD Module 3"],
  rows=[["Clinical batch release", "Per specification", "5 to 10 days"], ["Method validation", "10 to 50 g", "3 to 6 weeks"], ["PK sample analysis", "100 to 250 µL plasma", "1 to 3 weeks"]],
  svcs=["small-molecule-qc-release", "stability-studies", "method-development-validation", "bioanalytical-immunogenicity", "biologics-characterization-release"],
  faqs=[("When must methods be fully validated?", "<p>Before pivotal trials and commercial release. Phase 1 methods should be qualified and scientifically sound.</p>"),
        ("Can specifications change during development?", "<p>Yes. They usually tighten as data from more batches accumulates.</p>"),
        ("Do you analyse clinical PK samples?", "<p>Yes, with LC-MS/MS and ligand binding methods validated to ICH M10 principles.</p>")]),
"commercial-release": dict(
  img="inst-hplc", rig="Commercial release uses fully validated methods, registered specifications and strict change control.",
  ans="Commercial release is routine, high-volume and unforgiving. Every batch needs testing against the registered specification with validated methods, on a predictable timeline. PharmaCRO offers reserved capacity, turnaround tiers with dates shown before shipment, and e-signed CoAs released through the portal.",
  tests=["Routine release to registered specification", "Microbiology and sterility", "Environmental monitoring support", "Raw material and excipient release", "OOS investigation support"],
  gantt=[("Sample receipt and login", 0, 1), ("Chemical testing", 0, 1), ("Microbiology (sterility 14 days)", 0, 3), ("QA review and CoA", 3, 1)], wk=4,
  deliv=["E-signed CoA per batch", "Full data package on request", "Monthly service and trend review"],
  rows=[["Tablet release (assay, RS, dissolution)", "20 to 60 units", "3 to 10 days"], ["Sterility (membrane filtration)", "20 containers typical", "14 days incubation"], ["Endotoxin", "3 to 5 units", "1 to 3 days"]],
  svcs=["small-molecule-qc-release", "microbiology-sterility", "environmental-monitoring", "reference-standards-excipients", "biologics-characterization-release"],
  faqs=[("How do you guarantee turnaround?", "<p>Tiers with dates shown before shipment; if we miss the date, the fee for that test is credited (subject to commercial approval).</p>"),
        ("Who releases the batch?", "<p>We approve our results; your QP or QA releases the product.</p>"),
        ("What happens with an OOS?", "<p>We follow a phased investigation and you hear from the responsible scientist the same day.</p>")]),
"post-approval-stability": dict(
  img="lab-corridor", rig="Post-approval work follows the registered stability commitment and ICH Q12 lifecycle principles for changes.",
  ans="After approval, testing protects the licence. You need ongoing stability on commercial batches, data to support site, supplier and process changes, and fast answers when a trend appears. PharmaCRO runs annual stability programmes, comparability for changes and trend analysis across every lab on one LIMS.",
  tests=["Ongoing and annual stability commitments", "Comparability for post-approval changes", "Out-of-trend analysis", "Method lifecycle management (ICH Q14)", "Supplier change testing"],
  gantt=[("Annual batch on stability", 0, 1), ("3-month pull", 3, 1), ("6-month pull", 6, 1), ("9-month pull", 9, 1), ("12-month pull and annual report", 12, 1)], wk=13,
  deliv=["Stability reports per pull", "Trend and shelf-life regression", "Comparability reports for variations"],
  rows=[["Stability timepoint", "Per protocol", "5 to 10 days after pull"], ["Comparability study", "3 batches pre and post change", "4 to 8 weeks"], ["OOT investigation support", "Existing data", "1 to 2 weeks"]],
  svcs=["stability-studies", "regulatory-data-integrity-support", "reference-standards-excipients", "method-development-validation"],
  faqs=[("What is an ongoing stability programme?", "<p>At least one commercial batch a year per strength and pack, tested through shelf life, as required by GMP.</p>"),
        ("Can you take over an existing stability study?", "<p>Yes, with a transfer plan for samples, chambers and methods.</p>"),
        ("How do you spot trends early?", "<p>Every result is trended in the LIMS; out-of-trend flags go to the responsible scientist.</p>")]),
}

for k, n, d in STAGES:
    D = ST[k]
    i = [s[0] for s in STAGES].index(k)
    nxt = STAGES[(i + 1) % len(STAGES)]
    body = (ANSWER(D["ans"])
            + f'<div class="ind-rig reveal">{ICON("gauge", "ic")}<div><p class="ey">Phase-appropriate rigour</p><p>{D["rig"]}</p></div></div>'
            + SPLIT(D["img"], H2("What your product needs now") + TICKLIST(D["tests"]))
            + SH("Timeline", "How the work fits together.") + GANTT(D["gantt"], D["wk"], f"{n}: indicative timeline")
            + '<div class="two"><div>' + H3("Deliverables") + TICKLIST(D["deliv"]) + '</div><div>' + H3("Typical samples and turnaround") + T(["Test", "Typical sample", "Typical TAT"], D["rows"]) + '</div></div>'
            + GALLERY(["lab-sample-rack", "lab-analyst-pc", "lab-glassware"])
            + SH("Services", "Services that apply at this stage.") + SVCGRID(only=D["svcs"], filters=False)
            + SH("FAQ", "Questions at this stage.") + FAQS(D["faqs"], "faq-" + k)
            + f'<p><a class="btn o" href="/solutions/{nxt[0]}.html">Next stage: {nxt[1]} &rsaquo;</a> <a class="btn o" href="/solutions/index.html">All stages</a></p>')
    page(f"solutions/{k}", n, d + " " + D["rig"], body, img=D["img"], eyebrow="Solutions by stage", crumbs=SC,
         chips=[(n, "stage"), (str(len(D["tests"])), "core test areas"), (f'{D["wk"]} wk', "indicative plan")],
         cta=(f"Plan your {n.lower()} testing in one call.", "A client scientist will map the tests, the rigour and the timeline for your stage."))

STG_IMG = [ST[k]["img"] for k, _, _ in STAGES]
sol = (ANSWER("Testing rigour should match the stage of development. Discovery needs fast, fit-for-purpose answers; clinical work needs qualified, then validated methods; commercial release needs validated methods on a predictable clock; post-approval needs stability and change control. PharmaCRO plans the whole path so early methods grow into validated ones.")
       + LIFECYCLE()
       + SH("Phase-appropriate rigour", "How much validation, and when.")
       + T(["Stage", "Method status", "Typical focus", "Page"], [[n, ["Fit for purpose", "Qualified", "Qualified (Phase 1) to validated (Phase 3)", "Validated, registered", "Validated, under change control"][i], ST[k]["tests"][0], f'<a href="/solutions/{k}.html">Open</a>'] for i, (k, n, d) in enumerate(STAGES)])
       + MOSAIC([(STG_IMG[i], n, d, f"/solutions/{k}.html") for i, (k, n, d) in enumerate(STAGES)])
       + BAND("lab-microscopes-row", "Methods that grow with your molecule.", "Developed once, qualified early, validated on time, transferred anywhere in the network.")
       + FAQS([("Why not validate everything from the start?", "<p>It costs time and money before you know the candidate will progress, and specifications are not yet final. Regulators accept phase-appropriate methods.</p>"),
               ("What is the difference between qualified and validated?", "<p>A qualified method has evidence it is suitable for its current use; a validated method meets the full ICH Q2(R2) characteristics for its intended commercial use.</p>"),
               ("Can you take over a programme mid-stage?", "<p>Yes, with a method transfer or verification plan.</p>")], "faq-sol"))
page("solutions/index", "Testing for every stage, from first molecule to final batch.", "From discovery to post-approval stability: the testing each stage needs, and how much rigour is enough.", sol,
     img="lab-microscopes-row", eyebrow="Solutions by stage", chips=[("5", "stages"), ("1", "plan from start to licence"), ("ICH Q2(R2), Q14", "lifecycle methods")],
     cta=("Not sure what your stage needs?", "Book a scoping call and a client scientist will map it with you."))
