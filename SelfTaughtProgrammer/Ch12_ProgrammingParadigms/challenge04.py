class Hexagon:
    side1: float
    side2: float
    side3: float
    side4: float
    side5: float
    side6: float

    def __init__(self, a, b, c, d, e, f):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d
        self.side5 = e
        self.side6 = f

    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6


def app():
    hexagon = Hexagon(1, 1, 1, 1, 1, 1)
    print(hexagon.perimeter())


if __name__ == "__main__":
    app()