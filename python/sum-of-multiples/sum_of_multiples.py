def sum_of_multiples(limit, multiples):
    total = set()
    for number in multiples:
        if number > 0:
            for i in range(number, limit, number):
                total.add(i)
    return sum(total)
