class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        return Rational(self.numer*other.denom + other.numer*self.denom, self.denom*other.denom)

    def __sub__(self, other):
        return Rational(self.numer*other.denom - other.numer*self.denom, self.denom*other.denom)

    def __mul__(self, other):
        return Rational(self.numer*other.numer, self.denom*other.denom)

    def __truediv__(self, other):
        return Rational(self.numer*other.denom, self.denom*other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power >= 0:
            return Rational(self.numer**power, self.denom**power)
        power_abs = abs(power)
        return Rational(self.denom**power_abs, self.numer**power_abs)

    def __rpow__(self, base):
        """Exponentiation of a real number `x` to a rational number `r = a/b` is `x^(a/b) = root(x^a, b)`,
        where `root(p, q)` is the `q`th root of `p`."""
        return base**(self.numer/self.denom)