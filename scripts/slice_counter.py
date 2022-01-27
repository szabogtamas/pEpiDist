import os
import argparse

from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("proteom_file")
parser.add_argument("output_dir")
args = parser.parse_args()

def count_peptides_of_seq(protein_seq, window=9):
    epitopes = [protein_seq[i:i+window] for i in range(len(protein_seq)-window+1)]
    return Counter(epitopes)
 
def count_peptides_in_collection(proteins):
  return

def main(proteom_file, output_dir):
  proteins = parse_fasta_proteome(proteom_file)
  epitope_numbers = count_peptides_in_collection(proteins)
  return


if __name__ == "__main__":
    main(args.proteom_file, args.output_dir)
