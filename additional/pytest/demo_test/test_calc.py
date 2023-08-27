import calc
import pytest

TOLERANCE = 1e-9

# в файле могут быть вспомогательные функции, не тесты
def float_equal(a: float, b: float, tolerance: float = TOLERANCE):
    return abs(a - b) < tolerance

# какой-то отдельный тест
def test_something():
    assert (1, 2, 3) == (1, 2, 3)

# отдельный тест, который не должен пройти
def test_failed():
    assert (1, 2, 3) == (4, 5)

@pytest.mark.parametrize("a,b,res", [
    (2, 3, 5),
    (12, 8, 20),
    (-12, 8, -5),       
    (-12, -8, -20)
])
class TestCalcInt:
    def test_add(self, a, b, res):
        assert calc.add(a, b) == res
    '''
    def test_add(self):
        assert calc.add(2, 3) == 5
        assert calc.add(12, 8) == 20
        assert calc.add(-12, 8) == -4
        assert calc.add(-12, -8) == -20
    '''
    def test_sub(self, a, b, res):
        assert calc.sub(a, b) == a - b

    def test_mul(self, a, b, res):
        pass

    def test_div(self, a, b, res):
        pass


class TestCalcFloat:
    def test_add(self):
        assert float_equal(calc.add(0.1, 0.2), 0.3)

    def test_sub(self):
        pass
        
'''
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add(12, 8) == 20
    assert add(-12, 8) == -4
    assert add(-12, -8) == -20
'''