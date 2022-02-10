# if elif else

lesson = 526314

## TASKTEXT Задача: внутри круга

* Даны координаты точки (x, y)
* Даны координаты центра окружности (x0, y0) и ее радиуса r

* Скопируйте функцию **circle(x, y, r)**. 
	* Нарисовать центр окружности в точке (x0, y0). 
	* Нарисовать окружность радиуса r.
* Напишите функцию **cdot(x, y, x0, y0, r)**. Она рисует точку.	
	* Нарисовать точку **внутри** окружности **зеленой** (green), иначе нарисовать точку желтой (yellow).

Подсказка: посчитайте расстояние от точки до центра окружности.

```
x0 = 0
y0 = -10
r = 100
circle(x0, y0, r)
cdot(-70, -40, x0, y0, r)     # зеленая
cdot(80, 60, x0, y0, r)       # желтая
cdot(50, 40, x0, y0, r)       # зеленая на рисунке
cdot(-100, -50, x0, y0, r)    # желтая на рисунке
```

![точки](https://stepik.org/media/attachments/lesson/479601/06_circle_in.png)

Хорошо: нарисовать много точек и проверить решение задачи.

## TASKTEXT Задача: большой желтый, маленький красный

Написать функцию **sq2(size1, size2)**. Она рисует 2 квадрата размером `size1` и другой размером `size2`

* Нарисуйте сначала большой квадрат желтый.
* Потом маленький квадрат красный.

```python
sq2(50, 100)
```
![квадраты](https://stepik.org/media/attachments/lesson/479601/08_max1.png)

```python
sq2(170, 40)
```
![квадраты](https://stepik.org/media/attachments/lesson/479601/08_max2.png)

## elif это else if

* Дана вертикальная линия x0
* Дана точка (x,y)

* Возьмите функцию **vline(x0)**. Нарисуйте вертикальную линию $x=x0$.
* Напишите функцию **cdot(x, y, x0)**. Она рисует точку $(x, y)$. Цвет точки:
    * красный, если точка справа от линии.
    * синий, если точка слева от линии
    * желтый, если точка на линии.

Напишем функцию **get_color(x, y, x0)**. Она возвращает (return) цвет точки.

```
get_color(120, 10, 100)	# красная точка, справа
get_color(20, -50, 100)	# синяя точка, слева
get_color(100, 20, 100)	# желтая точка, на линии
```

![точки](https://stepik.org/media/attachments/lesson/479601/07_dot3.png)

Напишем функцию **get_color(x, y, x0)**. Она возвращает цвет точки.
```python
def get_color(x, y, x0):
    if x > x0:			# справа
        return 'red'
	else:				# слева или на линии
		if x == x0:			# на линии
			return 'yellow'
		else:				# слева
			return 'blue'
```
Для таких случаев в python есть специальный оператор `elif` от else + if.
```python
def get_color(x, y, x0):
    if x > x0:			# справа
        return 'red'
	elif x == x0:		# на линии
		return 'yellow'
	else:				# слева
		return 'blue'
```
Так лучше читать. Есть 3 случая. Мы их пишем. 

* if - 1 раз
* else - 1 или 0 раз
* elif - 0 или **много** раз, сколько нужно в задаче.

Вся программа:
```python
import turtle

def moveto(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()

def vline(x):
    moveto(x, -100)
    t.goto(x, 100)

def get_color(x, y, x0):
    if x > x0:
        return 'red'
    elif x == x0:
        return 'yellow'
    else:
        return 'blue'
        
def dot(x, y, x0):
    col = get_color(x, y, x0)
    t.color(col)   
    moveto(x, y)
    t.dot(10)
       
   
t = turtle.Turtle()
t.width(3)

x0 = int(input())
x, y = map(int, input().split())

vline(x0)
dot(x, y, x0)

turtle.done()    
```

Написать функцию **sq2(size1, size2)**. Она рисует 2 квадрата размером `size1` и другой размером `size2`

* Если квадраты разные,
	* Нарисуйте сначала большой квадрат желтый.
	* Потом маленький квадрат красный.
* Если квадраты одинаковые, нарисуйте 1 раз синий квадрат.

```python
sq2(50, 100)
```
![квадраты](https://stepik.org/media/attachments/lesson/479601/08_max1.png)

```python
sq2(170, 40)
```
![квадраты](https://stepik.org/media/attachments/lesson/479601/08_max2.png)

Пример 3:
```
sq2(70, 70)
```
![квадраты](https://stepik.org/media/attachments/lesson/479601/08_max3.png)

## Между

* Дан отрезок `[a, b]`. Цвет черный. Всегда a < b
* Дана точка x. Цвет точки
    * красный, если точка лежит на отрезке, $x \in [a, b]$
    * синий, если точка лежит вне отрезка, $x \notin [a, b]$
    
* Напишем функцию **cdot(x, a, b)**. Она рисует точку нужным цветом.
* Напишем функцию **between(x, a, b)**. Она возвращает:
    * True, если $x \in [a, b]$
    * Иначе она возвращает False. 
    
Специальные слова python **True** (да) и **False** (нет).   

```python
def between(x, a, b):
    if a <= x:             # дальше a
        if x <= b:         # дальше а и ближе b
            return True
        else:              # дальше а и дальше b
            return False
    else:                  # ближе a
        return False
        
def dot(x, a, b):
    if between(x, a, b):
        t.color('red')
    else:
        t.color('blue')
    moveto(x, 0)
    t.dot(5)
``` 

## and, or

Можно проще. 

* **and** - и то, и другое одновременно, 
* **or** - хоть что-нибудь.
```python
def between3(x, a, b):
    if a <= x and x <= b:
        return True
    else:
        return False
```

## Python и математика

Python любит математиков. Математики любят python. Можно написать так:
```python
def between3(x, a, b):
    if a <= x <= b:
        return True
    else:
        return False
```

Еще проще:
```python
def between3(x, a, b):
    return a <= x <= b:
```
Само выражение `a <= x <= b` будет True или False. 

