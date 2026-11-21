"""Resources: Insights hub + 12 articles, Regulatory Radar, case studies, webinars, whitepapers, glossary (blueprint 4.10 + section 8).
Articles are written by illustrative authors (AUTHOR() marks them); regulatory items are real public events, summarised, not advice."""
from ph import *

CATS = ["Regulatory", "Methods", "Biologics", "mRNA and Vaccines", "Quality", "Market"]
CRUMB = [("Insights", "/insights/index.html")]
ARTS = []  # filled by art(); index reads it

def art(slug, title, lede, img, cat, sci, mins, answer, keyt, sections, faqs, related=None):
    assert slug in ARTICLES, slug
    secs = "".join(f"<h2>{h}</h2>{b}" for h, b in list(sections) + EXTRA.get(slug, []))
    rel = related or []
    relh = ("<h2>Related</h2>" + UL([f'<a href="{u}">{t}</a>' for t, u in rel])) if rel else ""
    body = (AUTHOR(sci, mins) + ANSWER(answer) + KEYTAKE(keyt)
            + f'<div class="art">{TOC()}<div class="art-b">{secs}{relh}<h2>Frequently asked questions</h2>{FAQS(faqs, "af")}</div></div>')
    words = len(re.sub(r"<[^>]+>", " ", secs).split())
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": lede, "image": f"{DOMAIN}/img/{img}.jpg",
          "author": {"@type": "Person", "name": SCI[sci][0], "jobTitle": SCI[sci][1]}, "publisher": {"@type": "Organization", "name": BRAND},
          "datePublished": "2026-11-21", "dateModified": "2026-11-21", "wordCount": words, "articleSection": cat}
    page(f"insights/{slug}", title, lede, body, img=img, eyebrow=f"Insights &middot; {cat}", crumbs=CRUMB, jsonld=[ld],
         chips=[(f"{mins} min", "read"), (cat, "category")], hb="")
    ARTS.append(dict(slug=slug, title=title, lede=lede, img=img, cat=cat, sci=sci, mins=mins))

def pull(t): return f'<blockquote class="pull reveal">{t}</blockquote>'
def S(u): return svc_url(u)
def M(m): assert m in METHODS, m; return f"/method-library/{m}.html"
def TL(t): return f"/tools/{t}.html"

# extra long-form sections appended to each article by art()
EXTRA = {
 "stability-zone-ivb": [("Packaging comparison in practice",
   P("When the product is moisture sensitive, run a small packaging comparison at 40 °C / 75% RH before you commit registration batches. Three candidate packs, two months, a handful of tests: water content, dissolution and the main hydrolytic degradant. The pack that holds water content flat almost always wins on long-term too.",
     "Record the water vapour transmission rate of each pack from the supplier, then check it against your own data. Supplier figures are measured on flat film, not on formed blister cavities, and cavity corners thin out during forming.")
   + T(["Pack", "Typical moisture barrier", "When it fits"], [["PVC blister", "Low", "Robust, non-hygroscopic products"], ["PVC/PVDC blister", "Medium to high", "Moderately sensitive products"],
                                                            ["Alu-alu (cold form) blister", "Very high", "Moisture- and light-sensitive products"], ["HDPE bottle with desiccant", "High, depends on desiccant", "Bulk packs, multi-dose"]])
   + P("Treat chamber capacity as a real constraint. Zone IVb chambers fill quickly in India and Southeast Asia; book space when you book the batches, not when the batches are made."))],
 "mrna-critical-quality-attributes": [("Reference standards and controls",
   P("mRNA methods need well-characterised reference material early. A drug substance lot from an early, well-understood process is usually banked as an interim reference and replaced by a qualified primary standard before Phase 3. Characterise it with every method on the release panel and with extended characterisation such as sequencing and full-length LC-MS.",
     "System suitability controls matter as much as the standard. A capping control with a known proportion of uncapped RNA, and an integrity control with spiked fragments, show the method can still see the failures you care about on the day of analysis.")
   + P("Sample handling is the hidden variable. RNA degrades with repeated freeze-thaw and with RNase contamination, so aliquot on receipt, use RNase-free consumables and record every thaw. Many apparent integrity failures are handling artefacts.")),
  ("Stability of mRNA-LNP products",
   P("The main degradation routes are RNA hydrolysis and oxidation, lipid hydrolysis and oxidation, and particle growth or aggregation. Integrity falls first in most products; encapsulation efficiency and size follow. Stability programmes therefore track integrity, EE%, size and PDI, potency and lipid degradants at every pull point, usually at the frozen long-term condition plus a refrigerated in-use or excursion study."))],
 "method-transfer-failure": [("A worked example",
   P("A gradient HPLC related-substances method moved from a lab with a low dwell volume UHPLC to a site with a conventional HPLC. Retention times shifted later, two impurities co-eluted and the resolution criterion failed. The fix was simple: an isocratic hold at the start of the gradient in the receiving lab, permitted within the method's documented adjustment range, restored the separation.",
     "The lesson is to write allowed adjustments into the method. USP <621> describes permitted changes for chromatographic methods; quoting them in your method gives the receiving lab room to match performance without a deviation.")
   + P("Knowledge transfer is cheap and effective. A one-hour call where the sending analyst walks through sample preparation, integration and known pitfalls prevents more failures than any protocol clause. Record it and attach the notes to the transfer report.")),
  ("After the transfer",
   P("The method is not finished when the report is signed. Trend system suitability and control results at both sites for the first months, and compare them. Drift at one site is an early warning that a column, reagent or practice has diverged."))],
 "biosimilar-analytical-similarity": [("Presenting the data",
   P("Reviewers read hundreds of comparisons. Make them easy. For each attribute show the reference lots and biosimilar lots on the same plot, with the quality range drawn in. State the method, the number of lots and the acceptance approach in the caption. Explain every difference you see, even small ones, and say why it does or does not matter.",
     "Group the report by attribute class, not by method. A reviewer looking at charge variants wants icIEF, CEX and any functional data on charge-dependent activity in one place.")
   + BARS("Typical attribute counts in a similarity package (illustrative)", [("Primary and higher-order structure", 12, "~12"), ("Charge and size variants", 10, "~10"), ("Glycosylation", 14, "~14"), ("Biological function", 8, "~8")])),
  ("Common pitfalls",
   UL(["Reference lots bought too late, so expiry differences confuse degradation-related attributes.", "Methods qualified on the biosimilar only, not on the reference product.",
       "Ranges set after the data are seen.", "Functional assays with too much variability to detect a real difference."]))],
 "data-integrity-top-10-findings": [("Culture and training",
   P("Technical controls stop most problems. The rest depend on whether analysts feel safe saying 'I made a mistake'. Laboratories with strong data integrity records make errors easy to report, investigate them without blame and fix the system rather than the person.",
     "Training should use real examples: a manual integration that was fine, one that was not, and how the audit trail shows the difference. Short, frequent sessions beat an annual slide deck.")
   + P("Hybrid systems deserve special attention. When a paper logbook and an electronic system both hold parts of the record, define which is original for each data element, and reconcile them during review."))],
 "endotoxin-lal-vs-recombinant": [("Planning a switch to recombinant reagents",
   P("Switching from LAL to a recombinant reagent is a change to a validated method. Plan it like one. Run both methods side by side on representative lots, including spiked samples, and compare recovery and results against pre-set criteria. Repeat interference testing with the new reagent, because inhibition and enhancement depend on the reagent chemistry.",
     "File the change according to your regulator's variation rules. In many cases it is a minor change, but check with the authority for your product type.")
   + P("Recombinant reagents also help sustainability goals. Horseshoe crab populations are under pressure, and several companies now prefer animal-free methods where validation allows.")),
  ("Troubleshooting common problems",
   T(["Symptom", "Likely cause", "What to try"], [["Spike recovery below 50%", "Inhibition (chelation, pH, protein binding)", "Increase dilution within the MVD; adjust pH; heat treatment for proteins"],
                                                  ["Recovery above 200%", "Enhancement or glucan interference (LAL)", "Glucan-blocking buffer or a recombinant reagent"],
                                                  ["Variable results between replicates", "Pipetting, contaminated tips or tubes", "Depyrogenated consumables; check technique"]]))],
 "choosing-a-testing-partner": [("Red flags at audit",
   UL(["The lab cannot show you raw data from a recent run on the spot.", "Every analyst uses the same log-in on an instrument PC.", "Turnaround figures are quoted but not measured.",
       "The QA reviewer reports to the lab manager whose throughput they review.", "Out-of-specification results are rare to the point of being implausible.",
       "Accreditation certificates whose scope does not include the methods you need."])
   + P("None of these is automatically disqualifying, but each needs a clear answer. A good lab will be glad you asked.")),
  ("Running a fair comparison",
   P("Send each shortlisted lab the same request: the same product, tests, volume and timelines. Ask for a quote, a draft timeline and the names of the people who would run the work. Then score them on the sheet above, independently, before discussing as a team."))],
 "cgt-release-testing": [("Planning sample volumes",
   P("Cell and gene therapy material is scarce and expensive. Build a sample plan that lists every release, stability and retain test, the volume each needs, and the order in which aliquots are taken. Share it with the lab before the first batch. Methods can often be adapted to use less material if the lab knows early.")
   + T(["Test", "Typical volume or cells (indicative)"], [["Sterility (rapid)", "Product-dependent, often a few mL"], ["Mycoplasma NAT", "Small volume or cell pellet"],
                                                         ["Flow identity and purity", "Around 10⁶ cells"], ["Vector genome titre", "Tens of µL"], ["Potency", "Assay-dependent"]])
   + P("These are indicative ranges only; your product's methods set the real numbers.")),
  ("Shipping and chain of identity",
   P("Autologous samples carry the patient's identity through every step. The lab must keep chain of identity and chain of custody intact, with barcodes, two-person checks at receipt and a portal record of every handover. Shipping is usually in cryogenic dry shippers or controlled-temperature boxes with continuous logging."))],
 "el-prefilled-syringes": [("Simulation studies",
   P("Between a full extractables study and real leachables data sits the simulation study: the container is filled with a model solvent that mimics the drug product and stored under accelerated conditions. It gives an early read on likely leachables before stability samples exist, and helps choose which targeted methods to validate.")
   + P("For biologics, combine leachables results with protein quality data. A leachable at a safe level may still oxidise a methionine or seed aggregation. Correlating leachables trends with SEC and peptide mapping data shows whether the packaging is affecting the protein.")),
  ("Regional expectations",
   P("USP <1663> and <1664> describe extractables and leachables assessment. FDA and EMA both expect a risk-based approach linked to route and dose, and ICH Q3E on extractables and leachables is in development to harmonise expectations. Plan for the strictest market you will file in."))],
 "cost-of-a-delayed-batch": [("A launch example",
   P("For a launch, lost sales dominate. Imagine a product expected to sell $200,000 a day at full supply. If release testing delays first shipment by ten days, the revenue simply shifts later for most products, but for a first generic or a product with competitors launching the same week, part of it is lost for good, along with market share that is hard to win back.",
     "Even a 20% permanent loss on ten days of sales is $400,000. Against that, the premium for a Critical tier on a launch test package is small.")
   + LINE("Cumulative cost of delay (illustrative, $ thousands)", ["Day 0", "Day 2", "Day 4", "Day 6", "Day 8", "Day 10"], [("Routine batch", [0, 5, 11, 16, 22, 27]), ("Launch batch", [0, 80, 160, 240, 320, 400])])),
  ("What you can change tomorrow",
   UL(["Send samples with complete paperwork, so receipt and login take hours, not days.", "Agree specifications and methods before the batch is made.",
       "Book capacity for known peaks such as stability pulls and launches.", "Use a portal for status instead of email chains."]))],
 "state-of-pharma-testing-2027": [("Analysis plan",
   P("We will report descriptive statistics for every question, with sample sizes shown. Comparisons between regions or company types will only be reported where each group has at least 30 respondents, with confidence intervals. We will not present differences that are not statistically meaningful as findings.",
     "Free-text answers will be coded by two people independently and themes reported with example quotes, anonymised.")
   + T(["Milestone", "Planned timing"], [["Questionnaire finalised and published", "Q1 2027"], ["Fieldwork", "Q2 2027"], ["Analysis and review", "Q3 2027"], ["Report and webinar", "Q3 to Q4 2027"]])
   + P(f'Timings are plans, not commitments. {ILL("Planned")}')),
  ("Limitations we already know",
   P("Self-reported data has limits: people remember turnaround times differently from how labs measure them. Respondents who choose to answer a survey from a testing company may differ from those who do not. We will state these limits in the report rather than bury them."))],
}
_MORE = {
 "method-transfer-failure": ("What to send the receiving lab", UL(["The method, plus the development and robustness report, not just the SOP.", "Example chromatograms with integration events marked.", "Known failure modes and how they look.", "Column history: brands, lots and how many injections before performance drops.", "Reference standard certificates and storage conditions."])),
 "biosimilar-analytical-similarity": ("Timeline and sequencing", P("A full similarity package typically runs over several months. Qualify methods on both products first, then run reference and biosimilar lots in interleaved sequences so day-to-day variability affects both equally. Leave time for orthogonal follow-up: if one method shows a difference, a second method is how you decide whether it is real.", "Plan the statistics before the lab work starts, including how many lots you need for the comparison to have useful power. A plan written afterwards will be read sceptically.")),
 "data-integrity-top-10-findings": ("What good looks like on inspection day", P("Inspectors ask an analyst to show a recent result from the instrument to the CoA. In a well-run lab this takes minutes: the analyst logs in under their own name, opens the sequence, shows the audit trail, the reviewer's sign-off and the approved report. Nothing is printed, nothing is searched for, and nobody needs to call IT.", "Practise this. A quarterly retrieval drill at each site builds the habit and surfaces gaps before an inspector does.")),
 "endotoxin-lal-vs-recombinant": ("Choosing the method for your product", P("Gel-clot is simple and robust for a pass or fail answer at a single limit. Kinetic turbidimetric and chromogenic methods give quantitative results across a range and suit trending. Recombinant methods suit products with glucan interference, such as those made with cellulose-based filters, and organisations moving away from animal-derived reagents.", "Whatever you choose, keep one method per product in routine use and document the reason.")),
 "choosing-a-testing-partner": ("The commercial terms that matter", UL(["Turnaround commitments by test type, with credits if dates are missed.", "A repeat-test policy that says who pays when an OOS is lab error.", "Sample retention periods and disposal rules.", "Data ownership and access to raw data.", "Notice periods and transition help if you leave."]) + P("Put these in the MSA, not in an email thread.")),
 "cgt-release-testing": ("Potency assays: start early", P("Potency is the attribute regulators push hardest on for cell and gene therapies, and the one most often late. A potency assay should reflect the mechanism of action, show a dose response, and be precise enough to set a meaningful specification. Many programmes use a matrix of assays, for example transgene expression plus a functional readout, until one validated assay can carry release.", "Begin development in parallel with the first clinical batches, and keep retained samples to bridge old and new assays.")),
 "el-prefilled-syringes": ("Working with component suppliers", P("Ask suppliers for their extractables data, the conditions used and the materials of construction, including any changes over the last few years. Agree change notification terms: a silent change in rubber formulation or siliconisation process can invalidate your leachables data.", "Where supplier data is relevant and well documented, it can reduce your own extractables work. It does not replace leachables data in your product.")),
 "cost-of-a-delayed-batch": ("Bringing finance into the conversation", P("Testing teams often negotiate on price because price is the number procurement sees. Share the cost of delay with finance and procurement, and agree a simple rule for when a faster tier is justified. One page with the model and two worked examples is usually enough to change the conversation.", f'The <a href="{TL("quote-estimator")}">Instant Quote Estimator</a> shows how tier choice changes the price.')),
 "state-of-pharma-testing-2027": ("How to take part", P("Fieldwork will run online and take about 12 minutes. Respondents can skip any question. We will not use responses for sales contact unless a respondent asks us to, and we will publish a summary of the questionnaire before fieldwork opens so anyone can comment on it.", "If you lead QC, QA, regulatory, procurement or CMC at a pharmaceutical, biotech, CDMO or API company, we would value your view.")),
}
for _k, _v in _MORE.items(): EXTRA[_k].append(_v)

# ===================== 1. Nitrosamines =====================
art("nitrosamine-testing-2027", "Nitrosamine testing in 2027: what regulators now expect",
    "Acceptable intakes, NDSRIs, confirmatory testing and the method sensitivity regulators now assume. A practical guide for QC and regulatory teams.",
    "pharma-blisters", "Regulatory", "ananya", 11,
    "Regulators now expect a documented nitrosamine risk assessment for every marketed product, confirmatory testing wherever a risk is found, and control at or below an acceptable intake (AI). For nitrosamine drug substance-related impurities (NDSRIs), the AI usually comes from a structure-based potency category, so methods often need limits in the low ng/day range.",
    ["Risk assessment first, then confirmatory testing with a validated, sensitive method.",
     "NDSRIs are product-specific: each needs its own reference standard and often its own LC-MS/MS method.",
     "The potency category approach sets AIs from 18 to 1,500 ng/day; your limit of quantitation must sit well below the resulting specification.",
     "Root causes include nitrite in excipients, secondary amines in the API and nitrocellulose in blister lidding."],
    [("Why nitrosamines are still on every agenda",
      P("N-nitrosamines are probable human carcinogens. After NDMA was found in valsartan in 2018, regulators widened the problem from a handful of sartans to every chemically synthesised and biological product. The first wave of work focused on small, volatile nitrosamines such as NDMA and NDEA. The current wave is harder: nitrosamine drug substance-related impurities (NDSRIs), which form when the API itself carries a secondary or tertiary amine that can be nitrosated.",
        "NDSRIs are not generic. Each one is a new molecule, structurally related to your API, so the analytical work starts with a synthesised reference standard and a method built around that specific compound.")
      + SPLIT("lab-vial-dark", H3("The three-step model") + OL(["<b>Step 1. Risk evaluation.</b> Look at API route, excipients, water, packaging and process for nitrosating agents and vulnerable amines.",
                                                               "<b>Step 2. Confirmatory testing.</b> Where a risk is plausible, test representative batches with a validated, sufficiently sensitive method.",
                                                               "<b>Step 3. Mitigation and control.</b> Reformulate, change suppliers or packaging, add scavengers such as ascorbic acid, and set a specification."]))),
     ("Acceptable intakes and the potency category approach",
      P("For NDSRIs without robust compound-specific carcinogenicity data, FDA (guidance first issued August 2023) and EMA use a Carcinogenic Potency Categorisation Approach (CPCA). It scores structural features around the N-nitroso group and assigns one of five categories. Each category maps to a default acceptable intake.")
      + T(["CPCA category", "Default AI (ng/day)", "What it means"],
          [["1", "18", "Highest predicted potency; treated like the most potent nitrosamines"], ["2", "100", "High potency"], ["3", "400", "Moderate potency"],
           ["4", "1,500", "Low predicted potency (metabolic activation disfavoured)"], ["5", "1,500", "Lowest predicted potency"]])
      + P("Convert the AI to a specification using the maximum daily dose. A product dosed at 1 g/day with a 26.5 ng/day AI (the NDMA value) needs a limit of 0.0265 ppm. That is why sensitivity, not just selectivity, decides whether a method is fit for purpose. Always check the current published AI for your specific NDSRI; regulators update their lists.")),
     ("What a fit-for-purpose method looks like",
      P("Most confirmatory work uses LC-MS/MS in multiple reaction monitoring mode, or LC-HRMS where interferences are a problem. Volatile nitrosamines can also be run by GC-MS/MS. Three things decide success:")
      + UL(["<b>Sensitivity.</b> Aim for a limit of quantitation at or below 30% of the specification limit, so trending is meaningful.",
            "<b>No artefactual formation.</b> Nitrosamines can form during sample preparation if nitrite and amine meet in acid. Add a nitrosation inhibitor (sulfamic acid or ascorbic acid) and prove it with spiked controls.",
            "<b>Matrix effects.</b> Use isotopically labelled internal standards where available and validate accuracy in the real product matrix."])
      + pull("Start with the risk assessment. The method follows from the molecule, the dose and the limit, not the other way round.")
      + P(f'See our <a href="{M("nitrosamines-lc-ms-ms")}">LC-MS/MS nitrosamine method</a> and the <a href="{M("genotoxic-impurities")}">genotoxic impurity methods</a>.')),
     ("Where nitrosamines come from in finished products",
      BARS("Commonly reported root causes (qualitative ranking)", [("Nitrite in excipients reacting with API amines", 5, "Very common"), ("Secondary amine impurities in API", 4, "Common"),
                                                                    ("Nitrocellulose lidding in blisters", 3, "Occasional"), ("Contaminated recovered solvents", 3, "Occasional"), ("Water treatment chloramines", 2, "Rare")],
           "A qualitative ranking drawn from published regulatory findings, not a measured frequency.")
      + P("Excipient nitrite is often the deciding factor for NDSRIs. Nitrite levels vary between suppliers and lots of the same excipient, so supplier qualification and periodic nitrite testing are worth building into your control strategy.")),
     ("A practical 2027 checklist",
      TICKLIST(["Risk assessment on file for every product, reviewed after any change in API source, excipient supplier or packaging.",
                "Current AI checked against the latest FDA and EMA lists, not a copy from two years ago.",
                "Reference standard for each NDSRI, with identity and purity documented.",
                "Method validated with LOQ at or below 30% of the limit and proof of no in-situ formation.",
                "Batches tested: at least three representative commercial batches, plus stability samples at end of shelf life.",
                "A trending plan and a defined response if results approach the limit."])
      + IMG("inst-lcms", "LC-MS/MS is the workhorse for confirmatory NDSRI testing (illustrative stock photo)")
      + P(f'Use the <a href="{TL("nitrosamine-risk-assessor")}">Nitrosamine Risk Assessor</a> to structure your first pass, then talk to the <a href="{S("small-molecule-qc-release")}">small molecule QC team</a>.'))],
    [("Do I need to test if my risk assessment finds no risk?", "No. If the risk assessment is robust and documented, confirmatory testing is not required. Regulators expect you to revisit it when inputs change."),
     ("What LOQ should my method reach?", "A common expectation is an LOQ at or below 30% of the acceptable limit for routine control. For screening, regulators accept an LOQ at or below the limit itself."),
     ("Can one method cover several NDSRIs?", "Sometimes, if they share chromatographic behaviour and ionisation, but each NDSRI needs its own reference standard and validation data."),
     ("Is the CPCA used outside the US?", "Yes. EMA applies the same categorisation in its nitrosamine Q&A and Appendix 1 lists, and other regulators increasingly reference it.")],
    [("Small Molecule QC and Release", S("small-molecule-qc-release")), ("Nitrosamines by LC-MS/MS", M("nitrosamines-lc-ms-ms")), ("Regulatory Radar", "/regulatory-radar.html")])

# ===================== 2. Zone IVb =====================
art("stability-zone-ivb", "Stability zones explained: Zone IVb for India and ASEAN launches",
    "What the ICH climatic zones are, why Zone IVb is the hardest, and how to design a stability programme that supports launches across India and Southeast Asia.",
    "lab-corridor", "Methods", "rahul", 9,
    "Zone IVb covers hot and very humid climates, including India, most of ASEAN and much of Latin America. Long-term stability for these markets is run at 30 °C and 75% relative humidity. If you plan to launch there, design for Zone IVb from the start: it is the most demanding long-term condition and usually covers the milder zones too.",
    ["There are five climatic zones; Zone IVb long-term storage is 30 °C / 75% RH.", "Accelerated studies are 40 °C / 75% RH for six months in every zone.",
     "Moisture, not heat, is usually what fails in Zone IVb: packaging choice decides the outcome.", "Plan registration batches, pull points and chamber capacity before the first batch is made."],
    [("The five climatic zones",
      P("ICH Q1A(R2) and WHO guidance divide the world into climatic zones by mean kinetic temperature and humidity. The long-term condition you choose must represent the zone you will sell into.")
      + T(["Zone", "Climate", "Long-term condition", "Typical markets"],
          [["I", "Temperate", "21 °C / 45% RH", "Northern Europe, Canada, Russia"], ["II", "Subtropical, Mediterranean", "25 °C / 60% RH", "US, EU, Japan"],
           ["III", "Hot, dry", "30 °C / 35% RH", "Parts of the Middle East and Africa"], ["IVa", "Hot, humid", "30 °C / 65% RH", "China, Brazil (some regions)"],
           ["IVb", "Hot, very humid", "30 °C / 75% RH", "India, Indonesia, Malaysia, Singapore, Thailand, Vietnam, Philippines"]])
      + P("Accelerated storage is 40 °C / 75% RH for six months for every zone. Intermediate storage (30 °C / 65% RH) applies when a significant change occurs at accelerated and the long-term condition is 25 °C / 60% RH.")),
     ("Why Zone IVb is different",
      SPLIT("lab-instrument-bench", P("At 75% relative humidity, water uptake drives most failures: dissolution slows as film coats soften, hydrolytic degradants grow, capsules soften or crack, and moisture-sensitive APIs change polymorphic form. Heat alone rarely tells the story.",
                                       "That makes packaging the main lever. A product that is stable in HDPE bottles with desiccant may fail in PVC blisters. Alu-alu blisters or PVC/PVDC with higher barrier often turn a failure into a pass."), flip=True)
      + pull("In Zone IVb, the blister usually decides whether the batch passes. Test the packaging you will actually sell.")),
     ("Designing the programme",
      P("A registration stability package for an India and ASEAN launch typically includes three primary batches, at least pilot scale, in the commercial container closure.")
      + T(["Study", "Condition", "Pull points (months)"], [["Long-term", "30 °C / 75% RH", "0, 3, 6, 9, 12, 18, 24, 36"], ["Accelerated", "40 °C / 75% RH", "0, 3, 6"],
                                                         ["Photostability", "ICH Q1B option 1 or 2", "One batch, once"], ["In-use (if multi-dose)", "Per label", "As designed"]])
      + P(f'Bracketing and matrixing (ICH Q1D) can reduce the number of samples where you have several strengths or pack sizes. Our <a href="{TL("stability-study-designer")}">Stability Study Designer</a> builds a pull schedule and sample count for your zones.')
      + GANTT([("Protocol and chamber booking", 0, 2), ("Batch manufacture and t=0", 2, 2), ("Accelerated pulls (3, 6 months)", 4, 26), ("Long-term pulls to 12 months", 4, 52), ("Registration dossier", 30, 26)], 60, "Typical first-year timeline (weeks)")),
     ("Common pitfalls",
      UL(["Running Zone II long-term only and hoping for a waiver. Most ASEAN regulators expect 30 °C / 75% RH data.",
          "Changing the blister supplier after registration batches. That is a variation that needs new stability data.",
          "Chamber excursions without a documented impact assessment. Every chamber needs continuous monitoring and alarm records.",
          "No method stability-indicating proof. Forced degradation must show the method separates the degradants that matter."])
      + P(f'See <a href="{M("ich-stability-storage")}">ICH stability storage</a>, <a href="{M("photostability-q1b")}">photostability</a> and <a href="{M("forced-degradation")}">forced degradation</a> in the Method Library.')
      + IMG("lab-glassware", "Stability samples are pulled, logged and tested on a fixed schedule (illustrative stock photo)"))],
    [("Does Zone IVb data cover Zone II markets?", "Usually, yes, because 30 °C / 75% RH is more demanding than 25 °C / 60% RH. Check each regulator's expectations; some still want data at their own condition."),
     ("How many batches do I need?", "ICH expects three primary batches, at least two at pilot scale, for new drug products. Generics regulators often follow the same expectation."),
     ("What counts as a significant change at accelerated?", "Under ICH Q1A(R2), for example a 5% change in assay, any degradant exceeding its limit, or failure of appearance, physical attributes or dissolution criteria.")],
    [("Stability Studies", S("stability-studies")), ("Stability Study Designer", TL("stability-study-designer")), ("Kuala Lumpur lab", "/labs/kuala-lumpur.html")])

# ===================== 3. mRNA CQAs =====================
art("mrna-critical-quality-attributes", "mRNA critical quality attributes: the complete guide",
    "Identity, integrity, capping, poly(A), dsRNA, residual DNA and LNP attributes: what each one tells you, how it is measured and why it matters for potency and safety.",
    "vax-vials", "mRNA and Vaccines", "kenji", 13,
    "The critical quality attributes of an mRNA-LNP product fall into two groups. For the RNA: identity, integrity, 5' capping, poly(A) tail length and impurities such as dsRNA and residual DNA template. For the lipid nanoparticle: particle size, polydispersity, encapsulation efficiency, lipid identity and content. Potency ties them together through in vitro expression.",
    ["Integrity and capping usually predict potency problems before a cell assay does.", "dsRNA is a key process impurity because it triggers innate immune responses.",
     "LNP size, PDI and encapsulation efficiency need orthogonal methods.", "Methods must move from research-grade to validated as you approach commercial release."],
    [("The molecule and the particle",
      P("An mRNA drug substance is a long single-stranded RNA made by in vitro transcription from a linear DNA template. It carries a 5' cap, untranslated regions, the coding sequence and a poly(A) tail. The drug product wraps that RNA in a lipid nanoparticle made of an ionisable lipid, a PEG-lipid, a helper phospholipid and cholesterol.",
        "Each structural feature can fail in its own way, which is why the quality attribute list is long.")
      + IMG("bio-dna", "Each structural feature of the RNA has its own quality attribute (illustration)")),
     ("RNA attributes and how we measure them",
      T(["Attribute", "Why it matters", "Typical method"],
        [["Identity (sequence)", "Confirms the right construct", "RT-PCR, sequencing, oligonucleotide mapping by LC-MS"],
         ["Integrity (% full length)", "Truncated RNA does not translate", f'<a href="{M("mrna-integrity-ce")}">Capillary electrophoresis</a>, fragment analysis'],
         ["5' capping efficiency", "Uncapped RNA is translated poorly and is immunogenic", f'<a href="{M("mrna-capping-lc-ms")}">RNase H cleavage then LC-MS</a>'],
         ["Poly(A) tail length", "Affects stability and translation", f'<a href="{M("poly-a-tail-length")}">RNase digestion then LC-MS or CE</a>'],
         ["dsRNA", "Innate immune activation", f'<a href="{M("dsrna-elisa")}">J2 antibody dot blot or ELISA</a>'],
         ["Residual DNA template", "Process impurity", "qPCR"], ["Residual NTPs, enzyme", "Process impurities", "HPLC, ELISA"]])
      + pull("Most mRNA failures show up in the cap and the tail long before they show up in potency.")),
     ("LNP attributes",
      T(["Attribute", "Why it matters", "Typical method"],
        [["Particle size and PDI", "Biodistribution, uptake, consistency", f'<a href="{M("lnp-size-pdi-dls")}">Dynamic light scattering</a>, confirmed by NTA or MALS'],
         ["Encapsulation efficiency", "Free RNA degrades and does not deliver", f'<a href="{M("encapsulation-efficiency-ribogreen")}">Fluorescent dye assay with and without detergent</a>'],
         ["Lipid identity and content", "Composition drives performance", "HPLC with CAD or ELSD"], ["Lipid impurities", "Oxidation products can form RNA adducts", "LC-MS"],
         ["pH, osmolality, appearance", "Basic product quality", "Compendial methods"]])
      + P("Orthogonal methods matter here. DLS reports an intensity-weighted size that is sensitive to a few large particles; pairing it with a number-based method gives a truer picture of the distribution.")),
     ("Potency and safety",
      SPLIT("lab-plate-pink", P("Potency is usually an in vitro expression assay: transfect cells, then measure the encoded protein by flow cytometry, ELISA or a cell-based activity readout. It integrates RNA quality, capping, tail and LNP delivery into one number.",
                                 f'Safety testing adds bacterial endotoxins, sterility and container closure integrity. See <a href="{S("microbiology-sterility")}">Microbiology and Sterility</a>.'))),
     ("From clinical to commercial",
      P("Early-phase work can use qualified, fit-for-purpose methods. By Phase 3, release and stability methods should be validated to ICH Q2(R2), with specifications justified from clinical and stability data. Plan method transfer early: LC-MS cap and tail methods are sensitive to column lots and instrument configuration.")
      + BARS("Indicative method maturity by phase", [("Phase 1", 1, "Qualified"), ("Phase 2", 2, "Qualified, trending"), ("Phase 3", 3, "Validated"), ("Commercial", 4, "Validated and transferred")]))],
    [("Which attribute fails most often?", "In practice integrity and capping drift first, often from template, enzyme or purification changes. Encapsulation efficiency is the most common LNP issue."),
     ("Is DLS enough for size?", "Not on its own. Use an orthogonal method at least during development and comparability work."),
     ("How should mRNA samples be shipped?", "Frozen, usually at or below -60 °C on dry ice, with a temperature logger and minimal freeze-thaw cycles.")],
    [("mRNA and Vaccine Testing", S("mrna-vaccine-testing")), ("mRNA integrity by CE", M("mrna-integrity-ce")), ("LNP size and PDI", M("lnp-size-pdi-dls"))])

# ===================== 4. Method transfer =====================
art("method-transfer-failure", "How to avoid method transfer failure",
    "Why analytical method transfers fail, how to design one that passes first time, and the documents that make it boring in a good way.",
    "inst-hplc", "Methods", "mei", 9,
    "Most method transfers fail for preventable reasons: an under-specified method, different column or instrument dwell volume, unclear acceptance criteria, or an untrained receiving analyst. A good transfer starts with a robust method, a written protocol with pre-agreed criteria, a knowledge-transfer session and a gap assessment of instruments and materials.",
    ["Robustness work during development is the best transfer insurance.", "Agree acceptance criteria before any data is generated.",
     "Check dwell volume, column chemistry and integration rules between sites.", "Comparative testing is the usual approach; co-validation and waivers have their place."],
    [("Why transfers fail",
      P("Industry surveys and our own experience point to the same short list. The method was written for the people who developed it, not for someone reading it cold. The receiving lab has a different HPLC with a larger dwell volume, so gradient retention times shift. Integration parameters were never written down. Or the acceptance criteria were argued about after the results came in.")
      + BARS("Typical root causes of failed transfers (qualitative)", [("Method under-specified or not robust", 5, "Most common"), ("Instrument differences (dwell volume, detector)", 4, "Common"),
                                                                        ("Columns or reagents not equivalent", 3, "Common"), ("Analyst training gaps", 3, "Common"), ("Criteria not agreed upfront", 2, "Occasional")])),
     ("Choose the right transfer approach",
      T(["Approach", "When to use it", "What it involves"],
        [["Comparative testing", "Most transfers", "Both labs test the same lots; results compared against pre-set criteria"],
         ["Co-validation", "New method going to several sites", "Receiving lab takes part in validation, usually intermediate precision"],
         ["Revalidation", "Significant differences between sites", "Partial or full validation at the receiving lab"],
         ["Transfer waiver", "Compendial methods, experienced lab, simple tests", "Justified and documented; verification instead of transfer"]])
      + P("USP <1224> describes these options. Under ICH Q14 and Q2(R2), transfer is part of the method lifecycle rather than a one-off event.")),
     ("The protocol that passes first time",
      SPLIT("lab-team-three", OL(["Objective, scope and responsibilities for both labs.", "Materials: lots, reference standards, columns (with alternates), reagents.",
                                   "Instrument gap assessment, including dwell volume and detector settings.", "Number of determinations and analysts.",
                                   "Acceptance criteria for each parameter, agreed in writing.", "Handling of deviations and failures.", "Report template."]))
      + pull("Write the acceptance criteria before anyone touches an instrument. Arguments after the data are how transfers fail.")
      + T(["Test", "Common acceptance criterion"], [["Assay", "Difference in means ≤ 2.0% absolute"], ["Impurities", "Difference ≤ 0.05% absolute or ≤ 20% relative at specified level"],
                                                   ["Dissolution", "f2 ≥ 50 or difference at each time point ≤ 10%"], ["Content uniformity", "Both labs meet acceptance value; means comparable"]])
      + P("These are typical starting points, not rules. Set criteria from the method's own precision data.")),
     ("How a network makes transfer faster",
      P(f'Inside one network, the same SOPs, the same instrument models, the same LIMS templates and the same integration rules remove most of the gap assessment. That is why we aim for transfers in days, not months. See <a href="{S("method-development-validation")}">Method Development, Validation and Transfer</a> and the <a href="/labs/capabilities-matrix.html">capabilities matrix</a>.')
      + IMG("lab-analyst-pc", "Integration rules written into the method remove a common source of transfer failure (illustrative stock photo)"))],
    [("Is a transfer needed for a compendial method?", "Usually not. Compendial methods need verification under USP <1226> rather than full transfer."),
     ("How many lots should be tested?", "Often one to three lots, chosen to cover the specification range, with replicate determinations by more than one analyst."),
     ("What if one parameter fails?", "Investigate as a deviation. Do not change the criteria after the fact; fix the cause and repeat under the protocol.")],
    [("Method Development, Validation and Transfer", S("method-development-validation")), ("HPLC assay and related substances", M("hplc-assay-related-substances"))])

# ===================== 5. Biosimilar similarity =====================
art("biosimilar-analytical-similarity", "Biosimilar analytical similarity: what FDA and EMA look for",
    "How regulators assess analytical similarity, how to tier quality attributes, how many reference lots you need and how to present the data.",
    "lab-instrument-load", "Biologics", "elena", 10,
    "Regulators treat analytical similarity as the foundation of a biosimilar application. You must show that the biosimilar is highly similar to the reference product across structural and functional attributes, using sensitive orthogonal methods and enough reference lots to understand its variability. Attributes are ranked by criticality, and the most critical get the strictest statistical comparison.",
    ["Analytical similarity is the foundation; clinical studies confirm, they do not replace it.", "Rank attributes by risk to safety and efficacy before you compare them.",
     "Buy reference product lots across time and, where relevant, regions.", "Use orthogonal methods for the attributes that matter most."],
    [("The totality of evidence",
      P("Both FDA and EMA describe a stepwise approach. Analytical comparison comes first. Where it is strong, the residual uncertainty that clinical studies must resolve is smaller. Recent regulatory thinking has gone further, questioning whether comparative efficacy studies are always needed when analytical and pharmacokinetic data are convincing.")
      + IMG("lab-automation", "Structural and functional methods run side by side for reference and biosimilar lots (illustrative stock photo)")),
     ("Ranking quality attributes",
      P("Start with a risk assessment that ranks each quality attribute by its potential impact on activity, PK, immunogenicity and safety. The ranking decides how you compare it.")
      + T(["Tier (common practice)", "Typical attributes", "Comparison"],
          [["Highest criticality", "Potency, target binding, Fc effector function where relevant", "Statistical approach, for example quality range or equivalence"],
           ["Moderate", "Charge variants, glycan species, aggregates", "Quality range: most biosimilar lots within the reference range"],
           ["Lower", "Primary structure confirmation, higher-order structure", "Visual or qualitative comparison"]])
      + P("FDA's 2019 draft guidance on comparative analytical assessment discussed equivalence testing and quality ranges; agencies continue to refine statistical expectations, so confirm the current position for your filing.")),
     ("The method toolbox",
      T(["Attribute class", "Methods"], [["Primary structure", f'<a href="{M("peptide-mapping-lc-ms")}">Peptide mapping LC-MS</a>, <a href="{M("intact-mass-ms")}">intact mass</a>'],
                                          ["Charge variants", f'<a href="{M("icief-charge-variants")}">icIEF</a>, CEX-HPLC'], ["Size variants", f'<a href="{M("sec-hplc-aggregates")}">SEC</a>, <a href="{M("ce-sds")}">CE-SDS</a>, AUC'],
                                          ["Glycosylation", f'<a href="{M("glycan-profiling-hilic")}">Released glycans by HILIC-FLD</a>, glycopeptide MS'], ["Higher-order structure", "CD, FTIR, DSC, HDX-MS"],
                                          ["Function", f'<a href="{M("cell-based-potency")}">Cell-based potency</a>, binding (SPR, ELISA), ADCC and CDC']])
      + pull("Similarity is a statistical argument, not a single overlaid chromatogram.")),
     ("Reference product sourcing",
      SPLIT("lab-sample-rack", P("Regulators want to see the reference product's own variability. Buy lots spread over time, ideally ten or more for critical attributes, and record expiry dates. If you plan to use non-local reference product, you will need a bridging comparison between regions.",
                                  f'Our <a href="{S("biologics-characterization-release")}">biologics team</a> can run reference and biosimilar lots side by side on the same instruments and analysts, which reduces method variability in the comparison.'), flip=True))],
    [("How many reference lots are enough?", "There is no fixed number, but ten or more lots for critical attributes is a common target so the reference variability is well characterised."),
     ("Do I need orthogonal methods for every attribute?", "Not every one. Use them where the attribute is critical or a single method could miss a difference."),
     ("Can differences be acceptable?", "Yes, if you can show they have no clinically meaningful impact, often with additional functional data.")],
    [("Biologics Characterization and Release", S("biologics-characterization-release")), ("Biosimilars", "/industries/biosimilars.html")])

# ===================== 6. Data integrity =====================
art("data-integrity-top-10-findings", "Data integrity: the 10 findings inspectors see most",
    "The data integrity observations that keep appearing in FDA warning letters and EU GMP inspections, and the controls that prevent them.",
    "lab-analyst-pc", "Quality", "helen", 10,
    "The most common data integrity findings are not exotic. Inspectors keep finding shared log-ins, disabled audit trails, unreviewed audit trails, testing into compliance, deleted or overwritten data, uncontrolled spreadsheets and paper records that do not match electronic data. Each has a simple technical or procedural control; the hard part is applying it everywhere, every day.",
    ["ALCOA+ is the frame: attributable, legible, contemporaneous, original, accurate, plus complete, consistent, enduring, available.",
     "Most findings come from computerised systems configured with too much freedom.", "Audit trail review must be risk-based, routine and documented.",
     "Culture matters as much as software: people must feel safe reporting a mistake."],
    [("The ten findings",
      T(["#", "Finding", "Control that prevents it"],
        [["1", "Shared user accounts on instruments or software", "Unique log-ins, enforced by IT, reviewed quarterly"],
         ["2", "Audit trails disabled or not configured", "Audit trail on by validated configuration; changes under change control"],
         ["3", "Audit trails never reviewed", "Risk-based audit trail review before results are approved"],
         ["4", "Trial or unofficial injections", "System configured so every injection is part of a sequence and visible"],
         ["5", "Deleting or overwriting data", "No delete rights for analysts; data stored on secure servers"],
         ["6", "Manual integration without justification", "Integration SOP; manual integration flagged and reviewed"],
         ["7", "Uncontrolled spreadsheets for calculations", "Validated templates or LIMS calculations, locked cells, version control"],
         ["8", "Clock changes on standalone PCs", "Network time synchronisation; users cannot change system time"],
         ["9", "Paper and electronic records that disagree", "Electronic record defined as original; true copies controlled"],
         ["10", "Invalidating OOS results without investigation", "OOS procedure following FDA's OOS guidance, with QA oversight"]])),
     ("Why the same findings keep returning",
      SPLIT("lab-goggles", P("Laboratories buy validated software and then configure it for convenience: admin rights for everyone, audit trails off to save disk space, a generic 'lab' account to avoid log-in time. Each choice seems small. Together they make it impossible to prove who did what, when.",
                              "The FDA's December 2018 guidance on data integrity and the MHRA's 2018 GXP data integrity guidance both make the same point: data governance is a management responsibility, not an IT setting."))
      + pull("Every result has a name behind it. If you cannot say whose name, you do not have a result.")),
     ("Audit trail review that actually works",
      P("Reviewing every line of every audit trail is impossible. Risk-based review is expected instead. Define which events matter (reprocessing, manual integration, aborted runs, changed methods, deleted files), use system reports to filter them, and review them before the result is approved. Record that you did it.")
      + AUDIT()),
     ("Prepare before the inspector arrives",
      P(f'Run a mock inspection that samples raw data from a recent batch and traces it from the instrument to the CoA. Check the user list against the HR list. Ask an analyst to show the audit trail for their last run. Our <a href="{S("regulatory-data-integrity-support")}">regulatory and data integrity support</a> team runs ALCOA+ gap assessments, and the <a href="{TL("inspection-readiness-score")}">Inspection Readiness Score</a> gives you a quick self-check.')
      + IMG("sec-servers", "Validated, secure storage underpins the 'enduring' and 'available' principles (illustrative stock photo)"))],
    [("What does ALCOA+ stand for?", "Attributable, Legible, Contemporaneous, Original, Accurate, plus Complete, Consistent, Enduring and Available."),
     ("Is a paper printout the original record?", "Not for an electronic system. Regulators treat the electronic data, including metadata, as the original record."),
     ("How often should user access be reviewed?", "Periodically, commonly every quarter, and whenever someone joins, moves or leaves.")],
    [("Data integrity (ALCOA+)", "/quality/data-integrity.html"), ("Regulatory and Data Integrity Support", S("regulatory-data-integrity-support"))])

# ===================== 7. Endotoxin =====================
art("endotoxin-lal-vs-recombinant", "Endotoxin testing: LAL versus recombinant reagents",
    "How the bacterial endotoxins test works, how LAL compares with recombinant factor C and cascade reagents, and how to validate a switch.",
    "micro-petri-2", "Quality", "priya", 8,
    "Both LAL and recombinant reagents detect bacterial endotoxin. LAL is made from horseshoe crab blood and is the historical standard. Recombinant factor C (rFC) and recombinant cascade reagents remove the animal source and the glucan interference. They are accepted in the European Pharmacopoeia (chapter 2.6.32) and USP, but switching a product needs a documented comparability exercise.",
    ["Endotoxin limit = K / M, where K depends on route and M is the maximum dose per kg per hour.", "LAL methods: gel-clot, turbidimetric and chromogenic.",
     "Recombinant reagents remove beta-glucan false positives and reduce reliance on horseshoe crabs.", "Validate interference (inhibition and enhancement) for every product."],
    [("What endotoxin is and why we test for it",
      P("Endotoxins are lipopolysaccharides from the outer membrane of Gram-negative bacteria. Tiny amounts in a parenteral product can cause fever and, at higher levels, shock. Every injectable, and many medical devices, must meet an endotoxin limit.")
      + IMG("micro-petri-1", "Gram-negative bacteria are the source of endotoxin (illustrative stock photo)")),
     ("Calculating the limit",
      P("The endotoxin limit is K/M. K is 5 EU/kg for most parenteral routes and 0.2 EU/kg for intrathecal administration. M is the maximum dose per kg given in one hour. For a 70 kg adult, a 10 mL intravenous dose of a drug at 100 mg/mL gives M = 1,000 mg / 70 kg = 14.3 mg/kg, so the limit is 5 / 14.3 = 0.35 EU/mg.")
      + P(f'Try it with our <a href="{TL("endotoxin-limit-calculator")}">Endotoxin Limit Calculator</a>.')),
     ("LAL and recombinant reagents compared",
      T(["", "LAL (gel-clot, kinetic)", "Recombinant factor C", "Recombinant cascade"],
        [["Source", "Horseshoe crab amoebocytes", "Recombinant protein", "Recombinant proteins"], ["Glucan interference", "Yes (unless blocked)", "No", "No"],
         ["Readout", "Clot, turbidity or colour", "Fluorescence", "Colour"], ["Compendial status", "USP <85>, Ph. Eur. 2.6.14", "Ph. Eur. 2.6.32; USP chapter <86>", "Ph. Eur. 2.6.32; USP <86>"],
         ["Switching", "Reference method", "Comparability needed", "Comparability needed"]])
      + pull("The reagent is a choice. The interference study is not.")
      + P(f'See <a href="{M("bacterial-endotoxins-lal")}">bacterial endotoxins by LAL</a> and <a href="{M("recombinant-factor-c")}">recombinant factor C</a>.')),
     ("Validating a product",
      SPLIT("lab-pipette-blue", UL(["Find the maximum valid dilution (MVD) from the limit and the reagent sensitivity.", "Run inhibition and enhancement tests on at least three lots.",
                                     "Check for low endotoxin recovery (LER) if the product contains chelators and surfactants, such as many biologic formulations.", "Document the method and the dilution in the specification."])))],
    [("Is rFC accepted in the US?", "Yes, USP has a chapter for recombinant reagents and FDA accepts them with appropriate validation; confirm current expectations for your product."),
     ("What is low endotoxin recovery?", "A masking effect in some formulations where spiked endotoxin is not fully recovered over time. It must be studied for affected biologics."),
     ("Which method is fastest?", "Kinetic chromogenic or rFC methods give quantitative results in about an hour of instrument time.")],
    [("Microbiology and Sterility", S("microbiology-sterility")), ("Endotoxin Limit Calculator", TL("endotoxin-limit-calculator"))])

# ===================== 8. Choosing a partner =====================
art("choosing-a-testing-partner", "Choosing a testing partner: a procurement scorecard",
    "A weighted scorecard for comparing contract testing labs on quality, capability, turnaround, cost and risk, with the questions to ask at audit.",
    "biz-team-laptops", "Market", "arjun", 9,
    "Choose a testing partner on five weighted criteria: quality and compliance record, technical capability, turnaround reliability, total cost (not price per test) and supply risk. Weight quality highest, because a failed inspection at your lab partner becomes your problem. Verify every claim at audit: certificates, inspection history, method scope and real turnaround data.",
    ["Quality and compliance should carry the largest weight.", "Compare total cost of a programme, including repeats, investigations and delays.",
     "Ask for measured on-time delivery, not promised turnaround.", "Avoid single-source dependency for release-critical testing."],
    [("The scorecard",
      T(["Criterion", "Suggested weight", "What good looks like", "Evidence to request"],
        [["Quality and compliance", "30%", "Clean inspection history, mature data integrity", "Accreditation certificates and scope, inspection outcomes, audit reports"],
         ["Technical capability", "25%", "Methods and instruments for your molecule and market", "Method list, instrument list, validation reports"],
         ["Turnaround reliability", "20%", "Measured on-time delivery above 95%", "Last 12 months of on-time data by test type"],
         ["Total cost", "15%", "Transparent pricing, few surprises", "Rate card, repeat-test policy, MSA terms"],
         ["Risk and continuity", "10%", "Backup sites, financial stability, cyber security", "Business continuity plan, insurance, SOC 2 or ISO 27001 status"]])
      + P("Adjust the weights to your situation. A biotech with one product in Phase 1 may weight technical capability and responsiveness higher; a generic manufacturer with hundreds of batches a year may weight cost and turnaround higher.")),
     ("Questions to ask at audit",
      SPLIT("lab-team-three",
            OL(["Show me the audit trail for a result you released last week.", "Who reviews data, and who do they report to?", "What were your last three regulatory inspection outcomes?",
                "How do you handle an OOS result, and how fast will I hear about it?", "What happens to my samples if this site goes down?", "Can I see your measured turnaround for my test types?"]))
      + pull("Price per test is the easiest number to compare and the least useful one.")),
     ("Total cost, not price",
      BARS("Where the real cost of a test programme sits (illustrative)", [("List price of tests", 55, "55%"), ("Repeats and retests", 12, "12%"), ("Your staff time on queries and investigations", 18, "18%"), ("Delay cost (batches on hold)", 15, "15%")],
           "Illustrative split to show the idea; your numbers will differ.")
      + P(f'The <a href="{TL("cost-of-delay-calculator")}">Cost of Delay Calculator</a> turns days on hold into money, which helps compare a cheaper but slower lab with a faster one.')),
     ("Download the scorecard",
      P("We publish the scorecard as a free download alongside the vendor qualification pack. You can use it to assess us, too.")
      + MAILFORM([("email", "Work email", "email", True), ("company", "Company", "text", False)], "Procurement scorecard download", "Email me the scorecard")
      + IMG("docs-papers", "A written scorecard keeps the comparison honest (illustrative stock photo)"))],
    [("Should we audit before or after a trial project?", "For GMP release testing, audit first. A small paid pilot can follow to test responsiveness."),
     ("How many testing partners should we use?", "Many companies use one primary and one qualified backup for release-critical tests."),
     ("What is an MSA?", "A master service agreement sets the commercial and quality terms once, so individual projects only need a work order.")],
    [("Quality overview", "/quality/index.html"), ("Accreditations", "/quality/accreditations.html"), ("Request a quote", "/request-quote.html")])

# ===================== 9. CGT release =====================
art("cgt-release-testing", "Cell and gene therapy release testing explained",
    "Safety, identity, purity, potency and the clock: what release testing looks like for AAV, lentiviral and CAR-T products, and why timing changes everything.",
    "bio-cells-green", "Biologics", "sara", 10,
    "Cell and gene therapy release testing covers the same pillars as any biologic: safety, identity, purity, quantity and potency. What changes is the material and the clock. Samples are scarce, many products are personalised, and autologous cell therapies often need results within days. That pushes labs towards rapid sterility, ddPCR and flow cytometry, and towards running tests in parallel.",
    ["AAV and lentiviral vectors are tested like biologics plus vector-specific assays.", "Autologous products may be released before compendial sterility is complete, under a defined strategy.",
     "Empty/full capsid ratio and vector genome titre are key AAV attributes.", "Potency assays are the hardest to develop and should start early."],
    [("The release panel",
      T(["Pillar", "AAV vector", "CAR-T (autologous)"],
        [["Safety", "Sterility, endotoxin, mycoplasma, adventitious agents", "Rapid sterility, endotoxin, mycoplasma (NAT), RCL/RCR"],
         ["Identity", "Capsid serotype, transgene sequence", "Flow cytometry for CAR expression"],
         ["Purity", "Empty/full ratio, host cell protein and DNA", "Viability, T-cell purity, residual beads"],
         ["Quantity", f'<a href="{M("ddpcr-vector-titre")}">Vector genome titre by ddPCR</a>', "Viable cell count, CAR+ cell dose"],
         ["Potency", "Transgene expression or activity in cells", "Cytotoxicity or cytokine release on target cells"]])),
     ("Why timing matters for fresh products",
      SPLIT("lab-microscope-close", P("A CAR-T product made from a patient's own cells may have a shelf life of days. Compendial sterility takes 14 days, so many programmes use a rapid microbial method for release and complete the 14-day test afterwards, with a defined plan if it fails after infusion.",
                                       "Mycoplasma is similar: nucleic acid amplification methods give results in hours rather than the 28 days of culture."))
      + pull("For a patient waiting on an autologous product, the lab clock is part of the treatment.")
      + GANTT([("Sample receipt", 0, 0.2), ("Rapid sterility", 0.2, 1.8), ("Mycoplasma NAT", 0.2, 0.6), ("Flow identity and viability", 0.2, 0.4), ("Potency", 0.2, 1.5), ("QA review and release", 2, 0.6)], 3, "Parallel release testing (days)")),
     ("AAV-specific attributes",
      P(f'Empty and partially filled capsids add protein without therapeutic benefit and may increase immune responses. Analytical ultracentrifugation is the reference method for the empty/full ratio; mass photometry and charge-based methods offer faster options. See <a href="{M("aav-empty-full-auc")}">AAV empty/full by AUC</a>.')
      + IMG("inst-pcr", "ddPCR gives absolute vector genome titres without a standard curve (illustrative)")),
     ("Regulatory expectations",
      P(f'FDA, EMA and other regulators expect phase-appropriate controls: qualified assays early, validated release assays and a potency assay that reflects the mechanism of action by licensure. Expectations differ in detail between regions, so plan for the strictest market you will file in. Start with the <a href="{S("cell-gene-therapy-testing")}">CGT testing service</a> and our <a href="/industries/biotech-startups.html">biotech start-up</a> packages.'))],
    [("Can a cell therapy be released before sterility results?", "Yes, under a pre-agreed strategy that usually combines a rapid method, in-process controls and a plan for late positive results."),
     ("Why use ddPCR for titre?", "It gives absolute quantification without a standard curve and is less sensitive to inhibitors than qPCR."),
     ("How much sample does release need?", "It varies widely; plan sample volumes with the lab early because CGT material is scarce.")],
    [("Cell and Gene Therapy Testing", S("cell-gene-therapy-testing")), ("Flow cytometry identity", M("flow-cytometry-identity"))])

# ===================== 10. E&L PFS =====================
art("el-prefilled-syringes", "Extractables and leachables for prefilled syringes",
    "How to design an E&L programme for biologics in prefilled syringes: materials, extraction conditions, analytical thresholds and leachables on stability.",
    "lab-vials-bw", "Methods", "lukas", 9,
    "Prefilled syringes put a biologic in contact with glass, rubber, silicone oil, adhesive and sometimes tungsten for the whole shelf life. An E&L programme first identifies what the components can release (extractables), sets a safety threshold, then measures what actually migrates into the product over time (leachables). Biologics add a second risk: leachables can damage the protein, not just the patient.",
    ["Extractables studies use exaggerated conditions; leachables are measured in the real product on stability.", "The analytical evaluation threshold (AET) comes from a safety concern threshold and the dose.",
     "Tungsten, silicone oil and rubber components are classic PFS risks.", "USP <1663> and <1664> describe the approach; PQRI thresholds are widely used."],
    [("What can migrate from a prefilled syringe",
      T(["Component", "Typical species", "Concern"], [["Glass barrel", "Silicon, boron, sodium, aluminium", "Particles, pH shift, delamination"], ["Tungsten pin residue", "Tungsten oxides", "Protein aggregation"],
                                                     ["Silicone oil", "Siloxanes, droplets", "Subvisible particles, aggregation"], ["Rubber plunger and tip cap", "Antioxidants, oligomers, metals", "Toxicity, oxidation"],
                                                     ["Needle adhesive", "Acrylates, photoinitiators", "Toxicity"]])),
     ("Designing the extractables study",
      SPLIT("lab-flasks-pour", UL(["Use solvents that bracket the product: aqueous at low and high pH, and a solvent with some organic character.", "Extract at elevated temperature for a defined time, without degrading the material.",
                                   f'Analyse with orthogonal techniques: <a href="{M("extractables-gc-ms")}">GC-MS</a> for volatiles and semi-volatiles, LC-MS for non-volatiles, <a href="{M("elemental-impurities-icp-ms")}">ICP-MS</a> for elements.',
                                   "Identify every peak above the AET with a confidence level."]), flip=True)
      + pull("An extractables profile is a list of possibilities. Leachables on stability tell you which ones are real.")),
     ("Setting the analytical evaluation threshold",
      P("A common starting point is a safety concern threshold (SCT) of 1.5 µg/day for parenteral products. Divide by the number of doses per day and the volume, and correct for analytical uncertainty, to get the AET in µg/mL. Compounds above the AET must be identified and assessed toxicologically.")
      + P("Example: SCT 1.5 µg/day, one 1 mL dose per day gives an AET of 1.5 µg/mL before uncertainty correction. Using a 50% uncertainty factor gives 0.75 µg/mL.")),
     ("Leachables on stability",
      P(f'Targeted methods for the extractables of concern are validated in the drug product and run at stability pull points, including end of shelf life. For biologics, pair them with aggregation and oxidation testing. See <a href="{S("extractables-leachables")}">Extractables and Leachables</a> and <a href="{M("leachables-lc-ms")}">leachables by LC-MS</a>.')
      + IMG("pharma-pillbox", "Packaging choices start the E&L conversation early in development (illustrative stock photo)"))],
    [("Do I need E&L for every product?", "The depth depends on risk: route, dose, contact time and formulation. Parenteral and inhalation products sit at the high end."),
     ("Can supplier extractables data be used?", "Yes, as a starting point, if the conditions are relevant. Regulators still expect product-specific leachables data."),
     ("What is the SCT?", "A safety concern threshold below which a leachable is considered to pose negligible safety risk, commonly 1.5 µg/day for parenterals.")],
    [("Extractables and Leachables", S("extractables-leachables")), ("Extractables by GC-MS", M("extractables-gc-ms"))])

# ===================== 11. Cost of delay =====================
art("cost-of-a-delayed-batch", "The real cost of a delayed batch",
    "What a day of testing delay costs a manufacturer, how to calculate it, and how to use it in vendor decisions and turnaround negotiations.",
    "log-warehouse", "Market", "arjun", 8,
    "A batch waiting on test results costs money every day: working capital tied up in inventory, warehouse and cold-chain costs, the risk of stock-outs and, for launches, lost revenue. A simple model multiplies batch value by your cost of capital per day, adds holding costs, and adds the margin lost if a delay causes a stock-out. For high-value products the total often dwarfs the price of the tests.",
    ["Cost of delay = capital cost + holding cost + stock-out risk.", "For launch batches, lost sales usually dominate.",
     "A faster tier can pay for itself many times over.", "Measure your actual hold times; most teams underestimate them."],
    [("The model",
      P("Start with three components.")
      + T(["Component", "How to estimate it", "Example"], [["Capital cost", "Batch value × annual cost of capital ÷ 365", "$2M batch × 10% ÷ 365 = $548/day"],
                                                           ["Holding cost", "Warehouse, cold chain, insurance per day", "$150/day"],
                                                           ["Stock-out or launch risk", "Probability of stock-out × daily margin lost", "5% × $40,000 = $2,000/day"]])
      + P("In this example a day of delay costs about $2,700, or $19,000 a week. A Priority tier that saves a week on a $6,000 test package is easy to justify.")),
     ("Where the days go",
      SPLIT("log-plane", P("Testing time inside the lab is often less than half of the total hold. Shipping, sample receipt and login, queueing, investigations, report review and CoA approval all add days. Measure each step at least once."))
      + BARS("Illustrative breakdown of a 15-day hold", [("Shipping and receipt", 2, "2 days"), ("Queue", 4, "4 days"), ("Testing", 5, "5 days"), ("Review and CoA", 2, "2 days"), ("Queries and investigations", 2, "2 days")])
      + pull("Most of the delay sits outside the instrument. That is where a network and a portal earn their keep.")),
     ("Using it in decisions",
      UL(["Compare labs on total cost: price plus delay cost at their measured turnaround.", "Choose tiers per batch: Critical for line stoppages and launches, Standard for routine stability.",
          "Negotiate MSAs with turnaround commitments and credits if dates are missed."])
      + P(f'Run your own numbers in the <a href="{TL("cost-of-delay-calculator")}">Cost of Delay Calculator</a>, then check dates with the <a href="{TL("turnaround-calculator")}">Turnaround Calculator</a>.')
      + IMG("data-dashboard", "Tracking hold time per batch shows where days are lost (illustrative stock photo)"))],
    [("What cost of capital should we use?", "Your finance team's weighted average cost of capital is a good default; many use 8% to 12%."),
     ("Does this apply to clinical batches?", "Yes, but the main cost is usually programme delay rather than inventory."),
     ("How do turnaround credits work?", "If a lab misses a committed date, the fee for that test is credited. Our credit policy is subject to commercial approval.")],
    [("Cost of Delay Calculator", TL("cost-of-delay-calculator")), ("Turnaround tiers", "/services/index.html")])

# ===================== 12. State of Pharma Testing =====================
art("state-of-pharma-testing-2027", "State of Pharma Testing 2027: survey design and what we will publish",
    "How our annual survey of QC, QA and procurement leaders will work, the questions we will ask, how we will protect respondents and when results will appear.",
    "data-charts", "Market", "arjun", 7,
    "The State of Pharma Testing 2027 is an annual survey of QC, QA, regulatory and procurement leaders. We have not published results yet. This page sets out the method in advance: who we will survey, what we will ask, how we will analyse it and how we will avoid bias, so readers can judge the findings when they appear.",
    ["No results yet: this is the published method, written before data collection.", "Target: several hundred respondents across India, ASEAN, Europe and the US.",
     "Anonymous responses, aggregated reporting, minimum cell sizes.", "Full questionnaire and methodology released with the report."],
    [("Why publish the method first",
      P("Industry surveys are often designed after the conclusion has been chosen. Publishing the method first commits us to the questions, the sample and the analysis before we see any data. If the results are inconvenient for us, they will still be published.")
      + IMG("biz-team-laptops", "We will publish the questionnaire with the results (illustrative stock photo)")),
     ("Who we will survey",
      T(["Group", "Target share", "Recruitment"], [["QC and analytical leaders", "35%", "Professional networks, conferences"], ["QA and regulatory affairs", "25%", "Professional networks"],
                                                  ["Procurement and sourcing", "20%", "Industry associations"], ["Biotech founders and CMC leads", "20%", "Incubators and investor networks"]])
      + P("We will report results by region and company type only where the group has at least 30 respondents.")),
     ("What we will ask",
      UL(["How much analytical testing is outsourced today, and how that will change in two years.", "Measured versus promised turnaround from current labs.",
          "The tests hardest to source: NDSRIs, mRNA, CGT, E&L.", "Data integrity findings in the last inspection cycle.", "How teams choose and audit testing partners.", "Use of portals, APIs and automation in QC."])
      + pull("If the results are inconvenient for us, they will still be published.")),
     ("How we will handle the data",
      SPLIT("sec-servers", UL(["Anonymous by default; no company names collected unless a respondent opts in.", "Data held under GDPR and India's DPDP Act principles.",
                               "Weighting disclosed if used.", "Raw aggregated tables published alongside the report."]))
      + P(f'Want to take part or receive the report? Use the form below or subscribe to the <a href="/regulatory-radar.html">Regulatory Radar</a>.')
      + MAILFORM([("email", "Work email", "email", True), ("role", "Role", ["QC / analytical", "QA / regulatory", "Procurement", "Founder / CMC", "Other"], False),
                  ("part", "I would like to take part in the survey", "checkbox", False)], "State of Pharma Testing 2027", "Keep me informed"))],
    [("When will the results be published?", "We plan to publish in 2027 after fieldwork closes. The date will be announced in the Regulatory Radar."),
     ("Is the survey paid?", "No. Respondents receive the full report and raw aggregated tables."),
     ("Will PharmaCRO clients be over-represented?", "We will report the share of respondents who are clients and show results with and without them.")],
    [("Insights", "/insights/index.html"), ("Whitepapers", "/whitepapers.html")])

# ===================== Insights hub =====================
CALENDAR = [("1", "Nitrosamine testing in 2027: what regulators now expect", "Risk assessor tool, checklist, LinkedIn carousel"),
            ("2", "Stability zones explained: zone IVb for India and ASEAN launches", "Stability Study Designer, infographic"),
            ("3", "mRNA critical quality attributes: the complete guide", "Quality Attribute Map, webinar invite"),
            ("4", "How to avoid method transfer failure", "Transfer checklist, scientist Q and A video"),
            ("5", "Biosimilar analytical similarity: what FDA and EMA look for", "Similarity Explorer, whitepaper"),
            ("6", "Data integrity: the 10 findings inspectors see most", "Readiness Score, webinar"),
            ("7", "Endotoxin testing: LAL versus recombinant reagents", "Calculator, FAQ"),
            ("8", "Choosing a testing partner: a procurement scorecard", "Downloadable scorecard, comparison page"),
            ("9", "Cell and gene therapy release testing explained", "Test matrix, case study"),
            ("10", "Extractables and leachables for prefilled syringes", "Risk screener, video"),
            ("11", "The real cost of a delayed batch", "Cost of Delay Calculator, LinkedIn data post"),
            ("12", "State of Pharma Testing 2027: survey results", "Press release, gated report, webinar")]

def _card(a, big=False):
    n = SCI[a["sci"]][0]
    return (f'<a class="rs-card{" big" if big else ""} reveal" href="/insights/{a["slug"]}.html" data-cat="{a["cat"]}"><img src="/img/{a["img"]}.jpg" alt="" loading="lazy">'
            f'<div><p class="ey">{a["cat"]} &middot; {a["mins"]} min read</p><h3>{a["title"]}</h3><p>{a["lede"]}</p><small>By {n}</small></div></a>')

def _filter(cats, attr="cat", label="Filter"):
    return (f'<div class="rs-flt" role="group" aria-label="{label}" data-attr="{attr}"><button type="button" class="ch" aria-pressed="true" data-v="">All</button>'
            + "".join(f'<button type="button" class="ch" aria-pressed="false" data-v="{c}">{c}</button>' for c in cats) + "</div>")

page("insights/index", "Insights", "Weekly articles by our scientists on regulation, methods, biologics, mRNA, quality and the testing market. Answer-first, referenced, written for QC and regulatory teams.",
     ANSWER("Insights is where our scientists explain what is changing in pharmaceutical testing and what to do about it. Every article opens with a short answer, lists key takeaways, and links to the methods, services and tools it mentions. New articles arrive weekly, following the editorial calendar below.")
     + SH("Featured", "This week's long read.") + _card(ARTS[0], True)
     + SH("All articles", "Browse by topic.") + _filter(CATS, label="Filter articles by category")
     + '<div class="rs-grid">' + "".join(_card(a) for a in ARTS) + '</div><p class="nores" hidden>No articles in this category yet.</p>'
     + SH("Editorial calendar", "The first 90 days.", "One flagship article a week, each with a tool or asset beside it.")
     + T(["Week", "Flagship article", "Supporting assets"], [[w, f'<a href="/insights/{ARTICLES[int(w) - 1]}.html">{t}</a>', s] for w, t, s in CALENDAR])
     + STRIP(["lab-corridor", "inst-lcms", "vax-vials", "micro-petri-1", "lab-instrument-load", "pharma-blisters", "room-clean-1", "bio-cells-green"])
     + '<div class="two" style="margin-top:40px"><div>' + H2("The Regulatory Radar, weekly") + P("One email a week on FDA, EMA and CDSCO changes that affect testing. Plain summaries and a link to the source.")
     + '</div><div>' + MAILFORM([("email", "Work email", "email", True), ("topics", "Main interest", CATS, False)], "Insights newsletter", "Subscribe") + '</div></div>',
     img="lab-team-three", eyebrow="Resources", hb="", desc="Weekly articles from PharmaCRO scientists on nitrosamines, stability, mRNA, biosimilars, data integrity and more.")

# ===================== Regulatory Radar =====================
RADAR_ITEMS = [
 ("Dec 2018", "FDA", "Data Integrity and Compliance With Drug CGMP: Questions and Answers (final guidance)", "Audit trails, shared log-ins and 'original records' are judged against this Q&A in every US inspection.", "Data integrity", "Quality"),
 ("Jul 2018", "MHRA", "'GXP' Data Integrity Guidance and Definitions (March 2018 revision)", "Defines data governance expectations across GLP, GCP and GMP; a common reference for UK and EU audits.", "Data integrity", "Quality"),
 ("2021", "WHO", "Guideline on data integrity, TRS 1033 Annex 4", "WHO prequalification inspections apply these expectations; relevant for vaccine and generic suppliers.", "Data integrity", "Quality"),
 ("May 2022", "ICH", "M10 Bioanalytical Method Validation adopted (Step 4)", "Chromatographic and ligand-binding PK assays are validated to one harmonised standard.", "Bioanalytical", "Methods"),
 ("Aug 2022", "EC", "EU GMP Annex 1 (manufacture of sterile medicinal products) revision published", "A contamination control strategy now ties together EM, water, sterility and CCI testing.", "Environmental monitoring", "Sterility"),
 ("Aug 2023", "EC", "Annex 1 revision comes into effect (point 8.123 on lyophilisers from Aug 2024)", "Expect inspectors to ask how EM trending and rapid methods feed your CCS.", "Environmental monitoring", "Sterility"),
 ("Aug 2023", "FDA", "Recommended Acceptable Intake Limits for NDSRIs (guidance, CPCA introduced)", "AIs from 26.5 to 1,500 ng/day depending on potency category; methods must reach these limits.", "Small molecule QC", "Nitrosamines"),
 ("Jul 2023", "EMA", "Nitrosamine Q&A revised to include the carcinogenic potency categorisation approach", "EU and US approaches to NDSRI limits now largely align.", "Small molecule QC", "Nitrosamines"),
 ("Nov 2023", "ICH", "Q2(R2) Validation of Analytical Procedures and Q14 Analytical Procedure Development adopted", "Lifecycle validation and enhanced development approaches become the default for new methods.", "Method validation", "Methods"),
 ("Dec 2023", "CDSCO", "Revised Schedule M (GMP) notified under the Drugs Rules, India", "Phased compliance: larger firms first, MSMEs later. QC capacity, in-house or outsourced, must be documented.", "Generics", "GMP"),
 ("2024", "CDSCO", "Extended timelines for MSME compliance with revised Schedule M", "Smaller Indian manufacturers gained time but still need a credible QC plan.", "Generics", "GMP"),
 ("2025", "ICH", "Q1 Stability Testing draft guideline (consolidating Q1A to Q1F and Q5C) released for consultation", "Stability expectations may change for some product types; watch the final text before redesigning programmes.", "Stability", "Stability"),
 ("2023", "USP", "General chapter <1220> Analytical Procedure Life Cycle official", "USP's lifecycle approach complements ICH Q14 and Q2(R2) for compendial users.", "Method validation", "Methods"),
 ("2025", "USP", "Chapter <86> Bacterial Endotoxins Test Using Recombinant Reagents becomes official", "Recombinant reagents get a dedicated compendial route in the US; plan comparability before switching.", "Microbiology", "Sterility"),
 ("2020", "Ph. Eur.", "Chapter 2.6.32 Test for bacterial endotoxins using recombinant factor C", "rFC is a compendial option in Europe; supports animal-free endotoxin testing.", "Microbiology", "Sterility"),
 ("Sep 2024", "FDA", "Final guidance on Q14 and Q2(R2) published for US use", "US submissions can reference enhanced development and lifecycle validation directly.", "Method validation", "Methods"),
 ("2019", "FDA", "Development of Therapeutic Protein Biosimilars: Comparative Analytical Assessment (draft guidance)", "Sets out tiering and statistical comparison of quality attributes for biosimilars.", "Biologics", "Biologics"),
 ("2023", "EMA", "Guideline on quality aspects of mRNA vaccines (reflection and Q&A work under way)", "Integrity, capping and dsRNA are expected CQAs; confirm the latest EMA text before filing.", "mRNA", "mRNA and Vaccines"),
]
REGS_R = sorted({r[1] for r in RADAR_ITEMS}); TOPS = sorted({r[5] for r in RADAR_ITEMS})
_rad = "".join(f'<li class="rd-i rs-ri reveal" style="--i:{i % 6}" data-reg="{g}" data-top="{tp}" tabindex="0"><time>{d}</time><span class="rd-g">{g}</span><b>{t}</b><em>What it means for testing: {k}</em>'
               f'<small>{tg} &middot; check the source on the {g} website</small></li>' for i, (d, g, t, k, tg, tp) in enumerate(RADAR_ITEMS))
page("regulatory-radar", "Regulatory Radar", "A curated feed of changes from FDA, EMA, CDSCO, WHO, ICH, USP and the European Pharmacopoeia, each with a short note on what it means for testing.",
     ANSWER("The Regulatory Radar tracks regulator and pharmacopoeia changes that affect analytical testing and explains, in one line, what each means in the lab. Items are curated summaries of public documents, not legal or regulatory advice. Always read the source document before acting; dates are given to the month or year we are confident of.")
     + '<div class="rs-flts">' + _filter(REGS_R, "reg", "Filter by regulator") + _filter(TOPS, "top", "Filter by topic") + '</div>'
     + f'<ul class="radar rs-radar">{_rad}</ul><p class="nores" hidden>No items match both filters.</p>'
     + SPLIT("docs-papers", H2("How we curate") + UL(["We read primary sources: guidance documents, pharmacopoeial notices and official gazettes.", "A scientist writes the 'what it means for testing' line; a second scientist reviews it.",
                                                     "Items are tagged to the services they affect, so the same note appears on the relevant service page.", "Corrections are made openly, with the date of the change."]))
     + '<div class="two"><div>' + H2("Get it weekly") + P("One email every Friday. RSS feed planned for launch; until then, email is the only channel.") + '</div><div>'
     + MAILFORM([("email", "Work email", "email", True), ("reg", "Regulators you care about", ["All", "FDA", "EMA", "CDSCO", "WHO", "PMDA", "ICH and pharmacopoeias"], False)], "Regulatory Radar subscription", "Subscribe") + '</div></div>'
     + f'<p class="cn">Curated summaries for information only. Not regulatory advice. {ILL("Pre-launch feed")}</p>',
     img="docs-papers", eyebrow="Resources", hb="", jsonld=[{"@context": "https://schema.org", "@type": "Dataset", "name": "PharmaCRO Regulatory Radar", "description": "Curated summaries of regulatory changes affecting pharmaceutical testing.", "creator": {"@type": "Organization", "name": BRAND}}])

# ===================== Case studies =====================
CS = [("lab-instrument-load", 6, " weeks", "Biosimilar comparability, 14 weeks to 6", "Biosimilars", "Biologics", "An EMA similarity package was quoted at 14 weeks across three suppliers.", "Charge, size, glycan and potency methods run in parallel at two labs on one LIMS.", "One consolidated report in 6 weeks.", "One report, one reviewer, one set of raw data."),
      ("pharma-blisters2", 21, " days early", "Nitrosamine testing cleared before a US launch", "Generics", "Small molecule QC", "An NDSRI risk was found six weeks before launch.", "48-hour risk assessment, method transfer from the flagship lab, Critical tier.", "Results 21 days before the deadline.", "The risk assessment arrived before our PO was signed."),
      ("bio-cells-green", 48, " hours", "Autologous CAR-T release in 48 hours", "Biotech startups", "Cell and gene therapy", "A 72-hour vein-to-vein window.", "Rapid sterility, flow identity and potency in parallel.", "Release data in 48 hours.", "For our patients the clock matters most."),
      ("vax-vials", 3, " labs", "mRNA cap and tail method transferred to three labs", "Vaccine makers", "mRNA and vaccines", "A vaccine maker needed the same LC-MS method in Asia and Europe.", "One validated method, the same instrument model and LIMS template at each site.", "All three transfers passed first time.", "We stopped arguing about integration rules."),
      ("lab-corridor", 36, " months", "Zone IVb stability for an ASEAN launch", "Generics", "Stability", "A Zone II programme would not support ASEAN filings.", "Redesigned to 30 °C / 75% RH with alu-alu packaging comparison.", "36-month shelf life supported across seven markets.", "The packaging study saved the launch."),
      ("room-clean-2", 0, " repeat findings", "Annex 1 EM programme rebuilt for a sterile CDMO", "CDMOs", "Environmental monitoring", "EM trending gaps were cited in an inspection.", "Risk-based sampling plan, new alert and action limits, monthly trend reports.", "Zero repeat findings at the next inspection.", "Our CCS finally reads like one document."),
      ("lab-vials-bw", 9, " weeks", "E&L study for a biologic in a prefilled syringe", "Big pharma", "Extractables and leachables", "A device change needed new E&L data fast.", "Supplier data reused where valid; targeted leachables on stability.", "Study design to first data in 9 weeks.", "They told us early what we could reuse."),
      ("inst-lcms", 2, " assays", "PK and ADA assays validated to ICH M10", "Biotech startups", "Bioanalytical", "A first-in-human study needed PK and ADA assays.", "LC-MS/MS PK and a bridging ADA assay developed in parallel.", "Both validated before the first dosing.", "We had data in hand before dosing started."),
      ("docs-papers", 1, " day", "Mock inspection before an FDA pre-approval inspection", "API manufacturers", "Regulatory support", "A PAI was announced at short notice.", "Two-day mock inspection with an ALCOA+ gap list.", "Gap list delivered in one day; all high items closed.", "The mock was harder than the real thing.")]
_ind = sorted({c[4] for c in CS}); _sv = sorted({c[5] for c in CS})
_grid = "".join(f'<article class="rs-cs reveal" data-ind="{c[4]}" data-svc="{c[5]}" style="--i:{i % 3}"><img src="/img/{c[0]}.jpg" alt="{alt(c[0])}" loading="lazy"><div><p class="ey">{c[4]} &middot; {c[5]}</p>'
                f'<b class="rs-m">{c[1]}{c[2]}</b><h3>{c[3]}</h3><dl><dt>Problem</dt><dd>{c[6]}</dd><dt>Approach</dt><dd>{c[7]}</dd><dt>Result</dt><dd>{c[8]}</dd></dl><p class="rs-q">&ldquo;{c[9]}&rdquo;</p>{ILL("Illustrative case")}</div></article>'
                for i, c in enumerate(CS))
page("case-studies", "Case studies", "Problem, approach, result and a quote. Filter by industry and service.",
     ANSWER("These case studies show the kinds of problems PharmaCRO is designed to solve. Until the network is operating they are illustrative scenarios, not real client results; real, approved case studies with client permission will replace them at launch. Each one shows the problem, the approach and the result.")
     + CASES([(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9]) for c in CS[:5]])
     + SH("All case studies", "Find one like yours.") + '<div class="rs-flts">' + _filter(_ind, "ind", "Filter by industry") + _filter(_sv, "svc", "Filter by service") + '</div>'
     + f'<div class="rs-csg">{_grid}</div><p class="nores" hidden>No case study matches both filters.</p>'
     + BAND("lab-team-three", "Have a problem like these?", "Tell us about it. A scientist replies within 4 business hours.", BTN("Talk to a scientist", "/book-a-call.html")),
     img="lab-team-three", eyebrow="Resources", hb="")

# ===================== Webinars =====================
WEB = [("2027-01-21T14:00:00Z", "Nitrosamines in 2027: setting limits and proving your method", "ananya", "60 min", "Regulatory"),
       ("2027-02-18T14:00:00Z", "Zone IVb stability without surprises", "rahul", "45 min", "Methods"),
       ("2027-03-11T15:00:00Z", "mRNA CQAs: from clinical to commercial", "kenji", "60 min", "mRNA and Vaccines"),
       ("2027-04-08T14:00:00Z", "Ten data integrity findings and how to prevent them", "helen", "60 min", "Quality")]
ONDEM = [("Method transfer that passes first time", "mei", "lab-analyst-pc", "48 min"), ("Biosimilar similarity: building the statistical argument", "elena", "lab-instrument-load", "55 min"),
         ("Endotoxin: LAL, rFC and low endotoxin recovery", "priya", "micro-petri-2", "40 min"), ("Annex 1 contamination control strategies", "tom", "room-clean-1", "50 min"),
         ("E&L for prefilled syringes", "lukas", "lab-vials-bw", "45 min"), ("ICH M10 in practice", "james", "inst-lcms", "52 min")]
w0 = WEB[0]
_up = "".join(f'<li class="rs-ev reveal" style="--i:{i}"><time datetime="{d}">{d[8:10]} {["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][int(d[5:7]) - 1]} {d[:4]}</time>'
              f'<div><b>{t}</b><span>{SCI[s][0]}, {SCI[s][1]} &middot; {du} &middot; {c}</span></div>'
              f'<button type="button" class="btn sm o rs-ics" data-start="{d}" data-dur="{int(du.split()[0])}" data-title="{html.escape(t)}">Add to calendar</button></li>' for i, (d, t, s, du, c) in enumerate(WEB))
_od = "".join(f'<figure class="rs-od reveal" style="--i:{i % 3}"><img src="/img/{im}.jpg" alt="{alt(im)}" loading="lazy"><figcaption><b>{t}</b><span>{SCI[s][0]} &middot; {du}</span>'
              f'<a href="mailto:{MAIL}?subject={html.escape("Recording request: " + t)}">Request the recording</a></figcaption></figure>' for i, (t, s, im, du) in enumerate(ONDEM))
page("webinars", "Webinars and events", "Live sessions with our scientists, on-demand recordings and the events where you can meet us.",
     ANSWER("Our webinars are 45 to 60 minute technical sessions led by scientists, with time for questions. Upcoming sessions are listed below with a calendar download; recordings are available on request. The schedule is illustrative until launch and may change.")
     + f'<section class="rs-next reveal"><div><p class="ey">Next live session</p><h2>{w0[1]}</h2><p>With {SCI[w0[2]][0]}, {SCI[w0[2]][1]}. {w0[3]}, live Q&amp;A. {ILL("Illustrative schedule")}</p>'
     + f'<div class="rs-cd" data-to="{w0[0]}" aria-live="off"><span><b data-u="d">0</b>days</span><span><b data-u="h">0</b>hours</span><span><b data-u="m">0</b>minutes</span><span><b data-u="s">0</b>seconds</span></div>'
     + f'<p><button type="button" class="btn rs-ics" data-start="{w0[0]}" data-dur="60" data-title="{html.escape(w0[1])}">Add to calendar (.ics)</button></p></div>'
     + MAILFORM([("name", "Name", "text", True), ("email", "Work email", "email", True), ("company", "Company", "text", False), ("session", "Session", [w[1] for w in WEB], True)], "Webinar registration", "Register", cls="rs-reg") + '</section>'
     + SH("Upcoming", "Coming up next.") + f'<ol class="rs-evs">{_up}</ol>'
     + SH("On demand", "Watch when it suits you.") + f'<div class="rs-ods">{_od}</div>'
     + SH("Speakers", "The scientists you will hear from.") + '<div class="scis">' + "".join(SCICARD(k) for k in ["ananya", "rahul", "kenji", "helen", "mei", "elena"]) + '</div>'
     + SPLIT("biz-highfive", H2("Meet us in person") + P("We plan to attend the major analytical and pharmaceutical meetings in India, Europe and the US. Dates will be listed here once confirmed.") + BTN("Book a meeting", "/book-a-call.html"), flip=True),
     img="biz-team-laptops", eyebrow="Resources", hb="", jsonld=[{"@context": "https://schema.org", "@type": "Event", "name": w[1], "startDate": w[0], "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
                                                                 "eventStatus": "https://schema.org/EventScheduled", "location": {"@type": "VirtualLocation", "url": f"{DOMAIN}/webinars.html"}, "organizer": {"@type": "Organization", "name": BRAND}} for w in WEB])

# ===================== Whitepapers =====================
WP = [("The Complete Guide to Pharmaceutical Stability Testing", "Stability", ["ICH zones and conditions", "Protocol design, bracketing and matrixing", "OOT and OOS trending", "Shelf-life statistics", "Protocol template"], "48 pages"),
      ("mRNA Analytical Playbook: From Clinical to Commercial", "mRNA", ["CQA map for mRNA-LNP", "Method maturity by phase", "Reference standards", "Transfer and comparability"], "36 pages"),
      ("Biosimilar Analytical Similarity Handbook", "Biologics", ["Attribute risk ranking", "Reference lot sourcing", "Statistical approaches", "Presenting the data"], "42 pages"),
      ("Data Integrity Inspection Readiness Kit", "Quality", ["ALCOA+ self-assessment", "Audit trail review SOP template", "Mock inspection script", "Top findings checklist"], "30 pages"),
      ("Tech Transfer Checklist and Gantt Template", "Methods", ["Gap assessment checklist", "Protocol template", "Acceptance criteria guide", "Gantt template"], "20 pages + XLSX"),
      ("Vendor Qualification Pack", "Procurement", ["Quality manual summary", "Accreditation scope (target)", "SOP index", "Organisation chart", "Insurance summary"], "Pack"),
      ("Annual State of Pharma Testing Report", "Market", ["Survey method", "Outsourcing trends", "Turnaround benchmarks", "Data integrity trends"], "Published 2027")]
_wp = "".join(f'<article class="rs-wp reveal" style="--i:{i % 3}"><div class="rs-cov" aria-hidden="true"><div class="rs-bk" style="--h:{(i * 47) % 360}"><span>{BRAND}</span><b>{t}</b><em>{c}</em>{PEAK}</div></div>'
              f'<div><p class="ey">{c} &middot; {pg}</p><h3>{t}</h3>{UL(L)}</div></article>' for i, (t, c, L, pg) in enumerate(WP))
page("whitepapers", "Whitepapers", "Deep guides you can keep: stability, mRNA, biosimilars, data integrity, tech transfer, vendor qualification and our annual report.",
     ANSWER("Our whitepapers are practical, referenced guides written by scientists. Each one is free; we ask for your work email, company and role so we can send it and, if you agree, follow up once. Titles marked for 2027 are in preparation and will be emailed when ready.")
     + f'<div class="rs-wps">{_wp}</div>'
     + '<div class="two" style="margin-top:40px"><div>' + H2("Get a guide") + P("Choose a title. We send it by email and never share your details.") + IMG("docs-papers", "Every guide is reviewed by a second scientist (illustrative stock photo)") + '</div><div>'
     + MAILFORM([("email", "Work email", "email", True), ("company", "Company", "text", True), ("role", "Role", ["QC / analytical", "QA", "Regulatory affairs", "Procurement", "R&D / CMC", "Executive", "Other"], True),
                 ("title", "Guide", [w[0] for w in WP], True), ("ok", "I agree to one follow-up email about this guide", "checkbox", False)], "Whitepaper request", "Send me the guide",
                "Your email app has opened with the request. Press send and the guide arrives within one business day.") + '</div></div>'
     + f'<p class="cn">{ILL("In preparation")} Guides are being written ahead of launch.</p>',
     img="docs-papers", eyebrow="Resources", hb="")

# ===================== Glossary =====================
G = [("ADA", "Anti-drug antibody: an antibody a patient makes against a biologic medicine. Measured in immunogenicity testing."),
 ("Acceptable intake (AI)", "The daily intake of a mutagenic impurity, such as a nitrosamine, considered to pose negligible cancer risk over a lifetime."),
 ("Accelerated stability", "Storage at elevated stress, usually 40 °C / 75% RH for six months, to predict long-term behaviour."),
 ("Accuracy", "How close a measured result is to the true value. A validation characteristic under ICH Q2(R2)."),
 ("AET", "Analytical evaluation threshold: the level above which an extractable or leachable must be identified and assessed."),
 ("ALCOA+", "Data integrity principles: attributable, legible, contemporaneous, original, accurate, plus complete, consistent, enduring and available."),
 ("Alert limit", "An environmental monitoring level that signals a possible drift from normal conditions before the action limit is reached."),
 ("Action limit", "An environmental monitoring level that, when exceeded, requires investigation and corrective action."),
 ("API", "Active pharmaceutical ingredient: the substance in a medicine that produces its effect."),
 ("Assay", "A test that measures the amount of active ingredient, usually as a percentage of the label claim."),
 ("Audit trail", "A secure, computer-generated record of who created, changed or deleted data, when and why."),
 ("AUC (analytical ultracentrifugation)", "A method that separates particles by sedimentation; the reference method for AAV empty/full capsid ratio."),
 ("Batch release", "The formal decision, by a qualified person or equivalent, that a batch meets its specification and may be supplied."),
 ("Bioburden", "The number of viable microorganisms on or in a product or component before sterilisation."),
 ("Biosimilar", "A biologic medicine highly similar to an approved reference biologic, with no clinically meaningful differences."),
 ("Bracketing", "A stability design that tests only the extremes, such as highest and lowest strength, under ICH Q1D."),
 ("CAPA", "Corrective and preventive action: the process for fixing a problem's cause and stopping it recurring."),
 ("Capping efficiency", "The percentage of mRNA molecules with a correct 5' cap structure."),
 ("CCI", "Container closure integrity: the ability of a package to keep out microorganisms and gases over shelf life."),
 ("CDSCO", "Central Drugs Standard Control Organisation: India's national drug regulator."),
 ("CE-SDS", "Capillary electrophoresis with sodium dodecyl sulfate: measures protein size variants and fragments."),
 ("CFU", "Colony-forming unit: a count of viable microorganisms capable of forming a colony on a growth medium."),
 ("Change control", "A formal process for proposing, assessing, approving and documenting changes in a GMP environment."),
 ("Chromatogram", "The plot produced by chromatography showing detector response against time; peaks represent separated components."),
 ("CoA", "Certificate of analysis: a signed document listing the tests performed on a batch and the results."),
 ("Comparability", "Evidence that a product before and after a process change has comparable quality, safety and efficacy."),
 ("Content uniformity", "A test that each dosage unit contains the active ingredient within a narrow range of the label claim."),
 ("Contemporaneous", "Recorded at the time the activity is performed. One of the ALCOA principles."),
 ("CPCA", "Carcinogenic potency categorisation approach: assigns NDSRIs to potency categories that set default acceptable intakes."),
 ("CQA", "Critical quality attribute: a property that must stay within limits to ensure product quality."),
 ("CRO", "Contract research organisation: a company that provides research or testing services under contract."),
 ("CTD Module 3", "The quality section of the Common Technical Document used in regulatory submissions."),
 ("ddPCR", "Droplet digital PCR: absolute quantification of nucleic acids by partitioning a sample into thousands of droplets."),
 ("Data integrity", "The completeness, consistency and accuracy of data throughout its life cycle."),
 ("Degradant", "An impurity formed when the drug substance or product breaks down over time."),
 ("Deviation", "A departure from an approved procedure or specification that must be documented and assessed."),
 ("Dissolution", "A test of how fast and how completely the active ingredient dissolves from a solid dosage form."),
 ("DLS", "Dynamic light scattering: measures particle size from fluctuations in scattered light."),
 ("dsRNA", "Double-stranded RNA: an impurity in mRNA manufacture that can trigger innate immune responses."),
 ("Dwell volume", "The volume between the HPLC mixing point and the column head; differences shift gradient retention times."),
 ("E&L", "Extractables and leachables: compounds that can migrate, or do migrate, from packaging or equipment into a product."),
 ("Electronic signature", "A computer data compilation executed, adopted or authorised by a person as the legal equivalent of a handwritten signature."),
 ("Encapsulation efficiency", "The proportion of mRNA inside lipid nanoparticles rather than free in solution."),
 ("Endotoxin", "Lipopolysaccharide from Gram-negative bacteria that causes fever when injected."),
 ("Environmental monitoring (EM)", "Routine sampling of air, surfaces and personnel in cleanrooms to show control of contamination."),
 ("EU (endotoxin unit)", "The unit used to express endotoxin activity."),
 ("Excipient", "Any ingredient of a medicine other than the active ingredient."),
 ("Extractables", "Compounds released from a material under exaggerated laboratory conditions."),
 ("f2 similarity factor", "A statistic that compares two dissolution profiles; 50 or above suggests similarity."),
 ("Forced degradation", "Deliberate stress of a drug under heat, light, acid, base and oxidation to identify degradants and prove a method is stability-indicating."),
 ("FTIR", "Fourier transform infrared spectroscopy: identifies materials by their infrared absorption."),
 ("GC-HS", "Headspace gas chromatography: used to measure residual solvents."),
 ("GLP", "Good Laboratory Practice: the quality system for non-clinical safety studies."),
 ("GMP", "Good Manufacturing Practice: the quality system governing manufacture and testing of medicines."),
 ("Glycan profiling", "Characterisation of the sugar structures attached to a glycoprotein."),
 ("HCP", "Host cell proteins: process impurities from the cells used to make a biologic."),
 ("HPLC", "High-performance liquid chromatography: separates compounds in a liquid by passing them through a packed column."),
 ("ICH", "International Council for Harmonisation: develops harmonised guidelines for medicine quality, safety and efficacy."),
 ("ICH Q1A(R2)", "The ICH guideline on stability testing of new drug substances and products."),
 ("ICH Q2(R2)", "The ICH guideline on validation of analytical procedures, revised and adopted in 2023."),
 ("ICH Q3D", "The ICH guideline on elemental impurities, with permitted daily exposures for 24 elements."),
 ("ICH Q14", "The ICH guideline on analytical procedure development, adopted in 2023."),
 ("ICH M10", "The ICH guideline on bioanalytical method validation, adopted in 2022."),
 ("icIEF", "Imaged capillary isoelectric focusing: separates protein charge variants."),
 ("ICP-MS", "Inductively coupled plasma mass spectrometry: measures elements at trace levels."),
 ("Identification test", "A test that confirms a substance is what it is labelled to be."),
 ("Immunogenicity", "The tendency of a medicine to provoke an immune response."),
 ("In-use stability", "A study of how long a product stays within specification after the container is opened or the product is prepared."),
 ("Intermediate precision", "Variation within one laboratory across days, analysts or equipment."),
 ("ISO/IEC 17025", "The international standard for the competence of testing and calibration laboratories."),
 ("ISO 14644", "The international standard series for cleanroom classification and monitoring."),
 ("Karl Fischer", "A titration method for measuring water content."),
 ("LAL", "Limulus amebocyte lysate: a reagent from horseshoe crab blood used to detect endotoxin."),
 ("LC-MS/MS", "Liquid chromatography with tandem mass spectrometry: sensitive and selective quantification of compounds."),
 ("Leachables", "Compounds that migrate into a product from its packaging or contact materials under normal conditions."),
 ("LIMS", "Laboratory information management system: software that manages samples, tests, results and reports."),
 ("Limit of detection (LOD)", "The lowest amount of analyte that can be detected but not necessarily quantified."),
 ("Limit of quantitation (LOQ)", "The lowest amount of analyte that can be measured with acceptable accuracy and precision."),
 ("Linearity", "The ability of a method to give results proportional to analyte concentration over a range."),
 ("LNP", "Lipid nanoparticle: the delivery vehicle for most mRNA medicines."),
 ("Long-term stability", "Storage under the recommended condition for the climatic zone, over the proposed shelf life."),
 ("Matrixing", "A stability design that tests a subset of samples at each time point, under ICH Q1D."),
 ("MSA", "Master service agreement: a framework contract setting terms for future work orders."),
 ("Method transfer", "The documented process that qualifies a receiving laboratory to use an analytical method."),
 ("Method validation", "Documented evidence that an analytical method is suitable for its intended purpose."),
 ("Method verification", "Confirmation that a compendial method works in a given laboratory for a given product."),
 ("MVD", "Maximum valid dilution: the greatest dilution of a sample at which the endotoxin limit can still be detected."),
 ("Mycoplasma", "Small bacteria without a cell wall that can contaminate cell cultures and biologic processes."),
 ("NAT", "Nucleic acid amplification technique, such as PCR, used for rapid detection of organisms like mycoplasma."),
 ("NDSRI", "Nitrosamine drug substance-related impurity: a nitrosamine that shares structure with the API."),
 ("Nitrosamine", "A compound with an N-nitroso group; many are probable human carcinogens."),
 ("OOS", "Out of specification: a result outside the established acceptance criteria."),
 ("OOT", "Out of trend: a result within specification but unexpected compared with earlier data."),
 ("Orthogonal method", "A method based on a different principle, used to confirm a result."),
 ("Part 11", "US regulation 21 CFR Part 11 on electronic records and electronic signatures."),
 ("PDI", "Polydispersity index: a measure of how broad a particle size distribution is."),
 ("Peptide mapping", "Digestion of a protein into peptides and analysis by LC-MS to confirm its sequence and modifications."),
 ("Pharmacopoeia", "An official book of standards for medicines, such as USP, Ph. Eur., JP and IP."),
 ("Photostability", "Testing of how light affects a drug, under ICH Q1B."),
 ("PK", "Pharmacokinetics: how the body absorbs, distributes, metabolises and eliminates a drug."),
 ("Poly(A) tail", "The adenosine sequence at the 3' end of mRNA that supports stability and translation."),
 ("Polymorph", "One of several crystal forms of the same compound, which may differ in solubility and stability."),
 ("Potency", "A measure of biological activity, usually relative to a reference standard."),
 ("Precision", "How close repeated measurements are to each other."),
 ("Pull point", "A scheduled time at which stability samples are removed from storage and tested."),
 ("QbD", "Quality by design: a systematic approach that builds quality in from product and process understanding."),
 ("Qualified person (QP)", "In the EU, the person legally responsible for certifying each batch before release."),
 ("Reference standard", "A highly characterised material used as the benchmark in a test."),
 ("Related substances", "Impurities structurally related to the API, such as by-products and degradants."),
 ("Residual solvents", "Organic volatile chemicals left over from manufacture, limited under ICH Q3C."),
 ("rFC", "Recombinant factor C: an animal-free reagent for endotoxin testing."),
 ("Robustness", "A method's ability to stay unaffected by small, deliberate changes in conditions."),
 ("SEC", "Size-exclusion chromatography: separates molecules by size, used for protein aggregates."),
 ("Specification", "The list of tests, methods and acceptance criteria a product must meet."),
 ("Specificity", "A method's ability to measure the analyte without interference from other components."),
 ("Stability-indicating method", "A method that can detect changes in quality attributes over time, separating the API from its degradants."),
 ("Sterility test", "A compendial test for viable microorganisms in a product labelled sterile, usually 14 days of incubation."),
 ("System suitability", "Checks run with each analysis to confirm the system performs adequately on the day."),
 ("TAT", "Turnaround time: time from sample receipt to issue of the report."),
 ("TOC", "Total organic carbon: a test of organic contamination in pharmaceutical water."),
 ("True copy", "A verified copy of an original record that preserves its content and meaning."),
 ("UPLC", "Ultra-performance liquid chromatography: HPLC with small particles and high pressure for faster separations."),
 ("USP", "United States Pharmacopeia: sets public standards for medicines in the US."),
 ("Validation protocol", "A pre-approved plan that states how a validation will be done and what results are acceptable."),
 ("Vector genome titre", "The number of vector genomes per millilitre in a gene therapy product."),
 ("WFI", "Water for injections: highly purified water meeting pharmacopoeial limits for endotoxin and conductivity."),
 ("XRPD", "X-ray powder diffraction: identifies crystal forms by their diffraction pattern."),
 ("Zone IVb", "The hot and very humid ICH climatic zone; long-term stability at 30 °C / 75% RH."),
]
G.sort(key=lambda x: x[0].lower())
def _gid(t): return "g-" + re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
_letters = sorted({t[0].upper() for t, _ in G})
_jump = "".join(f'<a href="#L-{l}">{l}</a>' if l in _letters else f'<span>{l}</span>' for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
_gl = ""
for l in _letters:
    _gl += f'<section class="rs-gs" id="L-{l}"><h2>{l}</h2><dl>' + "".join(f'<div class="rs-gt" id="{_gid(t)}"><dt>{t}</dt><dd>{d}</dd></div>' for t, d in G if t[0].upper() == l) + "</dl></section>"
page("glossary", "Glossary", f"{len(G)} pharmaceutical testing terms in plain words, from accelerated stability to Zone IVb.",
     ANSWER(f"This glossary explains {len(G)} terms used in pharmaceutical analytical testing, quality and regulation, in plain words. Use the A to Z bar or the search box. Every term has its own anchor, so you can link straight to it.")
     + f'<div class="rs-gbar"><nav class="rs-az" aria-label="A to Z">{_jump}</nav><label><span class="vh">Search terms</span><input type="search" class="rs-gq" placeholder="Search {len(G)} terms"></label></div>'
     + f'<div class="rs-gl">{_gl}</div><p class="nores" hidden>No term matches. <a href="/request-quote.html">Ask a scientist</a>.</p>',
     img="lab-glassware", eyebrow="Resources", hb="",
     jsonld=[{"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "PharmaCRO pharmaceutical testing glossary", "url": f"{DOMAIN}/glossary.html",
              "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d, "url": f"{DOMAIN}/glossary.html#{_gid(t)}"} for t, d in G]}])
assert len(G) >= 120, len(G)
