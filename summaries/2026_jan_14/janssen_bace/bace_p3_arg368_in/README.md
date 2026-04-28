# Bace P3 Arg368 In Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.22
- RMSE: 1.49
- R²: 0.59
- Kendall 𝜏: 0.51
- Spearman ρ: 0.72

## System Details
- Ligands: 21
- Host Atoms: 6036
- Map Details:
  - Edges: 32
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 11
  - Mean Dummy Atoms: 6.9
  - Median Dummy Atoms: 7.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 10.00 Hours
- Average Time Per Edge: 0.31 Hours
- Total Nanoseconds Simulated: 4256.80
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
