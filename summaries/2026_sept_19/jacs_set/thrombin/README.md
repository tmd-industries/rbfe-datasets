# Thrombin Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.59
- RMSE: 0.82
- R²: 0.90
- Kendall 𝜏: 0.78
- Spearman ρ: 0.90

## System Details
- Ligands: 11
- Host Atoms: 5256
- Map Details:
  - Edges: 19
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 6
  - Mean Dummy Atoms: 2.9
  - Median Dummy Atoms: 3.0

## Simulation Details
- TMD Sha: [c4fbbffa1e2473414827fd473bca80feaa9865bb](https://github.com/tmd-industries/tmd/tree/c4fbbffa1e2473414827fd473bca80feaa9865bb)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 1.08 Hours
- Average Time Per Edge: 0.06 Hours
- Total Nanoseconds Simulated: 1268.80
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
