from os import listdir

from ccal import establish_path


def make_path_dict(setting):

    path_dict = {}

    for name in (
        "kallisto/",
        "enst_x_sample.tsv",
        "gene_x_sample.processed.tsv",
        "target_x_sample.tsv",
        "differentially_expressed_gene/",
        "gene_set_x_sample.tsv",
        "differentially_expressed_gene_set/",
        "hill_plot/",
        "expanded_gene_set/",
        "summary/",
        "mountain_plot/",
    ):

        path_dict[name] = "{}/{}".format(setting["output_directory_path"], name)

    for name, path in path_dict.items():

        if name.endswith("/"):

            path_type = "directory"

        else:

            path_type = "file"

        establish_path(path, path_type)

    return path_dict
