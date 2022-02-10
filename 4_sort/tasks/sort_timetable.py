"""
Дан список имя студента (1 слово) и его баллы за задачи (много чисел).
Отсортировать по убыванию суммы баллов.
При одинаковой сумме отсортировать по имени по возрастанию.
"""
import sys
fin = sys.stdin

def time(s):
    return map(int, s.split(':'))
    
def time2min(t):
    h, m = t
    return h*60 + m
    
def min2time(mm):
    return (mm/60)%24, mm%60
    
def time_plus(t1, t2):
    return min2time(time2min(t1) + time2min(t2))

a = []
for line in fin:
    if not line.rstrip():
        continue
    start, dt = line.split()
    h, m = time_plus(time(start), time(dt))
    a.append((start, dt, ))

def criteria(flight):
    return flight[2]
    
def tprint(h, m):
    return f'{h:02}:{m:02}'

b = sorted(a, key=criteria)

for flight in b:
    print(map(tprint, flight))
