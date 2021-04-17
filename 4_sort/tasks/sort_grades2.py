import sys
fin = sys.stdin

a = []
for line in fin:
    if not line.rstrip():
        continue
    name, grade = line.split()
    a.append((name, int(grade)))    # добавляем в список a кортеж (name, grade)

def by_grade(student):
    name, grade = student  # student - это кортеж
    return grade

b = sorted(a, key=by_grade, reverse=True)

for student in b:
    print(student[0], student[1])
