import unittest

from point import Point


class PointTestCase(unittest.TestCase):
    def test_create(self):
        """__init__ and __str__ functions"""
        p1 = Point(-5, 2)
        self.assertEqual(str(p1), '-5 2')

        p2 = Point(6, -5)
        self.assertEqual(str(p2), '6 -5')

    def test_move(self):
        p1 = Point(2, -4)
        p1.move(3, 7)
        self.assertEqual(str(p1), '5 3')

        p1.move(dx=-9)
        self.assertEqual(str(p1), '-4 3')

        p1.move(dy=-1)
        self.assertEqual(str(p1), '-4 2')

    def test_dist(self):
        # сначала пишем простые тесты
        p1 = Point(0, 5)
        d = p1.dist(Point(0, 2))
        self.assertEqual(d, 3)

        p1 = Point(-5, 0)
        d = p1.dist(Point(2, 0))
        self.assertEqual(d, 7)

        # посложнее, но можно вычислить без калькулятора
        p1 = Point(4, 0)
        d = p1.dist(Point(0, 3))
        self.assertEqual(d, 5)

        # обязательно тест, где все координаты != 0
        p1 = Point(7, 5)
        d = p1.dist(Point(3, 2))
        self.assertEqual(d, 5)

        # не целая длина
        p1 = Point(7, 5)
        d = p1.dist(Point(-3, 2))
        # сравним 10.44030650891055 с точностью до 4 знаков
        self.assertAlmostEqual(d, 10.4403, places=4)



    def test_left(self):
        # повернем 4 раза и получим ту же точку
        p = Point(3, 4)
        p.left()
        self.assertEqual(str(p), '-4 3')
        p.left()
        self.assertEqual(str(p), '-3 -4')
        p.left()
        self.assertEqual(str(p), '4 -3')
        p.left()
        self.assertEqual(str(p), '3 4')




if __name__ == '__main__':
    unittest.main()
