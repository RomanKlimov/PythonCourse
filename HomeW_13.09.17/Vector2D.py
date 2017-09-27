import math

class Vector2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) == type(self):
            return self.x * other.x + self.y * other.y
        else:
            return Vector2D(self.x * other, self.y * other)

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False




