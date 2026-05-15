# P2Y1 Ortho Sub Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.06
- RMSE: 1.37
- R²: 0.90
- Kendall 𝜏: 0.75
- Spearman ρ: 0.88

## System Details
- Ligands: 12
- Host Atoms: 4820
- Map Details:
  - Edges: 21
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 14
  - Mean Dummy Atoms: 6.9
  - Median Dummy Atoms: 6.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 5.18 Hours
- Average Time Per Edge: 0.25 Hours
- Total Nanoseconds Simulated: 1997.20
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
