# Pfkfb3 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.08
- RMSE: 1.42
- R²: 0.34
- Kendall 𝜏: 0.42
- Spearman ρ: 0.62

## System Details
- Ligands: 40
- Host Atoms: 8158
- Map Details:
  - Edges: 77
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 17
  - Mean Dummy Atoms: 4.9
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [c4fbbffa1e2473414827fd473bca80feaa9865bb](https://github.com/tmd-industries/tmd/tree/c4fbbffa1e2473414827fd473bca80feaa9865bb)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 10.98 Hours
- Average Time Per Edge: 0.14 Hours
- Total Nanoseconds Simulated: 8210.80
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
