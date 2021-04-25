a = [int(x) for x in input().split()]

d = {}
for x in a:
    d[x] = d.get(x, 0) + 1

# print(d)
for k in d:
    print(k, d[k])
