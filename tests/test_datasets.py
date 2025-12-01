import json
import os
from pathlib import Path

import networkx as nx
import pytest
from tmd.constants import DEFAULT_PROTEIN_FF, DEFAULT_WATER_FF
from tmd.fe.utils import get_mol_name, read_sdf, read_sdf_mols_by_name
from tmd.md.builders import build_protein_system

datasets_dir = os.path.dirname(os.path.dirname(__file__))

KJ_EXPERIMENTAL_LABEL = "kJ/mol experimental dG"
EXPERIMENTAL_FIELD = "experimental dG reference field"
EXPERIMENTAL_UNIT_FIELD = "experimental dG reference units"

AMBER_CHARGES_FIELD = "AmberAM1BCCCache"


def files_with_ext(dirname, ext):
    for root, _, files in os.walk(dirname):
        for file in files:
            if file.endswith(ext):
                yield os.path.join(root, file)


def build_graph_from_edges(edges: list[dict]) -> nx.Graph:
    g = nx.Graph()
    for edge_data in edges:
        g.add_edge(edge_data["mol_a"], edge_data["mol_b"], core=edge_data.get("core", None))
    return g


@pytest.mark.parametrize("ds", list(files_with_ext(datasets_dir, "map.json")))
def test_maps_are_connected(ds):
    directory = Path(ds).parent
    ligands_path = directory / "ligands.sdf"
    assert (ligands_path).is_file()
    with open(ds) as ifs:
        edges = json.load(ifs)
    assert len(edges) > 0
    mols_by_name = read_sdf_mols_by_name(ligands_path)
    graph = build_graph_from_edges(edges)
    for node in graph.nodes:
        assert node in mols_by_name
    assert nx.edge_connectivity(graph) == 3


@pytest.mark.parametrize("ds", list(files_with_ext(datasets_dir, ".sdf")))
def test_datasets_have_experimental_labels(ds):
    # Don't remove hydrogens, throws warnings
    mols = read_sdf(ds)
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


@pytest.mark.parametrize("ds", list(files_with_ext(datasets_dir, ".sdf")))
def test_datasets_have_amber_charges(ds):
    mols = read_sdf(ds)
    for mol in mols:
        assert mol.HasProp(AMBER_CHARGES_FIELD), f"Mol {get_mol_name(mol)} doesn't have amber charges"


@pytest.mark.parametrize("pdb", list(files_with_ext(datasets_dir, ".pdb")))
def test_dataset_structures_parsed_by_openmm(pdb):
    host_config = build_protein_system(pdb, DEFAULT_PROTEIN_FF, DEFAULT_WATER_FF)
    assert host_config is not None
