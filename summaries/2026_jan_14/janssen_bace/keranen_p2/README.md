# Keranen P2 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.59
- RMSE: 0.66
- R²: 0.00
- Kendall 𝜏: 0.02
- Spearman ρ: 0.02

## System Details
- Ligands: 12
- Host Atoms: 6003
- Map Details:
  - Edges: 19
  - Min Dummy Atoms: 3
  - Max Dummy Atoms: 17
  - Mean Dummy Atoms: 8.6
  - Median Dummy Atoms: 9.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 4.49 Hours
- Average Time Per Edge: 0.24 Hours
- Total Nanoseconds Simulated: 1767.60
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 614943
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
