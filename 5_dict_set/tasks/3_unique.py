a = [x for x in input().split()]

d = {}
for x in a:
    d[x] = d.get(x, 0) + 1

print(' '.join([x for x in d.keys() if d[x] == 1]))
