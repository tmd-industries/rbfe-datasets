# Eg5 Map Charge 0

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.24
- RMSE: 1.43
- R²: 0.52
- Kendall 𝜏: 0.37
- Spearman ρ: 0.50

## System Details
- Ligands: 9
- Host Atoms: 5906
- Map Details:
  - Edges: 15
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 27
  - Mean Dummy Atoms: 11.9
  - Median Dummy Atoms: 8.0

## Simulation Details
- TMD Sha: [8f0552287cd876f4ebb7cf42b46585074fd2ef9c](https://github.com/tmd-industries/tmd/tree/8f0552287cd876f4ebb7cf42b46585074fd2ef9c)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 1.89 Hours
- Average Time Per Edge: 0.13 Hours
- Total Nanoseconds Simulated: 1843.60
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 814
  - Timestep (femptoseconds): 2.5
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
