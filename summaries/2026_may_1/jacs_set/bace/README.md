# Bace Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.29
- RMSE: 1.60
- R²: 0.16
- Kendall 𝜏: 0.28
- Spearman ρ: 0.39

## System Details
- Ligands: 36
- Host Atoms: 6101
- Map Details:
  - Edges: 61
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 12
  - Mean Dummy Atoms: 5.3
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 6.28 Hours
- Average Time Per Edge: 0.10 Hours
- Total Nanoseconds Simulated: 6254.80
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
