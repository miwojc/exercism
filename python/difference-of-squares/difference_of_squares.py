def square_of_sum(number):
    return sum((number for number in range(1, number + 1))) ** 2


def sum_of_squares(number):
    return sum(number**2 for number in range(1, number + 1))


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
