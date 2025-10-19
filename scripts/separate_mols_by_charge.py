"""
Split an SDF file into sets of molecules by formal charge.
"""

from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path

from rdkit import Chem
from tmd.fe.utils import read_sdf


def main():
    parser = ArgumentParser()
    parser.add_argument("mols_path")
    args = parser.parse_args()

    path = Path(args.mols_path).expanduser()
    mols = read_sdf(path)
    separated = defaultdict(list)
    for mol in mols:
        charge = Chem.GetFormalCharge(mol)
        separated[charge].append(mol)
    for charge, subset in separated.items():
        output_path = path.parent / f"{path.stem}_charge_{charge:d}.sdf"
        with Chem.SDWriter(str(output_path)) as writer:
            for mol in subset:
                writer.write(mol)


if __name__ == "__main__":
    main()
