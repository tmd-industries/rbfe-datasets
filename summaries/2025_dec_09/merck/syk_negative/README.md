# Syk Negative Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.48
- RMSE: 0.66
- R²: 0.77
- Kendall 𝜏: 0.60
- Spearman ρ: 0.71

## System Details
- Ligands: 6
- Host Atoms: 4667
- Map Details:
  - Edges: 10
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 38
  - Mean Dummy Atoms: 15.6
  - Median Dummy Atoms: 7.0

## Simulation Details
- TMD Sha: [c1f675e11c1e05722eb072dcd5938757baab1a6b](https://github.com/tmd-industries/tmd/tree/c1f675e11c1e05722eb072dcd5938757baab1a6b)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 1.92 Hours
- Total Nanoseconds Simulated: 1727.00
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
