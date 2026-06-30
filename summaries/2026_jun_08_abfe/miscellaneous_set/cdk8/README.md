# Cdk8

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 25.69
- RMSE: 25.76
- R²: 0.17
- Kendall 𝜏: 0.16
- Spearman ρ: 0.27

## System Details
- Ligands: 10
- Host Atoms: 11038

## Simulation Details
- TMD Sha: [e393f948bec757f86ae1d25908107665ac16b907](https://github.com/tmd-industries/tmd/tree/e393f948bec757f86ae1d25908107665ac16b907)
- GPU: RTX 4090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 8.04 Hours
- Average Time Per Molecule: 0.80 Hours
- Total Nanoseconds Simulated: 1517.60
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
