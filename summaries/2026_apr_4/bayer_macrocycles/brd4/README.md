# Brd4 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.68
- RMSE: 0.78
- R²: 0.82
- Kendall 𝜏: 1.00
- Spearman ρ: 1.00

## System Details
- Ligands: 3
- Host Atoms: 2055
- Map Details:
  - Edges: 3
  - Min Dummy Atoms: 8
  - Max Dummy Atoms: 47
  - Mean Dummy Atoms: 29.3
  - Median Dummy Atoms: 33.0

## Simulation Details
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 1.24 Hours
- Average Time Per Edge: 0.41 Hours
- Total Nanoseconds Simulated: 605.20
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
