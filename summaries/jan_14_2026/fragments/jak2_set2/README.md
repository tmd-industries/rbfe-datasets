# Jak2 Set2 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.39
- RMSE: 2.02
- R²: 0.40
- Kendall 𝜏: 0.50
- Spearman ρ: 0.67

## System Details
- Ligands: 8
- Host Atoms: 4843
- Map Details:
  - Edges: 12
  - Min Dummy Atoms: 3
  - Max Dummy Atoms: 38
  - Mean Dummy Atoms: 19.1
  - Median Dummy Atoms: 21.5

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 3.81 Hours
- Average Time Per Edge: 0.32 Hours
- Total Nanoseconds Simulated: 1698.20
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
