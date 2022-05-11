---
jupyter:
  jupytext:
    formats: md,ipynb
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

## Setup

```python
import os, sys
```

```python
sys.path.append("../src")  # developmental hack, to load the local version of the module
%load_ext autoreload
%autoreload 2

import pEpiDist as epi
```

## Initialize reference DB

```python
epi.create_peptide_db("human_proteome.fasta", 8)
```
