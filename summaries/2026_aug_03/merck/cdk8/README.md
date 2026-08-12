# Cdk8 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.79
- RMSE: 2.18
- R²: 0.66
- Kendall 𝜏: 0.65
- Spearman ρ: 0.84

## System Details
- Ligands: 32
- Host Atoms: 11038
- Map Details:
  - Edges: 55
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 20
  - Mean Dummy Atoms: 11.2
  - Median Dummy Atoms: 11.0

## Simulation Details
- TMD Sha: [8f0552287cd876f4ebb7cf42b46585074fd2ef9c](https://github.com/tmd-industries/tmd/tree/8f0552287cd876f4ebb7cf42b46585074fd2ef9c)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 19.36 Hours
- Average Time Per Edge: 0.35 Hours
- Total Nanoseconds Simulated: 7865.20
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 814
  - Timestep (femptoseconds): 4.0
  - Equilibration Steps: 125000
  - Steps Per Frame: 250
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 244, Radius 1.2
