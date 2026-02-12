# Btk Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.56
- RMSE: 1.78
- R²: 0.71
- Kendall 𝜏: 0.60
- Spearman ρ: 0.71

## System Details
- Ligands: 6
- Host Atoms: 4386
- Map Details:
  - Edges: 10
  - Min Dummy Atoms: 5
  - Max Dummy Atoms: 16
  - Mean Dummy Atoms: 11.3
  - Median Dummy Atoms: 11.5

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 3.45 Hours
- Average Time Per Edge: 0.35 Hours
- Total Nanoseconds Simulated: 1384.00
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
