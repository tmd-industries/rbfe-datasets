# Cmet Map Charge 1

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.33
- RMSE: 1.70
- R²: 0.45
- Kendall 𝜏: 0.62
- Spearman ρ: 0.74

## System Details
- Ligands: 12
- Host Atoms: 4977
- Map Details:
  - Edges: 20
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 52
  - Mean Dummy Atoms: 19.8
  - Median Dummy Atoms: 16.5

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 3.23 Hours
- Average Time Per Edge: 0.16 Hours
- Total Nanoseconds Simulated: 3321.20
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
