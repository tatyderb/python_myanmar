import math


class Point:
    """Точка на плоскости ХУ"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'

    def __str__(self):
        return f'{self.x} {self.y}'

    def dist(self, other=None):
        if other is None:
            other = ZERO
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)

    def left(self):
        """
        Rotate left about (0,0)
        y' = x
        x' = -y
        """
        xnew = - self.y
        ynew = self.x
        self.x = xnew
        self.y = ynew

    def move(self, dx=0, dy=0):
        """Move point by dx, dy"""
        self.x += dx
        self.y += dy


ZERO = Point(0, 0)
