import os
import argparse
import iteritems
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("proteom_file")
parser.add_argument("output_dir")
args = parser.parse_args()

def main(proteom_file, output_dir):
  protein_seq = "AWRFARFGDSGAEWRWRWAERWRQQARWE"

  d = Counter(protein_seq)

  it = iter(seq)
  result = tuple(islice(it, n))
  return


if __name__ == "__main__":
    main(args.proteom_file, args.output_dir)
