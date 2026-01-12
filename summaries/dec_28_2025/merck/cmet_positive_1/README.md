# Cmet Map Charge 1

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.97
- RMSE: 1.22
- R²: 0.57
- Kendall 𝜏: 0.68
- Spearman ρ: 0.84

## System Details
- Ligands: 12
- Host Atoms: 4977
- Map Details:
  - Edges: 21
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 49
  - Mean Dummy Atoms: 15.3
  - Median Dummy Atoms: 11.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 3.92 Hours
- Total Nanoseconds Simulated: 3297.80
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
