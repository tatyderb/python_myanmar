import sys
import random

a = sys.stdin.readlines()
b = random.shuffle(a)
print(b)
print('-----')
print(''.join(a))
