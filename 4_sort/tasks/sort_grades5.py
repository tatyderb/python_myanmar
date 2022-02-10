"""
Дан список имя студента (1 слово) и его баллы за задачи (много чисел).
Отсортировать по убыванию суммы баллов.
При одинаковой сумме отсортировать по имени по возрастанию.
"""
import sys
fin = sys.stdin

a = []
for line in fin:
    if not line.rstrip():
        continue
    b = line.split()
    name = b[0]
    grades = list(map(int, b[1:]))
    a.append((name, sum(grades)))    # добавляем в список a кортеж (name, grade)

def criteria(student):
    name, grade = student  # student - это кортеж
    return (-grade, name)

b = sorted(a, key=criteria)

for student in b:
    print(student[0], student[1])
