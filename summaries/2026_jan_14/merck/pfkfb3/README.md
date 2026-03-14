# Pfkfb3 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.87
- RMSE: 1.14
- R²: 0.34
- Kendall 𝜏: 0.42
- Spearman ρ: 0.59

## System Details
- Ligands: 40
- Host Atoms: 8158
- Map Details:
  - Edges: 71
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 17
  - Mean Dummy Atoms: 4.9
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 19.28 Hours
- Average Time Per Edge: 0.27 Hours
- Total Nanoseconds Simulated: 6996.60
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
