# Eg5 Map Charge 0

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.88
- RMSE: 1.09
- R²: 0.72
- Kendall 𝜏: 0.54
- Spearman ρ: 0.74

## System Details
- Ligands: 9
- Host Atoms: 5906
- Map Details:
  - Edges: 15
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 27
  - Mean Dummy Atoms: 11.9
  - Median Dummy Atoms: 8.0

## Simulation Details
- TMD Sha: [7bfbc5dc44e1a1030ec36835a3e6d1725546d398](https://github.com/tmd-industries/tmd/tree/7bfbc5dc44e1a1030ec36835a3e6d1725546d398)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 1.83 Hours
- Average Time Per Edge: 0.12 Hours
- Total Nanoseconds Simulated: 1848.40
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
