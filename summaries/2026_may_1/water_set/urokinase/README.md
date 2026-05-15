# Urokinase Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.70
- RMSE: 0.78
- R²: 0.62
- Kendall 𝜏: 0.67
- Spearman ρ: 0.80

## System Details
- Ligands: 4
- Host Atoms: 4581
- Map Details:
  - Edges: 6
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 3
  - Mean Dummy Atoms: 1.8
  - Median Dummy Atoms: 2.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 0.46 Hours
- Average Time Per Edge: 0.08 Hours
- Total Nanoseconds Simulated: 495.60
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
