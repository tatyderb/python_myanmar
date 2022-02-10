import sys
file = sys.stdin

s = file.readline()
print(f'First: [{s}]')

s = file.readline()
print(f'Second: [{s}]')

for s in file:
    print(f'Other: [{s}]')
