# Hsp90 Single Ring Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.81
- RMSE: 0.99
- R²: 0.18
- Kendall 𝜏: 0.39
- Spearman ρ: 0.58

## System Details
- Ligands: 7
- Host Atoms: 3282
- Map Details:
  - Edges: 11
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 5
  - Mean Dummy Atoms: 3.4
  - Median Dummy Atoms: 4.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 1.72 Hours
- Average Time Per Edge: 0.16 Hours
- Total Nanoseconds Simulated: 848.40
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
