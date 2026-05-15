# Ftase Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.07
- RMSE: 1.27
- R²: 0.00
- Kendall 𝜏: 0.00
- Spearman ρ: -0.10

## System Details
- Ligands: 5
- Host Atoms: 13188
- Map Details:
  - Edges: 8
  - Min Dummy Atoms: 5
  - Max Dummy Atoms: 58
  - Mean Dummy Atoms: 36.6
  - Median Dummy Atoms: 39.5

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 3.66 Hours
- Average Time Per Edge: 0.46 Hours
- Total Nanoseconds Simulated: 1583.20
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
