# Thrombin Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.78
- RMSE: 0.98
- R²: 0.88
- Kendall 𝜏: 0.82
- Spearman ρ: 0.92

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
- TMD Sha: [c000e4ca8782afb02dc29c798166a1f46edca6af](https://github.com/tmd-industries/tmd/tree/c000e4ca8782afb02dc29c798166a1f46edca6af)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 1.12 Hours
- Average Time Per Edge: 0.06 Hours
- Total Nanoseconds Simulated: 1256.40
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
