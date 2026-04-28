# Galectin Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.70
- RMSE: 0.94
- R²: 0.56
- Kendall 𝜏: 0.49
- Spearman ρ: 0.69

## System Details
- Ligands: 26
- Host Atoms: 2225
- Map Details:
  - Edges: 45
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 15
  - Mean Dummy Atoms: 4.4
  - Median Dummy Atoms: 4.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 7.71 Hours
- Average Time Per Edge: 0.17 Hours
- Total Nanoseconds Simulated: 4006.40
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
