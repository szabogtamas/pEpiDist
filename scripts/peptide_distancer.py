import argparse
import peptides
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("peptides")
    parser.add_argument("output_file", nargs="?", default="kidera_distances.tsv")
    args = parser.parse_args()
    native_result = calculate similarities(args.peptides)
    with open(args.output_file, "w") as f:
        f.write("\n".join([a + "\t" + str(b) + "\t" + c for a, b, c in native_result]))
    return

def calculate similarities(peps):
    """Calculate chemical similarity of peptides based on Kidera factors."""
    
    scores = []
    for peptide in peps:
        peptide = peptides.Peptide(peptide)
        scores.append(peptide.kidera()
    return scores

def numeric_encode(peptide):
    """Numerically encode peptide based on Kidera factors."""
    coords = np.flatten(peptide.kidera())
    return coords

if __name__ == "__main__":
    main()
