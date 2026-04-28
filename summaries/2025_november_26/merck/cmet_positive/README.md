# Cmet Positive Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.59
- RMSE: 1.84
- R²: 0.73
- Kendall 𝜏: 0.77
- Spearman ρ: 0.92

## System Details
- Ligands: 12
- Host Atoms: 4580
- Map Details:
  - Edges: 20
  - Min Dummy Atoms: 10
  - Max Dummy Atoms: 43
  - Mean Dummy Atoms: 24.6
  - Median Dummy Atoms: 23.0

## Simulation Details
- TMD Sha: [963cb9609cdaf2ee1d8a570c06ea4f70ccede326](https://github.com/tmd-industries/tmd/tree/963cb9609cdaf2ee1d8a570c06ea4f70ccede326)
- GPU: RTX 4090
- MPS Processes: 13
- Total Wallclock Time: 8.93 Hours
- Total Nanoseconds Simulated: 3558.50
- TMD Forcefield: smirnoff_2_2_1_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
