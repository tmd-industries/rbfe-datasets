# T4 Lysozyme Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.60
- RMSE: 0.75
- R²: 0.53
- Kendall 𝜏: 0.55
- Spearman ρ: 0.73

## System Details
- Ligands: 12
- Host Atoms: 2609
- Map Details:
  - Edges: 21
  - Min Dummy Atoms: 3
  - Max Dummy Atoms: 6
  - Mean Dummy Atoms: 4.3
  - Median Dummy Atoms: 3.0

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 1.86 Hours
- Total Nanoseconds Simulated: 1847.80
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 9128
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
