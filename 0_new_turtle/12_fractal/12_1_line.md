# Кривые

lesson = 530689

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

## Пример. Кривая Коха

[https://en.wikipedia.org/wiki/Koch_snowflake](https://en.wikipedia.org/wiki/Koch_snowflake)

Попробуем сделать zoom любой части фрактала:

![кривая Коха](https://stepik.org/media/attachments/lesson/479604/Kochsim.gif)

По шагам:
Это снежинка Коха. У нее увеличивается глубина.

![кривая Коха](https://stepik.org/media/attachments/lesson/479604/Von_Koch_curve.gif)


Подробнее:

![кривая Коха поэтапно](https://stepik.org/media/attachments/lesson/479604/Koch_curve_construction.png)

Каждый раз 1 отрезок заменяется на много линий. 

**n** - сколько раз заменили 1 отрезок на много. Называется **глубина фрактала**. У настоящего фрактала глубина бесконечность $\infin$.

В программе мы не можем рисовать бесконечную глубину. Остановимся на конечной небольшой глубине.

## Рисуем кривую Коха

Надо нарисовать фрактал. Будем 1 линию заменять на много линий. Так для каждой линии.

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
 koch_line(200, 3)   # глубина 3, 1 линия -> 4 линии, повторили 3 раза
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
colors = [
  'yellow',   # colors[0]
  'gold',     # colors[1]
  'orange',   # colors[2]
  'red',      # colors[3]
  'violet',   # colors[4]
  'blue',     # colors[5]
  'green'     # colors[6]
  ]
```

Рисуем кривые Коха глубины от 0 до 4 цветами от `colors[0]` до `colors[4]`:
```python
for i in range(5):    # i = 0..4
  p0 = t.pos()           # запомнили начальную позицию в p0
  t.color(colors[i])      # новой итерации - новый цвет
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

colors = [
  'yellow',   # colors[0]
  'gold',     # colors[1]
  'orange',   # colors[2]
  'red',      # colors[3]
  'violet',   # colors[4]
  'blue',     # colors[5]
  'green'     # colors[6]
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
  t.color(colors[i])      # новой итерации - новый цвет
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

Пошлите на проверку глубину 7.
