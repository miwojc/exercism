def convert(number: int) -> str:
    """Converts a number into a string that contains raindrop sounds"""
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if number % 3 and number % 5 and number % 7 != 0:
        result += str(number)
    return result
