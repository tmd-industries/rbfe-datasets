# Bace1 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.09
- RMSE: 1.19
- R²: 0.76
- Kendall 𝜏: 1.00
- Spearman ρ: 1.00

## System Details
- Ligands: 3
- Host Atoms: 6049
- Map Details:
  - Edges: 3
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 6
  - Mean Dummy Atoms: 4.0
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 1.99 Hours
- Total Nanoseconds Simulated: 360.80
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
