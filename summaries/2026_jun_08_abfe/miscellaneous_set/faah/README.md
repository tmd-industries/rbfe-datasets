# Faah

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 27.01
- RMSE: 27.14
- R²: 0.30
- Kendall 𝜏: 0.40
- Spearman ρ: 0.56

## System Details
- Ligands: 24
- Host Atoms: 8446

## Simulation Details
- TMD Sha: [e393f948bec757f86ae1d25908107665ac16b907](https://github.com/tmd-industries/tmd/tree/e393f948bec757f86ae1d25908107665ac16b907)
- GPU: RTX 4090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 13.56 Hours
- Average Time Per Molecule: 0.57 Hours
- Total Nanoseconds Simulated: 4024.80
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
