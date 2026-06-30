# Ephx2

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 26.29
- RMSE: 26.98
- R²: 0.53
- Kendall 𝜏: 0.33
- Spearman ρ: 0.40

## System Details
- Ligands: 4
- Host Atoms: 5004

## Simulation Details
- TMD Sha: [e393f948bec757f86ae1d25908107665ac16b907](https://github.com/tmd-industries/tmd/tree/e393f948bec757f86ae1d25908107665ac16b907)
- GPU: RTX 4090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 1.78 Hours
- Average Time Per Molecule: 0.45 Hours
- Total Nanoseconds Simulated: 722.40
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
