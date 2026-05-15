# Hne Map Charge -1

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.39
- RMSE: 0.39
- R²: 1.00
- Kendall 𝜏: 1.00
- Spearman ρ: 1.00

## System Details
- Ligands: 2
- Host Atoms: 3804
- Map Details:
  - Edges: 1
  - Min Dummy Atoms: 10
  - Max Dummy Atoms: 10
  - Mean Dummy Atoms: 10.0
  - Median Dummy Atoms: 10.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 0.13 Hours
- Average Time Per Edge: 0.13 Hours
- Total Nanoseconds Simulated: 109.20
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
