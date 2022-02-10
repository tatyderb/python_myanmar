x = 0
y = 0
while True:
    s = input().strip()     # уберем лишние пробельные символы на конце
    if s == 'Treasure!':
        print(x, y)
        break

    direction, step = s.split()
    step = int(step)

    if direction == 'north':
        y += step
    elif direction == 'south':
        y -= step
    elif direction == 'east':
        x += step
    elif direction == 'west':
        x -= step
    else:
        print(f'Error: direction={direction}')
        break
