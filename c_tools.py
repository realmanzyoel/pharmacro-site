"""Tools hub + 12 interactive tools (blueprint section 5). Behaviour: assets/m_tools.js, styles: assets/m_tools.css (prefix .tk-)."""
from ph import *

TN = dict(TOOLS)
def J(o): return html.escape(json.dumps(o, ensure_ascii=False))
def SEND(label="Send this to a scientist"):
    return f'<a class="btn tk-send" href="/request-quote.html">{label}</a>'
def RADIOS(name, legend, opts, first=True):
    o = "".join(f'<label class="pick"><input type="radio" name="{name}" value="{v}"{" checked" if (first and i == 0) else ""}><span>{t}</span></label>' for i, (v, t) in enumerate(opts))
    return f'<fieldset class="tk-fs"><legend>{legend}</legend><div class="picks">{o}</div></fieldset>'
def SEL(name, label, opts, sel=None):
    o = "".join(f'<option value="{v}"{" selected" if v == sel else ""}>{t}</option>' for v, t in opts)
    return f'<label><span>{label}</span><select name="{name}">{o}</select></label>'
def NUM(name, label, val, mn=0, mx=None, step=1):
    return f'<label><span>{label}</span><input type="number" name="{name}" value="{val}" min="{mn}"' + (f' max="{mx}"' if mx is not None else "") + f' step="{step}" inputmode="decimal"></label>'

# ---------- per-tool data ----------
SVC_IDX = {s[0]: i for i, s in enumerate(SERVICES)}
BASE_DAYS = {"small-molecule-qc-release": 6, "stability-studies": 7, "method-development-validation": 30, "biologics-characterization-release": 10,
             "mrna-vaccine-testing": 8, "cell-gene-therapy-testing": 7, "microbiology-sterility": 14, "environmental-monitoring": 4,
             "extractables-leachables": 40, "bioanalytical-immunogenicity": 20, "reference-standards-excipients": 6, "regulatory-data-integrity-support": 20}
FINDER = dict(
    svc=[dict(k=s[0], n=s[1], u=svc_url(s[0]), i=i, mod=s[9], stg=s[10], tests=s[7], tat=s[6]) for i, s in enumerate(SERVICES)],
    labs=[dict(s=l[0], c=l[1], co=l[2], r=l[3], ph=l[6], sp=l[9]) for l in LABS],
    q={"release": ["small-molecule-qc-release", "biologics-characterization-release", "mrna-vaccine-testing", "cell-gene-therapy-testing", "microbiology-sterility"],
       "shelf": ["stability-studies"], "method": ["method-development-validation"], "similar": ["biologics-characterization-release", "bioanalytical-immunogenicity"],
       "impurity": ["small-molecule-qc-release", "extractables-leachables", "reference-standards-excipients"], "micro": ["microbiology-sterility", "environmental-monitoring"],
       "pack": ["extractables-leachables"], "clinical": ["bioanalytical-immunogenicity"], "inspect": ["regulatory-data-integrity-support"],
       "raw": ["reference-standards-excipients"]})
CAT = [("HPLC assay and related substances", 350, 650, 5), ("Dissolution profile (6 units)", 400, 800, 5), ("Content uniformity (10 units)", 300, 550, 5),
       ("Residual solvents (GC-HS, ICH Q3C)", 300, 600, 5), ("Elemental impurities panel (ICP-MS, ICH Q3D)", 450, 900, 7), ("Nitrosamines / NDSRI (LC-MS/MS)", 700, 1400, 7),
       ("Water content (Karl Fischer)", 80, 150, 3), ("XRPD polymorph identity", 250, 500, 5), ("Sterility (membrane filtration)", 450, 850, 14),
       ("Bacterial endotoxins (kinetic LAL)", 120, 250, 3), ("Bioburden (TAMC/TYMC)", 120, 250, 5), ("Mycoplasma (NAT)", 900, 1800, 5),
       ("SEC-HPLC aggregates", 350, 700, 7), ("CE-SDS (reduced and non-reduced)", 450, 900, 7), ("icIEF charge variants", 500, 950, 7),
       ("Peptide mapping (LC-MS)", 1800, 3500, 12), ("Released glycan profiling (HILIC-FLD)", 1200, 2400, 10), ("mRNA integrity (CE)", 400, 800, 5),
       ("5' capping efficiency (LC-MS)", 1500, 3000, 10), ("LNP size, PDI and encapsulation", 500, 1000, 5), ("Vector genome titre (ddPCR)", 700, 1400, 5),
       ("Stability pull, full specification (per batch)", 900, 1600, 10), ("HPLC method validation (ICH Q2(R2), per method)", 9000, 22000, 30)]
DAYS_SVC = [dict(n=s[1], b=BASE_DAYS[s[0]]) for s in SERVICES]
LOC = dict(labs=[dict(s=l[0], c=l[1], co=l[2], r=l[3], la=l[4], lo=l[5], ph=l[6], f=l[7]) for l in LABS], cities=CITIES)
CUSTOMS = {
 "India": "Import of drug samples for examination, test or analysis normally needs a test licence (Form 11 under the Drugs and Cosmetics Rules, 1945) held by the receiving lab. We arrange it before you ship; allow 2 to 4 weeks for a first licence.",
 "Singapore": "Samples for testing are declared to Singapore Customs; health products may also need HSA import authorisation. Mark the commercial invoice 'samples for laboratory analysis, no commercial value'.",
 "Malaysia": "Pharmaceutical samples may need NPRA import permission in addition to customs declaration. Ship only after we confirm the permit reference.",
 "Netherlands": "From outside the EU, samples clear EU customs with a pro-forma invoice. Controlled substances and biological materials of human origin need extra permits.",
 "United Kingdom": "Since 2021 the UK is outside the EU customs union: EU and non-EU shipments both need a customs declaration. Biological materials may need a Defra or HSE check.",
 "Ireland": "EU customs rules apply. Shipments from Great Britain need a customs declaration. Ship Monday to Wednesday to avoid weekend holds.",
 "United States": "Drug samples entering the US are subject to FDA import entry review via the broker; use 'for laboratory testing only' wording and include the FDA product code if known.",
}
COLD = [("Controlled room temperature (15 to 25 °C)", "Insulated box with a temperature logger. Avoid weekend transit."),
        ("Refrigerated (2 to 8 °C)", "Validated passive shipper with phase-change packs conditioned to 5 °C, plus a logger; 72 to 120 hour duration."),
        ("Frozen (−20 °C)", "Pre-frozen gel packs or dry ice depending on duration; logger required."),
        ("Deep frozen (−70 °C and below, dry ice)", "Dry ice is dangerous goods: UN1845, IATA Packing Instruction 954, and the box must vent CO₂."),
        ("Cryogenic (below −150 °C)", "Liquid nitrogen dry shipper for cell therapies; continuous temperature and tilt monitoring.")]

M = [  # slug, technique, purpose, standards, sample, TAT, modality
 ("hplc-assay-related-substances", "HPLC-UV", "Assay and impurity profile of drug substance and product", "USP <621>, Ph. Eur. 2.2.46, ICH Q2(R2)", "100 mg to 1 g or 10 units", "3 to 7 days", "Small molecule"),
 ("uplc-impurity-profiling", "UPLC-UV/PDA", "High-resolution impurity profiling and faster run times", "USP <621>, ICH Q3A/Q3B", "100 mg or 10 units", "3 to 7 days", "Small molecule"),
 ("dissolution-testing", "USP apparatus 1 to 4 with HPLC or UV", "Drug release rate from solid oral and modified-release forms", "USP <711>, <724>, Ph. Eur. 2.9.3", "12 to 24 units", "3 to 7 days", "Small molecule"),
 ("content-uniformity", "HPLC or UV per unit", "Dose uniformity between units", "USP <905>, Ph. Eur. 2.9.40", "30 units", "3 to 5 days", "Small molecule"),
 ("residual-solvents-gc-hs", "Headspace GC-FID", "Class 1 to 3 residual solvents", "USP <467>, ICH Q3C(R8)", "1 g", "3 to 5 days", "Small molecule"),
 ("elemental-impurities-icp-ms", "Microwave digestion + ICP-MS", "The 24 ICH Q3D elements by route of administration", "USP <232>/<233>, ICH Q3D(R2)", "1 to 2 g", "5 to 7 days", "All"),
 ("nitrosamines-lc-ms-ms", "LC-MS/MS (MRM) or LC-HRMS", "Small nitrosamines and NDSRIs at ng/g levels", "FDA nitrosamine guidance, EMA Art. 5(3) outcome, Ph. Eur. 2.5.42", "1 to 5 g", "5 to 10 days", "Small molecule"),
 ("genotoxic-impurities", "GC-MS or LC-MS/MS", "Mutagenic impurities against TTC-based limits", "ICH M7(R2)", "1 to 5 g", "5 to 10 days", "Small molecule"),
 ("xrpd-polymorph", "X-ray powder diffraction", "Crystal form identity and polymorph screening", "USP <941>, Ph. Eur. 2.9.33", "200 mg", "3 to 5 days", "Small molecule"),
 ("particle-size-laser-diffraction", "Laser diffraction", "Particle size distribution (D10, D50, D90)", "USP <429>, Ph. Eur. 2.9.31", "1 to 5 g", "3 to 5 days", "Small molecule"),
 ("water-content-karl-fischer", "Volumetric or coulometric KF", "Water content", "USP <921>, Ph. Eur. 2.5.12/2.5.32", "0.5 to 2 g", "1 to 3 days", "All"),
 ("ftir-identification", "FTIR (ATR or KBr)", "Identity against a reference spectrum", "USP <197>, Ph. Eur. 2.2.24", "50 mg", "1 to 3 days", "Small molecule"),
 ("raman-identification", "Raman spectroscopy", "Non-destructive raw material identity, through packaging", "USP <1120>, Ph. Eur. 2.2.48", "As received", "1 to 2 days", "Small molecule"),
 ("ich-stability-storage", "Qualified stability chambers", "Long-term, intermediate and accelerated storage", "ICH Q1A(R2), WHO TRS 1010 Annex 10", "Per protocol", "Per pull schedule", "All"),
 ("photostability-q1b", "ICH Q1B Option 1 or 2 light cabinet", "Light sensitivity of substance and product", "ICH Q1B", "Per protocol", "2 to 3 weeks", "All"),
 ("forced-degradation", "Stress studies + HPLC/LC-MS", "Degradation pathways and stability-indicating proof", "ICH Q1A(R2), Q2(R2)", "1 to 5 g", "2 to 4 weeks", "Small molecule"),
 ("sec-hplc-aggregates", "Size-exclusion HPLC (UV, optional MALS)", "High-molecular-weight species and fragments", "USP <129>, Ph. Eur. 2.2.30", "1 mg protein", "5 to 7 days", "Biologic"),
 ("ce-sds", "Capillary electrophoresis SDS", "Purity and fragments, reduced and non-reduced", "USP <1053>, Ph. Eur. 2.2.47", "0.5 mg protein", "5 to 7 days", "Biologic"),
 ("icief-charge-variants", "Imaged capillary isoelectric focusing", "Acidic and basic charge variants, pI", "USP <1053>", "0.5 mg protein", "5 to 7 days", "Biologic"),
 ("peptide-mapping-lc-ms", "Enzymatic digest + LC-MS/MS", "Primary structure, PTMs and sequence coverage", "USP <1055>, ICH Q6B", "1 mg protein", "10 to 15 days", "Biologic"),
 ("intact-mass-ms", "LC-HRMS (intact and subunit)", "Molecular mass, glycoforms and clipping", "ICH Q6B", "0.5 mg protein", "5 to 10 days", "Biologic"),
 ("glycan-profiling-hilic", "Released glycans, HILIC-FLD/MS", "N-glycan distribution (afucosylation, galactosylation, sialylation)", "USP <212>, ICH Q6B", "1 mg protein", "7 to 12 days", "Biologic"),
 ("cell-based-potency", "Cell-based bioassay (reporter, ADCC, CDC)", "Biological activity relative to a reference standard", "USP <1032>/<1033>/<1034>", "1 to 5 mg", "10 to 20 days", "Biologic"),
 ("hcp-elisa", "Host cell protein ELISA (+ LC-MS optional)", "Residual host cell proteins", "USP <1132>", "1 mL", "5 to 7 days", "Biologic"),
 ("residual-dna-qpcr", "qPCR", "Residual host cell DNA", "USP <1130>, WHO TRS 978", "1 mL", "5 to 7 days", "Biologic"),
 ("mrna-integrity-ce", "Capillary gel electrophoresis / fragment analyser", "Full-length mRNA percentage and fragments", "USP draft mRNA guidelines, Ph. Eur. 5.36", "50 µg RNA", "3 to 7 days", "mRNA"),
 ("mrna-capping-lc-ms", "RNase H cleavage + LC-MS", "5' cap structure and capping efficiency", "USP draft mRNA guidelines", "50 to 100 µg RNA", "7 to 12 days", "mRNA"),
 ("poly-a-tail-length", "RNase T1 digest + LC-MS or CE", "Poly(A) tail length and distribution", "USP draft mRNA guidelines", "50 µg RNA", "7 to 12 days", "mRNA"),
 ("dsrna-elisa", "J2 antibody ELISA or dot blot", "Residual double-stranded RNA", "USP draft mRNA guidelines", "20 µg RNA", "3 to 5 days", "mRNA"),
 ("lnp-size-pdi-dls", "Dynamic light scattering", "LNP particle size and polydispersity", "USP <1430.x> drafts, ISO 22412", "0.5 mL", "1 to 3 days", "mRNA"),
 ("encapsulation-efficiency-ribogreen", "RiboGreen fluorescence with detergent lysis", "Encapsulated vs free RNA", "In-house validated", "0.5 mL", "2 to 4 days", "mRNA"),
 ("ddpcr-vector-titre", "Droplet digital PCR", "Vector genome titre", "Ph. Eur. 2.6.21, USP <1047>", "100 µL", "3 to 7 days", "CGT"),
 ("aav-empty-full-auc", "Analytical ultracentrifugation (SV-AUC)", "Empty, partial and full capsid ratio", "USP <1047>", "400 µL", "7 to 14 days", "CGT"),
 ("flow-cytometry-identity", "Multicolour flow cytometry", "Identity, purity and viability of cell products", "USP <1027>, Ph. Eur. 2.7.24", "10⁶ cells", "1 to 3 days", "CGT"),
 ("sterility-membrane-filtration", "Membrane filtration or direct inoculation", "Absence of viable microorganisms", "USP <71>, Ph. Eur. 2.6.1, 21 CFR 610.12", "20 containers (typical)", "14 days + 2", "All"),
 ("bacterial-endotoxins-lal", "LAL kinetic chromogenic/turbidimetric or gel clot", "Bacterial endotoxins against K/M limit", "USP <85>, Ph. Eur. 2.6.14", "2 to 5 units", "1 to 3 days", "All"),
 ("recombinant-factor-c", "Recombinant factor C (fluorescent)", "Animal-free endotoxin test", "Ph. Eur. 2.6.32, USP <86>", "2 to 5 units", "1 to 3 days", "All"),
 ("mycoplasma-nat", "Nucleic acid amplification (qPCR)", "Rapid mycoplasma detection", "Ph. Eur. 2.6.7, USP <63>", "1 to 10 mL", "2 to 5 days", "Biologic, CGT"),
 ("bioburden", "Membrane filtration / plate count", "Total aerobic microbial and yeast/mould counts", "USP <61>/<62>, Ph. Eur. 2.6.12/2.6.13", "10 g or 10 mL", "5 to 7 days", "All"),
 ("container-closure-integrity", "Vacuum decay, HVLD or headspace analysis", "Deterministic container closure integrity", "USP <1207>", "30 to 100 units", "5 to 10 days", "All"),
 ("toc-conductivity-water", "TOC analyser and conductivity", "Purified water and WFI quality", "USP <643>, <645>, Ph. Eur. 2.2.44", "250 mL", "1 to 3 days", "All"),
 ("extractables-gc-ms", "GC-MS, LC-MS and ICP-MS after solvent extraction", "Extractable profile of packaging and components", "USP <1663>, PQRI", "Components", "4 to 8 weeks", "All"),
 ("leachables-lc-ms", "Targeted LC-MS/GC-MS in product", "Leachables on stability against safety thresholds", "USP <1664>", "Product per pull", "2 to 4 weeks per pull", "All"),
 ("lc-ms-ms-pk-assay", "LC-MS/MS bioanalysis", "Drug concentrations in plasma or serum for PK", "ICH M10", "100 to 250 µL", "1 to 3 weeks", "Small molecule, peptide"),
 ("ada-bridging-assay", "Bridging ELISA / ECL (screen, confirm, titre)", "Anti-drug antibodies in a tiered approach", "FDA immunogenicity guidance (2019), EMA", "100 µL serum", "2 to 4 weeks", "Biologic"),
 ("nab-cell-based-assay", "Cell-based neutralising antibody assay", "Neutralising capacity of ADA-positive samples", "FDA immunogenicity guidance (2019)", "100 µL serum", "3 to 5 weeks", "Biologic"),
]
MNAMES = ['HPLC assay and related substances', 'UPLC impurity profiling', 'Dissolution testing', 'Content uniformity', 'Residual solvents (GC-HS)', 'Elemental impurities (ICP-MS)', 'Nitrosamines and NDSRIs (LC-MS/MS)', 'Genotoxic impurities', 'XRPD polymorph identification', 'Particle size (laser diffraction)', 'Water content (Karl Fischer)', 'FTIR identification', 'Raman identification', 'ICH stability storage', 'Photostability (ICH Q1B)', 'Forced degradation', 'SEC-HPLC aggregates', 'CE-SDS purity', 'icIEF charge variants', 'Peptide mapping (LC-MS)', 'Intact and subunit mass (MS)', 'Glycan profiling (HILIC)', 'Cell-based potency', 'Host cell protein ELISA', 'Residual DNA (qPCR)', 'mRNA integrity (CE)', 'mRNA capping efficiency (LC-MS)', 'Poly(A) tail length', 'Residual dsRNA', 'LNP size and PDI (DLS)', 'Encapsulation efficiency (RiboGreen)', 'Vector genome titre (ddPCR)', 'AAV empty/full ratio (AUC)', 'Flow cytometry identity and purity', 'Sterility (membrane filtration)', 'Bacterial endotoxins (LAL)', 'Recombinant factor C', 'Mycoplasma (NAT)', 'Bioburden', 'Container closure integrity', 'TOC and conductivity (water)', 'Extractables (GC-MS, LC-MS)', 'Leachables (LC-MS)', 'LC-MS/MS PK assay', 'ADA bridging assay', 'Neutralising antibody assay']
METH = [dict(s=a, n=MNAMES[i], t=b, p=c, st=e, sa=f, tat=g, mo=h) for i, (a, b, c, e, f, g, h) in enumerate(M)]
assert [m["s"] for m in METH] == METHODS, "method list out of sync with ph.METHODS"

RULES = [  # market tags, product tags, title, meaning, service slug
 ("all", "all", "ICH Q1A(R2) and Q1B: stability and photostability", "Defines long-term, intermediate and accelerated conditions and light testing for registration batches.", "stability-studies"),
 ("all", "all", "ICH Q2(R2) and Q14: validation and analytical procedure development", "Lifecycle approach to methods; expect justification of range and robustness, not only a validation report.", "method-development-validation"),
 ("all", "small", "ICH Q3A/Q3B: impurities in drug substances and products", "Reporting, identification and qualification thresholds set by maximum daily dose.", "small-molecule-qc-release"),
 ("all", "small", "ICH Q3C(R8): residual solvents", "Class 1 solvents avoided; class 2 within PDE-based limits, tested by headspace GC.", "small-molecule-qc-release"),
 ("all", "all", "ICH Q3D(R2): elemental impurities", "Risk assessment of 24 elements by route; ICP-MS confirms where the assessment cannot rule them out.", "small-molecule-qc-release"),
 ("all", "small", "ICH M7(R2): mutagenic impurities", "Mutagenic impurities controlled to TTC-based limits; nitrosamines are a 'cohort of concern'.", "small-molecule-qc-release"),
 ("us", "small", "FDA guidance: Control of Nitrosamine Impurities in Human Drugs (Rev. 2) and NDSRI acceptable intake recommendations (2023)", "Risk assessment for every product; confirmatory testing with sensitive methods; AIs by the Carcinogenic Potency Categorization Approach.", "small-molecule-qc-release"),
 ("eu", "small", "EMA: nitrosamine Article 5(3) outcome and Q&A for MAHs", "Same three-step process (risk evaluation, confirmatory testing, changes) with EMA-published AIs.", "small-molecule-qc-release"),
 ("us", "all", "21 CFR Parts 210 and 211: cGMP for finished pharmaceuticals", "Laboratory controls (211.160 to 211.194): scientifically sound specifications, testing of every batch, records.", "regulatory-data-integrity-support"),
 ("us", "all", "21 CFR Part 11: electronic records and signatures", "Audit trails, unique logins and e-signatures on the systems that generate your results.", "regulatory-data-integrity-support"),
 ("eu", "all", "EU GMP Chapter 6 (Quality Control) and Annex 11 (computerised systems)", "Contract labs must be qualified by the MAH; data integrity expectations mirror Part 11.", "regulatory-data-integrity-support"),
 ("eu", "sterile", "EU GMP Annex 1 (2022, in force August 2023)", "A contamination control strategy that links environmental monitoring, water and sterility data.", "environmental-monitoring"),
 ("all", "sterile", "Sterility and endotoxins: USP <71>, <85>; Ph. Eur. 2.6.1, 2.6.14, 2.6.32", "Sterility per batch with validated method suitability; endotoxin limit = K/M; rFC accepted in Ph. Eur. 2.6.32.", "microbiology-sterility"),
 ("us", "bio", "21 CFR 600 and 610; FDA comparative analytical assessment guidance for biosimilars", "Lot release tests including 610.12 sterility; a tiered statistical comparison with the reference product.", "biologics-characterization-release"),
 ("eu", "bio", "EMA guideline on similar biological medicinal products: quality issues", "Comparability across multiple reference lots with orthogonal methods.", "biologics-characterization-release"),
 ("all", "bio", "ICH Q5C and Q6B: stability and specifications for biotechnological products", "Potency, purity, identity and quantity with justified acceptance criteria.", "biologics-characterization-release"),
 ("all", "bio", "ICH M10: bioanalytical method validation", "Harmonised validation for PK assays in plasma and serum.", "bioanalytical-immunogenicity"),
 ("all", "mrna", "WHO guidelines on mRNA vaccines (TRS 1039, Annex 3) and Ph. Eur. 5.36", "Identity, integrity, capping, poly(A), dsRNA, LNP size and encapsulation as critical quality attributes.", "mrna-vaccine-testing"),
 ("us", "cgt", "21 CFR 1271 and FDA CMC guidance for human gene therapy INDs (2020)", "Potency, vector titre, empty/full and replication-competent virus testing before release.", "cell-gene-therapy-testing"),
 ("eu", "cgt", "EudraLex Volume 4 Part IV: GMP for ATMPs", "Release testing for short shelf-life products, with rapid methods and parallel testing allowed when justified.", "cell-gene-therapy-testing"),
 ("in", "all", "Revised Schedule M (notified December 2023) and the Drugs and Cosmetics Rules, 1945", "Indian manufacturers, including MSMEs, need documented QC capability, in-house or through an approved lab.", "small-molecule-qc-release"),
 ("in", "all", "Indian Pharmacopoeia (IP 2022) monographs", "Products for India are tested against IP monographs, which can differ from USP or Ph. Eur.", "reference-standards-excipients"),
 ("in", "bio", "CDSCO Guidelines on Similar Biologics (2016)", "Stepwise comparability with a reference product; analytical data underpins reduced clinical programmes.", "biologics-characterization-release"),
 ("in", "all", "New Drugs and Clinical Trials Rules, 2019", "Quality data for clinical batches and import of trial material.", "method-development-validation"),
 ("apac", "all", "ASEAN stability guideline (Zone IVb: 30 °C / 75% RH)", "Long-term data at 30/75 for submissions across most ASEAN states.", "stability-studies"),
 ("apac", "all", "Japanese Pharmacopoeia (JP 18) and PMDA expectations", "JP monograph tests and Japanese-language documentation for PMDA submissions.", "reference-standards-excipients"),
 ("apac", "all", "PIC/S GMP Guide (Singapore HSA, Malaysia NPRA)", "PIC/S members follow EU-equivalent GMP, including Annex 1 and Annex 11.", "regulatory-data-integrity-support"),
 ("who", "all", "WHO TRS 1010 Annex 10: stability testing", "Zone IVb conditions for many WHO prequalification markets.", "stability-studies"),
 ("who", "all", "WHO GMP and prequalification (PQ)", "PQ dossiers need data from labs that meet WHO GMP; WHO may inspect contract labs.", "regulatory-data-integrity-support"),
 ("all", "all", "USP <1207>, <661>, <1663>, <1664>: packaging, extractables and leachables", "Container closure integrity and E&L assessment proportionate to route and risk.", "extractables-leachables"),
]

# ---------- tool UIs ----------
def ui_finder():
    mods = [(k, n) for k, n, _ in MODALITIES]
    stg = [("discovery", "Discovery"), ("preclinical", "Preclinical"), ("clinical", "Clinical (Phase 1 to 3)"), ("commercial", "Commercial"), ("post", "Post-approval")]
    mk = [("in", "India (CDSCO)"), ("eu", "Europe (EMA)"), ("us", "United States (FDA)"), ("apac", "Asia-Pacific (PMDA, HSA)"), ("global", "Several markets")]
    q = [("release", "Release a batch"), ("shelf", "Set or extend shelf life"), ("method", "Develop, validate or transfer a method"), ("similar", "Prove similarity or comparability"),
         ("impurity", "Investigate an impurity (e.g. nitrosamines)"), ("micro", "Sterility or microbiology"), ("pack", "Packaging, extractables and leachables"),
         ("clinical", "Clinical samples: PK or immunogenicity"), ("raw", "Raw materials and excipients"), ("inspect", "Prepare for an inspection")]
    steps = [RADIOS("mod", "1. What are you making?", mods), RADIOS("stg", "2. Development stage", stg, False), RADIOS("mk", "3. Main market", mk, False), RADIOS("q", "4. What is the question?", q, False)]
    s = "".join(f'<div class="tk-step{" on" if i == 0 else ""}" data-i="{i}">{x}</div>' for i, x in enumerate(steps))
    return (f'<div class="tk tk-wiz" data-tk="finder" data-cfg="{J(FINDER)}"><ol class="rq-p tk-prog"><li class="on">Product</li><li>Stage</li><li>Market</li><li>Question</li></ol>{s}'
            f'<div class="tk-nav"><button type="button" class="btn o tk-b" hidden>Back</button><button type="button" class="btn tk-n">Next</button></div>'
            f'<div class="tk-out" aria-live="polite" hidden></div></div>')

def ui_quote():
    rows = "".join(f'<tr><td>{n}</td><td class="mono-v">${lo:,} to ${hi:,}</td><td>{t} d</td><td><label class="vh" for="q{i}">Quantity for {n}</label><input id="q{i}" type="number" min="0" value="0" data-i="{i}" class="tk-qty"></td></tr>' for i, (n, lo, hi, t) in enumerate(CAT))
    return (f'<div class="tk tk-two" data-tk="quote" data-cfg="{J([[n, lo, hi, t] for n, lo, hi, t in CAT])}"><div><div class="tw"><table class="tk-cat"><thead><tr><th>Test</th><th>Per sample (USD)</th><th>Std TAT</th><th>Qty</th></tr></thead><tbody>{rows}</tbody></table></div></div>'
            f'<div class="tk-res"><div class="seg" role="radiogroup" aria-label="Tier">' + "".join(f'<label class="tk-seg"><input type="radio" name="qtier" value="{v}"{" checked" if i == 0 else ""}><span>{n}</span></label>' for i, (v, n) in enumerate([("std", "Standard"), ("pri", "Priority"), ("crit", "Critical")])) + '</div>'
            f'<span class="k">Indicative price band</span><b class="tk-big tk-qp">Add tests</b><span class="tk-qt"></span><ul class="tk-ql"></ul>'
            f'<p class="cn">{ILL("Illustrative prices")} Excludes shipping, method transfer and investigations. 10% volume discount applied to any line of 10 or more samples. Final quote confirmed by a scientist within hours.</p>{SEND("Send this to a scientist")}</div></div>')

def ui_tat():
    o = "".join(f'<option value="{i}">{s["n"]}</option>' for i, s in enumerate(DAYS_SVC))
    return (f'<div class="tk tk-two" data-tk="tat" data-cfg="{J(DAYS_SVC)}"><form class="tk-form" onsubmit="return false"><label><span>Ship date</span><input type="date" name="d"></label>'
            f'<label><span>Service</span><select name="s">{o}</select></label>'
            + SEL("tr", "Shipping lane", [("1", "Same country (1 business day)"), ("2", "Same region (2 business days)"), ("3", "Intercontinental (3 business days)")]) +
            f'<label class="chk"><input type="checkbox" name="hold"> <span>Samples need a test licence or permit check on arrival (add 2 business days)</span></label></form>'
            f'<div class="tk-res"><span class="k">Results by tier</span><div class="tw"><table><thead><tr><th>Tier</th><th>Lab days</th><th>Results by</th></tr></thead><tbody class="tk-tb"></tbody></table></div>'
            f'<p class="tk-note cn"></p>{SEND()}</div></div>')

def ui_stab():
    return (f'<div class="tk tk-two" data-tk="stab"><form class="tk-form" onsubmit="return false">'
            + SEL("zone", "Climatic zone of the target market", [("II", "Zone I/II: 25 °C / 60% RH (EU, US, Japan)"), ("III", "Zone III: 30 °C / 35% RH (hot, dry)"), ("IVa", "Zone IVa: 30 °C / 65% RH (hot, humid)"), ("IVb", "Zone IVb: 30 °C / 75% RH (India, ASEAN)")], "IVb")
            + SEL("store", "Labelled storage", [("rt", "Room temperature"), ("fridge", "Refrigerated, 2 to 8 °C"), ("frozen", "Frozen, −20 °C")])
            + SEL("pack", "Primary packaging", [("imp", "Impermeable: Alu-Alu blister, glass vial or ampoule"), ("semi", "Semi-permeable: HDPE bottle, PVC/PVDC blister, plastic bag or IV bag")])
            + SEL("dur", "Shelf life to support (months)", [(str(m), f"{m} months") for m in (12, 24, 36, 48, 60)], "36")
            + NUM("bat", "Batches", 3, 1, 6) + NUM("units", "Units per pull (per batch, per condition)", 20, 1, 500)
            + '<label class="chk"><input type="checkbox" name="inter" checked> <span>Plan intermediate 30 °C / 65% RH as a contingency (needed if accelerated shows significant change)</span></label>'
            + '<label class="chk"><input type="checkbox" name="photo" checked> <span>Include ICH Q1B photostability (one batch)</span></label></form>'
            f'<div class="tk-res"><span class="k">Your study</span><b class="tk-big tk-sn"></b><span class="tk-ss"></span><span class="tk-sc mono-v"></span>'
            f'<div class="tw"><table><thead><tr><th>Condition</th><th>Pull points (months)</th><th>Pulls</th></tr></thead><tbody class="tk-stb"></tbody></table></div>'
            f'<p class="tk-snote cn"></p><p class="cn">{ILL("Illustrative cost")} Based on full-specification testing at USD 900 to 1,600 per pull per batch and storage at USD 25 to 45 per condition, per batch, per month.</p>'
            f'<p><button type="button" class="btn o tk-dl">Download protocol draft (.txt)</button> <button type="button" class="btn o tk-csv">Pull schedule (.csv)</button></p>{SEND()}</div></div>')

NQ = [("api", "Drug substance", [("amine", "Does the API, an intermediate or a degradant contain a secondary, tertiary or quaternary amine?", 3),
                                  ("ndsri", "Could the API itself form a nitrosamine (an NDSRI), for example an accessible secondary amine?", 4)]),
      ("proc", "Process", [("nitrite", "Are nitrites, nitrous acid or other nitrosating agents used in any step, including azide quenching?", 4),
                            ("solv", "Are amide solvents (DMF, DMAc, NMP) or amine bases (e.g. triethylamine) used, especially with heat?", 3),
                            ("recov", "Are recovered solvents, reagents or catalysts used, or is the process at a third-party site?", 2),
                            ("water", "Is the API made or the product granulated with water that is not tested for nitrite?", 1)]),
      ("exc", "Formulation and excipients", [("excn", "Do excipients with known nitrite content (e.g. crospovidone, povidone, microcrystalline cellulose, starches) make up a large share?", 2),
                                             ("ph", "Is the micro-environment acidic, or does the product contain amine-containing excipients (e.g. meglumine)?", 2)]),
      ("pack", "Packaging and storage", [("lid", "Is the product in blisters with nitrocellulose-based lidding or printing inks?", 2),
                                          ("heat", "Will the product be stored or shipped hot and humid (Zone IVb)?", 1)])]

def ui_nitro():
    qs = ""
    for k, h, items in NQ:
        qs += f'<fieldset class="tk-fs"><legend>{h}</legend>' + "".join(
            f'<div class="tk-yn" data-w="{w}" data-k="{n}"><p>{t}</p><div class="picks">' + "".join(f'<label class="pick sm"><input type="radio" name="n-{n}" value="{v}"{" checked" if v == "0" else ""}><span>{lab}</span></label>' for v, lab in [("0", "No"), ("0.5", "Not sure"), ("1", "Yes")]) + '</div></div>' for n, t, w in items) + '</fieldset>'
    cat = SEL("cat", "Potency category (FDA CPCA) or known nitrosamine", [("26.5", "Category 1 or NDEA: 26.5 ng/day"), ("96", "NDMA: 96 ng/day"), ("100", "Category 2: 100 ng/day"), ("400", "Category 3: 400 ng/day"), ("1500", "Category 4 or 5: 1500 ng/day")], "26.5")
    return (f'<div class="tk tk-two" data-tk="nitro"><form class="tk-form" onsubmit="return false">{qs}</form><div class="tk-res"><span class="k">Risk indication</span><b class="tk-big tk-nr"></b><div class="tk-meter"><i></i></div>'
            f'<p class="tk-nx"></p><ol class="tk-np"></ol><hr><h3>Limit calculator</h3><form class="tk-form tk-lim" onsubmit="return false">{cat}{NUM("mdd", "Maximum daily dose of the API (mg/day)", 500, 0.001, None, "any")}</form>'
            f'<p class="tk-nl" aria-live="polite"></p><p class="cn">Indicative only, not regulatory advice. Follow the current FDA, EMA or CDSCO guidance for your product.</p>{SEND()}</div></div>')

def ui_endo():
    return (f'<div class="tk tk-two" data-tk="endo"><form class="tk-form" onsubmit="return false">'
            + SEL("route", "Route of administration", [("5", "Parenteral, any route except intrathecal (K = 5 EU/kg)"), ("0.2", "Intrathecal (K = 0.2 EU/kg)"), ("r175", "Radiopharmaceutical, not intrathecal (175/V)"), ("r14", "Radiopharmaceutical, intrathecal (14/V)")])
            + SEL("basis", "Dose is expressed", [("kg", "Per kg of body weight"), ("pt", "Per patient (flat dose)")])
            + NUM("dose", "Maximum dose given within one hour", 10, 0, None, "any")
            + SEL("unit", "Dose unit", [("mg", "mg"), ("mL", "mL"), ("U", "units (IU)")])
            + NUM("wt", "Patient body weight (kg); 70 kg adult default, use the real weight for paediatric products", 70, 0.5, 300, "any")
            + NUM("conc", "Product concentration (dose units per mL), for the maximum valid dilution", 50, 0, None, "any")
            + SEL("lam", "Test sensitivity λ (EU/mL)", [("0.125", "0.125: gel clot"), ("0.03", "0.03: gel clot, high sensitivity"), ("0.005", "0.005: kinetic chromogenic or rFC lowest standard")], "0.005")
            + f'</form><div class="tk-res"><span class="k">Endotoxin limit</span><b class="tk-big tk-el"></b><span class="tk-ef mono-v"></span><span class="k">Maximum valid dilution</span><b class="tk-mvd mono-v"></b><p class="tk-em"></p>'
            f'<p class="cn">Limit = K/M (USP &lt;85&gt;, Ph. Eur. 2.6.14). M is the maximum dose per kg given within one hour. For radiopharmaceuticals the limit is 175/V or 14/V EU per mL, where V is the maximum recommended dose in mL. MVD = (limit × concentration) / λ.</p>{SEND()}</div></div>')

IRS = [("di", "Data integrity", ["Every user has a unique login on every instrument and system; no shared accounts.", "Audit trails are switched on and reviewed before results are approved.",
                                 "Raw electronic data, not only printouts, is kept as the original record.", "Manual integration of chromatograms is controlled by an SOP and justified each time."]),
       ("doc", "Documentation", ["SOPs are current, approved and match what analysts actually do.", "Batch and test records are completed contemporaneously, with no blank fields or back-dating.",
                                  "Specifications and methods in use are the registered versions.", "Logbooks for instruments and rooms are complete for the last 12 months."]),
       ("trn", "Training", ["Every analyst has documented training on each method they run.", "Training on data integrity is refreshed at least yearly.", "Supervisors can show competency assessments, not only read-and-sign records."]),
       ("capa", "CAPA and change control", ["Previous inspection observations are closed with evidence of effectiveness.", "Deviations are investigated to root cause within your SOP timeline.", "Changes to methods, systems and equipment go through formal change control."]),
       ("eq", "Equipment and systems", ["Instruments are qualified (IQ/OQ/PQ) and within calibration.", "Computerised systems are validated, with periodic review.", "Reference standards are qualified, in date and properly stored."]),
       ("oos", "OOS and investigations", ["OOS results follow a two-phase investigation per FDA's OOS guidance.", "Retesting and resampling rules are defined before testing, not after.", "Trends (OOT) are monitored for stability and release data."])]

def ui_irs():
    i = 0; qs = ""
    for k, h, items in IRS:
        qs += f'<fieldset class="tk-fs"><legend>{h}</legend>'
        for t in items:
            qs += f'<div class="tk-yn" data-a="{k}"><p>{i + 1}. {t}</p><div class="picks">' + "".join(f'<label class="pick sm"><input type="radio" name="r{i}" value="{v}"{" checked" if v == "1" else ""}><span>{lab}</span></label>' for v, lab in [("0", "No"), ("1", "Partly"), ("2", "Yes")]) + '</div></div>'
            i += 1
        qs += '</fieldset>'
    assert i == 20
    gate = (f'<form class="mf tk-gate" data-mail="{MAIL}" data-kind="Inspection Readiness Score report" novalidate><h3>Get the full report</h3><p>A scientist sends a written report with your answers, the gaps that matter most to inspectors and a 90-day plan.</p>'
            f'<label><span>Work email</span><input name="email" type="email" required autocomplete="email"></label><label><span>Company</span><input name="company" autocomplete="organization"></label>'
            f'<input type="hidden" name="score" value=""><button class="btn" type="submit">Email me the report</button><p class="mf-ok" hidden>Your email app has opened with your scores filled in. Press send.</p></form>')
    return (f'<div class="tk tk-two" data-tk="irs" data-cfg="{J([[k, h] for k, h, _ in IRS])}"><form class="tk-form" onsubmit="return false">{qs}</form><div class="tk-res tk-sticky"><span class="k">Your readiness score</span>'
            f'<b class="tk-big tk-is"></b><span class="tk-il"></span><div class="tk-bars"></div><h3>Recommended actions</h3><ol class="tk-ia"></ol>{gate}</div></div>')

def ui_loc():
    cities = "".join(f"<option>{c}</option>" for c in CITIES)
    return (f'<div class="tk tk-two" data-tk="loc" data-cfg="{J(dict(LOC, customs=CUSTOMS, cold=COLD))}"><form class="tk-form" onsubmit="return false">'
            f'<label><span>Your city (where samples ship from)</span><input name="city" list="tk-cities" value="Ahmedabad" autocomplete="off"></label><datalist id="tk-cities">{cities}</datalist>'
            + SEL("cold", "Storage during transit", [(str(i), c[0]) for i, c in enumerate(COLD)], "1") +
            f'</form><div class="tk-res"><span class="k">Nearest planned labs</span><ol class="tk-ln"></ol><div class="tk-lc"></div><p class="cn">Planned sites. Transit days are typical express-courier estimates door to door; customs notes are general and are confirmed by our logistics team before you ship.</p>{SEND("Ask logistics to plan my shipment")}</div></div>')

def ui_meth():
    opts = "".join(f'<option value="{i}">{m["n"]}</option>' for i, m in enumerate(METH))
    return (f'<div class="tk" data-tk="meth" data-cfg="{J(METH)}"><div class="tk-mf"><label><span>Search methods</span><input type="search" class="tk-mq" placeholder="Try: endotoxin, glycan, ICH Q3D, mRNA"></label>'
            f'<label><span>Modality</span><select class="tk-mm"><option value="">All</option><option>Small molecule</option><option>Biologic</option><option>mRNA</option><option>CGT</option><option>All modalities</option></select></label></div>'
            f'<ul class="tk-ml" aria-live="polite"></ul><h3>Compare two methods</h3><div class="tk-mc"><label><span>Method A</span><select class="tk-ma">{opts}</select></label><label><span>Method B</span><select class="tk-mb">{opts}</select></label></div>'
            f'<div class="tw"><table class="tk-mt"><tbody></tbody></table></div></div>')

def ui_reg():
    return (f'<div class="tk" data-tk="reg" data-cfg="{J([dict(m=a, p=b, t=c, w=d_, s=SVC[e][1], u=svc_url(e)) for a, b, c, d_, e in RULES])}"><form class="tk-form tk-row" onsubmit="return false">'
            + SEL("p", "Product", [("small", "Small molecule (generic or new)"), ("sterile", "Sterile injectable (small molecule)"), ("bio", "Biologic or biosimilar"), ("mrna", "mRNA or vaccine"), ("cgt", "Cell or gene therapy")])
            + SEL("m", "Market", [("us", "United States (FDA)"), ("eu", "European Union (EMA)"), ("in", "India (CDSCO)"), ("apac", "Japan, Singapore, Malaysia and ASEAN"), ("who", "WHO prequalification markets")])
            + f'</form><p class="tk-rc mono-v" aria-live="polite"></p><ul class="tk-rl"></ul><p class="cn">Summaries of public guidance as of {ASOF}. Always read the current source document; this is not regulatory advice.</p>{SEND("Ask a regulatory scientist")}</div>')

def ui_cod():
    return (f'<div class="tk tk-two" data-tk="cod"><form class="tk-form" onsubmit="return false">'
            + NUM("val", "Value at risk per batch per day (USD): lost sales, idle capacity or launch delay", 25000, 0, None, 100)
            + NUM("n", "Batches waiting for release per year", 24, 1, 10000)
            + NUM("typ", "Typical testing turnaround today (days)", 18, 1, 365)
            + NUM("ours", "PharmaCRO target turnaround (days)", 7, 1, 365)
            + NUM("inv", "Inventory value per batch (USD), to include the cost of capital", 400000, 0, None, 1000)
            + NUM("rate", "Cost of capital (% a year)", 10, 0, 100, 0.5)
            + f'</form><div class="tk-res"><span class="k">Cost of each day of delay, per batch</span><b class="tk-big tk-cd"></b><span class="k">Annual saving from the shorter turnaround</span><b class="tk-big tk-cs"></b>'
            f'<div class="tk-cbars"></div><p class="tk-cx"></p><p class="cn">{ILL("Target TAT")} The 7-day figure is an illustrative target, not a measured result. Your own numbers stay in your browser.</p>{SEND("Build a business case with us")}</div></div>')

def ui_ask():
    return (f'<div class="tk tk-ask" data-tk="ask"><div class="tk-al" aria-live="polite"><p class="am bot">Ask whether we can test something. I answer only from pages on this site and always show the source.</p></div>'
            f'<div class="ask-q tk-aq">' + "".join(f'<button type="button">{q}</button>' for q in ["Can you test for nitrosamines?", "Zone IVb stability", "AAV empty full ratio", "Endotoxin limit for an IV product", "How do I ship frozen samples?"]) + '</div>'
            f'<form class="tk-af"><label class="vh" for="tk-ain">Your question</label><input id="tk-ain" placeholder="Can you test..." autocomplete="off"><button class="btn" type="submit">Ask</button></form></div>')

# ---------- pages ----------
SPEC = {
 "test-finder": dict(img="lab-goggles", cat="Find", ans="The Test Finder asks four questions (what you are making, its stage, your main market and what you need to know) and returns the services, key tests, typical turnaround and the nearest planned labs, with a quote button that carries your answers.",
   ui=ui_finder, how="It filters our twelve services by modality and stage, ranks them against your question, then picks labs in your market's region that offer each service. Nothing is sent until you press the quote button.",
   faq=[("Is the Test Finder a substitute for a scientist?", "No. It is a fast first pass. Every quote is reviewed by a scientist, who may add or remove tests."), ("Why does market matter?", "Pharmacopoeias and regulators differ: India uses IP monographs, the EU Ph. Eur., the US USP. The market also decides which lab is closest."), ("What if I am not sure what I am making?", "Choose 'Not sure yet'; the finder shows the services that apply to most products, and a scientist will narrow it down.")],
   svc=["small-molecule-qc-release", "biologics-characterization-release", "stability-studies"], rel=["quote-estimator", "turnaround-calculator", "ask-the-lab"]),
 "quote-estimator": dict(img="data-dashboard", cat="Estimate", ans="The Instant Quote Estimator gives an indicative price band and turnaround for the tests and quantities you choose, at Standard, Priority or Critical tier, in seconds. A scientist confirms the final price within hours.",
   ui=ui_quote, how="Each test has an illustrative per-sample price range. The tool multiplies by quantity, applies a 10% volume discount to lines of ten or more, then the tier multiplier (Priority ×1.5, Critical ×2.25). Turnaround is the longest test, shortened by tier.",
   faq=[("Why a range, not a price?", "Price depends on the method (compendial or yours), sample matrix, method transfer and reporting. The band shows where most quotes land."), ("Are method transfers included?", "No. Transfers of your own methods are quoted separately, usually as a fixed fee."), ("Do prices change by country?", "Quotes are issued in local currency by the lab that runs the work; the estimator uses USD for comparison.")],
   svc=["small-molecule-qc-release", "microbiology-sterility", "biologics-characterization-release"], rel=["turnaround-calculator", "test-finder", "cost-of-delay-calculator"]),
 "turnaround-calculator": dict(img="log-plane", cat="Plan", ans="The Turnaround Calculator shows the date your results arrive for each tier, counting business days from your ship date, the shipping lane and the typical lab time for the service.",
   ui=ui_tat, how="Receipt = ship date + transit business days (+2 if a permit check is needed). Lab time = the service's typical business days × 1.0 (Standard), 0.55 (Priority) or 0.3 (Critical), never less than one day. Weekends are skipped; public holidays are not included.",
   faq=[("Does the clock start when I ship?", "The lab clock starts when samples are received and accepted with complete paperwork."), ("What is the Critical tier for?", "Batches on hold, line stoppages and launch deadlines: results in 24 to 72 hours for most release tests."), ("What if you miss the date?", "The fee for that test is credited, subject to commercial approval at launch.")],
   svc=["small-molecule-qc-release", "microbiology-sterility", "stability-studies"], rel=["quote-estimator", "lab-locator-shipping-planner", "cost-of-delay-calculator"]),
 "stability-study-designer": dict(img="lab-corridor", cat="Plan", ans="The Stability Study Designer turns your market, storage, packaging and shelf life into an ICH Q1A(R2) study: conditions, pull points, total samples, chamber-months and a cost range, downloadable as a protocol draft.",
   ui=ui_stab, how="Long-term conditions follow the climatic zone (ICH Q1A(R2) and WHO TRS 1010). Accelerated is 40 °C/75% RH for room-temperature products and 25 °C/60% RH for refrigerated ones. Long-term pulls are 0, 3, 6, 9, 12, 18, 24 months, then yearly; accelerated 0, 3, 6. Samples = pulls × batches × units per pull, with time zero shared.",
   faq=[("Why three batches?", "ICH Q1A(R2) expects data on at least three primary batches for registration; one batch may be enough for early development."), ("When is intermediate needed?", "If accelerated testing shows significant change and long-term is 25 °C/60% RH. For Zone IVa and IVb long-term at 30 °C covers it."), ("What about semi-permeable packs?", "Water loss matters; ICH allows a low-humidity long-term condition for aqueous products and expects weight-loss monitoring."), ("Can I use the protocol draft as is?", "No. It is a starting point for your protocol, to be completed and approved by your QA.")],
   svc=["stability-studies", "method-development-validation", "small-molecule-qc-release"], rel=["turnaround-calculator", "regulatory-impact-checker", "quote-estimator"]),
 "nitrosamine-risk-assessor": dict(img="pharma-blisters", cat="Check", ans="The Nitrosamine Risk Assessor walks through the risk factors regulators ask about (amines, nitrosating agents, solvents, excipients and packaging) and returns a risk indication, a testing plan and the acceptable limit in ppm for your daily dose.",
   ui=ui_nitro, how="Each risk factor carries a weight; a 'Yes' to an API amine together with a nitrosating source is treated as high risk regardless of score. The limit is the acceptable intake (ng/day) divided by the maximum daily dose (mg/day), giving ppm (ng/mg). The target limit of quantitation is 30% of that limit or lower.",
   faq=[("What is the CPCA?", "FDA's Carcinogenic Potency Categorization Approach assigns NDSRIs to five categories with acceptable intakes of 26.5, 100, 400, 1500 and 1500 ng/day, based on structural features around the N-nitroso group."), ("Do I need to test if the risk is low?", "Document the assessment. Confirmatory testing is expected where a risk is identified; regulators can still ask for data."), ("Which method do you use?", "LC-MS/MS or LC-HRMS for NDSRIs and most small nitrosamines, GC-MS/MS for volatile ones, validated to an LOQ below the limit."), ("Is this regulatory advice?", "No. It is an indicative screen; the current FDA, EMA and CDSCO documents decide.")],
   svc=["small-molecule-qc-release", "method-development-validation", "extractables-leachables"], rel=["regulatory-impact-checker", "quote-estimator", "test-finder"]),
 "endotoxin-limit-calculator": dict(img="micro-petri-1", cat="Check", ans="The Endotoxin Limit Calculator gives the bacterial endotoxin limit for your product (K/M, USP <85> and Ph. Eur. 2.6.14), the maximum valid dilution for your test and a method suggestion.",
   ui=ui_endo, how="K is the threshold pyrogenic dose: 5 EU/kg for any parenteral route except intrathecal, 0.2 EU/kg intrathecal. M is the maximum dose per kg in one hour; for flat doses it is dose divided by body weight (70 kg adult unless you enter another). Radiopharmaceuticals use 175/V or 14/V.",
   faq=[("Why 70 kg?", "Pharmacopoeias use 70 kg for an average adult. For paediatric products use the lowest intended body weight, which gives a stricter limit."), ("LAL or recombinant factor C?", "Both are accepted in Ph. Eur. (2.6.14 and 2.6.32); in the US rFC needs validation as an alternative method under USP <86>/<1225>."), ("What is the MVD?", "The largest dilution at which the limit can still be detected; diluting overcomes product interference."), ("Does the calculator cover medical devices?", "No. Devices use USP <161> limits per device.")],
   svc=["microbiology-sterility", "environmental-monitoring", "biologics-characterization-release"], rel=["regulatory-impact-checker", "quote-estimator", "turnaround-calculator"]),
 "inspection-readiness-score": dict(img="docs-papers", cat="Check", ans="The Inspection Readiness Score is a 20-question self-assessment across data integrity, documentation, training, CAPA, equipment and OOS handling. You get an instant score with a breakdown and the actions inspectors would expect first.",
   ui=ui_irs, how="Each answer scores 0 (No), 1 (Partly) or 2 (Yes). Area scores are shown as a share of the maximum; the overall score is the average. Actions are drawn from the lowest-scoring areas, weighted towards data integrity because it drives the most serious observations.",
   faq=[("Is my data stored?", "No. Scores are calculated in your browser. Only if you ask for the report does your email app open with the scores."), ("What score is good?", "Above 85% suggests a mature system. Any 'No' on data integrity deserves action whatever the total."), ("Can you do a mock inspection?", "Yes. Our Regulatory and Data Integrity Support team runs mock FDA, EMA and CDSCO inspections.")],
   svc=["regulatory-data-integrity-support", "method-development-validation", "microbiology-sterility"], rel=["regulatory-impact-checker", "nitrosamine-risk-assessor", "ask-the-lab"]),
 "lab-locator-shipping-planner": dict(img="log-warehouse", cat="Find", ans="The Lab Locator and Shipping Planner finds the nearest planned PharmaCRO labs to your site, estimates transit time and shows courier options, customs notes for the destination country and cold-chain packing tips.",
   ui=ui_loc, how="Distance is great-circle distance from your city to each planned lab. Transit is estimated by lane: 1 to 2 business days within a country, 2 to 3 within a region and 3 to 5 intercontinental by express courier.",
   faq=[("Which couriers do you use?", "Specialist clinical and cold-chain couriers such as World Courier, Marken, Cryoport and DHL Medical Express are typical choices. These are examples, not partnerships."), ("Can you collect from our site?", "Yes. Collection can be booked with the quote, including validated shippers and loggers."), ("What paperwork travels with samples?", "A sample submission sheet, a commercial or pro-forma invoice, safety data where relevant and any permit or licence reference.")],
   svc=["stability-studies", "cell-gene-therapy-testing", "microbiology-sterility"], rel=["turnaround-calculator", "test-finder", "quote-estimator"]),
 "method-search-compare": dict(img="inst-hplc", cat="Find", ans="Method Search and Compare finds any method in our library by name, technique, standard or modality and puts two methods side by side: purpose, principle, standards, sample needed and typical turnaround.",
   ui=ui_meth, how="Search matches the method name, technique, purpose and standards. Each result links to the full Method Library entry with the principle, validation status and related methods.",
   faq=[("Can you run a method that is not listed?", "Very likely. The library is growing towards 500+ methods; send us your method and we will confirm."), ("Are these methods validated?", "Compendial methods are verified for your product; non-compendial methods are validated to ICH Q2(R2). Accreditation scope is per site."), ("Can I transfer my own method?", "Yes, through a formal method transfer protocol.")],
   svc=["method-development-validation", "small-molecule-qc-release", "biologics-characterization-release"], rel=["test-finder", "quote-estimator", "ask-the-lab"]),
 "regulatory-impact-checker": dict(img="docs-papers", cat="Check", ans="The Regulatory Impact Checker lists the guidance that shapes testing for your product type in your market, with one line on what each means for your lab work and the service that covers it.",
   ui=ui_reg, how="Each rule is tagged by market and product type; ICH guidelines apply to every ICH market. The list is a curated summary of public documents, reviewed by our regulatory team.",
   faq=[("Is the list complete?", "No. It covers the rules that most often change a testing plan. Your regulatory affairs team owns the full picture."), ("How often is it updated?", "With the Regulatory Radar, weekly once the network is live."), ("Does ICH apply in India?", "India is an ICH observer; CDSCO generally accepts ICH-aligned data, and the Indian Pharmacopoeia sets monograph tests.")],
   svc=["regulatory-data-integrity-support", "stability-studies", "small-molecule-qc-release"], rel=["nitrosamine-risk-assessor", "inspection-readiness-score", "stability-study-designer"]),
 "cost-of-delay-calculator": dict(img="biz-team-laptops", cat="Estimate", ans="The Cost of Delay Calculator shows what each day a batch waits for test results costs you, and what a shorter turnaround saves a year, as a business case procurement can use.",
   ui=ui_cod, how="Daily cost per batch = value at risk per day + inventory value × cost of capital ÷ 365. Annual saving = (typical days − our days) × daily cost × batches per year.",
   faq=[("What counts as value at risk?", "Lost or delayed sales, idle line capacity, expediting costs or penalties in supply contracts."), ("Is faster testing always worth more?", "Only for batches on the critical path. Many clients use Priority or Critical tiers for launches and Standard for routine work."), ("Are my numbers sent anywhere?", "No. They stay in your browser.")],
   svc=["small-molecule-qc-release", "stability-studies", "microbiology-sterility"], rel=["quote-estimator", "turnaround-calculator", "test-finder"]),
 "ask-the-lab": dict(img="lab-analyst-pc", cat="Find", ans="Ask the Lab answers questions such as 'can you test X' from the pages on this site, shows the source for every answer and hands a pre-filled quote request to a scientist. It never gives regulatory or medical advice.",
   ui=ui_ask, how="Your question is matched against an index of this site's pages (services, methods, tools and articles). The best matches are quoted with links; if nothing matches, it says so and offers a scientist. At launch, conversations will be reviewed weekly by a scientist to improve the pages.",
   faq=[("Is this a large language model?", "This preview uses search over our own pages, not a generative model, so it cannot invent answers."), ("Will a person see my question?", "Only if you choose 'send this to a scientist', which opens a quote request with your question."), ("What will it not answer?", "Regulatory conclusions, medical questions and pricing beyond published ranges.")],
   svc=["small-molecule-qc-release", "regulatory-data-integrity-support", "method-development-validation"], rel=["test-finder", "method-search-compare", "quote-estimator"]),
}
assert set(SPEC) == set(TN)
GUARD = TICKLIST(["Answers only from published pages on this site, and always cites them", "Never gives regulatory conclusions or medical advice", "Says 'I do not know' rather than guessing", "Hands off to a named scientist with a pre-filled quote request", "Questions are not stored by this preview"])

def related_tools(keys):
    return '<div class="tk-rt">' + "".join(f'<a class="tk-rc2 reveal" href="/tools/{k}.html"><img src="/img/{SPEC[k]["img"]}.jpg" alt="" loading="lazy"><span><small>{SPEC[k]["cat"]}</small><b>{TN[k]}</b></span></a>' for k in keys) + "</div>"

for slug, name in TOOLS:
    sp = SPEC[slug]
    extra = (SH("Guardrails", "What Ask the Lab will and will not do.") + GUARD) if slug == "ask-the-lab" else ""
    body = (ANSWER(sp["ans"]) + f'<section class="tk-wrap reveal" aria-label="{name}">{sp["ui"]()}</section>' + extra
            + SH("How it works", "Method and assumptions.") + SPLIT(sp["img"], f'<h3>How the {name} works</h3><p>{sp["how"]}</p>'
              + '<p class="cn">Everything runs in your browser. Nothing is sent unless you choose to send it to a scientist.</p>', flip=True)
            + SH("Questions", "Frequently asked.") + FAQS(sp["faq"], "tf") + RELATED(sp["svc"], "Services this tool feeds into:")
            + SH("More tools", "Keep planning.") + related_tools(sp["rel"]))
    page(f"tools/{slug}", name, sp["ans"].split(". ")[0] + ".", body, img=sp["img"], eyebrow=f"Tools &middot; {sp['cat']}",
         crumbs=[("Tools", "/tools/index.html")], chips=[("Free", "no sign-up"), ("Private", "runs in your browser"), (sp["cat"], "tool type")],
         jsonld=[{"@context": "https://schema.org", "@type": "WebApplication", "name": f"{BRAND} {name}", "applicationCategory": "BusinessApplication", "operatingSystem": "Any",
                  "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": re.sub("<[^>]+>", "", sp["ans"])}],
         cta=(f"Turn your {name.lower()} result into a quote.", "Press 'Send this to a scientist' on the tool, or tell us here. A scientist replies within 4 business hours."))

# ---------- hub ----------
cats = ["Plan", "Estimate", "Check", "Find"]
cards = "".join(f'<article class="tk-card reveal" data-cat="{SPEC[k]["cat"]}" style="--i:{i % 6}"><img src="/img/{SPEC[k]["img"]}.jpg" alt="" loading="lazy"><div><small>{SPEC[k]["cat"]}</small><h3>{n}</h3><p>{SPEC[k]["ans"].split(". ")[0]}.</p>'
                f'<p class="tk-cb"><a class="btn sm" href="/tools/{k}.html">Open tool</a> <button type="button" class="btn sm o tk-pv" data-k="{k}">Preview</button></p></div>'
                f'<template><img src="/img/{SPEC[k]["img"]}.jpg" alt="" loading="lazy"><p class="ey">{SPEC[k]["cat"]}</p><h2>{n}</h2><p>{SPEC[k]["ans"]}</p><h3>How it works</h3><p>{SPEC[k]["how"]}</p><p><a class="btn" href="/tools/{k}.html">Open the {n}</a></p></template></article>'
                for i, (k, n) in enumerate(TOOLS))
hub = (ANSWER("Twelve free tools for QC, procurement and regulatory teams: find the right test, estimate price and turnaround, design a stability study, screen nitrosamine risk, calculate endotoxin limits, score inspection readiness and build a business case. Every tool runs in your browser and ends with 'Send this to a scientist'.")
       + '<div class="sf tk-cf" role="group" aria-label="Filter tools"><span>Show</span><button type="button" class="ch" aria-pressed="true" data-c="">All</button>' + "".join(f'<button type="button" class="ch" aria-pressed="false" data-c="{c}">{c}</button>' for c in cats) + '</div>'
       + f'<div class="tk-cards">{cards}</div><dialog class="tk-dlg"><button class="cs-cl" type="button" aria-label="Close">&times;</button><div class="cs-b"></div></dialog>'
       + BAND("lab-team-three", "Tools that end with a person.", "Every result can be sent to a named scientist as a pre-filled quote request. You never have to retype what you just worked out.", BTN("Request a quote", "/request-quote.html"))
       + SH("Why we built them", "Answers in seconds, not email threads.")
       + ICARDS([("gauge", "Faster decisions", "Price bands, dates and study designs before you ask anyone."), ("lock", "Private by design", "Calculations run in your browser; nothing is stored."), ("doc", "Show your working", "Every tool states its method and assumptions, with sources."), ("people", "A scientist behind each", "Send any result to a scientist and get a reply within 4 business hours.")], 4)
       + GALLERY(["inst-hplc", "lab-plate-pink", "log-plane"], ["Method data behind the Method Search", "Assay plans behind the Quote Estimator", "Transit times behind the Shipping Planner"]))
page("tools/index", "Tools and calculators", "Plan, estimate and check your testing in seconds. Free, private, and every result can go straight to a scientist.", hub,
     img="data-dashboard", eyebrow="Resources", chips=[("12", "free tools"), ("0", "sign-ups needed"), ("4 h", "scientist reply time")],
     cta=("Got a result? Let us price it properly.", "Send it to a scientist and get a confirmed quote, usually within one business day."))
