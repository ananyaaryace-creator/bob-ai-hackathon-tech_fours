"""
data_generator.py
------------------
Generates synthetic-but-realistic data for the Drug Safety Signal Detector &
Regulatory Submission Readiness Checker (P2 hackathon problem statement).

Produces:
1. adverse_event_reports - report-level FAERS-style data (drug, event, report_id)
2. dossier_outline        - a submitted CTD dossier's section outline (some missing,
                             to demonstrate gap detection)
"""

import numpy as np
import pandas as pd

RNG_SEED = 7
rng = np.random.default_rng(RNG_SEED)

DRUGS = ["Drug A", "Drug B", "Drug C", "Drug D", "Drug E"]

# Common adverse event terms (MedDRA-style, simplified)
EVENTS = [
    "Headache", "Nausea", "Dizziness", "Rash", "Fatigue",
    "Myocardial infarction", "Liver injury", "Anaphylaxis",
    "Rhabdomyolysis", "GI bleeding", "Insomnia", "Constipation",
]

# Drug E will be deliberately "unsafe" for one event to create a clear signal (like Vioxx/MI)
INJECTED_SIGNAL = {"drug": "Drug E", "event": "Myocardial infarction", "boost": 12}


def generate_adverse_event_reports(n_reports=8000):
    drugs = rng.choice(DRUGS, size=n_reports, p=[0.30, 0.25, 0.20, 0.15, 0.10])
    events = rng.choice(EVENTS, size=n_reports)

    df = pd.DataFrame({
        "report_id": [f"FAERS-{100000+i}" for i in range(n_reports)],
        "drug": drugs,
        "event": events,
    })

    # Inject an elevated real signal: Drug E + Myocardial infarction co-occurring
    # far more than base rate would predict
    n_inject = int(n_reports * 0.02 * INJECTED_SIGNAL["boost"] / 12)
    inject_df = pd.DataFrame({
        "report_id": [f"FAERS-INJ-{i}" for i in range(n_inject)],
        "drug": INJECTED_SIGNAL["drug"],
        "event": INJECTED_SIGNAL["event"],
    })

    return pd.concat([df, inject_df], ignore_index=True)


# --- ICH M4 CTD structure (simplified but realistic) ---
CTD_REQUIRED_SECTIONS = {
    "Module 1 - Administrative & Prescribing Info": [
        "1.1 Table of Contents", "1.2 Application Form", "1.3 Product Labeling",
        "1.4 Patient Information", "1.5 Pharmacovigilance Info",
    ],
    "Module 2 - Common Technical Document Summaries": [
        "2.1 CTD Table of Contents", "2.2 Introduction", "2.3 Quality Overall Summary",
        "2.4 Nonclinical Overview", "2.5 Clinical Overview",
        "2.6 Nonclinical Written/Tabulated Summaries", "2.7 Clinical Summary",
    ],
    "Module 3 - Quality": [
        "3.1 Table of Contents", "3.2 Body of Data (Drug Substance/Product)",
        "3.3 Literature References",
    ],
    "Module 4 - Nonclinical Study Reports": [
        "4.1 Table of Contents", "4.2 Study Reports (Pharm/Tox)", "4.3 Literature References",
    ],
    "Module 5 - Clinical Study Reports": [
        "5.1 Table of Contents", "5.2 Tabular Listing of Studies",
        "5.3 Clinical Study Reports", "5.4 Literature References",
    ],
}


def generate_dossier_outline(missing_fraction=0.18):
    """Simulates a submitted dossier's outline with some sections missing."""
    all_sections = [
        (module, section)
        for module, sections in CTD_REQUIRED_SECTIONS.items()
        for section in sections
    ]
    n_missing = max(1, int(len(all_sections) * missing_fraction))
    missing_idx = rng.choice(len(all_sections), size=n_missing, replace=False)

    submitted = []
    for i, (module, section) in enumerate(all_sections):
        submitted.append({
            "module": module,
            "section": section,
            "submitted": i not in missing_idx,
        })
    return pd.DataFrame(submitted)


if __name__ == "__main__":
    reports = generate_adverse_event_reports()
    print(reports["drug"].value_counts())
    print(reports[(reports.drug == "Drug E") & (reports.event == "Myocardial infarction")].shape[0],
          "Drug E + MI reports")

    outline = generate_dossier_outline()
    print(outline[~outline.submitted])
