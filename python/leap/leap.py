def leap_year(year: int) -> bool:
    """Returns `True` for leap year and `False` if not"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0