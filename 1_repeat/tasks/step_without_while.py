# Дано
#L = 4           # прошли в первый день
#k = 2           # на сколько больше пройдем завтра
L = int(input())
k = int(input())

path = 0        # еще ничего не прошли
step = L        # в первый день пройдем L
i = 0           # еще не закончился первый день


# первый день
path = path + step
i = i + 1       # день закончился
# print(f'за день {i} прошли {step} км, всего {path} км')
step = step + k # готовимся к завтра


# второй день
path = path + step
i = i + 1       # день закончился
# print(f'за день {i} прошли {step} км, всего {path} км')
step = step + k # готовимся к завтра


# третий день
path = path + step
i = i + 1       # день закончился
# print(f'за день {i} прошли {step} км, всего {path} км')
step = step + k # готовимся к завтра

# 4 день
path = path + step
i = i + 1       # день закончился
# print(f'за день {i} прошли {step} км, всего {path} км')
step = step + k # готовимся к завтра

# 5 день
path = path + step
i = i + 1       # день закончился
# print(f'за день {i} прошли {step} км, всего {path} км')
step = step + k # готовимся к завтра

# 6 день
path = path + step
i = i + 1       # день закончился
# print(f'за день {i} прошли {step} км, всего {path} км')
step = step + k # готовимся к завтра

# 7 день
path = path + step
i = i + 1       # день закончился
# print(f'за день {i} прошли {step} км, всего {path} км')
step = step + k # готовимся к завтра

# ответ
# print(f'Всего прошли {path} км')
print(path)