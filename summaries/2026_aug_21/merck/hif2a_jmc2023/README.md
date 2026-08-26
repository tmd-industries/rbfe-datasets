# Hif2A Jmc2023 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 2.39
- RMSE: 2.61
- R²: 0.52
- Kendall 𝜏: 0.56
- Spearman ρ: 0.75

## System Details
- Ligands: 38
- Host Atoms: 1937
- Map Details:
  - Edges: 62
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 15
  - Mean Dummy Atoms: 5.8
  - Median Dummy Atoms: 5.5

## Simulation Details
- TMD Sha: [c000e4ca8782afb02dc29c798166a1f46edca6af](https://github.com/tmd-industries/tmd/tree/c000e4ca8782afb02dc29c798166a1f46edca6af)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 3.82 Hours
- Average Time Per Edge: 0.06 Hours
- Total Nanoseconds Simulated: 6351.20
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
