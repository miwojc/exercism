def is_valid(isbn: str) -> bool:
    """Returns `True` if ISBN-10 is valid, otherwise returns `False`"""

    val = 0
    multi = 10
    isbn = isbn.replace("-", "")

    # check if input string is 10 digits including a check character
    if len(isbn) != 10:
        return False

    # check if isbn contains valid characters only
    if not isbn[0:9].isdigit():
        return False
    
    if not isbn[-1:].isdigit():
        if not isbn[-1:] == "X":
            return False
    
    isbn = isbn.replace("X", "10")

    # check if isbn is valid
    if len(isbn) > 10:
        for digit in isbn[0:9]:
            val += int(digit) * multi
            multi -= 1
        val = val + 10
        return val % 11 == 0

    for digit in isbn:
        val += int(digit) * multi
        multi -= 1

    return val % 11 == 0
