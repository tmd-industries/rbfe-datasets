from shutil import copy2
from pathlib import Path
from argparse import ArgumentParser
from tmd.fe.utils import read_sdf, convert_uM_to_kJ_per_mole
from tmd.constants import DEFAULT_TEMP, KCAL_TO_KJ

from rdkit import Chem

EXPERIMENT_UNIT_TAG = "experimental dG reference units"
EXPERIMENT_FIELD_TAG = "experimental dG reference field"
KCAL_LABEL = "kcal/mol experimental dG"
KJ_TAG = "kJ/mol experimental dG"


def get_mol_experimental_value(mol: Chem.Mol, field: str, units: str) -> float:
    if field is None or units is None:
        return None
    if units == "kJ/mol":
        return float(mol.GetProp(field))
    elif units == "kcal/mol":
        return float(mol.GetProp(field)) * KCAL_TO_KJ
    elif units == "uM":
        return convert_uM_to_kJ_per_mole(float(mol.GetProp(field)))
    elif units == "nM":
        return convert_uM_to_kJ_per_mole(float(mol.GetProp(field)) / 1000.0)
    else:
        assert 0, f"Unknown units {units}"


def main():
    parser = ArgumentParser()
    parser.add_argument("sdf_path")
    parser.add_argument("field")
    parser.add_argument("units", choices=["kJ/mol", "kcal/mol", "uM", "nM"])
    args = parser.parse_args()
    sdf_path = Path(args.sdf_path).expanduser()
    mols = read_sdf(sdf_path)
    copy2(sdf_path, f"{sdf_path}.backup")
    has_field = False
    for mol in mols:
        if mol.HasProp(args.field):
            exp_dg = get_mol_experimental_value(mol, args.field, args.units)
            mol.SetProp(EXPERIMENT_UNIT_TAG, args.units)
            mol.SetProp(EXPERIMENT_FIELD_TAG, args.field)
            mol.SetProp(KJ_TAG, str(exp_dg))
            mol.SetProp(KCAL_LABEL, str(exp_dg / KCAL_TO_KJ))
            has_field = True
    assert has_field
    with Chem.SDWriter(sdf_path) as writer:
        for mol in mols:
            writer.write(mol)


if __name__ == "__main__":
    main()
