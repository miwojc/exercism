import re


def is_valid(isbn: str) -> bool:
    """Returns `True` if ISBN-10 is valid, otherwise returns `False`"""
    isbn = isbn.replace("-", "")
    if re.match("\\d{9}[\\dX]$", isbn):
        digits = [int(s) if s != "X" else 10 for s in isbn]
        formula = sum(map(lambda a, b: a * b, digits, range(10, 0, -1)))
        return formula % 11 == 0
    return False
