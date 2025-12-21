# Eg5 Positive Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 3.31
- RMSE: 3.93
- R²: 0.07
- Kendall 𝜏: 0.12
- Spearman ρ: 0.21

## System Details
- Ligands: 19
- Host Atoms: 5906
- Map Details:
  - Edges: 33
  - Min Dummy Atoms: 3
  - Max Dummy Atoms: 25
  - Mean Dummy Atoms: 12.3
  - Median Dummy Atoms: 12.0

## Simulation Details
- TMD Sha: [c1f675e11c1e05722eb072dcd5938757baab1a6b](https://github.com/tmd-industries/tmd/tree/c1f675e11c1e05722eb072dcd5938757baab1a6b)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 12.35 Hours
- Total Nanoseconds Simulated: 5311.00
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
