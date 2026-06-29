# Ciordia Retro

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 29.55
- RMSE: 29.60
- R²: 0.34
- Kendall 𝜏: 0.37
- Spearman ρ: 0.51

## System Details
- Ligands: 32
- Host Atoms: 7184

## Simulation Details
- TMD Sha: [e393f948bec757f86ae1d25908107665ac16b907](https://github.com/tmd-industries/tmd/tree/e393f948bec757f86ae1d25908107665ac16b907)
- GPU: RTX 4090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 17.15 Hours
- Average Time Per Molecule: 0.54 Hours
- Total Nanoseconds Simulated: 5889.20
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 608
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - Local MD: Steps 390, Radius 1.2
