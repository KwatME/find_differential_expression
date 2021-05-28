from kraft.plot import plot_point
from numpy import arange, where


def plot_peek(ft, p_, d):

    p = ft["Score"].dropna().sort_values().to_frame()

    p["Rank"] = arange(p.shape[0])

    p["Size"] = 2

    p["Color"] = where(p["Score"] < 0, "#0088ff", "#ff1968")

    p["Score"] = p["Score"].abs()

    p["Opacity"] = 0.48

    p["Annotate"] = [l in p_ for l in p.index]

    p.loc[p["Annotate"], ["Size", "Color", "Opacity"]] = [8, "#20d9ba", 1]

    plot_point(p, title="Peek", file_path="{}peek.html".format(d))
