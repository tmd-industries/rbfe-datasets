# Ftase Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.54
- RMSE: 2.08
- R²: 0.13
- Kendall 𝜏: 0.20
- Spearman ρ: 0.30

## System Details
- Ligands: 5
- Host Atoms: 11627
- Map Details:
  - Edges: 8
  - Min Dummy Atoms: 3
  - Max Dummy Atoms: 54
  - Mean Dummy Atoms: 33.9
  - Median Dummy Atoms: 37.5

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 4.64 Hours
- Total Nanoseconds Simulated: 1638.00
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
