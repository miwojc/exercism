from string import ascii_lowercase


def rotate(text, key):
    ascii_lowercase_rot = ascii_lowercase[key:] + ascii_lowercase[:key]
    trans = str.maketrans(
        ascii_lowercase + ascii_lowercase.upper(),
        ascii_lowercase_rot + ascii_lowercase_rot.upper(),
    )
    return text.translate(trans)
