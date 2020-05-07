import math


class Circle:
    diameter: float

    def __init__(self, d:float):
        self.diameter = d

    def area(self):
        return math.pi*(self.diameter/2)**2


def app():
    circle = Circle(2)
    print("The area of the circle is: {}".format(circle.area()))


if __name__ == "__main__":
    app()

