from os.path import join


import kraft

PROJECT = kraft.json.read("../project.json")

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

    path = join(PROJECT["output/"], name)

    kraft.path.path(path)

    PATH[name] = path
