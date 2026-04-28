# Urokinase Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.74
- RMSE: 0.81
- R²: 0.59
- Kendall 𝜏: 0.67
- Spearman ρ: 0.80

## System Details
- Ligands: 4
- Host Atoms: 4581
- Map Details:
  - Edges: 6
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 3
  - Mean Dummy Atoms: 1.8
  - Median Dummy Atoms: 2.0

## Simulation Details
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 1.33 Hours
- Average Time Per Edge: 0.22 Hours
- Total Nanoseconds Simulated: 502.80
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
