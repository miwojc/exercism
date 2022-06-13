def flatten(iterable):
    flattened = []
    for item in iterable:
        if item or item == 0:
            if isinstance(item, list):
                flattened += flatten(item)
            else:
                flattened.append(item)
    return flattened
