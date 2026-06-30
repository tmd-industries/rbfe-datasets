# Syk

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 22.13
- RMSE: 22.22
- R²: 0.04
- Kendall 𝜏: 0.13
- Spearman ρ: 0.19

## System Details
- Ligands: 46
- Host Atoms: 4558

## Simulation Details
- TMD Sha: [e393f948bec757f86ae1d25908107665ac16b907](https://github.com/tmd-industries/tmd/tree/e393f948bec757f86ae1d25908107665ac16b907)
- GPU: RTX 4090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 22.71 Hours
- Average Time Per Molecule: 0.49 Hours
- Total Nanoseconds Simulated: 8623.60
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
