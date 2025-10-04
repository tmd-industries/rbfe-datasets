# July 15th 2025 Results

* Run with ligands/maps at https://github.com/badisa/timemachine-datasets/commit/b895a5dab9fecf237de9588b598a616f08046c7b
* Run with NAGL charges
* Run with OpenFF 2.0.0 parameters
* Images with the suffix `_no_rest.png` has a temperature scale of 1.0, otherwise with 3.0.
* EG5 had not be separated by charges, resulting in a map that contained charge hops.
* Simulated with private version of TMD.
* Run on a RTX 4090 with MPS.
* Simulations run with 2ns, 0.667 min overlap, and 0.667 target overlap unless otherwise specified.
* Hif2a graph included ligand 35, but the experimental value was excluded from MLE. The justification is that the compound would be included in a graph in practice, even if the experimental label is incorrect.

## Issues

* The error bars are incorrect, they were not scaled from kJ/mol to kcal/mol, resulting in larger error bars than intended.