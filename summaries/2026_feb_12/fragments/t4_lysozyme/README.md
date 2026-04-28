# T4 Lysozyme Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.53
- RMSE: 0.68
- R²: 0.57
- Kendall 𝜏: 0.48
- Spearman ρ: 0.69

## System Details
- Ligands: 12
- Host Atoms: 2609
- Map Details:
  - Edges: 22
  - Min Dummy Atoms: 5
  - Max Dummy Atoms: 10
  - Mean Dummy Atoms: 7.2
  - Median Dummy Atoms: 6.5

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 1.55 Hours
- Average Time Per Edge: 0.07 Hours
- Total Nanoseconds Simulated: 1633.00
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
