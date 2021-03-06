from math import *


class Unit:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def get_distance_to(self, x, y):
        return hypot(x - self.x, y - self.y)

    def get_distance_to_unit(self, unit):
        return self.get_distance_to(unit.x, unit.y)
