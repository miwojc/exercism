def parse_numbers(question):
    numbers = []
    for c in question[:-1].split():
        c = c.strip()
        try:
            numbers.append(int(c))
        except ValueError:
            pass
    return numbers


def parse_operator(question):
    return [
        c.strip()
        for c in question.split()
        if c in ["plus", "minus", "multiplied", "divided"]
    ][0]


def answer(question):
    numbers = parse_numbers(question)
    operator = parse_operator(question)
    if operator == "plus":
        return sum(numbers)
    elif operator == "minus":
        return numbers[0] - numbers[1]
    elif operator == "multiplied":
        return numbers[0] * numbers[1]
    elif operator == "divided":
        return numbers[0] / numbers[1]
