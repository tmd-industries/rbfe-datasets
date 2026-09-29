# Ptp1B Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.32
- RMSE: 2.15
- R²: 0.31
- Kendall 𝜏: 0.56
- Spearman ρ: 0.67

## System Details
- Ligands: 23
- Host Atoms: 5488
- Map Details:
  - Edges: 41
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 30
  - Mean Dummy Atoms: 11.6
  - Median Dummy Atoms: 12.0

## Simulation Details
- TMD Sha: [c4fbbffa1e2473414827fd473bca80feaa9865bb](https://github.com/tmd-industries/tmd/tree/c4fbbffa1e2473414827fd473bca80feaa9865bb)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 4.92 Hours
- Average Time Per Edge: 0.12 Hours
- Total Nanoseconds Simulated: 5598.80
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
