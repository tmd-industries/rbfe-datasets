# Mcl1 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.44
- RMSE: 1.93
- R²: 0.53
- Kendall 𝜏: 0.55
- Spearman ρ: 0.71

## System Details
- Ligands: 42
- Host Atoms: 2542
- Map Details:
  - Edges: 74
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 15
  - Mean Dummy Atoms: 5.7
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 21.46 Hours
- Average Time Per Edge: 0.29 Hours
- Total Nanoseconds Simulated: 8052.80
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
