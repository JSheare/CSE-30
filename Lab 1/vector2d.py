# Vector2D class for operating with vector objects
import math as math


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.thresh = 0.000001

    def __add__(self, other):
        if type(other) == type(self):
            x_new = self.x + other.x
            y_new = self.y + other.y
            return Vector2D(x_new, y_new)
        else:
            raise TypeError('TypeError: unsupported operand type')

    def __sub__(self, other):
        if type(other) == type(self):
            x_new = self.x - other.x
            y_new = self.y - other.y
            return Vector2D(x_new, y_new)
        else:
            raise TypeError('TypeError: unsupported operand type')

    def __neg__(self):
        x_new = self.x * -1
        y_new = self.y * -1
        return Vector2D(x_new, y_new)

    def __mul__(self, scalar):
        x_new = self.x * scalar
        y_new = self.y * scalar
        return Vector2D(x_new, y_new)

    def __div__(self, scalar):
        if scalar != 0:
            x_new = self.x/scalar
            y_new = self.y/scalar
            return Vector2D(x_new, y_new)
        else:
            return None

    def __truediv__(self, scalar):
        return self.__div__(scalar)

    def __eq__(self, other):
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True

        return False

    def __ge__(self, other):
        if type(other) == type(self):
            mag = self.magnitude()
            other_mag = other.magnitude()
            if mag >= other_mag:
                return True
            else:
                return False

        else:
            raise TypeError('TypeError: unsupported operand type')

    def __lt__(self, other):
        if type(other) == type(self):
            mag = self.magnitude()
            other_mag = other.magnitude()
            if mag < other_mag:
                return True
            else:
                return False

        else:
            raise TypeError('TypeError: unsupported operand type')

    def __hash__(self):
        return id(self)

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def magnitudeSquared(self):
        return self.x**2 + self.y**2

    def magnitude(self):
        return math.sqrt(self.magnitudeSquared())

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            x_new = self.x/mag
            y_new = self.y/mag
            return Vector2D(x_new, y_new)
        else:
            return None

    def dot(self, other):
        if type(other) == type(self):
            x_new = self.x * other.x
            y_new = self.y * other.y
            return Vector2D(x_new, y_new)
        else:
            raise TypeError('TypeError: unsupported operand type')

    def copy(self):
        return Vector2D(self.x, self.y)


if __name__ == '__main__':
    v1 = Vector2D(2, 3)
    v2 = Vector2D(0.5, -1.5)
    print(f'The sum of {v1} and {v2} is {v1 + v2}')
    print(f'The dot product of {v1} and {v2} is {v1.dot(v2)}')