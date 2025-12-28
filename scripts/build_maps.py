import sys
from glob import glob
from pathlib import Path
from subprocess import run

import tmd
from tmd.fe.utils import read_sdf

# Requires TMD to be installed in editable mode, else examples don't come along for the ride
tmd_graph_script = Path(tmd.__file__).parent.parent / "examples" / "build_rbfe_graph.py"


def main():
    ligands_paths = glob("**/ligands.sdf", recursive=True)
    for lig_path in ligands_paths:
        if "charge_annihilation_set" in lig_path:
            print("Skipping charge annihilation set compounds")
            continue
        ds_name = str(Path(lig_path).parent.name)
        mols = read_sdf(lig_path)
        k_min_cut = 3
        if len(mols) < 4:
            k_min_cut = 2
        # print("Building graph", lig_path)
        run(
            [
                sys.executable,
                tmd_graph_script,
                str(Path(lig_path).resolve()),
                str(Path(lig_path).parent / f"{ds_name}_map.json"),
                "--greedy_k_min_cut",
                str(k_min_cut),
            ]
        )


if __name__ == "__main__":
    main()
