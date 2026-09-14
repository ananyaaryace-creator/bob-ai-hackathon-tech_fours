# Documentation

## Architecture
```
src/
  data_generator.py      → synthetic FAERS-style adverse event reports
                            (swap for real openFDA data in production)
                            + a synthetic CTD dossier outline with gaps
  signal_detector.py      → PRR / Chi-square disproportionality analysis
  submission_checker.py   → ICH M4 CTD completeness scoring + gap report
  main.py                 → orchestrates both modes, saves outputs + charts
```

## Why PRR + Chi-square?
This is the same disproportionality analysis method used in real-world
pharmacovigilance (used by regulatory bodies like the MHRA). PRR compares
how often an event is reported with a specific drug versus all other drugs;
Chi-square with Yates' correction confirms the association isn't due to
chance. A signal is only flagged when **all three** Evans criteria are met
(PRR ≥ 2, Chi² ≥ 4, case count ≥ 3), reducing false positives.

## Why ICH M4 CTD structure?
The Common Technical Document is the internationally standardized format
regulators (FDA, EMA, etc.) require for drug approval submissions,
organized into 5 modules (Administrative, Summaries, Quality, Nonclinical,
Clinical). Our checker mirrors this exact structure so the gap report maps
directly to what a regulatory affairs team already tracks manually.

## How to run
```bash
pip install pandas numpy matplotlib
cd src
python3 main.py
```

## Outputs
- `adverse_event_signals.csv` — every drug/event pair with PRR, Chi2, flag
- `signal_detection_summary.txt` — plain-English top signals
- `signal_detection_chart.png` — flagged signals ranked by PRR
- `submission_readiness_report.txt` — per-module completeness + missing sections
- `submission_readiness_chart.png` — completeness by CTD module

## Extending to production
Swap `data_generator.py` for a real ingestion connector to the openFDA
FAERS API; the detection and scoring logic in `signal_detector.py` and
`submission_checker.py` stays identical.

## Built with IBM Bob
This project was developed using IBM Bob IDE as the core development
partner. See `/bob_sessions` (or wherever your repo's session-log folder
is) for exported Bob task history and consumption screenshots.
