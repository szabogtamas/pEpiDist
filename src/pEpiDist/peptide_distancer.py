import argparse
import peptides
import math
import numpy as np
import pandas as pd

def query_mimicry_peptides(q, protemome, method="kidera", limit=150):
    """Calculates similarity of epitope peptides in query file to epitopes in reference proteome."""
    columns = ["Peptide", "Freq", "Proteins", "Score"]
    distances = [list(p) + [distance_between(p[0], q)] for p in protemome]  
    return pd.DataFrame.from_records(distances, columns=columns).sort_values(by="Score", ascending=False).head(limit)

def calculate_similarities(peps):
    """Calculate chemical similarity of peptides based on Kidera factors."""
    scores = [peptides.Peptide(peptide).kidera_factors()._asdict() for peptide in peps]
    return pd.DataFrame.from_records(scores)

def numeric_encode(peptide):
    """Numerically encode peptide based on Kidera factors."""
    kf = peptides.Peptide(peptide).kidera_factors()
    return np.array(kf)

def distance_between(p1, p2):
    """Calculated distance of two peptides."""
    return math.dist(numeric_encode(p1), numeric_encode(p2))

def calculate_distance_matrix(peptides):
    """A distance matrix of peptides."""
    return sklearn.metrics.pairwise_distances(peptides, metric=distance_between)
