# Galectin

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 21.64
- RMSE: 21.67
- R²: 0.38
- Kendall 𝜏: 0.37
- Spearman ρ: 0.50

## System Details
- Ligands: 26
- Host Atoms: 2712

## Simulation Details
- TMD Sha: [e393f948bec757f86ae1d25908107665ac16b907](https://github.com/tmd-industries/tmd/tree/e393f948bec757f86ae1d25908107665ac16b907)
- GPU: RTX 4090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 10.29 Hours
- Average Time Per Molecule: 0.40 Hours
- Total Nanoseconds Simulated: 4953.60
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
