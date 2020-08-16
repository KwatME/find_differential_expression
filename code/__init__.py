import os

import numpy as np
import pandas as pd

import kraft

SETTING = kraft.json.read("setting.json")

PATH = {}

for name in (
    "gene_x_sample.processed.tsv",
    "target_x_sample.tsv",
    "find_differentially_expressed_gene/",
    "gene_set_x_information.tsv",
    "gsea/",
    "gene_set_x_sample.tsv",
    "find_differentially_expressed_gene_set/",
    "compare_differentially_expressed_gene_set/",
    "expand_gene_set/",
    "summarize_gene_set/",
):

    path = os.path.join("../output/", name)

    kraft.path.path(path)

    PATH[name] = path
