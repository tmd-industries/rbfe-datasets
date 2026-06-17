# Hsp90 Single Ring Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.77
- RMSE: 0.94
- R²: 0.39
- Kendall 𝜏: 0.49
- Spearman ρ: 0.63

## System Details
- Ligands: 7
- Host Atoms: 3795
- Map Details:
  - Edges: 11
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 5
  - Mean Dummy Atoms: 3.4
  - Median Dummy Atoms: 4.0

## Simulation Details
- TMD Sha: [7bfbc5dc44e1a1030ec36835a3e6d1725546d398](https://github.com/tmd-industries/tmd/tree/7bfbc5dc44e1a1030ec36835a3e6d1725546d398)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 0.73 Hours
- Average Time Per Edge: 0.07 Hours
- Total Nanoseconds Simulated: 907.60
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
