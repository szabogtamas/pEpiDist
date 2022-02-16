import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file", nargs="?", default="kidera_distances.tsv")
    args = parser.parse_args()
    native_result = query_mimicry_peptides(args.input_file)
    with open(args.output_file, "w") as f:
        f.write("\n".join([a + "\t" + str(b) + "\t" + c for a, b, c in native_result]))
    return
  
def query_mimicry_peptides(q):
    """Calculates similarity of epitope peptides in query file to epitopes in reference proteome."""
    distance = []
    return distances

if __name__ == "__main__":
    main()
