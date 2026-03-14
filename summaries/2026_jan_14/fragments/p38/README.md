# P38 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.98
- RMSE: 1.06
- R²: 0.63
- Kendall 𝜏: 0.60
- Spearman ρ: 0.77

## System Details
- Ligands: 6
- Host Atoms: 5667
- Map Details:
  - Edges: 10
  - Min Dummy Atoms: 4
  - Max Dummy Atoms: 32
  - Mean Dummy Atoms: 19.6
  - Median Dummy Atoms: 20.5

## Simulation Details
- TMD Sha: [be54a617e0ca39fba04baa293394cc65f12327f5](https://github.com/tmd-industries/tmd/tree/be54a617e0ca39fba04baa293394cc65f12327f5)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 3.47 Hours
- Average Time Per Edge: 0.35 Hours
- Total Nanoseconds Simulated: 1325.00
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
