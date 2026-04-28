# Mcl1 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.98
- RMSE: 1.31
- R²: 0.54
- Kendall 𝜏: 0.57
- Spearman ρ: 0.75

## System Details
- Ligands: 42
- Host Atoms: 2542
- Map Details:
  - Edges: 73
  - Min Dummy Atoms: 1
  - Max Dummy Atoms: 15
  - Mean Dummy Atoms: 5.7
  - Median Dummy Atoms: 5.0

## Simulation Details
- TMD Sha: [d90311ea6b8fd4d5bddae32b2925ef72d57ec45e](https://github.com/tmd-industries/tmd/tree/d90311ea6b8fd4d5bddae32b2925ef72d57ec45e)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 13.77 Hours
- Average Time Per Edge: 0.19 Hours
- Total Nanoseconds Simulated: 7257.00
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 4115
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
