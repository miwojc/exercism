def commands(binary_str):
    out = []
    if int(binary_str[-1]):
        out.append("wink")
    if int(binary_str[-2]):
        out.append("double blink")
    if int(binary_str[-3]):
        out.append("close your eyes")
    if int(binary_str[-4]):
        out.append("jump")
    return out[::-1] if int(binary_str[-5]) else out
