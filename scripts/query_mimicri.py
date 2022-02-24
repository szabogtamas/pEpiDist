import argparse
import .

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file", nargs="?", default="kidera_distances.tsv")
    args = parser.parse_args()
    query_proteome = parse_fasta_proteome(args.input_file)
    native_result = query_mimicry_peptides(query_proteome, method=args.input_file)
    with open(args.output_file, "w") as f:
        f.write("\n".join([a + "\t" + str(b) + "\t" + c for a, b, c in native_result]))
    return

def query_mimicry_peptides(q, method="kidera"):
    """Calculates similarity of epitope peptides in query file to epitopes in reference proteome."""
    distances = []
    for p in q:
        distances.append(distance_between(p1, p2))
    return distances

if __name__ == "__main__":
    main()
