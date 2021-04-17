import sys

file = sys.stdin

name = file.readline()          # отдельно читаем первую строку
name = name.rstrip()            # удаляем пробелы в конце строки

for line in file:               # для каждой остальной строки
    data = line.split(',')      # разделим строку по ,
    if name == data[0]:         # нам нужен только один студент
        grades = list(map(int, data[1:]))
        print(sum(grades) / len(grades))
        break                   # нашли, дальше студентов можно не читать.
