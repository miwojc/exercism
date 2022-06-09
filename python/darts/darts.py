def score(x, y):
    dist = ((x**2 + y**2)) ** (1 / 2)
    if dist <= 1:
        return 10
    if dist <= 5:
        return 5
    if dist <= 10:
        return 1
    return 0
