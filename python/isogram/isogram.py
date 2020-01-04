def is_isogram(string: str) -> bool:
    """Returns True if the input string is isogram and False if not"""
    return len("".join(filter(str.isalpha, string.lower()))) == len(
        set("".join(filter(str.isalpha, string.lower())))
    )
