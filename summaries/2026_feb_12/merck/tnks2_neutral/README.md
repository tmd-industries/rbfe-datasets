# Tnks2 Map Charge 0

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.57
- RMSE: 0.74
- R²: 0.55
- Kendall 𝜏: 0.42
- Spearman ρ: 0.55

## System Details
- Ligands: 21
- Host Atoms: 4097
- Map Details:
  - Edges: 33
  - Min Dummy Atoms: 0
  - Max Dummy Atoms: 14
  - Mean Dummy Atoms: 4.5
  - Median Dummy Atoms: 3.0

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 2.46 Hours
- Average Time Per Edge: 0.07 Hours
- Total Nanoseconds Simulated: 2460.80
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 411
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
