# Btk Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.35
- RMSE: 1.50
- R²: 0.70
- Kendall 𝜏: 0.60
- Spearman ρ: 0.71

## System Details
- Ligands: 6
- Host Atoms: 5400
- Map Details:
  - Edges: 10
  - Min Dummy Atoms: 5
  - Max Dummy Atoms: 16
  - Mean Dummy Atoms: 11.3
  - Median Dummy Atoms: 11.5

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 1.53 Hours
- Average Time Per Edge: 0.15 Hours
- Total Nanoseconds Simulated: 1382.60
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
