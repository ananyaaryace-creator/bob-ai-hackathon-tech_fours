"""
submission_checker.py
----------------------
Mode 2: Regulatory Submission Readiness Checker.

Compares a submitted dossier outline against the ICH M4 Common Technical
Document (CTD) required structure, scores completeness per module, and
generates a gap report.
"""

import pandas as pd


def score_completeness(outline_df):
    module_scores = (
        outline_df.groupby("module")["submitted"]
        .agg(sections_total="count", sections_submitted="sum")
        .reset_index()
    )
    module_scores["completeness_pct"] = (
        100 * module_scores["sections_submitted"] / module_scores["sections_total"]
    ).round(1)
    return module_scores.sort_values("completeness_pct")


def build_gap_report(outline_df, module_scores_df):
    missing = outline_df[~outline_df["submitted"]]
    overall_pct = round(100 * outline_df["submitted"].sum() / len(outline_df), 1)

    lines = [
        "REGULATORY SUBMISSION READINESS REPORT (ICH M4 CTD)",
        "=" * 60,
        f"Overall completeness: {overall_pct}% ({outline_df['submitted'].sum()}/{len(outline_df)} sections present)",
        "",
        "Per-module completeness:",
    ]
    for _, row in module_scores_df.iterrows():
        flag = "  <-- INCOMPLETE" if row["completeness_pct"] < 100 else ""
        lines.append(
            f"  {row['module']}: {row['completeness_pct']}% "
            f"({row['sections_submitted']}/{row['sections_total']}){flag}"
        )

    lines.append("")
    if missing.empty:
        lines.append("No missing sections. Dossier is submission-ready.")
    else:
        lines.append(f"MISSING SECTIONS ({len(missing)}) — must be resolved before submission:")
        for _, row in missing.iterrows():
            lines.append(f"  - [{row['module']}] {row['section']}")
        lines.append("")
        lines.append("RISK: Historically, a single missing required section results in")
        lines.append("Refuse-to-File / rejection, costing 6-12 months and $50-100M in delay.")

    return "\n".join(lines)
