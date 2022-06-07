def is_armstrong_number(number):
    _number = str(number)
    return number == sum((int(n) ** len(_number) for n in _number))
