from string import ascii_lowercase


def is_pangram(sentence: str) -> bool:
    """Returns `True` if a sentence is a pangram, otherwise returns `False`"""
    return set(ascii_lowercase).issubset(sentence.lower())
