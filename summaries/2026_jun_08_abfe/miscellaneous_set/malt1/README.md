# Malt1

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 28.65
- RMSE: 28.77
- R²: 0.26
- Kendall 𝜏: 0.38
- Spearman ρ: 0.52

## System Details
- Ligands: 16
- Host Atoms: 6224

## Simulation Details
- TMD Sha: [e393f948bec757f86ae1d25908107665ac16b907](https://github.com/tmd-industries/tmd/tree/e393f948bec757f86ae1d25908107665ac16b907)
- GPU: RTX 4090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 11.17 Hours
- Average Time Per Molecule: 0.70 Hours
- Total Nanoseconds Simulated: 2678.80
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
