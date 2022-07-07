from string import ascii_lowercase


def rotate(text, key):
    ascii_lowercase_rot = ascii_lowercase[key:] + ascii_lowercase[:key]
    out = [
        ascii_lowercase_rot[ascii_lowercase.index(char)]
        if char.lower() in ascii_lowercase
        else char
        for char in text.lower()
    ]
    out = [o.upper() if text[idx].isupper() else o for idx, o in enumerate(out)]
    return "".join(out)
