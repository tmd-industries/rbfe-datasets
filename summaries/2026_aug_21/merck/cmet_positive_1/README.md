# Cmet Map Charge 1

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.26
- RMSE: 1.69
- R²: 0.43
- Kendall 𝜏: 0.68
- Spearman ρ: 0.76

## System Details
- Ligands: 12
- Host Atoms: 4977
- Map Details:
  - Edges: 20
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 52
  - Mean Dummy Atoms: 19.8
  - Median Dummy Atoms: 16.5

## Simulation Details
- TMD Sha: [c000e4ca8782afb02dc29c798166a1f46edca6af](https://github.com/tmd-industries/tmd/tree/c000e4ca8782afb02dc29c798166a1f46edca6af)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 3.01 Hours
- Average Time Per Edge: 0.15 Hours
- Total Nanoseconds Simulated: 3254.80
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
