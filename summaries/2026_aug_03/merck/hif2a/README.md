# Hif2A Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 2.40
- RMSE: 2.70
- R²: 0.05
- Kendall 𝜏: 0.11
- Spearman ρ: 0.15

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
- TMD Sha: [8f0552287cd876f4ebb7cf42b46585074fd2ef9c](https://github.com/tmd-industries/tmd/tree/8f0552287cd876f4ebb7cf42b46585074fd2ef9c)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 3.82 Hours
- Average Time Per Edge: 0.06 Hours
- Total Nanoseconds Simulated: 7328.40
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
