# Hne Map Charge 0

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.70
- RMSE: 0.91
- R²: 0.74
- Kendall 𝜏: 0.76
- Spearman ρ: 0.89

## System Details
- Ligands: 14
- Host Atoms: 3804
- Map Details:
  - Edges: 23
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 22
  - Mean Dummy Atoms: 6.7
  - Median Dummy Atoms: 4.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 3.67 Hours
- Total Nanoseconds Simulated: 2951.40
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
