# Hsp90 2Rings Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.13
- RMSE: 1.38
- R²: 0.29
- Kendall 𝜏: 0.33
- Spearman ρ: 0.43

## System Details
- Ligands: 6
- Host Atoms: 3282
- Map Details:
  - Edges: 9
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 6
  - Mean Dummy Atoms: 3.3
  - Median Dummy Atoms: 3.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 1.30 Hours
- Average Time Per Edge: 0.14 Hours
- Total Nanoseconds Simulated: 633.20
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
