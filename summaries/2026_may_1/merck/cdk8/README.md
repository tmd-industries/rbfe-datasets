# Cdk8 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.84
- RMSE: 2.08
- R²: 0.74
- Kendall 𝜏: 0.68
- Spearman ρ: 0.85

## System Details
- Ligands: 32
- Host Atoms: 11038
- Map Details:
  - Edges: 57
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 20
  - Mean Dummy Atoms: 10.7
  - Median Dummy Atoms: 10.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 1
- Batch Mode: True
- Total Wallclock Time: 132.89 Hours
- Average Time Per Edge: 2.33 Hours
- Total Nanoseconds Simulated: 8537.60
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
