# Jak2 Set1 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.72
- RMSE: 0.87
- R²: 0.62
- Kendall 𝜏: 0.42
- Spearman ρ: 0.59

## System Details
- Ligands: 10
- Host Atoms: 4824
- Map Details:
  - Edges: 17
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 12
  - Mean Dummy Atoms: 7.0
  - Median Dummy Atoms: 8.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 3.80 Hours
- Average Time Per Edge: 0.22 Hours
- Total Nanoseconds Simulated: 1716.80
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
