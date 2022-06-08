def transform(legacy_data):
    return {i.lower(): k for k in legacy_data for i in legacy_data[k]}
