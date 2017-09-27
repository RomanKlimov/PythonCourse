from math import gcd


class RationalFraction:
    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def reduce(self):
        g = gcd(self.x, self.y)
        self.x = self.x // g
        self.y = self.y // g

    def __str__(self):
        return str(self.x) + "/" + str(self.y)

    def __add__(self, other):
        x = self.y
        y = other.y

        while x != y:
            if x > y:
                x = x - y
            else:
                y = y - x

        lcd = self.y * other.y // x

        obj = RationalFraction(self.x * lcd // self.y + other.x * lcd // other.y, lcd)
        obj.reduce()
        return obj

    def __sub__(self, other):
        x = self.y
        y = other.y

        while x != y:
            if x > y:
                x = x - y
            else:
                y = y - x

        lcd = self.y * other.y // x

        obj = RationalFraction(self.x * lcd // self.y - other.x * lcd // other.y, lcd)
        obj.reduce()
        return obj

    def __mul__(self, other):
        obj = RationalFraction(self.x * other.x, self.y * other.y)
        obj.reduce()
        return obj

    def __truediv__(self, other):
        obj = RationalFraction(self.x * other.y, self.y * other.x)
        obj.reduce()
        return obj

    def value(self):
        return self.x / self.y

    def __eq__(self, other):
        true_Self = RationalFraction(self.x, self.y)
        true_Self.reduce()
        true_Other = RationalFraction(other.x, other.y)
        true_Other.reduce()
        if true_Other.x == true_Other.x and true_Self.y == true_Other.y:
            return True
        return False

    def numberPart(self):
        return self.x // self.y
