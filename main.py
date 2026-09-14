"""
main.py
-------
Bob Copilot: Drug Safety Signal Detector & Regulatory Submission
Readiness Checker (P2)

Mode 1: Signal Detection      -> PRR/Chi-square disproportionality analysis
Mode 2: Submission Readiness  -> ICH M4 CTD dossier gap report
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import data_generator as dg
import signal_detector as sd
import submission_checker as sc

OUTPUT_DIR = "/mnt/user-data/outputs"


def run_signal_detection():
    print("=== MODE 1: Drug Safety Signal Detection ===")
    reports = dg.generate_adverse_event_reports(n_reports=8000)
    signals = sd.compute_signals(reports)

    signals_path = os.path.join(OUTPUT_DIR, "adverse_event_signals.csv")
    signals.to_csv(signals_path, index=False)
    print(f"Saved: {signals_path}")

    summary = sd.summarize_signals(signals, top_n=5)
    summary_path = os.path.join(OUTPUT_DIR, "signal_detection_summary.txt")
    with open(summary_path, "w") as f:
        f.write(summary)
    print(summary)
    print()

    # Chart: PRR of flagged signals
    flagged = signals[signals["signal_flagged"]].head(10).iloc[::-1]
    if not flagged.empty:
        labels = flagged["drug"] + " + " + flagged["event"]
        fig, ax = plt.subplots(figsize=(9, 5))
        ax.barh(labels, flagged["prr"], color="#d62728")
        ax.axvline(2.0, color="black", linestyle="--", linewidth=1, label="PRR=2 threshold")
        ax.set_xlabel("Proportional Reporting Ratio (PRR)")
        ax.set_title("Flagged Adverse Event Signals")
        ax.legend()
        plt.tight_layout()
        chart_path = os.path.join(OUTPUT_DIR, "signal_detection_chart.png")
        plt.savefig(chart_path, dpi=150)
        print(f"Saved: {chart_path}")

    return signals_path, summary_path


def run_submission_readiness():
    print("=== MODE 2: Regulatory Submission Readiness ===")
    outline = dg.generate_dossier_outline(missing_fraction=0.18)
    module_scores = sc.score_completeness(outline)
    report = sc.build_gap_report(outline, module_scores)

    report_path = os.path.join(OUTPUT_DIR, "submission_readiness_report.txt")
    with open(report_path, "w") as f:
        f.write(report)
    print(report)
    print()

    # Chart: completeness per module
    fig, ax = plt.subplots(figsize=(8, 4.5))
    colors = ["#d62728" if p < 100 else "#2ca02c" for p in module_scores["completeness_pct"]]
    ax.barh(module_scores["module"], module_scores["completeness_pct"], color=colors)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Completeness (%)")
    ax.set_title("CTD Dossier Completeness by Module")
    plt.tight_layout()
    chart_path = os.path.join(OUTPUT_DIR, "submission_readiness_chart.png")
    plt.savefig(chart_path, dpi=150)
    print(f"Saved: {chart_path}")

    return report_path


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    run_signal_detection()
    print()
    run_submission_readiness()


if __name__ == "__main__":
    main()
