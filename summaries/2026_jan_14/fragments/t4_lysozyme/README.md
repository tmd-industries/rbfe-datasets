# T4 Lysozyme Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.57
- RMSE: 0.69
- R²: 0.56
- Kendall 𝜏: 0.48
- Spearman ρ: 0.69

## System Details
- Ligands: 12
- Host Atoms: 2609
- Map Details:
  - Edges: 22
  - Min Dummy Atoms: 5
  - Max Dummy Atoms: 10
  - Mean Dummy Atoms: 7.2
  - Median Dummy Atoms: 6.5

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 3.03 Hours
- Average Time Per Edge: 0.14 Hours
- Total Nanoseconds Simulated: 1626.40
- TMD Forcefield: smirnoff_2_0_0_amber_am1bcc.py
- Ligand Charges: Amber AM1BCC ELF10
- Simulation Details:
  - Seed: 614943
  - Equilibration Steps: 200000
  - Steps Per Frame: 400
  - Production Ns: 2
  - Target Overlap: 0.667
  - Water Sampling: True
  - REST: Temperature Scale 3.0
  - Local MD: Steps 390, Radius 1.2
