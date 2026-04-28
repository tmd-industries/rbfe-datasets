# Faah Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.98
- RMSE: 1.19
- R²: 0.56
- Kendall 𝜏: 0.32
- Spearman ρ: 0.44

## System Details
- Ligands: 24
- Host Atoms: 8440
- Map Details:
  - Edges: 41
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 10
  - Mean Dummy Atoms: 6.0
  - Median Dummy Atoms: 6.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 9.69 Hours
- Average Time Per Edge: 0.24 Hours
- Total Nanoseconds Simulated: 3738.80
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
