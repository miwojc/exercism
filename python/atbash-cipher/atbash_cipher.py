from string import ascii_lowercase, punctuation


def encode(plain_text):
    out = []
    for count, char in enumerate(
        plain_text.replace(" ", "").translate(str.maketrans("", "", punctuation))
    ):
        char = char.lower()
        if count % 5 == 0 and count != 0:
            out.append(" ")
        if char in ascii_lowercase and char not in punctuation:
            idx = ascii_lowercase.index(char.lower())
            out.append(ascii_lowercase[-(idx + 1)])
        elif char not in punctuation:
            out.append(char)
    return "".join(out)


def decode(ciphered_text):
    out = []
    for char in ciphered_text.replace(" ", ""):
        if char in ascii_lowercase:
            idx = ascii_lowercase.index(char)
            out.append(ascii_lowercase[-idx - 1])
        else:
            out.append(char)
    return "".join(out)
