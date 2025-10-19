import os

import pytest
from tmd.constants import DEFAULT_PROTEIN_FF, DEFAULT_WATER_FF
from tmd.fe.utils import read_sdf
from tmd.md.builders import build_protein_system

datasets_dir = os.path.dirname(os.path.dirname(__file__))

KJ_EXPERIMENTAL_LABEL = "kJ/mol experimental dG"
EXPERIMENTAL_FIELD = "experimental dG reference field"
EXPERIMENTAL_UNIT_FIELD = "experimental dG reference units"


def files_with_ext(dirname, ext):
    for root, _, files in os.walk(dirname):
        for file in files:
            if file.endswith(ext):
                yield os.path.join(root, file)


@pytest.mark.parametrize("ds", list(files_with_ext(datasets_dir, ".sdf")))
def test_datasets_have_experimental_labels(ds):
    # Don't remove hydrogens, throws warnings
    mols = list(read_sdf(ds))
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
    host_config = build_protein_system(pdb, DEFAULT_PROTEIN_FF, DEFAULT_WATER_FF)
    assert host_config is not None
