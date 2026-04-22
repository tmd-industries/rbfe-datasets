# 2Ep9 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.53
- RMSE: 1.85
- R²: 0.00
- Kendall 𝜏: 0.33
- Spearman ρ: 0.40

## System Details
- Ligands: 4
- Host Atoms: 4374
- Map Details:
  - Edges: 6
  - Min Dummy Atoms: 3
  - Max Dummy Atoms: 14
  - Mean Dummy Atoms: 10.2
  - Median Dummy Atoms: 11.5

## Simulation Details
- TMD Sha: [4a502e5c9bd790faf3166193240a2d0abd78c75b](https://github.com/tmd-industries/tmd/tree/4a502e5c9bd790faf3166193240a2d0abd78c75b)
- GPU: RTX 5090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 1.64 Hours
- Average Time Per Edge: 0.27 Hours
- Total Nanoseconds Simulated: 1074.40
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 421
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
