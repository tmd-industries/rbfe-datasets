# Cmet Positive Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.14
- RMSE: 1.33
- R²: 0.67
- Kendall 𝜏: 0.58
- Spearman ρ: 0.79

## System Details
- Ligands: 12
- Host Atoms: 4580
- Map Details:
  - Edges: 20
  - Min Dummy Atoms: 10
  - Max Dummy Atoms: 43
  - Mean Dummy Atoms: 24.6
  - Median Dummy Atoms: 23.0

## Simulation Details
- TMD Sha: [c1f675e11c1e05722eb072dcd5938757baab1a6b](https://github.com/tmd-industries/tmd/tree/c1f675e11c1e05722eb072dcd5938757baab1a6b)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 4.22 Hours
- Total Nanoseconds Simulated: 3889.80
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
