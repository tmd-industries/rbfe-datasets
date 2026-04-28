# Hne Map Charge -1

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.12
- RMSE: 0.12
- R²: 1.00
- Kendall 𝜏: 1.00
- Spearman ρ: 1.00

## System Details
- Ligands: 2
- Host Atoms: 3804
- Map Details:
  - Edges: 1
  - Min Dummy Atoms: 10
  - Max Dummy Atoms: 10
  - Mean Dummy Atoms: 10.0
  - Median Dummy Atoms: 10.0

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 0.64 Hours
- Average Time Per Edge: 0.64 Hours
- Total Nanoseconds Simulated: 94.80
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
