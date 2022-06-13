# list

lesson = 723108

## Список (list)

* **Строка** - это последовательность символов. Строку нельзя изменить. Можно создать новую строку.
* **Список** (list) - это последовательность любых элементов. Список можно изменить.

### Объявить список

```python
a1 = ['red', 'yellow', 'green']	# список из строк
a2 = [100, -50, 120, 34]		# список из целых чисел
a3 = ['red', 100, 'green', 50]  # список из элементов разных типов
a4 = [-4, [6, 12], 'hi']		# список может элементом другого списка
```
Список из строк:
```python
colors = [
  'violet',   # colors[0]
  'blue',     # colors[1]
  'green',    # colors[2]
  'yellow',   # colors[3]
  'gold',     # colors[4]
  'orange',   # colors[5]
  'red'       # colors[6]
  ]
```

## Список и строка

Строка отличается от списка: 

* Строки нельзя изменить. Список можно изменить.
* В строке только символы. В списке могут быть разные типы: числа, строки, другие списки и объекты.

| Что делаем | список list | строка str | 
|----|----|----|
| создать | `a = [3, -7, 19]` | `s = 'Myanmar'` |
| первый элемент | `a[0]` это 3 | `s[0]` это `'M'` |
| последний элемент | `a[-1]` это 19 | `s[-1]` это `'r'` |
| печать | `print(a)` напечатает `[3, -7, 19]` | `print(s)` напечатает `Myanmar` |
| изменить | `a[0] = 66`, список стал `[66, -7, 19]` | `s[0] = 'm'` **Ошибка! Нельзя изменить строку** |
| длина **len** | `len(a)` равен 3 | `len(s)` равен 7 | 
| a + b | `[1, 2, 3] + [10, 5]` получим `[1, 2, 3, 10, 5]` | `s + ' ' + 'Russia'` получим `'Myanmar Russia'` | 
| `a * 3` | `[10, 7] * 3` получим `[10, 7, 10, 7, 10, 7]` | `'hi'*3` получим `'hihihi'` | 

Список из 5 нулей:
```python
a = [0] * 5		# это a = [0, 0, 0, 0, 0]
```

## Прочитать список строк

Строку можно разделить по пробелам функцией **split()**. Получим список. Каждый элемент списка - это строка.

```python
s = 'violet blue green yellow gold orange red'
colors = s.split()
print(colors)	
```
напечатает
```python
['violet', 'blue', 'green', 'yellow', 'gold', 'orange', 'red']
```
Можно прочитать строку **input()** и сразу ее разделить на слова с помощью **split()**:
```python
colors = input().split()
```
Даны цвета. Нарисуем линии всеми цветами.

Дано:
```python
violet blue green yellow gold orange red
```
Нарисует:
![радуга 7](https://stepik.org/media/attachments/lesson/530425/rainbow7.png)

Дано:
```python
violet blue green yellow gold
```
Нарисует: ![радуга 5](https://stepik.org/media/attachments/lesson/479603/rainbow5.png)

```python
import turtle           

def line(size, col):  # нарисовать линию длины size цвета col
  t.color(col)
  t.fd(size)
  
def goto(x, y):
    t.pu()
    t.setpos((x, y))
    t.pd()

def lines(size, dy):
    x = t.xcor()
    y = t.ycor()
	n = len(colors)				# сколько элементов в списке colors
    for i in range(n):          # i меняется от 0 до n-1
        line(size, colors[i])   # colors[i] - взять цвет номер i из colors
        y -= dy
        goto(x, y)
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

colors = input().split()		# прочитали список цветов
n = len(colors)					# вычислили длину списка
lines(100, 20)				    # нарисовали линии цветами colors

turtle.done()    
```

## TASKTEXT n отрезков в радуге

Дан список цветов на одной строке через пробел.

На следующей строке дано число $n$. Нарисовать $n$ отрезков этими цветами.

Дано:
```python
violet blue green yellow gold orange red
9
```
Нарисует:

![радуга 9](https://stepik.org/media/attachments/lesson/723108/14_2_lines9.png)

Дано:
```python
red yellow green
6
```
Нарисует:

![светофор](https://stepik.org/media/attachments/lesson/723108/14_2_lines6.png)

## Цикл по элементам списка

Как для строк, цикл для списка бывает по элементам или по индексам (номерам).

### Цикл по элементам

```python
a = ['green', 'yellow', 'red']
for col in a:
	print(col)
```
напечатает
```python
green
yellow
red
```

### Цикл по индексам элементов

```python
a = ['green', 'yellow', 'red']
for i in range(len(a)):
	print(i, a[i])
```
напечатает
```python
0 green
1 yellow
2 red
```

## Запишем точки в список

* Черепаха рисует квадрат и записывает его вершины в список. 
* У квадрата 4 вершины. Сначала создадим список `[0, 0, 0, 0]`, потом вместо 0 будем записывать точку. 
* Элементы списка можно изменять. Будем изменять одно **число** 0 на одну **точку**.

```python
import turtle

def sq(size):
    points = [0, 0, 0, 0]
    # черепаха идет на первую точку
    for i in range(4):          # i меняется 0, 1, 2, 3
        points[i] = t.pos()     # запоминаем позицию черепахи
        t.fd(size)              # идем к следующей вершине квадрата
        t.lt(90)
    # тут закончился цикл
    # после цикла возвращаем список точек вершин квадрата
    return points


t = turtle.Turtle()
t.shape('turtle')
t.width(5)
t.color('blue')

points = sq(100)
print(points)   	# [(0.00,0.00), (100.00,0.00), (100.00,100.00), (0.00,100.00)]

turtle.done()
```
Напечатает 
```python
[(0.00,0.00), (100.00,0.00), (100.00,100.00), (0.00,100.00)]
```
то есть
```python
points = [
	(0, 0),		# points[0]
	(100, 0),	# points[1]
	(100, 100),	# points[2]
	(0, 100)	# points[3]
]	
```

## Треугольник

Зададим точки вершин треугольника в виде списка из 3 точек. Напишем функцию, которая по списку точек рисует треугольник.

Функция **tri(points)** рисует треугольник по точкам, заданным в списке **points**.

![треугольник](https://stepik.org/media/attachments/lesson/723108/14_2_tri.png)

Функцию `tri(points)` будем использовать так:
```python
tpoints = [(100, 0), (0, 50), (100, 100)]  # зададим список точек
tri(tpoints)
```
Напишем функцию  `tri(points)` (самый простой вариант). Явно перечисляем точки с номером 0, 1, 2 и опять 0:
```python
def tri(points):
    # черепаха идет на первую точку
    t.pu()
    t.goto(points[0])
    t.pd()
    t.begin_fill()
    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[0])
    t.end_fill()
```
Добавим цикл (стало больше кода и код стал хуже читаться):
```python
def tri(points):
    # черепаха идет на первую точку
    t.pu()
    t.goto(points[0])
    t.pd()
    t.begin_fill()
	for i in range(1, 3):
		t.goto(points[i])
    t.goto(points[0])
    t.end_fill()
```
Начнем рисовать с последней точки: 2, 0, 1, 2. Вспомним, что индекс последней точки -1.
```python
def tri(points):
    # черепаха идет на ПОСЛЕДНЮЮ точку
    t.pu()
    t.goto(points[-1])
    t.pd()
    t.begin_fill()
	for i in range(3):
		t.goto(points[i])
    t.end_fill()
```

Вся программа:
```python
import turtle

def tri(points):
    # черепаха идет на ПОСЛЕДНЮЮ точку
    t.pu()
    t.goto(points[-1])
    t.pd()
    t.begin_fill()
	for i in range(3):
		t.goto(points[i])
    t.end_fill()

t = turtle.Turtle()
t.shape('turtle')
t.width(5)
t.color('blue')

tpoints = [(100, 0), (0, 50), (100, 100)]
tri(tpoints)

turtle.done()
```

## TASKTEXT Флаг

* Запомнить вершины прямоугольника в список.
* Вычислить точку пересечения диагоналей прямоугольника (центр прямоугольника). Сохранить эту точку в отдельную переменную.
* Взять функцию `tri(points)` с предыдущего шага и нарисовать фигуру:

![флаг](https://stepik.org/media/attachments/lesson/509283/trk.png)

## TASKTEXT Узор

Мы [рисовали узор](https://stepik.org/lesson/509284/step/7). Перепишите задачу, используя списки.

![большой узор](https://stepik.org/media/attachments/lesson/509283/uzor_rect.png) 

![часть узора](https://stepik.org/media/attachments/lesson/509283/uzor_v1en.png)

Делаем из координат `x` и `y` точку `p`:
```python
p = (x, y)
```
Делаем из точки `p` координаты `x` и `y`:
```python
x, y = p
```
или
```python
x, y = t.pos()
```




