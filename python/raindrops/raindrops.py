def convert(number: int) -> str:
    """Converts a number into string that contains raindrop sounds"""
    if number % 3 and number % 5 and number % 7 != 0:
        return str(number)
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    return result
