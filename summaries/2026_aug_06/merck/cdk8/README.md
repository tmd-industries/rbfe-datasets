# Cdk8 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.68
- RMSE: 2.09
- R²: 0.63
- Kendall 𝜏: 0.64
- Spearman ρ: 0.83

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
- Total Wallclock Time: 21.01 Hours
- Average Time Per Edge: 0.38 Hours
- Total Nanoseconds Simulated: 7889.20
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
  - Local MD: Steps 240, Radius 1.2
