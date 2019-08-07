def is_pangram(sentence: str) -> bool:
    """Returns `True` if a sentence is a pangram, otherwise returns `False`"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        test = letter in sentence.lower()
        if not test:
            return test
    return test
