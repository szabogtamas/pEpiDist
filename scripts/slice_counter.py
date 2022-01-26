import os
import iteritems
from collections import Counter

protein_seq = "AWRFARFGDSGAEWRWRWAERWRQQARWE"

d = Counter(protein_seq)

it = iter(seq)
result = tuple(islice(it, n))
