---
jupyter:
  jupytext:
    formats: md,ipynb
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.8
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

## Setup

```python
import os, sys
```

```python
!pip install peptides
```

```python
sys.path.append("../src")  # developmental hack, to load the local version of the module
%load_ext autoreload
%autoreload 2

import pEpiDist as epi
```

## Initialize reference DB

```python
proteome_location = "../proteomes/human_proteome.fasta"
pepi_db = "../human_peptides.pep"
epi.create_peptide_db(proteome_location, 8 pepi_db)
```

## Query a peptide

```python
epitope_seq = "QWSWERTREWSDFDERWRWDSFREDSEQWDS"
epi.query(epitope_seq, pepi_db)
```
