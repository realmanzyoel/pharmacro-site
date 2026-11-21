"""Method Library (blueprint 4.10): a public, searchable catalogue. One index page + one page per slug in ph.METHODS.
Compendial references are to current general chapters as commonly cited; validation/accreditation status is a target placeholder."""
from ph import *
from urllib.parse import quote

FAM_IMG = {"Chromatography": "inst-hplc", "Mass spectrometry": "inst-lcms", "Spectroscopy": "lab-analyst-pc", "Physical and solid state": "lab-glassware",
           "Dissolution and performance": "inst-dissolution", "Microbiology": "micro-petri-1", "Molecular biology": "inst-pcr", "Immunoassay": "lab-plate-pink",
           "Cell-based": "bio-cells-green", "Stability": "lab-corridor"}
FAM_KEY = {"Chromatography": "chrom", "Mass spectrometry": "ms", "Spectroscopy": "spec", "Physical and solid state": "phys", "Dissolution and performance": "diss",
           "Microbiology": "micro", "Molecular biology": "mol", "Immunoassay": "imm", "Cell-based": "cell", "Stability": "stab"}
MODN = {"small": "Small molecule", "bio": "Biologics", "mrna": "mRNA and vaccines", "cgt": "Cell and gene therapy"}

MD = {}
def M(slug, name, fam, mods, stds, purpose, principle, sample, tat, instr, get, svcs, rel, when, pitfalls, img=None):
    MD[slug] = dict(slug=slug, name=name, fam=fam, mods=mods, stds=stds, purpose=purpose, principle=principle, sample=sample, tat=tat, instr=instr,
                    get=get, svcs=svcs, rel=rel, when=when, pitfalls=pitfalls, img=img or FAM_IMG[fam])

# ---------------- small molecule: chromatography, physical, spectroscopy ----------------
M("hplc-assay-related-substances", "HPLC assay and related substances", "Chromatography", ["small"],
  ["USP <621>", "Ph. Eur. 2.2.46", "JP 2.01", "ICH Q3A(R2)", "ICH Q3B(R2)", "ICH Q2(R2)"],
  "HPLC assay and related substances testing measures how much active ingredient a drug product contains and which impurities are present, against the limits in its specification or monograph.",
  "The sample is dissolved and injected onto a reversed-phase column. Components separate by how strongly they interact with the stationary phase and are detected by UV absorbance, usually with a diode-array detector that also checks peak purity. Assay is calculated against a reference standard; impurities are reported as area per cent or against a diluted standard with relative response factors.",
  "Typically 20 tablets or capsules, or 1 to 5 g of API", "3 to 7 business days", "HPLC with UV/PDA detection, chromatography data system with audit trail",
  ["Assay result with system suitability", "Impurity profile with reporting, identification and qualification thresholds applied", "Representative chromatograms", "E-signed CoA and raw data package"],
  ["small-molecule-qc-release", "method-development-validation"], ["uplc-impurity-profiling", "forced-degradation", "dissolution-testing"],
  ["Batch release of tablets, capsules, injectables and APIs", "Stability pulls", "Investigating an out-of-trend or out-of-specification result"],
  ["Unvalidated peak integration events: every manual integration needs a reason in the audit trail", "Relative response factors assumed to be 1.0 without data", "Diluent instability causing artefact peaks"])
M("uplc-impurity-profiling", "UHPLC impurity profiling", "Chromatography", ["small"],
  ["USP <621>", "Ph. Eur. 2.2.46", "ICH Q3A(R2)", "ICH Q3B(R2)", "ICH Q2(R2)"],
  "UHPLC impurity profiling separates and quantifies low-level impurities and degradation products with higher resolution and shorter run times than conventional HPLC.",
  "Columns packed with sub-2 µm particles run at high pressure give narrower peaks and better resolution of closely eluting impurities. Transfers from HPLC must stay inside the allowable adjustments of USP <621> and Ph. Eur. 2.2.46, or be revalidated.",
  "0.5 to 2 g of API or 10 dosage units", "3 to 7 business days", "UHPLC with PDA and optional QDa or single-quadrupole MS detection",
  ["Impurity table with RRTs and thresholds applied", "Peak purity or mass confirmation for unknowns above the identification threshold", "Chromatograms and CoA"],
  ["small-molecule-qc-release", "method-development-validation"], ["hplc-assay-related-substances", "forced-degradation", "genotoxic-impurities"],
  ["Complex impurity profiles that HPLC cannot resolve", "Faster release when sample volumes are high", "Method modernisation projects"],
  ["Transferring an HPLC method to UHPLC outside the allowable adjustments", "Extra-column volume effects on older systems", "Frictional heating changing selectivity"])
M("dissolution-testing", "Dissolution testing", "Dissolution and performance", ["small"],
  ["USP <711>", "USP <724>", "USP <1092>", "Ph. Eur. 2.9.3", "JP 6.10"],
  "Dissolution testing measures how quickly and completely the drug is released from a tablet or capsule into a defined medium, which is a release test and a surrogate for in vivo performance.",
  "Units are tested in apparatus 1 (basket), 2 (paddle), 3 (reciprocating cylinder) or 4 (flow-through cell) at 37.0 ± 0.5 °C in a specified medium. Samples are pulled at set times and analysed by UV or HPLC. Results are judged against the S1 to S3 stages for immediate release, or L1 to L3 for extended release.",
  "12 to 24 units per batch (6 per stage)", "2 to 5 business days", "Dissolution baths (apparatus 1 to 4) with mechanical qualification, autosamplers, UV-Vis and HPLC",
  ["Per-unit and mean release at each time point", "Profile plots and f2 similarity where requested", "Stage reached and conformance statement"],
  ["small-molecule-qc-release", "method-development-validation"], ["content-uniformity", "hplc-assay-related-substances", "particle-size-laser-diffraction"],
  ["Every batch release of an oral solid dose", "Comparative profiles for generic submissions and post-approval changes", "Stability"],
  ["Coning under the paddle giving low, variable results", "Dissolved air in the medium (deaeration matters)", "Vessel and shaft out of mechanical tolerance"])
M("content-uniformity", "Content uniformity", "Chromatography", ["small"],
  ["USP <905>", "Ph. Eur. 2.9.40", "JP 6.02"],
  "Content uniformity confirms that each individual dosage unit contains close to the labelled amount of drug, using the harmonised acceptance value approach.",
  "Ten units are assayed individually, usually by HPLC or UV. The acceptance value (AV) combines the mean deviation from target with the spread of results. If AV is above L1 (15.0), 20 more units are tested. Weight variation may be used instead when the drug content is high enough, as the chapter allows.",
  "30 dosage units", "2 to 5 business days", "HPLC or UV-Vis, calibrated analytical balances",
  ["Ten (or 30) individual results", "Acceptance value calculation", "Conformance statement against USP, Ph. Eur. and JP"],
  ["small-molecule-qc-release"], ["hplc-assay-related-substances", "dissolution-testing"],
  ["Low-dose tablets and capsules", "Blend and granulation problems", "Release and validation batches"],
  ["Incomplete extraction from the matrix inflating variability", "Applying weight variation where content uniformity is required", "Confusing sampling for blend uniformity with dosage-unit CU"])
M("residual-solvents-gc-hs", "Residual solvents by headspace GC", "Chromatography", ["small", "bio"],
  ["USP <467>", "Ph. Eur. 2.4.24", "ICH Q3C"],
  "Residual solvents testing measures organic solvents left over from manufacture against the Class 1, 2 and 3 limits in ICH Q3C.",
  "The sample is sealed in a vial and heated so volatile solvents partition into the headspace, which is injected onto a GC column and detected by FID. USP <467> uses a screening procedure and a confirmatory procedure on a different column; specific validated methods can replace them.",
  "1 to 2 g of API, excipient or product", "3 to 6 business days", "Headspace GC-FID, GC-MS for identification",
  ["Results per solvent against Option 1 or Option 2 limits", "Chromatograms", "CoA"],
  ["small-molecule-qc-release", "reference-standards-excipients"], ["elemental-impurities-icp-ms", "genotoxic-impurities"],
  ["API and excipient release", "Drug product release when a solvent is used late in the process", "Supplier qualification"],
  ["Matrix effects on headspace partitioning: use standard addition when recovery is poor", "Unexpected peaks from vial septa", "Benzene contamination from Class 2 sources"])
M("elemental-impurities-icp-ms", "Elemental impurities by ICP-MS", "Mass spectrometry", ["small", "bio"],
  ["USP <232>", "USP <233>", "ICH Q3D(R2)", "Ph. Eur. 2.4.20"],
  "Elemental impurities testing quantifies metals such as lead, arsenic, cadmium and mercury against the permitted daily exposures in ICH Q3D, using ICP-MS.",
  "Samples are digested in closed-vessel microwave systems with strong acids, then aerosolised into an argon plasma that ionises the elements. Ions are separated by mass, and a collision cell removes polyatomic interferences. Procedures are validated to USP <233> for accuracy, precision and specificity at the target limit.",
  "1 to 5 g of drug product or API", "4 to 8 business days", "ICP-MS with collision/reaction cell, closed-vessel microwave digestion",
  ["Results for the elements in your risk assessment, with J values", "Spike recoveries", "Data to support a Q3D risk assessment"],
  ["small-molecule-qc-release", "reference-standards-excipients"], ["residual-solvents-gc-hs", "extractables-gc-ms"],
  ["Supporting or confirming an ICH Q3D risk assessment", "Component and excipient screening", "Change of supplier or equipment"],
  ["Mercury loss and memory effects without gold stabilisation", "Osmium and other volatile elements lost in open digestion", "Testing every element when the risk assessment only needs a few"])
M("nitrosamines-lc-ms-ms", "Nitrosamines and NDSRIs by LC-MS/MS", "Mass spectrometry", ["small"],
  ["ICH M7(R2)", "Ph. Eur. 2.5.42", "USP <1469>", "FDA nitrosamine guidance", "EMA Article 5(3) Q&A"],
  "Nitrosamine testing detects and quantifies N-nitrosamines, including nitrosamine drug substance-related impurities (NDSRIs), at the low ng/g levels needed to meet regulator acceptable intakes.",
  "Samples are extracted and analysed by LC-MS/MS in multiple reaction monitoring mode, which detects a specific precursor-to-product ion transition for each nitrosamine. High-resolution MS is used for confirmation. Limits of quantitation are set from the acceptable intake and maximum daily dose, usually at or below 10% of the limit for screening.",
  "1 to 5 g of API or product per batch", "5 to 10 business days (Critical tier available)", "Triple quadrupole LC-MS/MS, LC-HRMS, GC-MS/MS for volatile nitrosamines",
  ["Results per nitrosamine against your AI-derived limit", "LOQ and recovery data", "Support for your risk assessment and confirmatory testing"],
  ["small-molecule-qc-release", "regulatory-data-integrity-support"], ["genotoxic-impurities", "hplc-assay-related-substances"],
  ["Confirmatory testing after a risk assessment finds a risk", "Products with secondary or tertiary amines and nitrite sources", "Change of API source or excipient supplier"],
  ["Artefactual nitrosamine formation during sample preparation: add a scavenger and test for it", "Using an outdated acceptable intake after a category change", "Insufficient sensitivity for high-dose products"])
M("genotoxic-impurities", "Mutagenic (genotoxic) impurities", "Mass spectrometry", ["small"],
  ["ICH M7(R2)", "ICH Q3A(R2)", "ICH Q2(R2)"],
  "Mutagenic impurity testing measures DNA-reactive impurities such as alkyl sulfonates, alkyl halides and epoxides at trace levels set by the ICH M7 threshold of toxicological concern.",
  "Methods are built around the impurity: GC-MS for volatile alkylating agents, LC-MS/MS for polar compounds, often with derivatisation to improve sensitivity. Limits come from the 1.5 µg/day lifetime TTC or less-than-lifetime limits, divided by maximum daily dose.",
  "1 to 5 g of API", "2 to 4 weeks including method development", "GC-MS, GC-MS/MS, LC-MS/MS",
  ["Validated trace method", "Results against the M7-derived limit", "Option 1 to 4 control strategy support"],
  ["small-molecule-qc-release", "method-development-validation"], ["nitrosamines-lc-ms-ms", "uplc-impurity-profiling"],
  ["New synthetic routes with alkylating reagents", "Demonstrating purge for an M7 control option", "Regulatory questions on a specific impurity"],
  ["Analyte instability during sample preparation", "Matrix suppression in LC-MS", "Limits copied from another product with a different daily dose"])
M("xrpd-polymorph", "XRPD polymorph identification", "Physical and solid state", ["small"],
  ["USP <941>", "Ph. Eur. 2.9.33"],
  "X-ray powder diffraction identifies the crystalline form of an API or excipient and detects unwanted polymorphs, which can change solubility, stability and bioavailability.",
  "A powder sample is irradiated with X-rays and the diffracted intensity is recorded against the angle 2θ. Each crystal form gives a characteristic pattern of peak positions, so the pattern acts as a fingerprint. Limits of detection for a minor form are typically around 1 to 5% w/w, depending on the forms and the matrix.",
  "200 mg to 1 g of powder", "3 to 5 business days", "Powder X-ray diffractometer with variable-temperature stage",
  ["Diffraction pattern overlaid on reference forms", "Form identification statement", "Optional quantitation of a minor form"],
  ["small-molecule-qc-release", "reference-standards-excipients"], ["particle-size-laser-diffraction", "raman-identification"],
  ["API release where the form is specified", "Stability of metastable forms", "Generic development and patent questions"],
  ["Preferred orientation distorting peak intensities", "Excipient peaks masking the API in drug product", "Grinding inducing a form change"])
M("particle-size-laser-diffraction", "Particle size by laser diffraction", "Physical and solid state", ["small"],
  ["USP <429>", "Ph. Eur. 2.9.31", "ISO 13320"],
  "Laser diffraction measures the particle size distribution of APIs and excipients, reported as Dv10, Dv50 and Dv90, which affects dissolution, content uniformity and processability.",
  "Particles dispersed in air or liquid scatter a laser beam at angles that depend on their size. The scattering pattern is converted to a volume-based size distribution using Mie or Fraunhofer theory. Dispersion conditions are critical and are set during method development.",
  "1 to 5 g of powder", "2 to 4 business days", "Laser diffraction analyser with wet and dry dispersion units",
  ["Dv10, Dv50, Dv90 and distribution plot", "Method parameters including refractive index used", "CoA"],
  ["small-molecule-qc-release", "method-development-validation"], ["xrpd-polymorph", "dissolution-testing"],
  ["Micronised API release", "Dissolution investigations", "Supplier changes"],
  ["Under- or over-dispersion changing the result", "Wrong refractive index for Mie calculations", "Comparing wet and dry results as if equivalent"])
M("water-content-karl-fischer", "Water content by Karl Fischer", "Physical and solid state", ["small", "bio"],
  ["USP <921>", "Ph. Eur. 2.5.12", "Ph. Eur. 2.5.32", "JP 2.48"],
  "Karl Fischer titration measures water content in APIs, excipients and drug products, a common specification for stability and handling.",
  "Water reacts with iodine and sulfur dioxide in a base and alcohol. Volumetric titration suits higher water levels; coulometric titration generates iodine electrically and suits trace water. An oven can drive water from samples that react with or do not dissolve in the reagent.",
  "0.5 to 2 g", "1 to 3 business days", "Volumetric and coulometric Karl Fischer titrators with oven sample processors",
  ["Water content (% w/w)", "Replicates and standard recovery", "CoA"],
  ["small-molecule-qc-release", "reference-standards-excipients", "stability-studies"], ["ich-stability-storage", "ftir-identification"],
  ["Release and stability of hygroscopic products", "Lyophilised products", "Excipient testing"],
  ["Ambient humidity uptake during weighing", "Side reactions with ketones and aldehydes", "Incomplete release of bound water without an oven"])
M("ftir-identification", "FTIR identification", "Spectroscopy", ["small", "bio"],
  ["USP <197>", "USP <854>", "Ph. Eur. 2.2.24", "JP 2.25"],
  "FTIR identification confirms that a raw material, API or excipient is what it claims to be by matching its infrared spectrum to a reference.",
  "Infrared light is absorbed at frequencies that correspond to molecular bond vibrations, giving a fingerprint spectrum. Samples are measured by attenuated total reflectance (ATR) or as KBr discs, and compared with a reference standard spectrum or library.",
  "100 mg to 1 g", "1 to 2 business days", "FTIR spectrometer with ATR and KBr accessories, validated spectral libraries",
  ["Overlay against reference", "Match statement", "CoA"],
  ["reference-standards-excipients", "small-molecule-qc-release"], ["raman-identification", "xrpd-polymorph"],
  ["Incoming raw material identity", "API identity on release", "Counterfeit and adulteration screening"],
  ["Polymorphs giving different spectra in the solid state", "Moisture bands in KBr discs", "Library match scores used without visual review"])
M("raman-identification", "Raman identification", "Spectroscopy", ["small"],
  ["USP <858>", "USP <1858>", "Ph. Eur. 2.2.48"],
  "Raman spectroscopy confirms material identity quickly, often through transparent packaging, which makes it useful for 100% incoming raw material checks.",
  "A laser excites the sample and a small fraction of light is scattered at shifted wavelengths that correspond to molecular vibrations. The spectrum is matched to a validated library. Handheld instruments allow testing in the warehouse through bags or glass.",
  "As received, in transparent packaging, or 100 mg", "1 to 2 business days", "Benchtop and handheld Raman spectrometers",
  ["Pass/fail identity with match score", "Spectrum overlay", "Report"],
  ["reference-standards-excipients"], ["ftir-identification", "xrpd-polymorph"],
  ["Testing every container of incoming material", "Fast identity on high-volume excipients", "Supply chain integrity checks"],
  ["Fluorescence swamping the signal", "Coloured or opaque packaging", "Libraries built on one supplier's material"])

# ---------------- stability ----------------
M("ich-stability-storage", "ICH stability storage and testing", "Stability", ["small", "bio", "mrna", "cgt"],
  ["ICH Q1A(R2)", "ICH Q1E", "ICH Q5C", "WHO TRS 1010 Annex 10"],
  "ICH stability studies store product at defined temperature and humidity conditions and test it at set intervals to support a shelf life and storage statement.",
  "Batches are placed in qualified chambers at long-term, intermediate and accelerated conditions chosen for the target climatic zones, for example 25 °C/60% RH for zones I and II and 30 °C/75% RH for zone IVb. Samples are pulled at 0, 3, 6, 9, 12, 18, 24 and 36 months and tested against the specification. Shelf life is estimated by regression under ICH Q1E. A consolidated revision of the ICH Q1 guidelines is in progress.",
  "Per protocol, from the pull schedule (often 30 to 200 units per condition)", "Pull to report in 5 to 10 business days", "Qualified walk-in and reach-in chambers with continuous monitoring and alarms, all analytical techniques",
  ["Stability protocol and pull schedule", "Data tables and trend plots per attribute", "Shelf-life regression and report"],
  ["stability-studies"], ["photostability-q1b", "forced-degradation", "hplc-assay-related-substances"],
  ["New product registration", "Post-approval changes", "Ongoing annual stability commitments"],
  ["Excursions without documented impact assessment", "Choosing zone II conditions for products sold in zone IVb markets", "Pull points missed during holidays"])
M("photostability-q1b", "Photostability (ICH Q1B)", "Stability", ["small", "bio"],
  ["ICH Q1B"],
  "Photostability testing shows whether light exposure changes a drug substance or product, and whether light-protective packaging is needed.",
  "Samples are exposed to not less than 1.2 million lux hours of visible light and not less than 200 watt hours per square metre of near-UV energy, using option 1 or option 2 light sources, with dark controls wrapped in foil. Exposed and control samples are then tested for appearance, assay and degradation products.",
  "Enough for exposed, dark control and packaged arms (often 20 to 60 units)", "2 to 3 weeks", "Calibrated photostability chamber with lux and UV radiometers",
  ["Exposure records", "Comparative results for exposed, dark control and packaged samples", "Conclusion on light sensitivity"],
  ["stability-studies"], ["ich-stability-storage", "forced-degradation"],
  ["Registration stability packages", "Packaging selection", "Clear or translucent containers"],
  ["Temperature rise in the chamber confounding results", "Dark control not exposed to the same temperature", "Sample layer too thick for uniform exposure"])
M("forced-degradation", "Forced degradation studies", "Stability", ["small", "bio"],
  ["ICH Q1A(R2)", "ICH Q1B", "ICH Q2(R2)", "ICH Q14"],
  "Forced degradation deliberately stresses a drug with acid, base, oxidation, heat, humidity and light to reveal its degradation pathways and prove a method is stability-indicating.",
  "Stress conditions are tuned to give roughly 5 to 20% degradation, enough to form relevant degradants without secondary breakdown. Stressed samples are analysed by HPLC with PDA and MS to show the main peak is resolved and pure, and to identify major degradants.",
  "1 to 5 g of API or product", "2 to 4 weeks", "Stability ovens, photostability chamber, HPLC-PDA, LC-MS",
  ["Degradation pathway summary", "Peak purity and mass balance", "Evidence that the method is stability-indicating"],
  ["method-development-validation", "stability-studies"], ["hplc-assay-related-substances", "uplc-impurity-profiling", "photostability-q1b"],
  ["Before method validation", "New formulations", "Explaining a new peak on stability"],
  ["Over-stressing so that degradants are not relevant", "Poor mass balance left unexplained", "Skipping the drug product and stressing API only"])

# ---------------- biologics ----------------
M("sec-hplc-aggregates", "SEC-HPLC for aggregates and fragments", "Chromatography", ["bio", "mrna"],
  ["USP <129>", "Ph. Eur. 2.2.30", "ICH Q6B"],
  "Size-exclusion chromatography measures monomer purity, aggregates and fragments of monoclonal antibodies and other proteins, a critical quality attribute for safety and efficacy.",
  "Proteins pass through a porous column where larger molecules elute first because they are excluded from the pores. UV detection at 280 nm quantifies high-molecular-weight species, monomer and low-molecular-weight species. Multi-angle light scattering can be added to confirm molecular weight.",
  "100 to 500 µg of protein", "3 to 5 business days", "Bio-inert UHPLC with SEC columns, UV and optional MALS detection",
  ["% HMW, % monomer and % LMW", "Chromatograms with system suitability", "Comparability overlays on request"],
  ["biologics-characterization-release"], ["ce-sds", "icief-charge-variants", "intact-mass-ms"],
  ["mAb release and stability", "Biosimilar comparability", "Formulation screening"],
  ["Secondary interactions with the column causing tailing", "Shear or dilution changing aggregate levels", "Not confirming SEC against an orthogonal method"])
M("ce-sds", "CE-SDS purity (reduced and non-reduced)", "Chromatography", ["bio"],
  ["USP <129>", "Ph. Eur. 2.2.47", "ICH Q6B"],
  "CE-SDS measures the size purity of proteins under reducing and non-reducing conditions, detecting fragments, non-glycosylated heavy chain and incompletely assembled antibody.",
  "Proteins are denatured with SDS, which gives them a uniform charge-to-mass ratio, and separated by size in a gel-filled capillary. Under reducing conditions heavy and light chains are resolved; under non-reducing conditions the intact antibody and its fragments are measured.",
  "50 to 200 µg of protein", "3 to 5 business days", "Capillary electrophoresis systems with UV or LIF detection",
  ["% purity, % fragments and non-glycosylated heavy chain", "Electropherograms", "CoA"],
  ["biologics-characterization-release"], ["sec-hplc-aggregates", "icief-charge-variants"],
  ["mAb release and stability", "Process changes", "Biosimilar comparability"],
  ["Sample preparation artefacts from incomplete alkylation", "Thermal fragmentation during heating", "Capillary conditioning drift"])
M("icief-charge-variants", "icIEF charge variants", "Chromatography", ["bio"],
  ["Ph. Eur. 2.2.54", "USP <1054>", "ICH Q6B"],
  "Imaged capillary isoelectric focusing separates charge variants of a protein by isoelectric point, measuring the acidic, main and basic species that reflect deamidation, C-terminal lysine and other modifications.",
  "The protein is mixed with carrier ampholytes that form a pH gradient in a capillary under voltage. Each variant migrates to its isoelectric point and the whole capillary is imaged, so results are fast and quantitative. Cation-exchange chromatography is an orthogonal option.",
  "50 to 200 µg of protein", "3 to 5 business days", "Imaged cIEF systems, CEX-HPLC",
  ["% acidic, main and basic species with pI", "Electropherograms", "Comparability overlays"],
  ["biologics-characterization-release"], ["ce-sds", "peptide-mapping-lc-ms", "sec-hplc-aggregates"],
  ["Release and stability of mAbs", "Biosimilar similarity", "Process and formulation changes"],
  ["Ampholyte lot differences shifting profiles", "Protein precipitation at the pI", "Comparing profiles run on different platforms"])
M("peptide-mapping-lc-ms", "Peptide mapping by LC-MS", "Mass spectrometry", ["bio"],
  ["USP <1055>", "Ph. Eur. 2.2.55", "ICH Q6B"],
  "Peptide mapping confirms a protein's amino acid sequence and locates post-translational modifications such as oxidation, deamidation and glycosylation sites.",
  "The protein is reduced, alkylated and digested, usually with trypsin, into peptides that are separated by reversed-phase LC and identified by high-resolution MS/MS. Sequence coverage and modification levels are reported, and UV maps serve as an identity test on release.",
  "100 to 500 µg of protein", "1 to 2 weeks", "UHPLC coupled to high-resolution mass spectrometry",
  ["Sequence coverage map", "Modification sites and relative levels", "Identity comparison to reference"],
  ["biologics-characterization-release"], ["intact-mass-ms", "glycan-profiling-hilic", "icief-charge-variants"],
  ["Identity testing", "Characterisation for filings", "Biosimilar similarity and comparability"],
  ["Artificial deamidation during digestion", "Missed cleavages reducing coverage", "Disulfide scrambling if alkylation is incomplete"])
M("intact-mass-ms", "Intact and subunit mass analysis", "Mass spectrometry", ["bio"],
  ["ICH Q6B", "Ph. Eur. 2.2.43"],
  "Intact and subunit mass analysis measures the molecular mass of a protein or its chains to confirm identity and reveal major modifications such as glycoforms and clipping.",
  "The intact protein, or subunits produced by reduction or IdeS digestion, is desalted and analysed by high-resolution MS. The charge-state envelope is deconvoluted to give accurate masses, which are compared with the theoretical sequence.",
  "20 to 100 µg of protein", "3 to 7 business days", "LC coupled to high-resolution QTOF or Orbitrap mass spectrometry",
  ["Deconvoluted masses with mass error", "Glycoform distribution", "Identity statement"],
  ["biologics-characterization-release"], ["peptide-mapping-lc-ms", "glycan-profiling-hilic"],
  ["Identity confirmation", "Characterisation", "Biosimilar similarity"],
  ["Adducts broadening peaks", "Over-interpreting deconvolution artefacts", "Heterogeneous glycosylation complicating spectra"])
M("glycan-profiling-hilic", "Released N-glycan profiling (HILIC)", "Chromatography", ["bio"],
  ["USP <212>", "Ph. Eur. 2.2.59", "ICH Q6B"],
  "Glycan profiling measures the N-linked sugar structures on a glycoprotein, which influence effector function, half-life and immunogenicity.",
  "N-glycans are released with PNGase F, labelled with a fluorescent tag and separated by hydrophilic interaction chromatography with fluorescence detection; MS confirms structures. Key outputs include afucosylation, galactosylation, high-mannose and sialylation.",
  "100 to 300 µg of protein", "1 to 2 weeks", "UHPLC-FLD with HILIC columns, LC-MS",
  ["Relative glycan distribution", "Key glycan attribute summaries", "Comparability overlays"],
  ["biologics-characterization-release"], ["intact-mass-ms", "cell-based-potency", "peptide-mapping-lc-ms"],
  ["Biosimilar similarity", "Cell line and process changes", "Characterisation"],
  ["Incomplete release under denaturing conditions", "Label-dependent response differences", "Sialic acid loss during sample preparation"])
M("cell-based-potency", "Cell-based potency bioassay", "Cell-based", ["bio", "cgt", "mrna"],
  ["USP <1032>", "USP <1033>", "USP <1034>", "Ph. Eur. 5.3", "ICH Q6B"],
  "A cell-based potency assay measures the biological activity of a product relative to a reference standard, using a cellular response that reflects its mechanism of action.",
  "Cells are exposed to serial dilutions of test and reference samples, and a response such as proliferation, reporter gene expression or cell killing is measured. Relative potency is calculated from parallel dose-response curves, usually four-parameter logistic, after testing for parallelism.",
  "0.5 to 2 mg of product (assay dependent)", "2 to 4 weeks", "Validated cell banks, plate readers, statistical analysis software",
  ["Relative potency with confidence interval", "Parallelism and system suitability results", "Assay report"],
  ["biologics-characterization-release", "cell-gene-therapy-testing"], ["hcp-elisa", "nab-cell-based-assay", "glycan-profiling-hilic"],
  ["Release and stability", "Biosimilar functional similarity", "Comparability after process change"],
  ["Cell passage drift changing response", "Plate position effects", "Variability that hides real potency changes"])
M("hcp-elisa", "Host cell protein ELISA", "Immunoassay", ["bio", "cgt"],
  ["USP <1132>", "Ph. Eur. 2.6.34", "ICH Q6B"],
  "Host cell protein testing measures residual proteins from the production cell line, an impurity that must be reduced to low levels for safety.",
  "A sandwich ELISA uses polyclonal antibodies raised against host cell proteins to capture and detect them. Antibody coverage of the HCP population should be shown, typically by 2D gel and Western blot or by MS; LC-MS can identify individual high-risk proteins.",
  "0.5 to 1 mL of in-process or drug substance sample", "3 to 7 business days", "Plate readers, automated washers, LC-MS for HCP identification",
  ["HCP concentration (ng/mg)", "Dilution linearity and spike recovery", "Report"],
  ["biologics-characterization-release", "cell-gene-therapy-testing"], ["residual-dna-qpcr", "sec-hplc-aggregates"],
  ["Drug substance release", "Purification process development", "Process changes"],
  ["Poor antibody coverage of some HCPs", "Dilution non-linearity", "Using a generic kit without checking coverage for your cell line"])
M("residual-dna-qpcr", "Residual host cell DNA by qPCR", "Molecular biology", ["bio", "mrna", "cgt"],
  ["USP <509>", "Ph. Eur. 2.6.35", "WHO TRS 978 Annex 3"],
  "Residual DNA testing quantifies host cell DNA left in a biological product, commonly against the WHO limit of 10 ng per parenteral dose for continuous cell lines.",
  "DNA is extracted from the sample and a host-specific repetitive sequence is amplified by quantitative PCR. Fluorescence rises with each cycle and the threshold cycle is compared with a standard curve of host DNA. Extraction recovery is checked with a spike.",
  "0.5 to 1 mL", "3 to 7 business days", "Real-time PCR systems, automated nucleic acid extraction",
  ["Residual DNA per dose or per mg", "Spike recovery", "Report"],
  ["biologics-characterization-release", "mrna-vaccine-testing", "cell-gene-therapy-testing"], ["hcp-elisa", "ddpcr-vector-titre"],
  ["Drug substance release", "Viral vaccine and vector products", "DNA template clearance for mRNA"],
  ["Low extraction recovery in protein-rich matrices", "Fragment size not considered in risk assessment", "Contamination from lab DNA"])

# ---------------- mRNA and LNP ----------------
_MRNA = ["USP mRNA vaccine quality guidance", "WHO mRNA vaccine guidelines", "ICH Q6B (principles)"]
M("mrna-integrity-ce", "mRNA integrity by capillary electrophoresis", "Molecular biology", ["mrna"], _MRNA,
  "mRNA integrity testing measures the percentage of full-length mRNA versus fragments, which is a critical quality attribute because only intact transcripts produce the full protein.",
  "RNA is denatured and separated by size in a gel-filled capillary, with fluorescent detection. The main peak is full-length mRNA; shorter species reflect truncated transcription or degradation. For LNP products, the RNA is released from the particles with detergent first.",
  "5 to 20 µg of RNA", "3 to 5 business days", "Capillary electrophoresis and fragment analyser systems",
  ["% intact mRNA", "Size profile", "Trend data on stability"],
  ["mrna-vaccine-testing"], ["mrna-capping-lc-ms", "poly-a-tail-length", "encapsulation-efficiency-ribogreen"],
  ["Drug substance and drug product release", "Stability and in-use studies", "Process development"],
  ["Incomplete denaturation showing secondary structure peaks", "RNase contamination during handling", "Incomplete release from LNPs"])
M("mrna-capping-lc-ms", "mRNA 5' capping efficiency by LC-MS", "Mass spectrometry", ["mrna"], _MRNA,
  "Capping efficiency testing measures what fraction of mRNA molecules carry the 5' cap structure needed for translation and to avoid innate immune recognition.",
  "A probe-directed RNase H cleavage releases a short 5' fragment from each molecule. The fragments are separated by ion-pair reversed-phase LC and identified by mass, distinguishing Cap 1, Cap 0 and uncapped species such as 5' triphosphate.",
  "10 to 50 µg of RNA", "5 to 8 business days", "Bio-inert UHPLC with high-resolution MS",
  ["% capped with cap structure breakdown", "Mass spectra of 5' fragments", "Report"],
  ["mrna-vaccine-testing"], ["mrna-integrity-ce", "poly-a-tail-length", "dsrna-elisa"],
  ["Drug substance release", "Capping chemistry optimisation", "Comparability"],
  ["Incomplete RNase H cleavage", "Adducts complicating spectra", "Probe design that does not suit the 5' UTR"])
M("poly-a-tail-length", "Poly(A) tail length and distribution", "Mass spectrometry", ["mrna"], _MRNA,
  "Poly(A) tail analysis measures the length and heterogeneity of the 3' poly(A) tail, which affects mRNA stability and translation.",
  "The tail is released by RNase T1 or RNase H digestion and separated by ion-pair reversed-phase LC with UV or MS detection, giving a length distribution. Alternative approaches include capillary electrophoresis of the released tail.",
  "10 to 50 µg of RNA", "5 to 8 business days", "UHPLC with UV and high-resolution MS",
  ["Mean tail length and distribution", "% tailed molecules", "Report"],
  ["mrna-vaccine-testing"], ["mrna-capping-lc-ms", "mrna-integrity-ce"],
  ["Release of plasmid-templated and enzymatically tailed mRNA", "Template plasmid stability", "Process changes"],
  ["Plasmid recombination shortening encoded tails", "Incomplete digestion", "Comparing results between UV and MS methods without bridging"])
M("dsrna-elisa", "Residual dsRNA", "Immunoassay", ["mrna"], _MRNA,
  "Residual double-stranded RNA testing measures dsRNA by-products of in vitro transcription, which can trigger innate immune responses and reduce protein expression.",
  "A dsRNA-specific monoclonal antibody (such as J2) captures dsRNA in a sandwich ELISA or dot-blot format, quantified against a dsRNA standard. Methods must show they do not cross-react with single-stranded mRNA at the test concentration.",
  "10 to 50 µg of RNA", "3 to 6 business days", "Plate readers, immunoblot imaging systems",
  ["dsRNA content (ng/µg mRNA)", "Standard curve and controls", "Report"],
  ["mrna-vaccine-testing"], ["mrna-integrity-ce", "mrna-capping-lc-ms"],
  ["Drug substance release", "Purification development", "Comparability"],
  ["Size-dependent antibody binding", "Standard that does not resemble the product's dsRNA", "Matrix interference from LNP lipids"])
M("lnp-size-pdi-dls", "LNP size and polydispersity (DLS)", "Physical and solid state", ["mrna"], ["ISO 22412"] + _MRNA[:1],
  "Dynamic light scattering measures the mean size and polydispersity index of lipid nanoparticles, which influence delivery, biodistribution and stability.",
  "Particles in suspension move by Brownian motion, causing fluctuations in scattered laser light. The fluctuation rate gives a diffusion coefficient and, through the Stokes-Einstein equation, a hydrodynamic diameter. PDI describes the width of the distribution; nanoparticle tracking or multi-detector methods add resolution.",
  "50 to 200 µL of drug product", "2 to 4 business days", "DLS instruments, nanoparticle tracking analysis, SEC-MALS",
  ["Z-average diameter and PDI", "Size distribution plot", "Trend on stability and freeze-thaw"],
  ["mrna-vaccine-testing"], ["encapsulation-efficiency-ribogreen", "mrna-integrity-ce"],
  ["LNP drug product release", "Freeze-thaw and shipping studies", "Formulation development"],
  ["Dust and aggregates dominating intensity-weighted results", "Wrong dispersant viscosity", "Over-reliance on Z-average for multimodal samples"])
M("encapsulation-efficiency-ribogreen", "Encapsulation efficiency (RiboGreen)", "Immunoassay", ["mrna"], _MRNA,
  "Encapsulation efficiency measures what percentage of the mRNA in a product is protected inside the lipid nanoparticle rather than free in solution.",
  "A fluorescent RNA-binding dye such as RiboGreen is added with and without a detergent like Triton X-100. Without detergent the dye only sees free RNA; with detergent it sees total RNA. Encapsulation efficiency is the difference expressed as a percentage of total.",
  "50 to 200 µL of drug product", "2 to 4 business days", "Fluorescence plate readers",
  ["% encapsulation and total RNA content", "Standard curves", "Report"],
  ["mrna-vaccine-testing"], ["lnp-size-pdi-dls", "mrna-integrity-ce"],
  ["LNP release and stability", "Process development", "Freeze-thaw studies"],
  ["Detergent affecting dye fluorescence", "Incomplete particle disruption", "Lipid interference at high concentration"])

# ---------------- cell and gene therapy ----------------
M("ddpcr-vector-titre", "Vector genome titre by ddPCR", "Molecular biology", ["cgt"],
  ["USP <1047>", "Ph. Eur. 5.14"],
  "Droplet digital PCR measures the number of vector genomes in an AAV or lentiviral product, which sets the dose given to patients.",
  "The sample is treated with DNase to remove unpackaged DNA, then capsids are lysed and the DNA is partitioned into thousands of droplets for PCR. Counting positive droplets gives an absolute copy number without a standard curve, which reduces variability compared with qPCR.",
  "50 to 200 µL", "3 to 7 business days", "Droplet digital PCR systems",
  ["Vector genomes per mL with confidence interval", "Controls and DNase efficiency", "Report"],
  ["cell-gene-therapy-testing"], ["aav-empty-full-auc", "residual-dna-qpcr", "flow-cytometry-identity"],
  ["AAV and LV release", "Dose determination for clinical batches", "Stability"],
  ["Incomplete DNase digestion overestimating titre", "Target region secondary structure lowering efficiency", "Dilution errors at high titre"])
M("aav-empty-full-auc", "AAV empty/full ratio by AUC", "Physical and solid state", ["cgt"],
  ["USP <1047>", "Ph. Eur. 5.14"],
  "Analytical ultracentrifugation measures the proportion of AAV capsids that are empty, partially filled or full, an important purity and potency attribute.",
  "In sedimentation velocity AUC, capsids are spun at high speed and their sedimentation is tracked optically. Full capsids, which carry the genome, sediment faster than empty ones. Mass photometry and charge-detection MS are faster orthogonal methods.",
  "300 to 500 µL at 1E12 to 1E13 capsids per mL", "1 to 2 weeks", "Analytical ultracentrifuge, mass photometer",
  ["% empty, partial and full capsids", "Sedimentation coefficient distributions", "Report"],
  ["cell-gene-therapy-testing"], ["ddpcr-vector-titre", "sec-hplc-aggregates"],
  ["AAV release and characterisation", "Purification development", "Comparability"],
  ["Low concentration samples", "Partial capsids misclassified", "Long run times limiting throughput"])
M("flow-cytometry-identity", "Flow cytometry identity and purity", "Cell-based", ["cgt"],
  ["USP <1027>", "Ph. Eur. 2.7.24"],
  "Flow cytometry confirms the identity, purity and viability of cell therapy products such as CAR-T by measuring surface markers on individual cells.",
  "Cells are stained with fluorescent antibodies against markers such as CD3, CD4, CD8 and the CAR construct, then passed one by one through lasers. Each cell's fluorescence is measured, so populations can be counted and gated. Viability dyes exclude dead cells.",
  "1 to 2 mL or about 10^6 cells", "1 to 2 business days (same day available)", "Multi-colour flow cytometers with validated panels",
  ["% viable cells, % CD3+, % CAR+ and subsets", "Gating strategy and plots", "Report"],
  ["cell-gene-therapy-testing"], ["cell-based-potency", "sterility-membrane-filtration", "mycoplasma-nat"],
  ["Autologous and allogeneic release", "In-process monitoring", "Stability of cryopreserved product"],
  ["Gating inconsistency between analysts", "Sample age before analysis", "Compensation errors in large panels"])

# ---------------- microbiology ----------------
M("sterility-membrane-filtration", "Sterility test (membrane filtration)", "Microbiology", ["small", "bio", "mrna", "cgt"],
  ["USP <71>", "Ph. Eur. 2.6.1", "JP 4.06"],
  "The sterility test checks that a sterile product contains no viable micro-organisms, using the harmonised compendial method.",
  "The product is filtered through a 0.45 µm membrane, which is rinsed to remove antimicrobial activity and then incubated in fluid thioglycollate medium and soybean-casein digest medium for at least 14 days. Direct inoculation is used when filtration is not possible. Method suitability shows the product does not inhibit growth.",
  "Per compendial tables, typically 20 containers", "14 days incubation plus 1 to 2 days to report", "Closed membrane filtration systems in isolators or Grade A clean air",
  ["Sterility result", "Method suitability report", "Environmental and negative controls"],
  ["microbiology-sterility"], ["bacterial-endotoxins-lal", "bioburden", "container-closure-integrity"],
  ["Release of every sterile batch", "Media fill and process simulation support", "Investigation of failures"],
  ["False positives from testing environment", "Inadequate rinsing of antimicrobial products", "Too few containers tested"])
M("bacterial-endotoxins-lal", "Bacterial endotoxins (LAL)", "Microbiology", ["small", "bio", "mrna", "cgt"],
  ["USP <85>", "Ph. Eur. 2.6.14", "JP 4.01"],
  "The bacterial endotoxins test detects and quantifies endotoxin from Gram-negative bacteria, which can cause fever and shock if injected.",
  "Limulus amoebocyte lysate reacts with endotoxin. Gel-clot, kinetic turbidimetric and kinetic chromogenic methods are used; the kinetic methods give a quantitative result against a standard curve. The endotoxin limit is calculated as K divided by M, and the maximum valid dilution is set from it.",
  "3 to 5 containers or 1 to 5 mL", "1 to 3 business days", "Kinetic plate readers, gel-clot heating blocks",
  ["Endotoxin result (EU/mL or EU/mg)", "Positive product controls and inhibition/enhancement data", "CoA"],
  ["microbiology-sterility"], ["recombinant-factor-c", "sterility-membrane-filtration"],
  ["Parenteral product release", "Water for injection monitoring", "Raw material testing"],
  ["Low endotoxin recovery in some protein and surfactant matrices", "Beta-glucan interference", "Wrong maximum valid dilution"])
M("recombinant-factor-c", "Endotoxin by recombinant reagents (rFC)", "Microbiology", ["small", "bio", "mrna", "cgt"],
  ["Ph. Eur. 2.6.32", "USP <86>"],
  "Recombinant factor C testing detects endotoxin with a reagent made without horseshoe crab blood, and is not affected by beta-glucans.",
  "Recombinant factor C is activated by endotoxin and cleaves a fluorogenic substrate; fluorescence is measured against a standard curve. Ph. Eur. 2.6.32 allows its use, and USP <86> describes recombinant reagents. Switching from LAL requires a comparability assessment.",
  "3 to 5 containers or 1 to 5 mL", "1 to 3 business days", "Fluorescence plate readers",
  ["Endotoxin result", "Positive product controls", "LAL comparability data on request"],
  ["microbiology-sterility"], ["bacterial-endotoxins-lal", "sterility-membrane-filtration"],
  ["Sustainability goals", "Products with beta-glucan interference", "New products starting on rFC"],
  ["Regulatory acceptance varies by market and product", "Comparability not demonstrated before switching", "Different sensitivity to some matrices"])
M("mycoplasma-nat", "Mycoplasma by culture and NAT", "Molecular biology", ["bio", "cgt", "mrna"],
  ["Ph. Eur. 2.6.7", "USP <63>", "JP 18 G3"],
  "Mycoplasma testing detects contamination of cell banks, harvests and cell therapy products by mycoplasmas, which are too small to be removed by standard filters.",
  "The compendial culture method incubates samples in broth and on agar for 28 days, with an indicator cell culture method for non-cultivable species. Nucleic acid amplification techniques (NAT) give results in about a day and can replace culture when validated to show equivalent detection.",
  "10 mL of unfiltered harvest or 1 to 2 mL for NAT", "NAT 1 to 2 days, culture 28 days", "Real-time PCR, culture incubators, indicator cell lines",
  ["Detected/not detected", "Controls and detection limit evidence", "Report"],
  ["microbiology-sterility", "cell-gene-therapy-testing"], ["sterility-membrane-filtration", "flow-cytometry-identity"],
  ["Cell bank and harvest release", "Autologous cell therapy release on short shelf life", "Raw material testing"],
  ["Sampling filtered material", "NAT validation not covering required species", "Inhibitors in the sample matrix"])
M("bioburden", "Bioburden and microbial limits", "Microbiology", ["small", "bio"],
  ["USP <61>", "USP <62>", "Ph. Eur. 2.6.12", "Ph. Eur. 2.6.13", "JP 4.05"],
  "Bioburden testing counts the micro-organisms in non-sterile products and pre-filtration samples and checks for specified organisms such as E. coli.",
  "Total aerobic microbial count and total yeast and mould count are measured by plate count, membrane filtration or MPN. Tests for specified micro-organisms use selective enrichment. Method suitability confirms the product does not suppress recovery.",
  "10 to 30 g or mL", "5 to 8 business days", "Biosafety cabinets, incubators, membrane filtration",
  ["TAMC, TYMC (CFU/g or mL)", "Absence or presence of specified organisms", "Suitability report"],
  ["microbiology-sterility"], ["sterility-membrane-filtration", "toc-conductivity-water"],
  ["Oral and topical product release", "Pre-filtration bioburden for sterile manufacture", "Raw materials"],
  ["Antimicrobial products suppressing recovery", "Sample hold times too long", "Choosing wrong acceptance criteria for the dosage form"])
M("container-closure-integrity", "Container closure integrity", "Physical and solid state", ["small", "bio", "mrna", "cgt"],
  ["USP <1207>", "USP <1207.1>", "USP <1207.2>", "USP <1207.3>", "EU GMP Annex 1"],
  "Container closure integrity testing shows that a vial, syringe or other package keeps out micro-organisms and gases throughout shelf life.",
  "Deterministic methods such as helium leak, vacuum decay, high-voltage leak detection and laser headspace analysis are preferred to probabilistic dye ingress or microbial challenge tests. Methods are validated with positive controls of known leak size.",
  "30 to 100 units plus positive controls", "1 to 3 weeks", "Helium leak detector, vacuum decay, HVLD, laser headspace analyser",
  ["Pass/fail per unit with leak size sensitivity", "Method validation summary", "Report"],
  ["microbiology-sterility", "extractables-leachables"], ["sterility-membrane-filtration", "leachables-lc-ms"],
  ["Packaging qualification", "Stability in place of sterility testing", "Cold-chain and freezing studies"],
  ["Using dye ingress where a deterministic method would work", "Positive controls not representative of real defects", "Low temperature effects on stoppers ignored"])
M("toc-conductivity-water", "Water testing: TOC and conductivity", "Spectroscopy", ["small", "bio", "mrna", "cgt"],
  ["USP <643>", "USP <645>", "Ph. Eur. 2.2.44", "Ph. Eur. 2.2.38"],
  "Total organic carbon and conductivity testing check that purified water and water for injection meet compendial quality, as part of environmental and utility monitoring.",
  "TOC analysers oxidise organic carbon to carbon dioxide and measure it, with system suitability using sucrose and 1,4-benzoquinone. Conductivity is measured in up to three stages with temperature compensation, as described in USP <645>.",
  "250 to 500 mL per point in clean containers", "1 to 3 business days", "TOC analysers, conductivity meters",
  ["TOC (ppb C) and conductivity results", "System suitability", "Trend reports"],
  ["environmental-monitoring"], ["bacterial-endotoxins-lal", "bioburden"],
  ["Routine water system monitoring", "Water system qualification", "Excursion investigation"],
  ["Contaminated sample containers", "Long transit times changing TOC", "Ignoring trends that stay inside limits"])

# ---------------- E&L ----------------
M("extractables-gc-ms", "Extractables study (GC-MS, LC-MS, ICP-MS)", "Mass spectrometry", ["small", "bio", "mrna"],
  ["USP <1663>", "USP <661.1>", "USP <661.2>", "ISO 10993-18"],
  "An extractables study identifies the chemicals that can be pulled from packaging or manufacturing components under exaggerated conditions, to predict what may leach into a product.",
  "Components are extracted with solvents of different polarity at elevated temperature. Extracts are screened by headspace GC-MS for volatiles, GC-MS for semi-volatiles, LC-MS for non-volatiles and ICP-MS for elements. Compounds above the analytical evaluation threshold are identified and assessed by toxicologists.",
  "Components or packaging units as agreed in the protocol", "4 to 8 weeks", "HS-GC-MS, GC-MS, LC-HRMS, ICP-MS",
  ["Extractables profile with identification confidence", "AET calculation", "Report to support toxicological assessment"],
  ["extractables-leachables"], ["leachables-lc-ms", "elemental-impurities-icp-ms"],
  ["New container closure systems", "Single-use manufacturing components", "Change of packaging supplier"],
  ["AET set without considering dose", "Low identification confidence for unknowns", "Extraction conditions that do not reflect the product"])
M("leachables-lc-ms", "Leachables on stability", "Mass spectrometry", ["small", "bio", "mrna"],
  ["USP <1664>", "ICH Q3E (draft)"],
  "A leachables study measures which compounds actually migrate from packaging into a drug product during storage, using targeted methods built from the extractables data.",
  "Target leachables chosen from the extractables study are quantified in drug product stability samples by sensitive, validated methods, typically LC-MS/MS and GC-MS. Results are compared with safety thresholds. ICH Q3E on extractables and leachables was released as a draft for consultation.",
  "Stability samples per protocol", "Method set-up 4 to 6 weeks, then per pull", "LC-MS/MS, GC-MS, ICP-MS",
  ["Validated leachables methods", "Results per time point", "Final report for the dossier"],
  ["extractables-leachables", "stability-studies"], ["extractables-gc-ms", "container-closure-integrity"],
  ["Registration of injectables and inhalation products", "Biologics in prefilled syringes", "Packaging changes"],
  ["Targets not linked to the extractables study", "Product matrix suppression", "Not covering the end of shelf life"])

# ---------------- bioanalytical ----------------
M("lc-ms-ms-pk-assay", "LC-MS/MS pharmacokinetic assay", "Mass spectrometry", ["small", "bio"],
  ["ICH M10"],
  "An LC-MS/MS PK assay measures drug or metabolite concentrations in plasma, serum or tissue, so that exposure can be related to dose in clinical and nonclinical studies.",
  "Analytes are extracted by protein precipitation, liquid-liquid or solid-phase extraction, separated by LC and detected by tandem MS in MRM mode with a stable isotope internal standard. Validation and sample analysis follow ICH M10, including incurred sample reanalysis.",
  "50 to 250 µL of plasma per sample", "Validation 3 to 6 weeks; sample analysis per batch in 1 to 2 weeks", "Triple quadrupole LC-MS/MS, automated extraction",
  ["Validation report", "Concentration data with QC performance", "ISR results"],
  ["bioanalytical-immunogenicity"], ["ada-bridging-assay", "nab-cell-based-assay"],
  ["Bioequivalence studies", "Phase 1 to 3 PK", "Toxicokinetics"],
  ["Matrix effects and phospholipid suppression", "Analyte instability in whole blood", "Carry-over at high concentrations"])
M("ada-bridging-assay", "Anti-drug antibody (ADA) bridging assay", "Immunoassay", ["bio", "mrna", "cgt"],
  ["FDA immunogenicity testing guidance (2019)", "EMA immunogenicity guideline", "USP <1106>"],
  "An ADA assay detects antibodies a patient makes against a biologic drug, using a tiered approach of screening, confirmation and titre.",
  "In a bridging format, the drug is labelled twice (for example biotin and a detection label); ADA in the sample bridges the two. Samples above a statistically set cut point are confirmed by drug competition, then titred. Drug tolerance and sensitivity are established during validation.",
  "100 to 200 µL of serum per sample", "Validation 4 to 8 weeks; samples per batch 1 to 2 weeks", "Electrochemiluminescence and ELISA platforms",
  ["Screen, confirmatory and titre results", "Cut point and validation reports", "Data for immunogenicity reporting"],
  ["bioanalytical-immunogenicity"], ["nab-cell-based-assay", "lc-ms-ms-pk-assay"],
  ["Clinical trials of biologics", "Biosimilar comparative immunogenicity", "Post-marketing studies"],
  ["Drug interference masking ADA", "Cut points from unrepresentative populations", "Target interference causing false positives"])
M("nab-cell-based-assay", "Neutralising antibody (NAb) assay", "Cell-based", ["bio", "cgt"],
  ["FDA immunogenicity testing guidance (2019)", "USP <1106.1>"],
  "A neutralising antibody assay shows whether ADA detected in a patient block the drug's biological activity.",
  "Confirmed ADA-positive samples are tested in a cell-based or competitive ligand-binding assay that reflects the drug's mechanism. If antibodies neutralise, the drug's response is reduced. Cut points, sensitivity and drug tolerance are established in validation.",
  "100 to 200 µL of serum per sample", "Validation 6 to 10 weeks; samples per batch 2 weeks", "Cell culture, luminescence and reporter assays",
  ["Neutralising positive or negative", "Validation report", "Data for clinical reporting"],
  ["bioanalytical-immunogenicity"], ["ada-bridging-assay", "cell-based-potency"],
  ["Clinical immunogenicity assessment", "Biosimilar comparisons", "Gene therapy pre-existing immunity screening"],
  ["Serum matrix effects on cells", "Low drug tolerance", "Format that does not reflect mechanism of action"])

assert sorted(MD) == sorted(METHODS), set(MD) ^ set(METHODS)
for _s, _m in MD.items():
    assert all(r in MD for r in _m["rel"]), _s
    assert all(v in SVC for v in _m["svcs"]), _s
    assert _m["img"] in ALT, _s

# ---------------- principle diagrams (animated SVG, one per technique family) ----------------
def DIAG(fam):
    k = FAM_KEY[fam]
    if k == "chrom":
        g = ('<rect x="40" y="20" width="44" height="200" rx="8" class="ml-col"/>'
             + "".join(f'<rect x="48" y="30" width="28" height="12" rx="4" class="ml-band" style="--c:{c};--d:{i * .7}s"/>' for i, c in enumerate(["#00B8A9", "#F2A900", "#7fe7dc"]))
             + '<path class="ml-base" d="M120 210H460"/><path class="ml-tr" pathLength="1" d="M120 210h60c10 0 12-4 16-30l6-60c3-16 7-16 10 0l6 60c4 26 6 30 16 30h50c8 0 10-2 13-14l5-26c2-8 5-8 7 0l5 26c3 12 5 14 13 14h40c10 0 12-6 16-50l7-100c3-18 7-18 10 0l7 100c4 44 6 50 16 50h40"/>'
             + '<text x="190" y="235">t (min)</text><text x="40" y="240">column</text>')
    elif k == "ms":
        g = ('<path d="M30 120l60-20v40z" class="ml-col"/>' + "".join(f'<circle cx="100" cy="120" r="3" class="ml-ion" style="--d:{i * .25}s;--y:{(i % 5 - 2) * 10}px"/>' for i in range(10))
             + '<rect x="150" y="96" width="120" height="48" rx="10" class="ml-col"/><text x="168" y="125">mass filter</text><path class="ml-base" d="M300 210H470"/>'
             + "".join(f'<rect x="{310 + i * 26}" y="{210 - h}" width="10" height="{h}" class="ml-bar" style="--d:{i * .15 + 1}s"/>' for i, h in enumerate([30, 90, 40, 150, 60, 20])) + '<text x="360" y="235">m/z</text>')
    elif k == "spec":
        g = ('<path class="ml-beam" d="M20 60H200"/><rect x="200" y="40" width="40" height="40" rx="6" class="ml-col"/><path class="ml-base" d="M40 210H470"/>'
             '<path class="ml-tr" pathLength="1" d="M40 200c30 0 30-20 50-20s20 20 40 20 20-110 30-110 10 110 30 110 40-60 55-60 15 60 35 60 20-140 35-140 15 140 35 140 30-30 45-30 20 30 40 30 30-80 45-80 15 80 30 80"/>'
             '<text x="200" y="235">wavenumber (cm⁻¹)</text>')
    elif k == "phys":
        g = ("".join(f'<circle cx="{60 + (i * 37) % 160}" cy="{60 + (i * 53) % 150}" r="{4 + i % 4 * 3}" class="ml-p" style="--d:{i * .2}s"/>' for i in range(14))
             + '<path class="ml-base" d="M250 210H470"/>' + "".join(f'<rect x="{262 + i * 20}" y="{210 - h}" width="4" height="{h}" class="ml-bar" style="--d:{i * .12 + .4}s"/>' for i, h in enumerate([20, 60, 150, 35, 90, 25, 120, 40, 70, 18]))
             + '<text x="300" y="235">2θ or size</text>')
    elif k == "diss":
        g = ('<path d="M50 40v150a40 40 0 0 0 40 40h60a40 40 0 0 0 40-40V40" class="ml-col"/><rect x="52" y="90" width="136" height="138" rx="30" class="ml-med"/>'
             '<g class="ml-pad"><path d="M120 20v170" class="ml-shaft"/><path d="M90 190h60" class="ml-shaft"/></g><rect x="110" y="200" width="22" height="12" rx="6" class="ml-tab"/>'
             '<path class="ml-base" d="M250 210H470M250 210V40"/><path class="ml-tr" pathLength="1" d="M250 210C280 120 320 70 380 56S450 50 470 50"/><text x="330" y="235">% released vs time</text>')
    elif k == "micro":
        g = ('<ellipse cx="150" cy="130" rx="110" ry="90" class="ml-col"/>' + "".join(f'<circle cx="{80 + (i * 41) % 140}" cy="{80 + (i * 29) % 100}" r="{5 + i % 3 * 3}" class="ml-col2" style="--d:{i * .3}s"/>' for i in range(12))
             + '<rect x="300" y="60" width="150" height="140" rx="12" class="ml-col"/><text x="318" y="90">14 days</text><text x="318" y="120">FTM 30–35 °C</text><text x="318" y="150">SCDM 20–25 °C</text><text x="318" y="180">no growth = pass</text>')
    elif k == "mol":
        g = ('<path class="ml-base" d="M40 210H470M40 210V30"/><path d="M40 120H470" class="ml-thr"/>'
             + "".join(f'<path class="ml-tr" pathLength="1" style="--d:{i * .4}s" d="M40 205C{120 + i * 50} 205 {160 + i * 50} 205 {200 + i * 50} 120S{260 + i * 50} 45 470 42"/>' for i in range(3))
             + '<text x="400" y="114">threshold</text><text x="200" y="235">cycle number</text>')
    elif k == "imm":
        g = "".join(f'<circle cx="{60 + c * 34}" cy="{40 + r * 30}" r="11" class="ml-well" style="--d:{(r + c) * .12}s;--o:{.25 + ((r * 3 + c) % 7) / 9:.2f}"/>' for r in range(6) for c in range(12))
        g += '<text x="60" y="235">96-well plate: signal rises with concentration</text>'
    elif k == "cell":
        g = ("".join(f'<circle cx="{50 + (i * 47) % 170}" cy="{50 + (i * 31) % 150}" r="16" class="ml-cell" style="--d:{i * .25}s"/>' for i in range(10))
             + '<path class="ml-base" d="M260 210H470M260 210V30"/><path class="ml-tr" pathLength="1" d="M260 200C320 200 330 200 360 120S410 45 470 42"/><path class="ml-tr" pathLength="1" style="--d:.5s;stroke:var(--amb)" d="M260 200C330 200 350 200 380 120S430 45 470 44"/><text x="300" y="235">log dose</text>')
    else:  # stability
        g = ("".join(f'<rect x="{40 + i * 110}" y="50" width="90" height="140" rx="10" class="ml-col"/><text x="{52 + i * 110}" y="80">{t}</text><text x="{52 + i * 110}" y="100">{h}</text>'
                     f'<rect x="{52 + i * 110}" y="120" width="66" height="10" rx="5" class="ml-fill" style="--d:{i * .4}s"/>' for i, (t, h) in enumerate([("25 °C", "60% RH"), ("30 °C", "75% RH"), ("40 °C", "75% RH"), ("5 °C", "ambient")]))
             + '<text x="40" y="225">pulls at 0, 3, 6, 9, 12, 18, 24, 36 months</text>')
    return f'<figure class="ml-d reveal" aria-hidden="true"><svg viewBox="0 0 500 250">{g}</svg></figure>'

# ---------------- index ----------------
def _svcidx(slug): return [s[0] for s in SERVICES].index(slug)
def _quote(m): return f'/request-quote.html?service={_svcidx(m["svcs"][0])}&amp;q={quote(m["name"])}'
def _std_family(s):
    for k in ("USP", "Ph. Eur.", "JP", "ICH", "ISO", "WHO", "FDA", "EMA", "EU GMP"):
        if s.startswith(k): return k
    return "Other"

_data = [dict(s=m["slug"], n=m["name"], f=m["fam"], m=m["mods"], st=m["stds"], sf=sorted({_std_family(x) for x in m["stds"]}), p=m["purpose"], t=m["tat"], sv=_svcidx(m["svcs"][0])) for m in MD.values()]
_fams = sorted({m["fam"] for m in MD.values()})
_stdf = ["USP", "Ph. Eur.", "JP", "ICH", "ISO", "WHO", "FDA", "EMA"]
_cards = "".join(f'<a class="ml-c" href="/method-library/{m["slug"]}.html" data-s="{m["slug"]}"><small>{m["fam"]}</small><b>{m["name"]}</b><span>{m["purpose"]}</span><em>{" &middot; ".join(m["stds"][:3])}</em><i>{m["tat"]}</i></a>' for m in MD.values())
INDEX = (ANSWER("The Method Library is our public catalogue of pharmaceutical test methods. Each entry explains what the test is for, how it works, which pharmacopoeia chapters and ICH guidelines apply, how much sample we need, typical turnaround and what you receive. It covers 46 methods today and is growing towards 500.")
         + '<section class="ml-x"><div class="ml-f"><label class="ml-q"><span class="vh">Search methods</span><input type="search" placeholder="Search: endotoxin, USP 711, capping, AAV..." data-mlq></label>'
         + f'<label><span class="vh">Technique</span><select data-mlf="f"><option value="">All techniques</option>{"".join(f"<option>{f}</option>" for f in _fams)}</select></label>'
         + f'<label><span class="vh">Standard</span><select data-mlf="sf"><option value="">All standards</option>{"".join(f"<option>{f}</option>" for f in _stdf)}</select></label>'
         + '<div class="ml-mods" role="group" aria-label="Modality">' + "".join(f'<button type="button" class="ch" data-mlm="{k}" aria-pressed="false">{n}</button>' for k, n in MODN.items()) + '</div>'
         + '<span class="ml-n" aria-live="polite"></span></div>'
         + f'<div class="ml-g" data-root-rel="method-library/">{_cards}</div><p class="nores ml-none" hidden>No method matches. <a href="/request-quote.html">Ask us anyway</a>: we run many methods that are not listed yet.</p>'
         + f'<script type="application/json" class="ml-json">{json.dumps(_data, ensure_ascii=False)}</script></section>'
         + SH("Browse by technique", "Ten technique families, one data standard.")
         + GRID([(f, f'{sum(1 for m in MD.values() if m["fam"] == f)} methods, for example {next(m["name"] for m in MD.values() if m["fam"] == f)}.', f'/method-library/{next(m["slug"] for m in MD.values() if m["fam"] == f)}.html', "Open an example") for f in _fams], 3)
         + STRIP(["inst-hplc", "inst-lcms", "inst-dissolution", "micro-petri-1", "inst-pcr", "lab-plate-pink", "bio-cells-green", "inst-icp", "inst-gc", "lab-corridor"])
         + SPLIT("lab-analyst-pc", H2("How to read a method page") + UL(["<b>The short answer</b> says what the test is for in one or two sentences.", "<b>Spec sheet</b> lists the pharmacopoeia chapters, sample amount, turnaround and instruments.",
                                                                         "<b>Validation status</b> shows our target accreditation scope. Until a site holds it, it is marked as a placeholder.", "<b>Request this test</b> opens a quote request with the method already filled in."]))
         + CALL(f"{ILL('Placeholder status')} Validation and accreditation status per method is a target until each site's scope is issued. Turnaround times are indicative business days after sample receipt. Compendial chapter numbers are cited as commonly referenced; always check the current official edition."))

_ld_list = {"@context": "https://schema.org", "@type": "ItemList", "name": "PharmaCRO Method Library", "numberOfItems": len(MD),
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": m["name"], "url": f"{DOMAIN}/method-library/{m['slug']}"} for i, m in enumerate(MD.values())]}
page("method-library/index", "Method Library", f"A public, searchable catalogue of {len(MD)} pharmaceutical test methods: purpose, principle, standards, sample, turnaround and instruments.",
     INDEX, img="inst-hplc", eyebrow="Resources", chips=[(str(len(MD)), "methods today"), ("500+", "planned"), ("10", "technique families")],
     jsonld=[_ld_list], cta=("Need a method that is not listed?", "Send us your specification or monograph. A scientist replies within 4 business hours with what we can run and how fast."))

# ---------------- method pages ----------------
for m in MD.values():
    s0 = SVC[m["svcs"][0]]
    faqs = [(f"How much sample do you need for {m['name'].lower()}?", f"<p>{m['sample']}. Exact amounts depend on your specification and the number of replicates; we confirm them in the quote.</p>"),
            (f"How long does {m['name'].lower()} take?", f"<p>Typically {m['tat'].lower()}, from sample receipt and acceptance. Priority and Critical tiers are available for most methods. {ILL('Indicative')}</p>"),
            ("Which standards does this method follow?", f"<p>{', '.join(m['stds'])}. We run the compendial procedure where one exists, or a validated in-house method justified against it.</p>"),
            ("Is the method validated and accredited?", f"<p>Our target is a validated method within the ISO/IEC 17025 scope at each lab that offers it. Until a site's scope is issued this is a placeholder, and the accreditation wall shows the current status. {ILL('Target')}</p>")]
    spec = KV([("Technique", m["fam"]), ("Standards", ", ".join(m["stds"])), ("Modalities", ", ".join(MODN[x] for x in m["mods"])), ("Typical sample", m["sample"]),
               ("Indicative turnaround", m["tat"]), ("Instruments", m["instr"]), ("Validation status", f"Validated method in target ISO/IEC 17025 scope {ILL('Target')}")])
    rel = GRID([(MD[r]["name"], MD[r]["purpose"].split(",")[0].split(" measures")[0][:120] + ".", f"/method-library/{r}.html", "Open method") for r in m["rel"]], 3)
    body = (ANSWER(m["purpose"])
            + '<div class="two"><div>' + DIAG(m["fam"]) + f'<p class="cn">Simplified diagram of the {m["fam"].lower()} principle.</p></div><div>' + H3("Spec sheet") + spec + '</div></div>'
            + SPLIT(m["img"], H2("How it works") + P(m["principle"]))
            + '<div class="two"><div>' + H2("When you need it") + TICKLIST(m["when"]) + '</div><div>' + H2("What you receive") + TICKLIST(m["get"]) + '</div></div>'
            + H2("Limitations and common pitfalls") + P("What goes wrong most often, and what we check for:") + UL(m["pitfalls"])
            + H2("Related methods") + rel
            + f'<div class="box ml-svc reveal"><p class="ey">Part of a service</p><h3><a href="{svc_url(s0[0])}">{s0[1]}</a></h3><p>{s0[2]} Typical turnaround {s0[6]}.</p>'
            + f'<p><a class="btn" href="{_quote(m)}">Request this test</a> <a class="btn o" href="{svc_url(s0[0])}">See the service</a> <a class="btn o" href="/method-library/index.html">All methods</a></p></div>'
            + H2("Questions") + FAQS(faqs, "mf"))
    ld = {"@context": "https://schema.org", "@type": "TechArticle", "headline": m["name"], "description": m["purpose"], "about": m["fam"], "proficiencyLevel": "Expert",
          "dateModified": "2026-11-21", "author": {"@type": "Organization", "name": BRAND}, "url": f"{DOMAIN}/method-library/{m['slug']}", "keywords": ", ".join(m["stds"])}
    page(f"method-library/{m['slug']}", m["name"], f"{m['fam']} method to {', '.join(m['stds'][:3])}. Typical sample: {m['sample'][0].lower() + m['sample'][1:]}. Indicative turnaround: {m['tat'].lower()}.", body,
         img=m["img"], eyebrow=f"Method Library &middot; {m['fam']}", crumbs=[("Method Library", "/method-library/index.html")], desc=m["purpose"],
         chips=[(m["tat"].split(" (")[0].split(";")[0], "indicative turnaround"), (m["stds"][0], "key standard"), (MODN[m["mods"][0]], "modality")],
         hb=f'<a class="btn big mag" href="{_quote(m)}"><span>Request this test</span></a> <a class="btn o big" href="/book-a-call.html">Talk to a scientist</a>',
         jsonld=[ld], cta=(f"Need {m['name'].lower()} on your next batch?", f"Send the product, specification and date. A scientist replies within 4 business hours with a quote for {m['name'].lower()}."))
