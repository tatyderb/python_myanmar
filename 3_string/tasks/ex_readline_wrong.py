import sys
file = sys.stdin

while True:
    s = file.readline()
    if s == '':
        break
    print(f'[{s}]')
