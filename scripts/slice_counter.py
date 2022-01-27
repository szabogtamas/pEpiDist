import os
import argparse

from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("proteom_file")
parser.add_argument("output_dir")
args = parser.parse_args()

def parse_fasta_proteome(fasta_file):
    with open(fasta_file, "r") as f:
        fasta_seqs = f.read().split(">")
        protein_seqs = list()
        for s in fasta_seqs[1:]:
            name, seq = s.split("\n", 1)
            protein_seqs.append((name.split("|")[1], seq.replace("\n", "").replace(" ", "")))
    return protein_seqs

def count_peptides_of_seq(protein, protein_seq, window=9, epitopes=None):
    if epitopes is None:
        epitopes = defaultdict(list)
    for i in range(len(protein_seq)-window+1):
        epitopes[protein_seq[i:i+window]].append(str(i) + "_" + protein)
    return epitopes
 
def count_peptides_in_collection(proteins):
      epi_map = defaultdict(list)
      for name, seq in proteins:
        epi_map = count_peptides_of_seq(name, seq, epitopes=epi_map)
      return epi_map

def main(proteom_file, output_dir):
      proteins = parse_fasta_proteome(proteom_file)
      epitope_numbers = count_peptides_in_collection(proteins)
      return


if __name__ == "__main__":
      main(args.proteom_file, args.output_dir)
