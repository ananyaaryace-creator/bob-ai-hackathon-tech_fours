"""
signal_detector.py
-------------------
Mode 1: Drug Safety Signal Detection.

Computes Proportional Reporting Ratio (PRR) and Chi-square statistic for
every (drug, event) pair in the adverse event reports, using the standard
2x2 disproportionality contingency table:

                 Event Y        All other events
Drug X             a                  b
Other drugs        c                  d

PRR = (a / (a+b)) / (c / (c+d))

A signal is flagged using the common Evans criteria (used by MHRA/FDA-style
pharmacovigilance screening):
  - PRR >= 2
  - Chi-square >= 4
  - a (case count) >= 3
"""

import numpy as np
import pandas as pd


def compute_signals(reports_df, min_cases=3, prr_threshold=2.0, chi2_threshold=4.0):
    total_reports = len(reports_df)
    results = []

    drugs = reports_df["drug"].unique()
    events = reports_df["event"].unique()

    for drug in drugs:
        drug_reports = reports_df[reports_df["drug"] == drug]
        other_reports = reports_df[reports_df["drug"] != drug]

        for event in events:
            a = (drug_reports["event"] == event).sum()
            b = len(drug_reports) - a
            c = (other_reports["event"] == event).sum()
            d = len(other_reports) - c

            if a < min_cases or (a + b) == 0 or (c + d) == 0 or c == 0:
                continue

            prr = (a / (a + b)) / (c / (c + d))

            # Chi-square with Yates' continuity correction
            n = a + b + c + d
            numerator = n * (abs(a * d - b * c) - n / 2) ** 2
            denominator = (a + b) * (c + d) * (a + c) * (b + d)
            chi2 = numerator / denominator if denominator > 0 else 0

            is_signal = (prr >= prr_threshold) and (chi2 >= chi2_threshold) and (a >= min_cases)

            results.append({
                "drug": drug,
                "event": event,
                "case_count_a": int(a),
                "prr": round(prr, 2),
                "chi_square": round(chi2, 2),
                "signal_flagged": is_signal,
            })

    signals_df = pd.DataFrame(results).sort_values("prr", ascending=False).reset_index(drop=True)
    return signals_df


def summarize_signals(signals_df, top_n=5):
    flagged = signals_df[signals_df["signal_flagged"]].head(top_n)
    lines = ["DRUG SAFETY SIGNAL DETECTION SUMMARY", "=" * 60]
    if flagged.empty:
        lines.append("No signals met the flagging criteria (PRR>=2, Chi2>=4, cases>=3).")
    else:
        lines.append(f"{len(signals_df[signals_df['signal_flagged']])} signal(s) flagged. Top {min(top_n, len(flagged))}:")
        lines.append("")
        for _, row in flagged.iterrows():
            lines.append(
                f"- {row['drug']} + {row['event']}: PRR={row['prr']}, "
                f"Chi2={row['chi_square']}, cases={row['case_count_a']} "
                f"-> RECOMMEND: escalate for clinical review"
            )
    return "\n".join(lines)
