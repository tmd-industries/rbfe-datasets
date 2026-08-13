# P38 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.98
- RMSE: 1.27
- R²: 0.52
- Kendall 𝜏: 0.52
- Spearman ρ: 0.70

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
- TMD Sha: [8f0552287cd876f4ebb7cf42b46585074fd2ef9c](https://github.com/tmd-industries/tmd/tree/8f0552287cd876f4ebb7cf42b46585074fd2ef9c)
- GPU: RTX 4090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 14.41 Hours
- Average Time Per Edge: 0.24 Hours
- Total Nanoseconds Simulated: 7974.08
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 814
  - Timestep (femptoseconds): 4.0
  - Equilibration Steps: 125000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
