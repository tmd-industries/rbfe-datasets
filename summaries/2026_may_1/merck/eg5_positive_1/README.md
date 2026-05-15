# Eg5 Map Charge 1

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.91
- RMSE: 1.11
- R²: 0.07
- Kendall 𝜏: 0.16
- Spearman ρ: 0.23

## System Details
- Ligands: 19
- Host Atoms: 5906
- Map Details:
  - Edges: 31
  - Min Dummy Atoms: 5
  - Max Dummy Atoms: 36
  - Mean Dummy Atoms: 16.8
  - Median Dummy Atoms: 16.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 5.11 Hours
- Average Time Per Edge: 0.16 Hours
- Total Nanoseconds Simulated: 5100.00
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 501
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
