# Hiv1 Protease Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.37
- RMSE: 1.72
- R²: 0.01
- Kendall 𝜏: 0.09
- Spearman ρ: 0.08

## System Details
- Ligands: 13
- Host Atoms: 3626
- Map Details:
  - Edges: 22
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 15
  - Mean Dummy Atoms: 7.5
  - Median Dummy Atoms: 7.5

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 2.56 Hours
- Average Time Per Edge: 0.12 Hours
- Total Nanoseconds Simulated: 2334.80
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
