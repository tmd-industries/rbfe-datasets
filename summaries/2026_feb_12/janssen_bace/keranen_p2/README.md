# Keranen P2 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.33
- RMSE: 0.39
- R²: 0.34
- Kendall 𝜏: 0.40
- Spearman ρ: 0.52

## System Details
- Ligands: 12
- Host Atoms: 6252
- Map Details:
  - Edges: 19
  - Min Dummy Atoms: 3
  - Max Dummy Atoms: 17
  - Mean Dummy Atoms: 8.6
  - Median Dummy Atoms: 9.0

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 2.04 Hours
- Average Time Per Edge: 0.11 Hours
- Total Nanoseconds Simulated: 1761.00
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
