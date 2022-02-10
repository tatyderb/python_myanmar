def perimetr(a, b):
    p = (a + b)   # ошибка
    return p

assert(perimetr(3,5) == 16)
assert(perimetr(7,2) == 18)
assert(perimetr(5,5) == 25)
    
w, h = map(int, input().split())
res = perimetr(w, h)
print(res)