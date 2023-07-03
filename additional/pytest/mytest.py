import calc

TOLERANCE = 1e-9
def float_equal(a: float, b: float, tolerance :float = TOLERANCE):
    return abs(a - b) < tolerance

# assert calc.add(2, 3) == 5

assert calc.add(2, 3) == 5, f'Сложение целых положительных чисел'

assert calc.add(2, 3) == 5
assert calc.add(12, 8) == 20
assert calc.add(-12, 8) == -4
assert calc.add(-12, -8) == -20
res = calc.add(0.1, 0.2)
# assert res == 0.3, f'calc.add(0.1, 0.2) = {res} != 0.3'
assert float_equal(res, 0.3), f'calc.add(0.1, 0.2) = {res} != 0.3'
