# P38 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.10
- RMSE: 1.37
- R²: 0.83
- Kendall 𝜏: 0.60
- Spearman ρ: 0.77

## System Details
- Ligands: 6
- Host Atoms: 7065
- Map Details:
  - Edges: 10
  - Min Dummy Atoms: 4
  - Max Dummy Atoms: 32
  - Mean Dummy Atoms: 19.6
  - Median Dummy Atoms: 20.5

## Simulation Details
- TMD Sha: [7bfbc5dc44e1a1030ec36835a3e6d1725546d398](https://github.com/tmd-industries/tmd/tree/7bfbc5dc44e1a1030ec36835a3e6d1725546d398)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 1.62 Hours
- Average Time Per Edge: 0.16 Hours
- Total Nanoseconds Simulated: 1437.20
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
