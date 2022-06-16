def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    out = []
    while number != 1:
        if number % 2:  # odd
            number = number * 3 + 1
            out.append(number)
        else:  # even
            number /= 2
            out.append(number)
    return len(out)
