# Galectin Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.99
- RMSE: 1.32
- R²: 0.52
- Kendall 𝜏: 0.50
- Spearman ρ: 0.70

## System Details
- Ligands: 26
- Host Atoms: 2712
- Map Details:
  - Edges: 45
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 15
  - Mean Dummy Atoms: 4.4
  - Median Dummy Atoms: 4.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 4.04 Hours
- Average Time Per Edge: 0.09 Hours
- Total Nanoseconds Simulated: 4444.00
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
