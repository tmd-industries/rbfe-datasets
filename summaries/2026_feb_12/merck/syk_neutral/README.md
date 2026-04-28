# Syk Map Charge 0

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.25
- RMSE: 1.47
- R²: 0.04
- Kendall 𝜏: 0.00
- Spearman ρ: 0.00

## System Details
- Ligands: 40
- Host Atoms: 4558
- Map Details:
  - Edges: 67
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 42
  - Mean Dummy Atoms: 9.8
  - Median Dummy Atoms: 7.0

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 8.28 Hours
- Average Time Per Edge: 0.12 Hours
- Total Nanoseconds Simulated: 8212.00
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
