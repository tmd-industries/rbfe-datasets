# Jak2 Set1 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.50
- RMSE: 0.59
- R²: 0.86
- Kendall 𝜏: 0.78
- Spearman ρ: 0.87

## System Details
- Ligands: 10
- Host Atoms: 5622
- Map Details:
  - Edges: 17
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 12
  - Mean Dummy Atoms: 7.0
  - Median Dummy Atoms: 8.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 1.71 Hours
- Average Time Per Edge: 0.10 Hours
- Total Nanoseconds Simulated: 1948.00
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
