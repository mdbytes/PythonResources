from abc import ABC, abstractmethod
import math


class Shape(ABC):
    type: str
    area: float
    perimeter: float

    def __init__(self, t: str, a: float, p: float):
        self.type = t
        self.area = a
        self.perimeter = p

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    radius: float

    def __init__(self, r: float):
        self.type = "Circle"
        self.radius = r
        self.area = self.area()
        self.perimeter = self.perimeter()

    def area(self) -> float:
        return math.pi*self.radius**2

    def perimeter(self) -> float:
        return math.pi*2*self.radius


class Square(Shape):
    side_length: float

    def __init__(self, s: float):
        self.type = "Square"
        self.side_length = s
        self.area = self.area()
        self.perimeter = self.perimeter()

    def area(self) -> float:
        return self.side_length*2

    def perimeter(self) -> float:
        return self.side_length*4


class Rectangle(Shape):
    long_side: float
    short_side: float

    def __init__(self, l: float, s: float):
        self.type = "Rectangle"
        self.long_side = l
        self.short_side = s
        self.area = self.area()
        self.perimeter = self.perimeter()

    def area(self):
        return self.long_side*self.short_side

    def perimeter(self):
        return 2*self.long_side + 2*self.short_side


def app():
    shape = Circle(5)
    print("You have made a {} with perimeter of {} and area of {}".format(shape.type, shape.perimeter, shape.area))
    shape = Square(5)
    print("You have made a {} with perimeter of {} and area of {}".format(shape.type, shape.perimeter, shape.area))
    shape = Rectangle(5, 4)
    print("You have made a {} with perimeter of {} and area of {}".format(shape.type, shape.perimeter, shape.area))


if __name__ == "__main__":
    app()


