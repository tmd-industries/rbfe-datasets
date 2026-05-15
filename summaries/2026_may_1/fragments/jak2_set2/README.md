# Jak2 Set2 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.91
- RMSE: 2.33
- R²: 0.46
- Kendall 𝜏: 0.57
- Spearman ρ: 0.76

## System Details
- Ligands: 8
- Host Atoms: 5857
- Map Details:
  - Edges: 12
  - Min Dummy Atoms: 3
  - Max Dummy Atoms: 38
  - Mean Dummy Atoms: 19.1
  - Median Dummy Atoms: 21.5

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 1.69 Hours
- Average Time Per Edge: 0.14 Hours
- Total Nanoseconds Simulated: 1813.20
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
