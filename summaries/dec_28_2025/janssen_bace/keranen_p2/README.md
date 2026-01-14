# Keranen P2 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.31
- RMSE: 0.39
- R²: 0.23
- Kendall 𝜏: 0.40
- Spearman ρ: 0.51

## System Details
- Ligands: 12
- Host Atoms: 6003
- Map Details:
  - Edges: 20
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 14
  - Mean Dummy Atoms: 6.3
  - Median Dummy Atoms: 6.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 2.57 Hours
- Total Nanoseconds Simulated: 2113.80
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
