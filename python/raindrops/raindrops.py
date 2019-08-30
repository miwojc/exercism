def convert(number: int) -> str:
    """Converts a number into a string that contains raindrop sounds"""
    sounds = ""
    if number % 3 == 0:
        sounds += "Pling"
    if number % 5 == 0:
        sounds += "Plang"
    if number % 7 == 0:
        sounds += "Plong"
    if sounds == "":
        sounds += str(number)
    return sounds
