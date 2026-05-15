# Cdk2 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.74
- RMSE: 0.89
- R²: 0.57
- Kendall 𝜏: 0.53
- Spearman ρ: 0.73

## System Details
- Ligands: 16
- Host Atoms: 9028
- Map Details:
  - Edges: 28
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 11
  - Mean Dummy Atoms: 5.9
  - Median Dummy Atoms: 6.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 4.98 Hours
- Average Time Per Edge: 0.18 Hours
- Total Nanoseconds Simulated: 2998.00
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
