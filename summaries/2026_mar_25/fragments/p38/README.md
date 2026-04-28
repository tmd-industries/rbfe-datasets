# P38 Map

![Retrospective dG performance](dg_plot.png)

## Statistics Summary
- MUE: 0.76
- RMSE: 0.87
- R²: 0.89
- Kendall 𝜏: 0.73
- Spearman ρ: 0.89

## System Details
- Ligands: 6
- Host Atoms: 7065
- Map Details:
  - Edges: 10
  - Min Dummy Atoms: 4
  - Max Dummy Atoms: 32
  - Mean Dummy Atoms: 19.6
  - Median Dummy Atoms: 20.5

## Simulation Details
- TMD Sha: [d90311ea6b8fd4d5bddae32b2925ef72d57ec45e](https://github.com/tmd-industries/tmd/tree/d90311ea6b8fd4d5bddae32b2925ef72d57ec45e)
- GPU: RTX 4090
- MPS Processes: 12
- Total Wallclock Time: 3.68 Hours
- Average Time Per Edge: 0.37 Hours
- Total Nanoseconds Simulated: 1327.20
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
