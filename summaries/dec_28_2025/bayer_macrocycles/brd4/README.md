# Brd4 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.08
- RMSE: 1.14
- R²: 0.60
- Kendall 𝜏: 1.00
- Spearman ρ: 1.00

## System Details
- Ligands: 3
- Host Atoms: 1776
- Map Details:
  - Edges: 3
  - Min Dummy Atoms: 6
  - Max Dummy Atoms: 41
  - Mean Dummy Atoms: 24.7
  - Median Dummy Atoms: 27.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 2.00 Hours
- Total Nanoseconds Simulated: 625.20
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 9128
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
