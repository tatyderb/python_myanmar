import sys
fin = sys.stdin

a = []
for line in fin:
    if not line.rstrip():
        continue
    w, h = line.split()
    w = int(w)
    h = float(h)
    a.append((w, h))    # добавляем в список a кортеж (w, h)

print(a)    # [(166, 55.2), (157, 55.2), (170, 55.2), (175, 90.0), (166, 73.0), (180, 73.0)]