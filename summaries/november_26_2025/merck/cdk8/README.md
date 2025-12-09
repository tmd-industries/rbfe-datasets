# Cdk8 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.41
- RMSE: 1.63
- R²: 0.62
- Kendall 𝜏: 0.69
- Spearman ρ: 0.87

## System Details
- Ligands: 33
- Host Atoms: 6224
- Map Details:
  - Edges: 58
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 16
  - Mean Dummy Atoms: 7.7
  - Median Dummy Atoms: 8.0

## Simulation Details
- TMD Sha: [963cb9609cdaf2ee1d8a570c06ea4f70ccede326](https://github.com/tmd-industries/tmd/tree/963cb9609cdaf2ee1d8a570c06ea4f70ccede326)
- GPU: RTX 4090
- MPS Processes: 13
- Total Wallclock Time: 20.72 Hours
- Total Nanoseconds Simulated: 7716.00
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
