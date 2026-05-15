# Hsp90 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.73
- RMSE: 0.91
- R²: 0.78
- Kendall 𝜏: 0.69
- Spearman ρ: 0.83

## System Details
- Ligands: 10
- Host Atoms: 3366
- Map Details:
  - Edges: 17
  - Min Dummy Atoms: 7
  - Max Dummy Atoms: 31
  - Mean Dummy Atoms: 19.2
  - Median Dummy Atoms: 21.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 2.79 Hours
- Average Time Per Edge: 0.16 Hours
- Total Nanoseconds Simulated: 3319.20
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
