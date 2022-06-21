def equilateral(sides):
    a, b, c = sides
    return (a == b == c) and is_triangle(a, b, c)


def isosceles(sides):
    a, b, c = sides
    return (a == b or a == c or b == c) and is_triangle(a, b, c)


def scalene(sides):
    a, b, c = sides
    return a != b and a != c and b != c and is_triangle(a, b, c)


def is_triangle(a, b, c):
    return a + b >= c and b + c >= a and a + c >= b and a > 0 and b > 0 and c > 0
