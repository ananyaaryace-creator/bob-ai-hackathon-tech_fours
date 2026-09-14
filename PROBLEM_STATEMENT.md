# Problem Statement — P2

**Drug Safety Signal Detector & Regulatory Submission Readiness Checker**
*(Pharma & Biotech | Critical Now)*

FDA's FAERS database has 20M+ adverse event reports. Vioxx caused 27,000+
heart attacks before its signal was acted on. Separately, a drug approval
CTD dossier spans 100,000+ pages across 5 modules — one missing section
gets it rejected, costing 6–12 months and $50–100M. Both problems share the
same root cause: too much complex data for manual review.

## Our Challenge (as given)
Build a Bob solution with two modes:
1. **Signal Detection** — cluster adverse event reports and calculate PRR
   statistics to flag emerging safety signals.
2. **Submission Readiness** — check a dossier outline against ICH M4 CTD
   requirements, score completeness per module, and generate a gap report.
