# Demo Script

## Live demo flow (under 90 seconds)

1. **Run the pipeline live on screen:**
   ```bash
   cd src
   python3 main.py
   ```

2. **Point out the flagged signal** in the terminal output:
   > "This is the exact kind of pattern that took years to catch with
   > Vioxx — our tool flags it instantly using PRR and Chi-square, the
   > same statistics real regulators use."

   Expected output includes:
   ```
   Drug E + Myocardial infarction: PRR=3.13, Chi2=259.79, cases=232
   -> RECOMMEND: escalate for clinical review
   ```

3. **Scroll to the submission readiness output:**
   > "And here's a dossier with 3 missing sections out of 22 — normally
   > only caught after a 6-12 month rejection and $50-100M in delay."

4. **Show the two generated charts** (in `/outputs` after running):
   - `signal_detection_chart.png` — flagged signals ranked by PRR
   - `submission_readiness_chart.png` — completeness by CTD module

## Recording a demo video
If a recorded video is required, capture:
- Terminal running `main.py` start to finish
- Both output charts on screen
- (Optional) A quick look at the code in Bob IDE, showing Bob's assistance

Save the recording in this `demo/` folder (e.g. `demo/demo_video.mp4`) or
link it here if hosted externally:

**Demo video link:** _[add link here]_
