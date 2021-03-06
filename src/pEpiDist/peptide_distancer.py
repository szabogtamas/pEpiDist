import argparse
import peptides
import math
import numpy as np
import pandas as pd


def query_mimicry_peptides(q, protemome, method="kidera"):
    """Calculates similarity of epitope peptides in query file to epitopes in reference proteome."""
    distances = []
    for p in protemome:
        distances.append((p, distance_between(p, q)))
    return pd.DataFrame.from_records(distances).sort_values(ascending=False)

def calculate_similarities(peps):
    """Calculate chemical similarity of peptides based on Kidera factors."""
    
    scores = []
    for peptide in peps:
        peptide = peptides.Peptide(peptide)
        scores.append(peptide.kidera())
    return scores

def numeric_encode(peptide):
    """Numerically encode peptide based on Kidera factors."""
    coords = np.flatten(peptide.kidera())
    return coords

def distance_between(p1, p2):
    """Calculated distance of two peptides."""
    return math.dist(numeric_encode(p1), numeric_encode(p2))

def calculate_distance_matrix(peptides):
    """A distance matrix of peptides."""
    return sklearn.metrics.pairwise_distances(peptides, metric=distance_between)
