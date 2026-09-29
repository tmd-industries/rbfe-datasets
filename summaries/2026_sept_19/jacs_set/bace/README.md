# Bace Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.24
- RMSE: 1.53
- R²: 0.16
- Kendall 𝜏: 0.25
- Spearman ρ: 0.37

## System Details
- Ligands: 36
- Host Atoms: 6101
- Map Details:
  - Edges: 61
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 12
  - Mean Dummy Atoms: 5.3
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [c4fbbffa1e2473414827fd473bca80feaa9865bb](https://github.com/tmd-industries/tmd/tree/c4fbbffa1e2473414827fd473bca80feaa9865bb)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 5.66 Hours
- Average Time Per Edge: 0.09 Hours
- Total Nanoseconds Simulated: 5835.20
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 262
  - Timestep (femptoseconds): 4.0
  - Equilibration Steps: 125000
  - Steps Per Frame: 250
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 240, Radius 1.2
