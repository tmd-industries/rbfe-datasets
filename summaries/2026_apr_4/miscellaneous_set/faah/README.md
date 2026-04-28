# Faah Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.22
- RMSE: 1.43
- R²: 0.62
- Kendall 𝜏: 0.48
- Spearman ρ: 0.60

## System Details
- Ligands: 24
- Host Atoms: 8446
- Map Details:
  - Edges: 41
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 10
  - Mean Dummy Atoms: 6.0
  - Median Dummy Atoms: 6.0

## Simulation Details
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 16.52 Hours
- Average Time Per Edge: 0.40 Hours
- Total Nanoseconds Simulated: 4172.80
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
