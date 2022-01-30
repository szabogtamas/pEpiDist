import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("peptides")
    parser.add_argument("output_file", nargs="?", default="pepi_net.tsv")
    args = parser.parse_args()
    native_result = calculate similarities(args.peptides)
    with open(args.output_file, "w") as f:
        f.write("\n".join([a + "\t" + str(b) + "\t" + c for a, b, c in native_result]))
    return

def calculate similarities(peptides):
    """Calculate chemical similarity of peptides."""
    return []

if __name__ == "__main__":
    main()