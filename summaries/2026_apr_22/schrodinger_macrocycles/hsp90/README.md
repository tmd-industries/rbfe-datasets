# Hsp90 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.68
- RMSE: 0.79
- R²: 0.81
- Kendall 𝜏: 0.64
- Spearman ρ: 0.84

## System Details
- Ligands: 10
- Host Atoms: 3366
- Map Details:
  - Edges: 17
  - Min Dummy Atoms: 7
  - Max Dummy Atoms: 31
  - Mean Dummy Atoms: 19.2
  - Median Dummy Atoms: 21.0

## Simulation Details
- TMD Sha: [4a502e5c9bd790faf3166193240a2d0abd78c75b](https://github.com/tmd-industries/tmd/tree/4a502e5c9bd790faf3166193240a2d0abd78c75b)
- GPU: RTX 5090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 4.84 Hours
- Average Time Per Edge: 0.28 Hours
- Total Nanoseconds Simulated: 3297.20
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
