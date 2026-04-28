# Bace P3 Arg368 In Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.16
- RMSE: 1.44
- R²: 0.34
- Kendall 𝜏: 0.45
- Spearman ρ: 0.58

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
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 15.82 Hours
- Average Time Per Edge: 0.47 Hours
- Total Nanoseconds Simulated: 4552.40
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 4589
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
