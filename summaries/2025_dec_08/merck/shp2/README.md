# Shp2 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.43
- RMSE: 1.83
- R²: 0.28
- Kendall 𝜏: 0.42
- Spearman ρ: 0.58

## System Details
- Ligands: 26
- Host Atoms: 8422
- Map Details:
  - Edges: 48
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 25
  - Mean Dummy Atoms: 5.4
  - Median Dummy Atoms: 4.0

## Simulation Details
- TMD Sha: [c1f675e11c1e05722eb072dcd5938757baab1a6b](https://github.com/tmd-industries/tmd/tree/c1f675e11c1e05722eb072dcd5938757baab1a6b)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 17.36 Hours
- Total Nanoseconds Simulated: 5627.60
- TMD Forcefield: smirnoff_2_2_1_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 912
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
