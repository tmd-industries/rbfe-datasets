from functools import partial
from glob import glob
from multiprocessing import Pool
from shutil import copy2

from rdkit import Chem
from tmd.fe.utils import read_sdf
from tmd.ff import Forcefield

Chem.SetDefaultPickleProperties(Chem.PropertyPickleOptions.AllProps)


def charge_mol(ff, mol):
    for handle in ff.get_ordered_handles():
        if handle is None:
            continue
        handle.parameterize(mol)
    return mol


def main():
    ff = Forcefield.load_from_file("smirnoff_2_0_0_amber_am1bcc.py")
    charge_func = partial(charge_mol, ff)

    ligands_paths = glob("**/ligands.sdf", recursive=True)
    for lig_path in ligands_paths:
        print("Charging", lig_path)
        mols = read_sdf(lig_path)
        copy2(lig_path, f"{lig_path}.backup")
        with Pool() as pool:
            charged_ligands = pool.map(charge_func, mols)
        with Chem.SDWriter(lig_path) as writer:
            for mol in charged_ligands:
                writer.write(mol)


if __name__ == "__main__":
    main()
