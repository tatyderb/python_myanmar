"""
Напечатайте числа, отсортировав их по возрастанию четных чисел, нечетные остаются на своих местах.
"""

a = list(map(int, input().split()))
even = sorted([x for x in a if x%2 == 0])

ieven = 0
res = []
for i, x in enumerate(a):
    if x%2 == 0:
        res.append(even[ieven])
        ieven += 1
    else:
        res.append(x)
        
print(*res)        