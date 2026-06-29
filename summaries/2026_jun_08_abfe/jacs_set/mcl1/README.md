# Mcl1

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 21.36
- RMSE: 21.54
- R²: 0.09
- Kendall 𝜏: 0.14
- Spearman ρ: 0.23

## System Details
- Ligands: 42
- Host Atoms: 2542

## Simulation Details
- TMD Sha: [e393f948bec757f86ae1d25908107665ac16b907](https://github.com/tmd-industries/tmd/tree/e393f948bec757f86ae1d25908107665ac16b907)
- GPU: RTX 4090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 16.78 Hours
- Average Time Per Molecule: 0.40 Hours
- Total Nanoseconds Simulated: 7813.20
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
