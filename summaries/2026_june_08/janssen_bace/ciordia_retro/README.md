# Ciordia Retro Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.01
- RMSE: 1.31
- R²: 0.62
- Kendall 𝜏: 0.59
- Spearman ρ: 0.79

## System Details
- Ligands: 32
- Host Atoms: 7184
- Map Details:
  - Edges: 55
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 17
  - Mean Dummy Atoms: 5.7
  - Median Dummy Atoms: 4.0

## Simulation Details
- TMD Sha: [7bfbc5dc44e1a1030ec36835a3e6d1725546d398](https://github.com/tmd-industries/tmd/tree/7bfbc5dc44e1a1030ec36835a3e6d1725546d398)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 5.71 Hours
- Average Time Per Edge: 0.10 Hours
- Total Nanoseconds Simulated: 5631.60
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 608
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
