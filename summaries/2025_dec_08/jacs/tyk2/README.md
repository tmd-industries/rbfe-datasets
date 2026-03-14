# Tyk2 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.61
- RMSE: 0.78
- R²: 0.62
- Kendall 𝜏: 0.57
- Spearman ρ: 0.74

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
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 5.72 Hours
- Total Nanoseconds Simulated: 2648.00
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
