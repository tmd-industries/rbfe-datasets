# Renin Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.37
- RMSE: 1.76
- R²: 0.27
- Kendall 𝜏: 0.36
- Spearman ρ: 0.53

## System Details
- Ligands: 29
- Host Atoms: 5321
- Map Details:
  - Edges: 56
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 24
  - Mean Dummy Atoms: 9.6
  - Median Dummy Atoms: 7.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 6.45 Hours
- Average Time Per Edge: 0.12 Hours
- Total Nanoseconds Simulated: 6605.60
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
