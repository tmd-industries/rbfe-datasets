# Eg5 Map Charge 1

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.69
- RMSE: 0.90
- R²: 0.17
- Kendall 𝜏: 0.31
- Spearman ρ: 0.41

## System Details
- Ligands: 19
- Host Atoms: 5906
- Map Details:
  - Edges: 31
  - Min Dummy Atoms: 5
  - Max Dummy Atoms: 36
  - Mean Dummy Atoms: 16.8
  - Median Dummy Atoms: 16.0

## Simulation Details
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 16.95 Hours
- Average Time Per Edge: 0.55 Hours
- Total Nanoseconds Simulated: 4958.40
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
