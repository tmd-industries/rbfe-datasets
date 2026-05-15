# Bace1 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.75
- RMSE: 1.90
- R²: 0.69
- Kendall 𝜏: 1.00
- Spearman ρ: 1.00

## System Details
- Ligands: 3
- Host Atoms: 6106
- Map Details:
  - Edges: 3
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 10
  - Mean Dummy Atoms: 6.7
  - Median Dummy Atoms: 9.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 0.48 Hours
- Average Time Per Edge: 0.16 Hours
- Total Nanoseconds Simulated: 388.40
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
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
