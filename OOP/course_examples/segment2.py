from point import Point

class Segment2:
    """Отрезок на плоскости XY"""

    def __init__(self, p1, p2):
        # концы отрезка
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'{self.p1} {self.p2}'

    def length(self):
        """Длина отрезка"""
        return self.p1.dist(self.p2)

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def left(self):
        """Поворот отрезка на +90 градусов относительно (0,0)"""
        self.p1.left()
        self.p2.left()
