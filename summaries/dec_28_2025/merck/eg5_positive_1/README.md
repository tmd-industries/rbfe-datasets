# Eg5 Map Charge 1

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.05
- RMSE: 1.21
- R²: 0.12
- Kendall 𝜏: 0.24
- Spearman ρ: 0.34

## System Details
- Ligands: 19
- Host Atoms: 5474
- Map Details:
  - Edges: 33
  - Min Dummy Atoms: 3
  - Max Dummy Atoms: 25
  - Mean Dummy Atoms: 12.3
  - Median Dummy Atoms: 12.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 6.77 Hours
- Total Nanoseconds Simulated: 5478.80
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
