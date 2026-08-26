# Hif2A Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.71
- RMSE: 2.05
- R²: 0.06
- Kendall 𝜏: 0.12
- Spearman ρ: 0.18

## System Details
- Ligands: 41
- Host Atoms: 1770
- Map Details:
  - Edges: 68
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 13
  - Mean Dummy Atoms: 5.0
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [c000e4ca8782afb02dc29c798166a1f46edca6af](https://github.com/tmd-industries/tmd/tree/c000e4ca8782afb02dc29c798166a1f46edca6af)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 4.31 Hours
- Average Time Per Edge: 0.06 Hours
- Total Nanoseconds Simulated: 7262.40
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
