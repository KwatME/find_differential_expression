from pandas import concat, read_csv


def read_statistic(co, na):

    te = "../output/compare_{{}}/{}/{}/statistic.tsv".format(co, na)

    return concat(
        [
            read_csv(
                te.format("feature"),
                "\t",
                index_col=0,
            ),
            read_csv(
                te.format("set"),
                "\t",
                index_col=0,
            ),
        ]
    )
