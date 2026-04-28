# Jak2 Set2 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.72
- RMSE: 2.15
- R²: 0.45
- Kendall 𝜏: 0.57
- Spearman ρ: 0.76

## System Details
- Ligands: 8
- Host Atoms: 5857
- Map Details:
  - Edges: 12
  - Min Dummy Atoms: 3
  - Max Dummy Atoms: 38
  - Mean Dummy Atoms: 19.1
  - Median Dummy Atoms: 21.5

## Simulation Details
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 5.34 Hours
- Average Time Per Edge: 0.45 Hours
- Total Nanoseconds Simulated: 1786.00
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
