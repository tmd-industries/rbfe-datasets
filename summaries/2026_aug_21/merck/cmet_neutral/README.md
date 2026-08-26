# Cmet Map Charge 0

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.06
- RMSE: 1.28
- R²: 0.83
- Kendall 𝜏: 0.72
- Spearman ρ: 0.87

## System Details
- Ligands: 12
- Host Atoms: 4977
- Map Details:
  - Edges: 19
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 36
  - Mean Dummy Atoms: 9.9
  - Median Dummy Atoms: 6.0

## Simulation Details
- TMD Sha: [c000e4ca8782afb02dc29c798166a1f46edca6af](https://github.com/tmd-industries/tmd/tree/c000e4ca8782afb02dc29c798166a1f46edca6af)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 2.13 Hours
- Average Time Per Edge: 0.11 Hours
- Total Nanoseconds Simulated: 2369.20
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 618
  - Timestep (femptoseconds): 4.0
  - Equilibration Steps: 125000
  - Steps Per Frame: 250
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 244, Radius 1.2
