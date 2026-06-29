# Jak2 Set2

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 18.95
- RMSE: 19.15
- R²: 0.40
- Kendall 𝜏: 0.57
- Spearman ρ: 0.74

## System Details
- Ligands: 8
- Host Atoms: 5857

## Simulation Details
- TMD Sha: [e393f948bec757f86ae1d25908107665ac16b907](https://github.com/tmd-industries/tmd/tree/e393f948bec757f86ae1d25908107665ac16b907)
- GPU: RTX 4090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 3.69 Hours
- Average Time Per Molecule: 0.46 Hours
- Total Nanoseconds Simulated: 1412.80
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
