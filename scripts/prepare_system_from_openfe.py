"""Script for pulling structures and ligands from the OpenFE IndustryBenchmarks2024 repository

This is simply a starting point to reduce the number of systems that have to be re-prepared.
"""

import os
import sys
from glob import glob
from pathlib import Path
from shutil import copy2
from subprocess import run
from tempfile import NamedTemporaryFile

from openmm.app import Modeller, PDBFile
from tmd.constants import DEFAULT_PROTEIN_FF, DEFAULT_WATER_FF
from tmd.md.builders import build_protein_system


def prepare_system_for_tmd(pdb_file, output_file):
    """
    Prepare PDB systems for TMD.

    Will attempt to take systems as they are, else will remove the UNK and WAT residues.
    - UNK: Cofactors, which are ignored by TMD currently
    - WAT: If waters are not all after the protein, there are issues. TMD has a water sampler so this seems reasonable.
    """
    # if output_file.is_file():
    #     return

    def verify_and_copy_file(path, modified=False):
        try:
            assert build_protein_system(str(path), DEFAULT_PROTEIN_FF, DEFAULT_WATER_FF) is not None
            output_file.parent.mkdir(parents=True, exist_ok=True)
            copy2(path, output_file)
            with open(output_file.parent / "README.md", "w") as ofs:
                ofs.write(f"""# {output_file.name}

Retrieved from OpenFE's IndustryBenchmarks2024 repo at tag V1.0.0
Removed Co-factors or Waters: {modified}
""")
        except (ValueError, AssertionError) as e:
            print(f"Failed to build and copy system: {e!s}")

    verify_and_copy_file(pdb_file)
    host_pdb = PDBFile(pdb_file)
    modeller = Modeller(host_pdb.topology, host_pdb.positions)
    residues_to_delete = []
    for res in modeller.topology.residues():
        if res.name in ["UNK", "WAT"]:
            residues_to_delete.append(res)
    modeller.delete(residues_to_delete)

    with NamedTemporaryFile(suffix=".pdb") as tempfile:
        with open(tempfile.name, "w") as f:
            PDBFile.writeFile(modeller.topology, modeller.positions, f, True)

        verify_and_copy_file(tempfile.name, True)


def main():
    cache_dir = Path(__file__).parent / ".reference_dataset_cache"
    # Pull all of the input structures from the OpenFE industries benchmark. Doesn't contain all sets, but it is a starting point
    if not cache_dir.is_dir():
        run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "--branch",
                "v1.0.0",
                "https://github.com/OpenFreeEnergy/IndustryBenchmarks2024.git",
                str(cache_dir),
            ]
        )
    protein_structures = glob(
        str(cache_dir / "industry_benchmarks" / "input_structures" / "prepared_structures" / "**" / "*.pdb"),
        recursive=True,
    )
    failed_structures = []
    for structure in protein_structures:
        if os.stat(structure).st_size == 0:
            continue
        dataset_collection = Path(structure).parent.parent.name
        collection_dir = Path(__file__).parent.parent / dataset_collection
        dataset_dir = collection_dir / str(Path(structure).parent.name)
        output_path = dataset_dir / f"{Path(structure).parent.name}_structure.pdb"
        prepare_system_for_tmd(structure, output_path)
        if output_path.is_file():
            ligands_path = Path(structure.replace("protein.pdb", "ligands.sdf"))
            assert ligands_path.is_file()
            copy2(ligands_path, output_path.parent / "ligands.sdf")
            run(
                [
                    sys.executable,
                    str(Path(__file__).parent / "assign_experimental_labels.py"),
                    str(ligands_path),
                    "r_exp_dg",
                    "kcal/mol",
                ]
            )
        else:
            failed_structures.append(structure)

    if len(failed_structures) > 0:
        print("Structures that failed to convert")
        print("-" * 30)
        for struc in failed_structures:
            print(struc)


if __name__ == "__main__":
    main()
