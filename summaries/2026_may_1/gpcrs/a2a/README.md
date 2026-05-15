# A2A Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.43
- RMSE: 1.95
- R²: 0.59
- Kendall 𝜏: 0.56
- Spearman ρ: 0.75

## System Details
- Ligands: 25
- Host Atoms: 4651
- Map Details:
  - Edges: 41
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 8
  - Mean Dummy Atoms: 3.4
  - Median Dummy Atoms: 3.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 8.08 Hours
- Average Time Per Edge: 0.20 Hours
- Total Nanoseconds Simulated: 3073.60
- TMD Forcefield: smirnoff_2_0_0_amber_am1ccc_amber14.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 501
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
