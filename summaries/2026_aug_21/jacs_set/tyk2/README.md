# Tyk2 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.79
- RMSE: 1.09
- R²: 0.46
- Kendall 𝜏: 0.47
- Spearman ρ: 0.54

## System Details
- Ligands: 16
- Host Atoms: 4670
- Map Details:
  - Edges: 27
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 13
  - Mean Dummy Atoms: 6.7
  - Median Dummy Atoms: 8.0

## Simulation Details
- TMD Sha: [c000e4ca8782afb02dc29c798166a1f46edca6af](https://github.com/tmd-industries/tmd/tree/c000e4ca8782afb02dc29c798166a1f46edca6af)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 2.41 Hours
- Average Time Per Edge: 0.09 Hours
- Total Nanoseconds Simulated: 2721.20
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
