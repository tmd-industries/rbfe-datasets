# Relative Binding Free Energy Datasets

A collection of relative binding free energy (RBFE) datasets for use with the [TMD package](https://github.com/tmd-industries/tmd).

## Datasets

Each dataset directory contains:

- **`*_map.json`** — RBFE transformation maps defining the connectivity between ligands
- **`ligands.sdf`** — Ligand structures with assigned Amber AM1BCC charges and experimental free energy labels
- **`*_structure.pdb`** — Prepared protein structures ready for use with the TMD package
- **`README.md`** — Dataset-specific notes and provenance

Available datasets:

| Dataset | Description |
|---|---|
| `merck/` | Merck datasets |
| `bayer_macrocycles/` | Bayer macrocycle datasets |
| `jacs_set/` | JACS publication datasets |
| `janssen_bace/` | Janssen BACE datasets |
| `mcs_docking_set/` | MCS docking datasets |
| `scaffold_hopping_set/` | Scaffold hopping datasets |
| `schrodinger_macrocycles/` | Schrödinger macrocycle datasets |
| `water_set/` | Water reference datasets |
| `miscellaneous_set/` | Miscellaneous datasets |
| `fragments/` | Fragment-based datasets |
| `gpcrs/` | GPCR datasets |

## Summaries

The `summaries/` directory contains summaries from previous runs of the datasets, organized by date (e.g. `2026_apr_22/`).

- Dataset statistics (number of ligands, edges, wallclock time, hardware, etc)
- TMD commit hash used for the run
- Retrospective dG performance plots
- Notes on observed behavior

## Scripts

Utility scripts in `scripts/`:

- `assign_amber_charges.py` — Assign Amber charges to ligands
- `assign_experimental_labels.py` — Assign experimental free energy labels
- `build_maps.py` — Build RBFE transformation maps
- `prepare_system_from_openfe.py` — Prepare systems from OpenFE outputs
- `separate_mols_by_charge.py` — Separate ligands by charge state
