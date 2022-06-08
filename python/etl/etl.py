def transform(legacy_data):
    out = {}
    for k, v in legacy_data.items():
        for nk in v:
            out[nk.lower()] = k
    return out
