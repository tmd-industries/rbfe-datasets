# 3Rkz Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.83
- RMSE: 2.09
- R²: 0.17
- Kendall 𝜏: 0.24
- Spearman ρ: 0.25

## System Details
- Ligands: 7
- Host Atoms: 3289
- Map Details:
  - Edges: 12
  - Min Dummy Atoms: 8
  - Max Dummy Atoms: 39
  - Mean Dummy Atoms: 26.2
  - Median Dummy Atoms: 28.0

## Simulation Details
- TMD Sha: [4a502e5c9bd790faf3166193240a2d0abd78c75b](https://github.com/tmd-industries/tmd/tree/4a502e5c9bd790faf3166193240a2d0abd78c75b)
- GPU: RTX 5090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 3.97 Hours
- Average Time Per Edge: 0.33 Hours
- Total Nanoseconds Simulated: 2486.80
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
