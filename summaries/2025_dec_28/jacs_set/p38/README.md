# P38 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.96
- RMSE: 1.20
- R²: 0.41
- Kendall 𝜏: 0.47
- Spearman ρ: 0.65

## System Details
- Ligands: 34
- Host Atoms: 5651
- Map Details:
  - Edges: 67
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 17
  - Mean Dummy Atoms: 6.9
  - Median Dummy Atoms: 7.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 11.87 Hours
- Total Nanoseconds Simulated: 9229.20
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
