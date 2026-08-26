# Eg5 Map Charge 1

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.12
- RMSE: 1.47
- R²: 0.07
- Kendall 𝜏: 0.21
- Spearman ρ: 0.26

## System Details
- Ligands: 19
- Host Atoms: 5906
- Map Details:
  - Edges: 29
  - Min Dummy Atoms: 5
  - Max Dummy Atoms: 36
  - Mean Dummy Atoms: 18.3
  - Median Dummy Atoms: 20.0

## Simulation Details
- TMD Sha: [c000e4ca8782afb02dc29c798166a1f46edca6af](https://github.com/tmd-industries/tmd/tree/c000e4ca8782afb02dc29c798166a1f46edca6af)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 4.84 Hours
- Average Time Per Edge: 0.17 Hours
- Total Nanoseconds Simulated: 4760.40
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
