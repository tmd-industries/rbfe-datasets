# 3Rkz Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.35
- RMSE: 1.52
- R²: 0.54
- Kendall 𝜏: 0.52
- Spearman ρ: 0.61

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
- TMD Sha: [https://github.com/tmd-industries/tmd/pull/132/commits/2651d87e17c5e18fe8f0dc9c26a7007c2c730053](https://github.com/tmd-industries/tmd/tree/https://github.com/tmd-industries/tmd/pull/132/commits/2651d87e17c5e18fe8f0dc9c26a7007c2c730053)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 2.37 Hours
- Average Time Per Edge: 0.20 Hours
- Total Nanoseconds Simulated: 2532.00
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 604
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
