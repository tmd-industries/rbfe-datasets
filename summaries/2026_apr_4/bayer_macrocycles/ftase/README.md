# Ftase Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.97
- RMSE: 1.04
- R²: 0.36
- Kendall 𝜏: 0.40
- Spearman ρ: 0.50

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
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 7.37 Hours
- Average Time Per Edge: 0.92 Hours
- Total Nanoseconds Simulated: 1546.40
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
