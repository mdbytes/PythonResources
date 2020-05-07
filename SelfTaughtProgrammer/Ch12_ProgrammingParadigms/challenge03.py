import math


class RightTriangle:
    side1: float
    side2: float
    side3: float

    def __init__(self, a: float, b: float):
        self.side1 = a
        self.side2 = b
        self.side3 = math.sqrt(a ** 2 + b ** 2)

    def area(self):
        return self.side1 * self.side2 / 2


def app():
    triangle = RightTriangle(2, 3)
    print(triangle.area())


if __name__ == "__main__":
    app()