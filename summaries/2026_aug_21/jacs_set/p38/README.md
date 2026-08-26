# P38 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.99
- RMSE: 1.22
- R²: 0.37
- Kendall 𝜏: 0.40
- Spearman ρ: 0.60

## System Details
- Ligands: 34
- Host Atoms: 6680
- Map Details:
  - Edges: 61
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 21
  - Mean Dummy Atoms: 9.7
  - Median Dummy Atoms: 10.0

## Simulation Details
- TMD Sha: [c000e4ca8782afb02dc29c798166a1f46edca6af](https://github.com/tmd-industries/tmd/tree/c000e4ca8782afb02dc29c798166a1f46edca6af)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 7.66 Hours
- Average Time Per Edge: 0.13 Hours
- Total Nanoseconds Simulated: 7723.60
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
