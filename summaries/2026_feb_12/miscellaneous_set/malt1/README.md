# Malt1 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.13
- RMSE: 1.43
- R²: 0.47
- Kendall 𝜏: 0.42
- Spearman ρ: 0.53

## System Details
- Ligands: 10
- Host Atoms: 6224
- Map Details:
  - Edges: 16
  - Min Dummy Atoms: 3
  - Max Dummy Atoms: 16
  - Mean Dummy Atoms: 10.6
  - Median Dummy Atoms: 12.0

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 2.23 Hours
- Average Time Per Edge: 0.14 Hours
- Total Nanoseconds Simulated: 1683.40
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
