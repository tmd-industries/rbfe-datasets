# Bace Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.33
- RMSE: 1.57
- R²: 0.09
- Kendall 𝜏: 0.20
- Spearman ρ: 0.24

## System Details
- Ligands: 36
- Host Atoms: 6101
- Map Details:
  - Edges: 61
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 12
  - Mean Dummy Atoms: 5.3
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 5.26 Hours
- Average Time Per Edge: 0.09 Hours
- Total Nanoseconds Simulated: 5497.20
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 411
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
