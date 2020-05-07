import datetime


class Apple:
    type: str
    weight: float
    color: str
    date_picked: datetime

    def __init__(self, t: str, w: float, c: str, d: datetime):
        self.type = t
        self.weight = w
        self.color = c
        self.date_picked = d
