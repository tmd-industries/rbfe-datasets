# Hif2A Jmc2023 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.95
- RMSE: 1.11
- R²: 0.46
- Kendall 𝜏: 0.50
- Spearman ρ: 0.70

## System Details
- Ligands: 38
- Host Atoms: 1937
- Map Details:
  - Edges: 62
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 15
  - Mean Dummy Atoms: 5.8
  - Median Dummy Atoms: 5.5

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 5.37 Hours
- Average Time Per Edge: 0.09 Hours
- Total Nanoseconds Simulated: 5898.60
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
