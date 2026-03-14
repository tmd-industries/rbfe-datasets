# Tnks2 Neutral Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.57
- RMSE: 0.74
- R²: 0.62
- Kendall 𝜏: 0.49
- Spearman ρ: 0.64

## System Details
- Ligands: 21
- Host Atoms: 4074
- Map Details:
  - Edges: 39
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 10
  - Mean Dummy Atoms: 3.5
  - Median Dummy Atoms: 3.0

## Simulation Details
- TMD Sha: [963cb9609cdaf2ee1d8a570c06ea4f70ccede326](https://github.com/tmd-industries/tmd/tree/963cb9609cdaf2ee1d8a570c06ea4f70ccede326)
- GPU: RTX 4090
- MPS Processes: 13
- Total Wallclock Time: 7.38 Hours
- Total Nanoseconds Simulated: 3504.50
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
