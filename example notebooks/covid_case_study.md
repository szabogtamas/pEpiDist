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

# Potentially crossreactive SARS-CoV2 epitopes

A case study of searching epitope similarities between SARS-CoV2 epitope peptides and the human proteome.

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

## Download proteomes

```python
!curl https://rest.uniprot.org/uniprotkb/stream?compressed=true&format=fasta&query=%28%28organism_id%3A2697049%29%29
```

## Initialize reference DB