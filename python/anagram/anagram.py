def find_anagrams(word, candidates):
    word_lower = word.lower()
    word_sorted = sorted(word_lower)
    _candidates = [[candidate, candidate.lower()] for candidate in candidates]
    return [
        candidate[0]
        for candidate in _candidates
        if sorted(candidate[1]) == word_sorted and candidate[1] != word_lower
    ]
