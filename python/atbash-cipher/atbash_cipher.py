from string import ascii_lowercase, punctuation


def trans(text):
    return text.translate(str.maketrans(ascii_lowercase, ascii_lowercase[::-1]))


def encode(plain_text):
    text = (
        plain_text.lower()
        .replace(" ", "")
        .translate(str.maketrans("", "", punctuation))
    )
    text = trans(text)
    return " ".join(text[i : i + 5] for i in range(0, len(text), 5))


def decode(ciphered_text):
    text = ciphered_text.replace(" ", "")
    return trans(text)
