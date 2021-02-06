# Рекурсия

lesson = 479603

## Цвет по номеру

Сделаем список (анг. list) цветов. Назовем список tones. Один цвет можно взять по его номеру.
 
Сделаем список. Элементы в списке пишутся в `[  ]` через запятую `,`

```python
tones = [
  'violet',   # tones[0]
  'blue',     # tones[1]
  'green',    # tones[2]
  'yellow',   # tones[3]
  'gold',     # tones[4]
  'orange',   # tones[5]
  'red'       # tones[6]
  ]
```

Возьмем цвет по его номеру:
```python
t.color(tones[1])         # t.color('blue')
t.fillcolor(tones[6])     # t.fillcolor('red')
```

```cpp
Число i    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
Число i%7  0 1 2 3 4 5 6 0 1 2  3  4  5  6  0  1  2
```

```python
t.fillcolor(tones[10%7])  # t.fillcolor('yellow')
i = 10
t.fillcolor(tones[i%7])  # t.fillcolor('yellow')
```

len(tones) - сколько элементов в списке tones. len - специальная функция python.

```python
t.fillcolor(tones[i % len(tones)])  # t.fillcolor('yellow')
```
Нарисуем 5 линий

![радуга 5](https://stepik.org/media/attachments/lesson/479603/rainbow5.png)

Вся программа:
```python
import turtle           

def write(data):
    t.write(data, font=("Arial", 14, "normal"))
    
tones = [
  'violet',   # tones[0]
  'blue',     # tones[1]
  'green',    # tones[2]
  'yellow',   # tones[3]
  'gold',     # tones[4]
  'orange',   # tones[5]
  'red'       # tones[6]
  ]
  
def rainbow():
    x = t.xcor()    # x, где сейчас черепаха
    y = t.ycor()    # y, где сейчас черепаха
    dy = 10         # следующая линия на dy ниже
    size = 100      # длина линии
    for i in range(5):
        t.color(tones[i])    # берем цвет
        t.goto(x+size, y)    # рисуем линию
        y -= dy              # следующая линия ниже
        t.pu()               # идем на начало следующей линии
        t.goto(x, y)
        t.pd()
        
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.color('blue')

rainbow()

turtle.done()
```

## TASKTEXT Задача: радуга n линий

Напишите функцию ranbow(n). Она рисует радугу из n линий.
Число n прочитать из консоли.

Пример 1 ввода:
```python
5
```
нарисует 
![радуга 5](https://stepik.org/media/attachments/lesson/479603/rainbow5.png)

Пример 2 ввода:
```python
10
```
нарисует 
![радуга 10](https://stepik.org/media/attachments/lesson/479603/rainbow10.png)

## Повторение 

Напишем функцию sqn(size, d, n). Она рисует n квадратов. Первый квадрат со стороной size. Каждый следующий на d меньше.

По номеру цвета i возвращает цвет из списка tones
```python
def get_color(i):
	return tones[i % len(tones)]
```

Рисует квадраты в цикле
```python
# n квадратов, первый размера size, каждый следующий на d меньше
def sqn(size, d, n):    
  for i in range(n):        # i меняется от 0 до n-1
    sq(size, get_color(i))  # get_color(i) - новый цвет 
    size -= d
    if size < 0:            # если следующий квадрат маленький, 
      return                # больше не рисовать
```

```python
sqn(200, 20, 7) 
```
нарисует 
![квадраты](https://stepik.org/media/attachments/lesson/479603/ex11_1.png)

```python
sqn(100, 20, 7) 
```
нарисует 5 квадратов: 
![квадраты](https://stepik.org/media/attachments/lesson/479603/ex11_2.png)

## TASKTEXT Задача. Нарисовать от самого маленького до самого большого

TODO: убрать, они рисуют прежним кодом + потом рисуют большой квадрат.

Нарисовать сначала самый маленький квадрат. Потом на d больше. Последний квадрат размера size. Не больше n квадратов.

```python
sqn(110, 30, 5) 
```
нарисует квадраты 20, 50, 80, 110. **Первый 20, последний 110.**

![квадраты](https://stepik.org/media/attachments/lesson/479603/sq_while1.png)

## Рекурсия

Как нарисовать n квадратов без цикла?

Напишем функцию sqn(size, d, n, i). 

* size - размер первого квадрата
* Каждый следующий квадрат на d меньше.
* n - осталось нарисовать n квадратов.
* i - уже нарисовали i квадратов (по i получаем цвет квадрата).

Изменится только эта функция. Остальной код не изменится.

В функции sqn вызовем sqn еще раз. Это называется рекурсивным вызовом функции или рекурсией.

```python
def sqn(size, d, n, i):
  if n == 0:        # не надо рисовать?
    return          # не рисовать!
  if size <= 0:     # маленький квадрат?
    return          # не рисовать!
    
  # рисовать 1 квадрат, цвет из i
  col = get_color(i) 
  sq(size, col)
  
  # рисовать остальные квадраты
  sqn(size-d, d, n-1, i+1)             # вызвали саму себя 
  # следующий квадрат размера size-d
  # осталось нарисовать n-1 квадрат (1 нарисовали тут)
  # уже нарисовали i+1 квадрат (1 нарисовали тут)
```

Вызов функции
```python
sqn(200, 20, 7, 0)   
# 7 квадратов, первый размером 200, другие на 20 меньше
# уже нарисовали 0 квадратов
```
Вся программа:
```python
import turtle           
import time

tones = [
  'violet',   # tones[0]
  'blue',     # tones[1]
  'green',    # tones[2]
  'yellow',   # tones[3]
  'gold',     # tones[4]
  'orange',   # tones[5]
  'red'       # tones[6]
  ]

def sq(size, col):  # нарисовать квадрат размера size цвета col
  t.color(col)
  for i in range(4):
    t.fd(size)
    t.left(90)

# возвращает цвет по номеру i из списка tones
def get_color(i):
	return tones[i % len(tones)]

# n квадратов, 
# этот размера size, 
# следующий на d меньше
# уже нарисовали i квадратов
def sqn(size, d, n, i):
  if n == 0:        # не надо рисовать?
    return          # не рисовать!
  if size <= 0:     # маленький квадрат?
    return          # не рисовать!
    
  # рисовать 1 квадрат, цвет из i
  col = get_color(i) 
  sq(size, col)
  
  # рисовать остальные квадраты
  sqn(size-d, d, n-1, i+1)
  # следующий квадрат размера size-d
  # осталось нарисовать n-1 квадрат (1 нарисовали тут)
  # уже нарисовали i+1 квадрат (1 нарисовали тут)
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

sqn(200, 20, 7, 0)   
# 7 квадратов, первый размером 200, другие на 20 меньше
# уже нарисовали 0 квадратов

turtle.done()
```

## Сначала - условие выхода

Проверьте, как будет работать такая функция

```python
def sqn_endless(size, d, n, i):
  # рисовать 1 квадрат, цвет из i
  col = get_color(i) 
  sq(size, col)
  
  # рисовать остальные квадраты
  sqn(size-d, d, n-1, i+1)             # вызвали саму себя 

  # потом проверим
  if n == 0:        # не надо рисовать?
    return          # не рисовать!
  if size <= 0:     # маленький квадрат?
    return          # не рисовать!
```
Почему эта функция работает неправильно?

## Кто первый - один или остальные?

В функции sqn можно написать 

```python
sq(size, get_color(i))    # сначала этот 1 квадрат        
sqn(size-d, d, n-1, i+1)  # потом остальные квадраты
```
или так:
```python
sqn(size-d, d, n-1, i+1)  # сначала остальные квадраты
sq(size, get_color(i))    # потом этот 1 квадрат        
```
![квадраты](https://stepik.org/media/attachments/lesson/479603/order.png)

## TASKTEXT Задача: вложенные квадраты

* Написать функцию sqn(size, d, n, i). 
* **Написать рекурсию. Цикл нельзя.**
    * size - размер первого квадрата
    * Каждый следующий квадрат на d меньше.
    * n - осталось нарисовать n квадратов.
    * i - уже нарисовали i квадратов (по i получаем цвет квадрата).

```python
sqn(200, 20, 7, 0) 
```
нарисует

![квадраты 7](https://stepik.org/media/attachments/lesson/479603/ex11_00.png)

```python
sqn(100, 20, 7, 0) 
```
нарисует

![квадраты 7](https://stepik.org/media/attachments/lesson/479603/ex11_01.png)

## TASKTEXT Задача: квадраты с поворотом

* Если сумеете, сделайте вариант 2.
* Если проблемы с математикой, то вариант 1.

### Вариант 1 - квадраты с поворотом на 30 градусов

* Следующий квадрат повернут на 30 градусов.
* Напишите функцию  sqn(size, n, i)
* Она рекурсией рисует квадраты (циклы нельзя). 
* Если квадрат слишком маленький, не рисовать.
    * size - размер стороны квадрата
    * n - сколько еще квадратов надо нарисовать
    * i - сколько квадратов уже нарисовали

```python
sqn(200, 7, 0)
```
нарисует
![квадраты 7](https://stepik.org/media/attachments/lesson/479603/t11_2.png)

### Вариант 2 - квадраты с поворотом на *ang* градусов

* Следующий квадрат повернут на `ang` градусов.
* Напишите функцию  sqn(size, ang, n, i)
* Она рекурсией рисует квадраты (циклы нельзя). 
* Если квадрат слишком маленький, не рисовать.
    * size - размер стороны квадрата
    * n - сколько еще квадратов надо нарисовать
    * i - сколько квадратов уже нарисовали

```python
sqn(200, 30, 7, 0)
```
нарисует
![квадраты 7](https://stepik.org/media/attachments/lesson/479603/t11_2.png)

## TASKTEXT Задача: вписанные многоугольники

Если можете, делайте вариант 2.
Если с математикой плохо, делайте вариант 1.

### Вариант 1. Вписанные треугольники

* Написать функцию trin(size, n, i). Она рекурсией рисует вложенные правильные треугольники. 
* Если сторона треугольника меньше 20, не рисовать.
    * size - размер стороны треугольника
    * n - сколько еще фигур надо нарисовать
    * i - сколько фигур уже нарисовали
```
trin(200, 7, 0)
```
Нарисует 
![треугольники](https://stepik.org/media/attachments/lesson/479603/t11_3_3.png)

### Вариант 2. Вписанные многоугольники

Написать функцию polyn(size, k, n, i). Она рекурсией рисует вложенные правильные k-угольники. 

Сумма углов правильного k-угольника `(k-2)*180`

* Если сторона многоугольника меньше 20, не рисовать.
* size - размер стороны многоугольника
* k - рисовать правильный k-угольник
* n - сколько еще фигур надо нарисовать
* i - сколько фигур уже нарисовали
```
polyn(200, 3, 7, 0)
```
Нарисует 
![треугольники](https://stepik.org/media/attachments/lesson/479603/t11_3_3.png)

```python
polyn(200, 4, 3, 0)
```
Нарисует 
![квадраты](https://stepik.org/media/attachments/lesson/479603/t11_3_4.png)

```python
polyn(200, 5, 5, 0)
```
Нарисует 
![пятиугольники](https://stepik.org/media/attachments/lesson/479603/t11_3_5.png)

## TASKTEXT Задача: рекурсивная спираль

Спираль вовнутрь (меняем 3 цвета)

* Написать функцию spi(size, d, n, col), цикл нельзя.
* Она рисует спираль. 
* Если сторона спирали меньше 10, не рисовать.
    * size - длина отрезка спирали
    * d - на сколько следующий отрезок меньше предыдущего
    * n - сколько еще отрезков надо нарисовать
    * col - цвет отрезка; цвета меняются по очереди: red, gold, blue

```python
spi(200, 10, 15, 'red') 
```
нарисует
![спираль](https://stepik.org/media/attachments/lesson/479603/t11_4.png)

## TASKTEXT Задача. Рекурсивный узор из веток

Напишите функцию uzor(n, size0, dsize, ang0, dang, k), которая использует функцию branch и рисует узор из k веток РЕКУРСИВНО.  Цикл в функции нельзя.

```python
t.seth(0)  # установить черепаху в направлении 0.
```
![ветка](https://stepik.org/media/attachments/lesson/479603/branch.png)

* Функция branch(n, size0, dsize, ang0, dang) рисует 1 ветку из n отрезков. 
    * n - сколько отрезков
    * size0 - длина первого отрезка
    * dsize - следующий отрезок на dsize меньше
    * ang0 - первый угол поворота
    * dang - следующий поворот на dang больше.

В функции есть цикл.
```python
def branch(n, size0, dsize, ang0, dang):
  size = size0
  ang = ang0
  for i in range(n):
    if i == n/2:
      p = t.pos()
    t.fd(size)
    t.left(ang)
    size -= dsize
    ang += dang
  return p
```

Одну ветку можно нарисовать так:
```python
pc = branch(6, 50, 5, 20, 10)
```

Напишите функцию uzor **без цикла**. Нарисуйте узор.

```python
import turtle           

# нарисовать 1 ветку
def branch(n, size0, dsize, ang0, dang):
  size = size0
  ang = ang0
  for i in range(n):
    if i == n/2:
      p = t.pos()
    t.fd(size)
    t.left(ang)
    size -= dsize
    ang += dang
  return p
  
# нарисовать k веток
def uzor(n, size0, dsize, ang0, dang, k):
	  # тут нужно написать код
	  pc = branch(n, size0, dsize, ang0, dang)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

t.color('blue')
# 1 ветку можно нарисовать так:
pc = branch(6, 50, 5, 20, 10)

t.color('red')
t.goto(pc)
t.stamp()

t.color('green')
t.seth(0)

turtle.done()
```

## TASKTEXT Задача: квадраты Фибоначчи

Задачу можно НЕ делать.

Числа Фибоначчи - это последовательность 1, 1, 2, 3, 5, 8, 13, 21 и дальше.

$$F_n = F_{n-1} + F_{n-2}$$
$$F_1 = F_2 = 1$$

![фибоначчи клеточки](https://stepik.org/media/attachments/lesson/479603/fib.png)

Дано n. Нарисовать n квадратов со сторонами как у первых n чисел Фибоначчи. 

![фибоначчи клеточки](https://stepik.org/media/attachments/lesson/479603/t11_7.png)
