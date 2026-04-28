# Hsp90 2Rings Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.27
- RMSE: 1.46
- R²: 0.35
- Kendall 𝜏: 0.60
- Spearman ρ: 0.66

## System Details
- Ligands: 6
- Host Atoms: 3795
- Map Details:
  - Edges: 9
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 6
  - Mean Dummy Atoms: 3.3
  - Median Dummy Atoms: 3.0

## Simulation Details
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 1.79 Hours
- Average Time Per Edge: 0.20 Hours
- Total Nanoseconds Simulated: 716.80
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
