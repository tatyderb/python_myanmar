a = [x for x in input().split()]

d = {}
for x in a:
    d[x] = d.get(x, 0) + 1

print(' '.join(d.keys()))
