# Renin Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.14
- RMSE: 1.50
- R²: 0.27
- Kendall 𝜏: 0.37
- Spearman ρ: 0.48

## System Details
- Ligands: 29
- Host Atoms: 5321
- Map Details:
  - Edges: 56
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 24
  - Mean Dummy Atoms: 9.6
  - Median Dummy Atoms: 7.0

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 6.13 Hours
- Average Time Per Edge: 0.11 Hours
- Total Nanoseconds Simulated: 6078.80
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
