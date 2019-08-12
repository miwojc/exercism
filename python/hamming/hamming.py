def distance(strand_a: str, strand_b: str) -> int:
    """Returns the Hamming Distance for two input DNA strands"""
    if len(strand_a) == len(strand_b):
        return sum(c1 != c2 for c1, c2 in zip(strand_a, strand_b))
    raise ValueError("The Hamming distance is only defined for sequences of equal length.")