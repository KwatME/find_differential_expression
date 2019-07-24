from os.path import join

from kraft import establish_path, normalize_path


def make_path_dict(setting):

    output_directory_path = normalize_path(setting["output_directory_path"])

    path_dict = {}

    for name in (
        "kallisto/",
        "enst_x_sample.tsv",
        "gene_x_sample.tsv",
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

        path_dict[name] = join(output_directory_path, name)

    for name, path in path_dict.items():

        if name.endswith("/"):

            path_type = "directory"

        else:

            path_type = "file"

        establish_path(path, path_type)

    return path_dict
