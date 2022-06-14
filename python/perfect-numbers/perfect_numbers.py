def aliquot_sum(number):
    """Returns the sum of its positive divisors.

    :param number: int a positive integer
    :return: int sum of input number positive divisors
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    return sum((num for num in range(1, number // 2 + 1) if not number % num))


def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    asum = aliquot_sum(number)
    if asum == number:
        return "perfect"
    if asum > number:
        return "abundant"
    if asum < number:
        return "deficient"
