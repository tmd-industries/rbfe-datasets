# Eg5 Map Charge 0

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 1.12
- RMSE: 1.23
- R²: 0.43
- Kendall 𝜏: 0.20
- Spearman ρ: 0.32

## System Details
- Ligands: 9
- Host Atoms: 5906
- Map Details:
  - Edges: 15
  - Min Dummy Atoms: 2
  - Max Dummy Atoms: 27
  - Mean Dummy Atoms: 11.9
  - Median Dummy Atoms: 8.0

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 2.02 Hours
- Average Time Per Edge: 0.13 Hours
- Total Nanoseconds Simulated: 1676.20
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
