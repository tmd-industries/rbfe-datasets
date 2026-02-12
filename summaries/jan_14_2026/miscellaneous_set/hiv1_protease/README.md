# Hiv1 Protease Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.06
- RMSE: 1.25
- R²: 0.02
- Kendall 𝜏: 0.12
- Spearman ρ: 0.16

## System Details
- Ligands: 13
- Host Atoms: 3128
- Map Details:
  - Edges: 22
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 15
  - Mean Dummy Atoms: 7.5
  - Median Dummy Atoms: 7.5

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 5.29 Hours
- Average Time Per Edge: 0.24 Hours
- Total Nanoseconds Simulated: 2333.60
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
