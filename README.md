# pEpiDist

Similarity metrics for peptide epitopes

## Usage
A typical use case is to search for peptides similar to an epitope.

## Database initialization
Proteome-wide census of peptide overlaps and similarities for epitope screens

To create a database of peptide overlaps on some made-up sequences, run
```
docker run -v $PWD:/local_folder pepidist reference
```

A file named `reference_peptidome.tsv` should show up in your local directory.


## Epitope query

Epitopes derived from sequences in a query FASTA file can be checked for similarity to the reference proteome.
