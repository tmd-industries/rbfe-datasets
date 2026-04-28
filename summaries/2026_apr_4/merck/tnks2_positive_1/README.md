# Tnks2 Map Charge 1

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.84
- RMSE: 0.95
- R²: 0.01
- Kendall 𝜏: 0.07
- Spearman ρ: 0.03

## System Details
- Ligands: 6
- Host Atoms: 4097
- Map Details:
  - Edges: 9
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 8
  - Mean Dummy Atoms: 4.3
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [3807bc3316f1fc03f6fb7e120b900339116f2427](https://github.com/tmd-industries/tmd/tree/3807bc3316f1fc03f6fb7e120b900339116f2427)
- GPU: RTX 4090
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 2.29 Hours
- Average Time Per Edge: 0.25 Hours
- Total Nanoseconds Simulated: 864.40
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
