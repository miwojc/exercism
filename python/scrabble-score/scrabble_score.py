def score(word):
    def score_word(word):
        if word in ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"):
            return 1
        elif word in ("D", "G"):
            return 2
        elif word in ("B", "C", "M", "P"):
            return 3
        elif word in ("F", "H", "V", "W", "Y"):
            return 4
        elif word in ("K"):
            return 5
        elif word in ("J", "X"):
            return 8
        elif word in ("Q", "Z"):
            return 10
        else:
            return 0

    return sum((score_word(w) for w in word.upper()))
