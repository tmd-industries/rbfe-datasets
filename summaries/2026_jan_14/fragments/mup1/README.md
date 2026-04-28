# Mup1 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.40
- RMSE: 0.49
- R²: 0.98
- Kendall 𝜏: 1.00
- Spearman ρ: 1.00

## System Details
- Ligands: 6
- Host Atoms: 2486
- Map Details:
  - Edges: 10
  - Min Dummy Atoms: 5
  - Max Dummy Atoms: 10
  - Mean Dummy Atoms: 7.8
  - Median Dummy Atoms: 9.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 1.40 Hours
- Average Time Per Edge: 0.14 Hours
- Total Nanoseconds Simulated: 719.60
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
