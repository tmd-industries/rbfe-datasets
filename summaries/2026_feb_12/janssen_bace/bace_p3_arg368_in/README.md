# Bace P3 Arg368 In Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.96
- RMSE: 1.23
- R²: 0.50
- Kendall 𝜏: 0.54
- Spearman ρ: 0.72

## System Details
- Ligands: 21
- Host Atoms: 6894
- Map Details:
  - Edges: 32
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 11
  - Mean Dummy Atoms: 6.9
  - Median Dummy Atoms: 7.0

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 4.71 Hours
- Average Time Per Edge: 0.15 Hours
- Total Nanoseconds Simulated: 4261.40
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
