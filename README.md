# Drug Safety Signal Detector & Regulatory Submission Readiness Checker (P2)

A Bob Copilot solution for IBM BoB AI Innovation Hackathon 2026, addressing
problem statement **P2** (Pharma & Biotech, Critical Now).

## What it does
Two modes in one tool:
1. **Signal Detection** — flags dangerous drug/adverse-event patterns using
   PRR + Chi-square statistics (the same method real regulators use)
2. **Submission Readiness** — checks a regulatory dossier against the ICH
   M4 CTD structure and reports exactly which sections are missing

## Repository structure
- [`docs/PROBLEM_STATEMENT.md`](docs/PROBLEM_STATEMENT.md) — the challenge
- [`docs/PROPOSED_SOLUTION.md`](docs/PROPOSED_SOLUTION.md) — our approach
- [`docs/DOCUMENTATION.md`](docs/DOCUMENTATION.md) — architecture, how to run, methodology
- [`src/`](src/) — all source code
- [`demo/DEMO.md`](demo/DEMO.md) — demo script and video link
- [`presentation/PRESENTATION_OUTLINE.md`](presentation/PRESENTATION_OUTLINE.md) — slide deck outline

## Quick start
```bash
pip install pandas numpy matplotlib
cd src
python3 main.py
```

## Built with IBM Bob
This project was developed using IBM Bob IDE as the core development
partner for code generation, refactoring, and documentation. Exported Bob
task session reports are included per the hackathon submission
requirements.
