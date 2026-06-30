# Thrombin

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 26.53
- RMSE: 26.61
- R²: 0.02
- Kendall 𝜏: -0.16
- Spearman ρ: -0.13

## System Details
- Ligands: 11
- Host Atoms: 5256

## Simulation Details
- TMD Sha: [e393f948bec757f86ae1d25908107665ac16b907](https://github.com/tmd-industries/tmd/tree/e393f948bec757f86ae1d25908107665ac16b907)
- GPU: RTX 4090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 5.27 Hours
- Average Time Per Molecule: 0.48 Hours
- Total Nanoseconds Simulated: 2129.60
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
