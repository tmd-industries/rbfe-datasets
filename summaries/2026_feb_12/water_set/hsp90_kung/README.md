# Hsp90 Kung Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.74
- RMSE: 2.25
- R²: 0.52
- Kendall 𝜏: 0.56
- Spearman ρ: 0.74

## System Details
- Ligands: 11
- Host Atoms: 3924
- Map Details:
  - Edges: 18
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 8
  - Mean Dummy Atoms: 4.6
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 1.80 Hours
- Average Time Per Edge: 0.10 Hours
- Total Nanoseconds Simulated: 1583.20
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
