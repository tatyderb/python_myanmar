# Фракталы

lesson = 479604

## Повторение рекурсии

* Нарисуем дерево. 
* В первый год вырастает ветка длиной size.
* Каждый следующий год из 1 ветки вырастают 
    * 2 ветки 
    * размером size-d 
    * под углом +ang и -ang к направлению старой ветки.

* tree(size, d, ang, n, i) - функция. Она рисует дерево рекурсивно.
    * n - сколько лет осталось расти дереву
    * size - длина веток в этом году
    * size - d - длина веток в следующем году.
    * ang - угол поворота ветки следующего года

Функция возвращает черепаху в точку старта.

```python
tree(100, 20, 30, 1)   # дерево растет 1 год
```
нарисует 
![дерево 1 год](https://stepik.org/media/attachments/lesson/479604/e12_1_1.png)

```python
tree(100, 20, 30, 3)   # дерево растет 3 года
```
нарисует 
![дерево 3 года](https://stepik.org/media/attachments/lesson/479604/e12_1_3.png)

```python
tree(100, 20, 30, 5)   # дерево растет 5 лет
```
нарисует 
![дерево 5 лет](https://stepik.org/media/attachments/lesson/479604/e12_1_5.png)

* Функция рисует ветки для 1 года
    * рисует ветку этого года
    * идет рисовать левую ветку следующего года (на следующий год длина ветки будет size-d, расти дереву нужно будет n-1 год)
    * идет рисовать правую ветку
    * возвращается в начало
    
```python
'''
tree(size, d, ang, n) - рисовать дерево, которое росло n лет.
Пусть дерево каждый год вырастает на 1 уровень, 
каждая ветка дает 2 новые веточки, 
отклоняющиеся на угол +ang и -ang от направления роста ветки. 
Размер ветки size, а веточки меньше ее на d.
'''
def tree(size, d, ang, n):
  if n == 0:                  # дерево закончило расти, возвращаемся
    return
  
  t.fd(size)                  # рисуем ветку
  t.left(ang)                 # поворачиваемся рисовать левую веточку
  tree(size-d, d, ang, n-1)   # рисуем левое поддерево (веточку и дальше)
                              # после этой функции черепаха будет в том же месте
                              # и повернута на тот же угол
  t.left(-2*ang)              # поворачиваемся рисовать правую веточку
  tree(size-d, d, ang,  n-1)  # рисуем правое поддерево (веточку и дальше)
                              # после этой функции черепаха будет в том же месте
  t.left(ang)                 # возвращаем направление ветки
  t.fd(-size)                 # возвращаемся в начало ветки
                              # конец функции
```    
 
Вся программа:
```python
import turtle           
import time

# tree(size, d, ang, n) - рисовать дерево, оно росло n лет.
# Пусть дерево каждый год вырастает на 1 этаж, 
# каждая ветка дает 2 новые веточки, 
# новые веточки отклоняются на угол +ang и -ang от направления роста ветки. 
# Размер ветки size, а веточки меньше ее на d.

def tree(size, d, ang, n):
  if n == 0:                  # дерево закончило расти, возвращаемся
    return
  
  t.fd(size)                  # рисуем ветку
  t.left(ang)                 # поворачиваемся рисовать левую веточку
  tree(size-d, d, ang, n-1)   # рисуем левое поддерево (веточку и дальше)
                              # после этой функции черепаха будет в том же месте
                              # и повернута на тот же угол
  t.left(-2*ang)              # поворачиваемся рисовать правую веточку
  tree(size-d, d, ang,  n-1)  # рисуем правое поддерево (веточку и дальше)
                              # после этой функции черепаха будет в том же месте
  t.left(ang)                 # возвращаем направление ветки
  t.fd(-size)                 # возвращаемся в начало ветки
                              # конец функции

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

t.seth(90)
t.up()
t.bk(100)
t.down()
t.color('brown')

tree(100, 20, 30, 5)

turtle.done() 
```

## TASKTEXT Задача: на дереве зеленые листья

Ветки последнего года нарисовать зеленые green, другие ветки коричневые brown.

```python
tree(100, 20, 30, 1)   # дерево растет 1 год
```
нарисует 
![дерево 1 год](https://stepik.org/media/attachments/lesson/479604/t12_1_1.png)

```python
tree(100, 20, 30, 3)   # дерево растет 3 года
```
нарисует 
![дерево 3 года](https://stepik.org/media/attachments/lesson/479604/t12_1_3.png)

```python
tree(100, 20, 30, 5)   # дерево растет 5 лет
```
нарисует 
![дерево 5 лет](https://stepik.org/media/attachments/lesson/479604/t12_1_5.png)

## Фракталы (теория)

https://en.wikipedia.org/wiki/Fractal 

Фракта́л (лат. fractus — дроблёный, сломанный, разбитый) — математическое множество, обладающее свойством самоподобия (объект, в точности или приближённо совпадающий с частью себя самого, то есть целое имеет ту же форму, что и одна или более частей.

Список фракталов (английский язык):  https://en.wikipedia.org/wiki/List_of_fractals_by_Hausdorff_dimension 

Надо нарисовать фрактал. Будем 1 линию заменять на много линий. Так для каждой линии.

В разделе используются изображения из википедии.

## Пример. Кривая Коха

https://en.wikipedia.org/wiki/Koch_snowflake 
Попробуем сделать zoom любой части фрактала:

![кривая Коха](https://stepik.org/media/attachments/lesson/479604/Kochsim.gif)

По шагам:
Это снежинка Коха. У нее увеличивается глубина.

![кривая Коха](https://stepik.org/media/attachments/lesson/479604/Von_Koch_curve.gif)


Подробнее:

![кривая Коха поэтапно](https://stepik.org/media/attachments/lesson/479604/Koch_curve_construction.png)

## Рисуем кривую Коха

Функция  **koch_line(size, n)** рисует на отрезке длины size кривую Коха и делает n итераций (рисует кривую Коха глубины n).

```python
koch_line(200, 0)    # глубина 0, 1 линия
```
![koch_line(200, 0)](https://stepik.org/media/attachments/lesson/479604/e12_2_0.png)

```python
 koch_line(200, 1)   # глубина 1, 1 линия -> 4 линии
```
![koch_line(200, 1)](https://stepik.org/media/attachments/lesson/479604/e12_2_1.png)

```python
 koch_line(200, 1)   # глубина 1, 1 линия -> 4 линии
```
![koch_line(200, 3)](https://stepik.org/media/attachments/lesson/479604/e12_2_3.png)

```python
def koch_line(size, n):
  if n == 0:        # рисуем линию и дальше не идем
    t.fd(size)
    return
    
  a = size/3        # иначе разбиваем отрезок 
                    # и вместо него делаем набор отрезков  
  koch_line(a, n-1)
  t.left(60)
  koch_line(a, n-1)
  t.right(120)
  koch_line(a, n-1)
  t.left(60)
  koch_line(a, n-1)
```

## Кривые Коха разной глубины

Нарисуем кривые Коха разной глубины разным цветом на 1 рисунке.

![кривые Коха](https://stepik.org/media/attachments/lesson/479604/e12_2_all.png)

Вспомните, как мы определяли список из разных цветов и брали следующий цвет:
```python
tones = [
  'yellow',   # tones[0]
  'gold',     # tones[1]
  'orange',   # tones[2]
  'red',      # tones[3]
  'violet',   # tones[4]
  'blue',     # tones[5]
  'green'     # tones[6]
  ]
```

Рисуем кривые Коха глубины от 0 до 4 цветами от `tones[0]` до `tones[4]`:
```python
for i in range(5):    # i = 0..4
  p0 = t.pos()           # запомнили начальную позицию в p0
  t.color(tones[i])      # новой итерации - новый цвет
  koch_line(300, i)      # нарисовали кривую Коха глубины i
  
  t.up()                 # вернулись на начальную позицию
  t.goto(p0)
  t.down()
  time.sleep(1)          # ждем 1 секунду
```

Вся программа:
```python
import turtle           
import time

tones = [
  'yellow',   # tones[0]
  'gold',     # tones[1]
  'orange',   # tones[2]
  'red',      # tones[3]
  'violet',   # tones[4]
  'blue',     # tones[5]
  'green'     # tones[6]
  ]

def koch_line(size, n):
  if n == 0:        # рисуем линию и дальше не идем
    t.fd(size)
    return
    
  a = size/3.0      # иначе разбиваем отрезок 
                    # и вместо него рисуем много отрезков  
  koch_line(a, n-1)
  t.left(60)
  koch_line(a, n-1)
  t.right(120)
  koch_line(a, n-1)
  t.left(60)
  koch_line(a, n-1)
                    # конец функции

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

for i in range(5):    # i = 0..4
  p0 = t.pos()           # запомнили начальную позицию в p0
  t.color(tones[i])      # новой итерации - новый цвет
  koch_line(300, i)      # нарисовали кривую Коха глубины i
  t.stamp()              # тут закончили рисовать линию
  
  t.pu()                 # вернулись на начальную позицию
  t.goto(p0)
  t.pd()
  time.sleep(1)          # ждем 1 секунду

turtle.done()
```

## TASKTEXT Задача: снежинка Коха

Функция  koch_tri(size, n) рисует снежинку Коха глубины n.
```python
koch_tri(200, 0)
koch_tri(200, 1)
koch_tri(200, 2)
koch_tri(200, 3)
```
нарисуют 
![снежинки Коха](https://stepik.org/media/attachments/lesson/479604/KochFlake.png)

Нарисуйте:
![снежинка Коха разной глубины](https://stepik.org/media/attachments/lesson/479604/koch_flake_task.png)

## TASKTEXT Задача: Кубическая кривая 1 типа

Кривую рисуют так (глубина увеличивается): 

![этапы](https://stepik.org/media/attachments/lesson/479604/koch_1_iter.png)

Большая глубина:

![этапы](https://stepik.org/media/attachments/lesson/479604/koch_1_res.png)

Нарисовать:
![этапы](https://stepik.org/media/attachments/lesson/479604/t12_2a.png)

## TASKTEXT Задача: Кубическая кривая 2 типа (кривая Минковского)

Кривую рисуют так (глубина увеличивается): 

![этапы](https://stepik.org/media/attachments/lesson/479604/03_cube2.png)

Большая глубина:

![этапы](https://stepik.org/media/attachments/lesson/479604/koch_2_res.png)

Анимация по шагам:

![этапы](https://stepik.org/media/attachments/lesson/479604/Minkowsky01.gif)

Нарисовать:
![этапы](https://stepik.org/media/attachments/lesson/479604/t12_2b.png)

## TASKTEXT Задача: Кривая Леви

Написать функцию **levi_line(size, n)**. Она рисует на отрезке size кривую Леви глубины n.

Увеличение глубины:
![этапы](https://stepik.org/media/attachments/lesson/479604/levi_iter.png)

Анимация по шагам:

![этапы](https://stepik.org/media/attachments/lesson/479604/levi_res.gif)

Нарисовать:
![этапы](https://stepik.org/media/attachments/lesson/479604/t12_2b.png)

```python
levi_line(200, 4)
```
нарисует ![levi_line(200, 4)](https://stepik.org/media/attachments/lesson/479604/t12_levi_4.png)

```python
levi_line(200, 7)
```
нарисует ![levi_line(200, 7)](https://stepik.org/media/attachments/lesson/479604/t12_levi_7.png)

```python
levi_line(200, 10)
```
нарисует ![levi_line(200, 10)](https://stepik.org/media/attachments/lesson/479604/t12_levi_10.png)

## TASKTEXT Задача. Крест Висека - 1

Вместо 1 квадрата рисуют много квадратов.
Глубина увеличивается

![этапы](https://stepik.org/media/attachments/lesson/479604/cross_iter2.png)

Написать функцию **cross(size, n)** и нарисовать

![задача](https://stepik.org/media/attachments/lesson/479604/t12_cross1.png)

## TASKTEXT Задача. Крест Висека - 2

Вместо 1 квадрата рисуют много квадратов.
Глубина увеличивается

![этапы](https://stepik.org/media/attachments/lesson/479604/cross_iter1.png)

Написать функцию **cross(size, n)** и нарисовать

![задача](https://stepik.org/media/attachments/lesson/479604/t12_cross2.png)

## TASKTEXT Задача. Ковер Серпинского

Ковер Серпинского с увеличением глубины строится так: 

![этапы](https://stepik.org/media/attachments/lesson/479604/Animated_Sierpinski_carpet.gif)

Написать функцию carpet(size, n). Она рисует ковер Серпинского размера size и глубины n.
```python
carpet(200, 3)
```
![задача](https://stepik.org/media/attachments/lesson/479604/t12_carpet_sq.png)


## TASKTEXT Задача. Ковер Серпинского треугольный

Ковер Серпинского с увеличением глубины строится так: 

![этапы](https://stepik.org/media/attachments/lesson/479604/Sierpinsky_triangle.png)

Анимация:
![этапы](https://stepik.org/media/attachments/lesson/479604/Animated_construction_of_Sierpinski_Triangle.gif)


Написать функцию septri(size, n). Она рисует ковер Серпинского размера size и глубины n.
```python
septri(200, 3)
```
![задача](https://stepik.org/media/attachments/lesson/479604/t12_carpet_tr.png)

## TASKTEXT Задача. Дерево Пифагора

Нарисуйте один вариант. Какой вы хотите.

* Вариант 1 и 2 - легкий.
* Вариант 4 самый сложный.

Дерево Пифагора делают так (глубина увеличивается) 

![задача](https://stepik.org/media/attachments/lesson/479604/PythagorasTree.gif)

* Первое дерево обычное.
* Второе дерево "обдуваемое ветром".

### Вариант 1. Классическое дерево Пифагора (ang = 45)

Написать функцию tree(size, n). Она строит дерево Пифагора глубины n. Размер первого квадрата size.

На квадрате построен **равнобедренный треугольник с углом при основании 45 градусов**.

Построенное дерево глубины 7.

```python
tree(50, 7)
```

![задача](https://stepik.org/media/attachments/lesson/479604/t12_pitree0.png)

### Вариант 2 Классическое дерево Пифагора (ang = 30)

Написать функцию tree(size, n). Она строит дерево Пифагора глубины n. Размер первого квадрата size.

На квадрате построен **равнобедренный треугольник с углом при основании 30 градусов**.

Построенное дерево глубины 7.

```python
tree(50, 7)
```

![задача](https://stepik.org/media/attachments/lesson/479604/t12_pitree30s.png)

### Вариант 3 Дерево Пифагора (ang = 30), обдуваемое ветром

Написать функцию tree(size, n). Она строит дерево Пифагора глубины n. Размер первого квадрата size.

На квадрате построен **ПРЯМОУГОЛЬНЫЙ треугольник с углом при основании 30 градусов**.

Построенное дерево глубины 7.

```python
tree(50, 7)
```

![задача](https://stepik.org/media/attachments/lesson/479604/t12_pitree30r.png)

### Вариант 4 Обобщенное дерево Пифагора (ang любое), обдуваемое ветром

Написать функцию tree(size, ang, n). Она строит дерево Пифагора глубины n. Размер первого квадрата size. 

На квадрате построен **ПРЯМОУГОЛЬНЫЙ треугольник с углом при основании `ang` градусов**.

Построенное дерево глубины 7.

```python
tree(50, 30, 7)
```

![задача](https://stepik.org/media/attachments/lesson/479604/t12_pitree30r.png)
