# Bace P3 Arg368 In Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.62
- RMSE: 1.84
- R²: 0.16
- Kendall 𝜏: 0.22
- Spearman ρ: 0.32

## System Details
- Ligands: 21
- Host Atoms: 6894
- Map Details:
  - Edges: 34
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 11
  - Mean Dummy Atoms: 6.8
  - Median Dummy Atoms: 7.5

## Simulation Details
- TMD Sha: [7bfbc5dc44e1a1030ec36835a3e6d1725546d398](https://github.com/tmd-industries/tmd/tree/7bfbc5dc44e1a1030ec36835a3e6d1725546d398)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 4.77 Hours
- Average Time Per Edge: 0.14 Hours
- Total Nanoseconds Simulated: 4610.40
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
