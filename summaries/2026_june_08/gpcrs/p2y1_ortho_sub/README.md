# P2Y1 Ortho Sub Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.19
- RMSE: 1.46
- R²: 0.92
- Kendall 𝜏: 0.75
- Spearman ρ: 0.88

## System Details
- Ligands: 12
- Host Atoms: 4820
- Map Details:
  - Edges: 21
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 14
  - Mean Dummy Atoms: 6.9
  - Median Dummy Atoms: 6.0

## Simulation Details
- TMD Sha: [7bfbc5dc44e1a1030ec36835a3e6d1725546d398](https://github.com/tmd-industries/tmd/tree/7bfbc5dc44e1a1030ec36835a3e6d1725546d398)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 5.12 Hours
- Average Time Per Edge: 0.24 Hours
- Total Nanoseconds Simulated: 1986.40
- TMD Forcefield: smirnoff_2_0_0_amber_am1ccc_amber14.py
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
