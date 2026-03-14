# Eg5 Neutral Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.95
- RMSE: 1.13
- R²: 0.56
- Kendall 𝜏: 0.42
- Spearman ρ: 0.54

## System Details
- Ligands: 9
- Host Atoms: 5906
- Map Details:
  - Edges: 15
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 22
  - Mean Dummy Atoms: 9.5
  - Median Dummy Atoms: 9.0

## Simulation Details
- TMD Sha: [c1f675e11c1e05722eb072dcd5938757baab1a6b](https://github.com/tmd-industries/tmd/tree/c1f675e11c1e05722eb072dcd5938757baab1a6b)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 2.26 Hours
- Total Nanoseconds Simulated: 1916.20
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
