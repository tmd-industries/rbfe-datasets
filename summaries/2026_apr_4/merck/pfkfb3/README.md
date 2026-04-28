# Pfkfb3 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.87
- RMSE: 1.16
- R²: 0.32
- Kendall 𝜏: 0.42
- Spearman ρ: 0.56

## System Details
- Ligands: 40
- Host Atoms: 8158
- Map Details:
  - Edges: 72
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 17
  - Mean Dummy Atoms: 4.9
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 33.77 Hours
- Average Time Per Edge: 0.47 Hours
- Total Nanoseconds Simulated: 7892.80
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
