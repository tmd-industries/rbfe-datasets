# Taf12 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.73
- RMSE: 0.88
- R²: 0.02
- Kendall 𝜏: 0.07
- Spearman ρ: 0.14

## System Details
- Ligands: 8
- Host Atoms: 2177
- Map Details:
  - Edges: 13
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 8
  - Mean Dummy Atoms: 4.2
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 2.03 Hours
- Average Time Per Edge: 0.16 Hours
- Total Nanoseconds Simulated: 978.60
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
