# Syk Map Charge 0

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.27
- RMSE: 1.55
- R²: 0.03
- Kendall 𝜏: 0.00
- Spearman ρ: 0.01

## System Details
- Ligands: 40
- Host Atoms: 4558
- Map Details:
  - Edges: 66
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 42
  - Mean Dummy Atoms: 10.0
  - Median Dummy Atoms: 7.5

## Simulation Details
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 28.39 Hours
- Average Time Per Edge: 0.43 Hours
- Total Nanoseconds Simulated: 8499.20
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
