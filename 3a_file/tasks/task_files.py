filename = 'lesson.txt'
count = 0
with open(filename) as fin:
    for line in fin:
        if line.strip().endswith('.py'):
            count += 1
            
print(count)
