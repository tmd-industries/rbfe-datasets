# Mcl1 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.69
- RMSE: 0.84
- R²: 0.21
- Kendall 𝜏: 0.18
- Spearman ρ: 0.31

## System Details
- Ligands: 12
- Host Atoms: 2428
- Map Details:
  - Edges: 20
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 19
  - Mean Dummy Atoms: 7.2
  - Median Dummy Atoms: 6.0

## Simulation Details
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 5.15 Hours
- Average Time Per Edge: 0.26 Hours
- Total Nanoseconds Simulated: 2197.60
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
