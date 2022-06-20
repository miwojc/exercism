import re

METHODS = {
    "plus": "__add__",
    "minus": "__sub__",
    "multiplied by": "__mul__",
    "divided by": "__truediv__",
}


def parse_question(question):
    question = question.removeprefix("What is").removesuffix("?").strip()
    return question


def answer(question):
    question = parse_question(question)
    if not question:
        raise ValueError("syntax error")
    if re.search(re.compile("^-?\d$"), question):
        return int(question)
    foundOp = False
    for name, op in METHODS.items():
        if name in question:
            question = question.replace(name, op)
            foundOp = True
    if not foundOp:
        raise ValueError("unknown operation")
    ret = question.split()
    while len(ret) > 1:
        try:
            x, op, y, *tail = ret
            if op not in METHODS.values():
                raise ValueError("syntax error")
            ret = [int(x).__getattribute__(op)(int(y)), *tail]
        except:
            raise ValueError("syntax error")
    return ret[0]
