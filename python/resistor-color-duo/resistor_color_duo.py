RES_COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):
    return int(f"{RES_COLORS.index(colors[0])}{RES_COLORS.index(colors[1])}")
