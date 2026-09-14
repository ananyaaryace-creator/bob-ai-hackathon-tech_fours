# Proposed Solution

We built a **Bob Copilot with two operating modes**, using the same
statistical rigor regulators actually use:

## Mode 1 — Drug Safety Signal Detection
Ingests adverse event reports and automatically flags drug/event pairs with
disproportionate reporting using the industry-standard **Proportional
Reporting Ratio (PRR)** and **Chi-square** statistical test — the same
method (Evans criteria: PRR ≥ 2, Chi² ≥ 4, cases ≥ 3) used in real
pharmacovigilance signal screening at regulatory agencies. Instead of a
human scanning millions of rows, the system surfaces only the pairs that
are statistically significant, ranked by strength of signal.

## Mode 2 — Regulatory Submission Readiness Checker
Compares a dossier's submitted section outline against the **ICH M4 CTD**
required structure (all 5 modules), scores completeness per module, and
generates a plain-English gap report listing exactly which sections are
missing — before the dossier ever reaches the regulator.

## Why this matters
Together, these two modes turn a problem that used to take **teams of
analysts weeks** into something that runs **in seconds**, catching both the
dangerous safety signal and the submission-ending clerical gap.

## Validation
On our test dataset, the tool correctly caught an injected "Drug E +
Myocardial Infarction" signal (PRR 3.13, Chi² 259.79) — mirroring the
real-world Vioxx/MI pattern — and correctly identified 3 missing CTD
sections out of 22 in a simulated dossier.
