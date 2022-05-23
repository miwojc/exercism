import re

def abbreviate(words):
    return "".join(w[0].upper() for w in re.findall("[a-zA-Z']+", words))