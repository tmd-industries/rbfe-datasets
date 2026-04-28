# Hsp90 Woodhead Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.94
- RMSE: 1.04
- R²: 0.67
- Kendall 𝜏: 0.33
- Spearman ρ: 0.60

## System Details
- Ligands: 4
- Host Atoms: 4042
- Map Details:
  - Edges: 6
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 9
  - Mean Dummy Atoms: 5.3
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4](https://github.com/tmd-industries/tmd/tree/b6fbbb7d2cbfc8e9c5e14c767131c7183da0bcf4)
- GPU: RTX 5090, RTX 5080
- MPS Processes: 12
- Total Wallclock Time: 0.98 Hours
- Average Time Per Edge: 0.16 Hours
- Total Nanoseconds Simulated: 624.00
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
