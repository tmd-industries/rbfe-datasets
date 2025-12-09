# Syk Neutral Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.26
- RMSE: 1.52
- R²: 0.00
- Kendall 𝜏: 0.00
- Spearman ρ: -0.03

## System Details
- Ligands: 38
- Host Atoms: 4667
- Map Details:
  - Edges: 67
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 17
  - Mean Dummy Atoms: 5.7
  - Median Dummy Atoms: 4.0

## Simulation Details
- TMD Sha: [963cb9609cdaf2ee1d8a570c06ea4f70ccede326](https://github.com/tmd-industries/tmd/tree/963cb9609cdaf2ee1d8a570c06ea4f70ccede326)
- GPU: RTX 4090
- MPS Processes: 13
- Total Wallclock Time: 18.07 Hours
- Total Nanoseconds Simulated: 7358.00
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
