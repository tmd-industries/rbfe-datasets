# August 8th 2025 Results

* All run with Global MD only
* Run with ligands/maps in Repo as of this commit
* Run with NAGL charges
* Run with OpenFF 2.0.0 parameters
* Images with the suffix `_no_rest.png` has a temperature scale of 1.0, otherwise with 3.0.
* EG5 had not be separated by charges, resulting in a map that contained charge hops.
* Simulated with non-public version of TMD circa August 08 2025. Should be similar to initial released commit at https://github.com/tmd-industries/tmd/commit/7d6db6cfadd7680a0d236363cb2fbac42911315c
* Run on a RTX 4090 with 6 MPS processes.
* Simulations run with 2ns, 0.667 min overlap, and 0.667 target overlap unless otherwise specified.
* Hif2a graph included ligand 35, but the experimental value was excluded from MLE. The justification is that the compound would be included in a graph in practice, even if the experimental label is incorrect.
