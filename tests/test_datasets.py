import os

from rdkit import Chem

from openmm import app

import pytest

datasets_dir = os.path.dirname(os.path.dirname(__file__))

KJ_EXPERIMENTAL_LABEL = "kJ/mol experimental dG"
EXPERIMENTAL_FIELD = "experimental dG reference field"
EXPERIMENTAL_UNIT_FIELD = "experimental dG reference units"


def get_ion_residue_templates(modeller) -> dict[app.Residue, str]:
    """When using amber99sbildn with the amber14 water models the ion templates get duplicated. This forces
    the use of the NA/CL/MG templates (from the amber14 water models) rather than the amber99sbildn templates.

    # Taken from TMD
    """
    residue_templates = {}
    for res_name in (SODIUM_ION_RESIDUE, CHLORINE_ION_RESIDUE, MAGNESIUM_ION_RESIDUE):
        residue_templates.update({res: res_name for res in modeller.getTopology().residues() if res.name == res_name})
    return residue_templates


def files_with_ext(dirname, ext):
    for root, _, files in os.walk(dirname):
        for file in files:
            if file.endswith(ext):
                yield os.path.join(root, file)

@pytest.mark.parametrize("ds", list(files_with_ext(datasets_dir, ".sdf")))
def test_datasets_have_experimental_labels(ds):
    # Don't remove hydrogens, throws warnings
    mols = list(Chem.SDMolSupplier(ds, removeHs=False))
    has_label = False
    for mol in mols:
        kj_label = mol.GetProp(KJ_EXPERIMENTAL_LABEL)
        try:
            float(kj_label)
            has_label = True
            assert mol.HasProp(EXPERIMENTAL_FIELD)
            assert mol.HasProp(EXPERIMENTAL_UNIT_FIELD)
        except ValueError:
            pass
    assert has_label


@pytest.mark.parametrize("pdb", list(files_with_ext(datasets_dir, ".pdb")))
def test_dataset_structures_parsed_by_openmm(pdb):
    ff = app.ForceField("amber99sbildn.xml", "amber14/tip3p.xml")
    pdb_file = app.PDBFile(pdb)
    modeller = app.Modeller(pdb_file.topology, pdb_file.positions)
    modeller.addSolvent(
        ff,
        padding=0.1,
    )

