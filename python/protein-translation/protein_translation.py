def proteins(strand):
    out = []
    for idx in range(0, len(strand), 3):
        condon = strand[idx : idx + 3]
        if condon in ["UAA", "UAG", "UGA"]:
            break
        if condon == "AUG":
            out.append("Methionine")
        if condon in ["UUU", "UUC"]:
            out.append("Phenylalanine")
        if condon in ["UUA", "UUG"]:
            out.append("Leucine")
        if condon in ["UCU", "UCC", "UCA", "UCG"]:
            out.append("Serine")
        if condon in ["UAU", "UAC"]:
            out.append("Tyrosine")
        if condon in ["UGU", "UGC"]:
            out.append("Cysteine")
        if condon in ["UGG"]:
            out.append("Tryptophan")
    return out
