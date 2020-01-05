def is_isogram(string: str) -> bool:
    """Returns True if the input string is isogram and False if not"""
    x: str = "".join(c for c in string.lower() if c.isalpha())
    return len(x) == len(set(x))
