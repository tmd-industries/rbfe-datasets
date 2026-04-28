# Tyk2 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.54
- RMSE: 0.71
- R²: 0.68
- Kendall 𝜏: 0.53
- Spearman ρ: 0.75

## System Details
- Ligands: 16
- Host Atoms: 4670
- Map Details:
  - Edges: 26
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 12
  - Mean Dummy Atoms: 5.1
  - Median Dummy Atoms: 5.5

## Simulation Details
- TMD Sha: [c1f675e11c1e05722eb072dcd5938757baab1a6b](https://github.com/tmd-industries/tmd/tree/c1f675e11c1e05722eb072dcd5938757baab1a6b)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 2.66 Hours
- Total Nanoseconds Simulated: 2817.80
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
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
