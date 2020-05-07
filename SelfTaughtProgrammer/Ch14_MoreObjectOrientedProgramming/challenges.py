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
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return math.pi * 2 * self.radius


class Square(Shape):
    side_length: float
    square_list = []

    def __init__(self, s: float):
        self.type = "Square"
        self.side_length = s
        self.area = self.area()
        self.perimeter = self.perimeter()
        self.square_list.append(self)

    def area(self) -> float:
        return self.side_length * 2

    def perimeter(self) -> float:
        return self.side_length * 4

    def __str__(self):
        return str(self.side_length)

    def __eq__(self, other):
        if other is not None:
            if isinstance(other, Square):
                if self.side_length == other.side_length:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


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
        return self.long_side * self.short_side

    def perimeter(self):
        return 2 * self.long_side + 2 * self.short_side


def app():
    s1 = Square(5)
    s2 = Square(10)
    s3 = Square(15)
    s4 = Square(20)
    s5 = Square(25)
    s6 = Square(30)
    s7 = Square(20)
    s8 = Square(20)

    r1 = Rectangle(5, 4)

    c1 = Circle(5)

    n1 = None

    print("You have made {} square objects. The side length for each is as follows:".format(len(Square.square_list)))

    for square in Square.square_list:
        print("Square side length: {}".format(square))

    print("Now testing equality...")
    for square in Square.square_list:
        square_length = square.side_length
        is_equal = (s4 == square)
        print("Testing to see if square with side {} is equal to one with side {}: {}".format(s4.side_length,
                                                                                              square_length,
                                                                                              is_equal))
    print("Testing if a {} is equal to a {}: {}".format(s1.type, r1.type, s1 == r1))
    print("Testing if a {} is equal to a {}: {}".format(s1.type, c1.type, s1 == c1))
    print("Testing if a {} is equal to a {}: {}".format(s1.type, "None", s1 == n1))


if __name__ == "__main__":
    app()
