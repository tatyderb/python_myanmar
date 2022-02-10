# Отсортировать убыванию оценки.
# При одинаковых оценках отсортировать по имени по возрастанию.
import sys
fin = sys.stdin

a = []
for line in fin:
    if not line.rstrip():
        continue
    name, grade = line.split()
    a.append((name, int(grade)))    # добавляем в список a кортеж (name, grade)

def criteria(student):
    name, grade = student  # student - это кортеж
    return (-grade, name)

b = sorted(a, key=criteria)

for student in b:
    print(student[0], student[1])
