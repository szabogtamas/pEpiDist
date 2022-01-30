import os
import argparse

from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("proteome_file")
parser.add_argument("output_dir", nargs="?", default="")
parser.add_argument("window_size", nargs="?", default=8)
args = parser.parse_args()

def parse_fasta_proteome(fasta_file):
    with open(fasta_file, "r") as f:
        fasta_seqs = f.read().split("\n>")
        protein_seqs = fasta_seqs[0].split("\n", 1)
        protein_seqs = [(protein_seqs[0].replace(">", "").split("|")[0], protein_seqs[1].replace("\n", "").replace(" ", ""))]
        for s in fasta_seqs[1:]:
          name, seq = s.split("\n", 1)
          protein_seqs.append((name.split("|")[0], seq.replace("\n", "").replace(" ", "")))
    return protein_seqs

def count_peptides_of_seq(protein, protein_seq, window=9, epitopes=None):
    if epitopes is None:
        epitopes = defaultdict(list)
    for i in range(len(protein_seq)-window+1):
        epitopes[protein_seq[i:i+window]].append(str(i) + "_" + protein)
    return epitopes
 
def count_peptides_in_collection(proteins, window_size):
    epi_map = defaultdict(list)
    for name, seq in proteins:
        epi_map = count_peptides_of_seq(name, seq, window_size, epitopes=epi_map)
    return epi_map

def summarise_pepinet(d):
    summary_stats = [(k, len(v), ";".join(v)) for k, v in d.items()]
    summary_stats.sort(key=lambda x: x[1], reverse=True)
    return summary_stats

def main(proteome_file, output_dir, window_size):
    proteins = parse_fasta_proteome(proteome_file)
    epitope_numbers = count_peptides_in_collection(proteins, window_size)
    overlap_list = summarise_pepinet(epitope_numbers)
    return


if __name__ == "__main__":
    main(args.proteome_file, args.output_dir, args.window_size)
