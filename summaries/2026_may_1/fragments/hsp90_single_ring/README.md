# Hsp90 Single Ring Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.70
- RMSE: 0.85
- R²: 0.23
- Kendall 𝜏: 0.59
- Spearman ρ: 0.70

## System Details
- Ligands: 7
- Host Atoms: 3795
- Map Details:
  - Edges: 11
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 5
  - Mean Dummy Atoms: 3.4
  - Median Dummy Atoms: 4.0

## Simulation Details
- TMD Sha: [10dc832c303aa794b47663a4da8d114ca6eea151](https://github.com/tmd-industries/tmd/tree/10dc832c303aa794b47663a4da8d114ca6eea151)
- GPU: RTX 5090, RTX 50080
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 0.80 Hours
- Average Time Per Edge: 0.07 Hours
- Total Nanoseconds Simulated: 1005.60
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
