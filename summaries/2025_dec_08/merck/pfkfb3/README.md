# Pfkfb3 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.95
- RMSE: 1.20
- R²: 0.31
- Kendall 𝜏: 0.42
- Spearman ρ: 0.57

## System Details
- Ligands: 40
- Host Atoms: 7834
- Map Details:
  - Edges: 69
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 16
  - Mean Dummy Atoms: 3.7
  - Median Dummy Atoms: 3.0

## Simulation Details
- TMD Sha: [c1f675e11c1e05722eb072dcd5938757baab1a6b](https://github.com/tmd-industries/tmd/tree/c1f675e11c1e05722eb072dcd5938757baab1a6b)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 18.67 Hours
- Total Nanoseconds Simulated: 7276.40
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
