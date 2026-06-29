# Hsp90 2Rings

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 20.78
- RMSE: 21.01
- R²: 0.00
- Kendall 𝜏: 0.07
- Spearman ρ: 0.09

## System Details
- Ligands: 6
- Host Atoms: 3795

## Simulation Details
- TMD Sha: [e393f948bec757f86ae1d25908107665ac16b907](https://github.com/tmd-industries/tmd/tree/e393f948bec757f86ae1d25908107665ac16b907)
- GPU: RTX 4090
- MPS Processes: 2
- Batch Mode: True
- Total Wallclock Time: 2.34 Hours
- Average Time Per Molecule: 0.39 Hours
- Total Nanoseconds Simulated: 1035.60
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
