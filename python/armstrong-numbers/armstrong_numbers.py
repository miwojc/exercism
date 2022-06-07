def is_armstrong_number(number):
    _number = str(number)
    exp = len(_number)
    return number == sum((int(n) ** exp for n in _number))
