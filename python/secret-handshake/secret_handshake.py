ACTIONS = ["wink", "double blink", "close your eyes", "jump", "reverse"]


def commands(binary_str):
    code = int(binary_str, 2)
    out = [action for idx, action in enumerate(ACTIONS) if code & (1 << idx)]
    return out[-2::-1] if "reverse" in out else out
