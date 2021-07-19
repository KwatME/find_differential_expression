from kraft.plot import plot_point
from numpy import arange, where


def plot_peek(se, la_, pa):

    da = se.dropna().sort_values().to_frame()

    da["Rank"] = arange(da.shape[0])

    da["Size"] = 2

    da["Color"] = where(da["Score"] < 0, "#0088ff", "#ff1968")

    da["Score"] = da["Score"].abs()

    da["Opacity"] = 0.48

    da["Annotate"] = [la in la_ for la in da.index]

    da.loc[da["Annotate"], ["Size", "Color", "Opacity"]] = [8, "#20d9ba", 1]

    plot_point(da, title="Peek", pa="{}peek.html".format(pa))
