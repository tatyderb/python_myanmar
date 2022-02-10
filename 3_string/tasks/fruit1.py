import sys

total = 0                       # в total будет сумма килограмм

file = sys.stdin

for line in file:               # для каждой строки с клавиатуры
    fruit, kg = line.split()    # разделим строку по пробелу на фрукт и вес
    kg = float(kg)              # вес - это число
    total = total + kg
    print(f'{fruit} weight={kg} total={total}')
    
print(total)
