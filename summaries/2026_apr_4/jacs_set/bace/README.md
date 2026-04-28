# Bace Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.35
- RMSE: 1.67
- R²: 0.10
- Kendall 𝜏: 0.22
- Spearman ρ: 0.27

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
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 20.98 Hours
- Average Time Per Edge: 0.34 Hours
- Total Nanoseconds Simulated: 6097.60
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 4589
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
