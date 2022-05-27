import argparse
from collections import defaultdict

def write_peptide_db(proteome_file, fn, window_size=9):
    """A helper function that calls `create_peptide_db` and writes the db to a file."""
    overlap_list = create_peptide_db(proteome_file, window_size)
    with open(fn, "r") as f:
        f.write("\n".join([";".join(x) for x in overlap_list])
    return

def create_peptide_db(proteome_file, window_size=9):
    """The main coordinating function that processes a fasta proteome and returns shared peptides."""
    proteins = parse_fasta_proteome(proteome_file)
    epitope_numbers = count_peptides_in_collection(proteins, window_size)
    overlap_list = summarise_pepinet(epitope_numbers)
    return overlap_list

def parse_fasta_proteome(fasta_file):
    """Yet another FASTA parser to read input sequences."""
    with open(fasta_file, "r") as f:
        fasta_seqs = f.read().split("\n>")
        protein_seqs = fasta_seqs[0].split("\n", 1)
        protein_seqs = [(protein_seqs[0].replace(">", "").split("|")[0], protein_seqs[1].replace("\n", "").replace(" ", ""))]
        for s in fasta_seqs[1:]:
            name, seq = s.split("\n", 1)
            protein_seqs.append((name.split("|")[1], seq.replace("\n", "").replace(" ", "")))
    return protein_seqs

def count_peptides_of_seq(protein, protein_seq, window=9, epitopes=None):
    """The workhorse function that actually counts peptides in a given sequence."""
    if epitopes is None:
        epitopes = defaultdict(list)
    for i in range(len(protein_seq)-window+1):
        epitopes[protein_seq[i:i+window]].append(str(i) + "_" + protein)
    return epitopes

def count_peptides_in_collection(proteins, window_size):
    """Issues the peptide counting function for all sequences."""
    epi_map = defaultdict(list)
    for name, seq in proteins:
        epi_map = count_peptides_of_seq(name, seq, window_size, epitopes=epi_map)
    return epi_map

def summarise_pepinet(d):
    """Sums up the results and sorts by the number of proteins the peptide overlaps."""
    summary_stats = [(k, len(v), ";".join(v)) for k, v in d.items()]
    summary_stats.sort(key=lambda x: x[1], reverse=True)
    return summary_stats