# Много цветов

lesson = 530425

## Цвет по номеру

* рисовать разными цветами
* менять цвета в цикле
* получить цвет по его номеру

Объединим цвета в **список** (list). Назовем список colors.
 
Сделаем список. Элементы в списке пишутся в `[  ]` через запятую `,`

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

Возьмем цвет по его номеру:
```python
t.color(colors[1])         # t.color('blue')
t.fillcolor(colors[6])     # t.fillcolor('red')
```

![радуга 7](https://stepik.org/media/attachments/lesson/530425/rainbow7.png)

Нарисуем 7 линий:
```python
import turtle           

colors = [
  'violet',   # colors[0]
  'blue',     # colors[1]
  'green',    # colors[2]
  'yellow',   # colors[3]
  'gold',     # colors[4]
  'orange',   # colors[5]
  'red'       # colors[6]
]

def line(size, col):  # нарисовать линию длины size цвета col
  t.color(col)
  t.fd(size)
  
def goto(x, y):
    t.pu()
    t.setpos((x, y))
    t.pd()

def lines(size, dy, n):
    x = t.xcor()
    y = t.ycor()
    for i in range(n):          # i меняется от 0 до n-1
        line(size, colors[i])   # colors[i] - взять цвет номер i из colors
        y -= dy
        goto(x, y)
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

lines(100, 20, 7)

turtle.done()    
```

## Повторить 

Можно взять меньше цветов.

![радуга 5](https://stepik.org/media/attachments/lesson/479603/rainbow5.png)

```python
n = 5
for i in range(n):          # i меняется от 0 до n-1
    line(size, colors[i])   # colors[i] - взять цвет номер i из colors
    y -= dy
    goto(x, y)
```

Как нарисовать 10 линий? Хотим опять повторять цвета. После 'red' взять опять 'violet'.

Но у нас нет `colors[9]`. Получаем ошибку:
```python
    colors[9]
IndexError: list index out of range
```

## Повторяем числа

Чтобы повторить цвета, нужно повторить числа. После 0, 1, 2, 3, 4, 5, 6, нужно опять 0, 1, 2 и дальше.

У нас есть числа от 0 до 9.

Возьмем остаток от деления на 7.

| `i` | `i % 7` |
|----|----|
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 6 |
| 7 | **0** |
| 8 | **1** |
| 9 | **2** |

Из любых положительных чисел мы получили числа от 0 до 6.

Пишем программу:
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

def lines(size, dy, n):
    x = t.xcor()
    y = t.ycor()
    for i in range(n):              # i меняется от 0 до n-1
        line(size, colors[i%7])     # colors[i] - взять цвет номер i из colors
        y -= dy
        goto(x, y)
```

## Сколько цветов в списке

Получили формулу `i % k`, где `k` - сколько элементов в списке.

Можно добавить цвета или убрать. Тогда нужно в коде заменить 7 на другое число. Неудобно. Можно ошибиться.

```python
k = len(colors)
```

**len** - функция python, считает сколько элементов в списке.

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

def lines(size, dy, n):
    x = t.xcor()
    y = t.ycor()
    k = len(colors)
    for i in range(n):              # i меняется от 0 до n-1
        line(size, colors[i % k])   # colors[i] - взять цвет номер i из colors
        y -= dy
        goto(x, y)
```

## TASKTEXT квадраты

Возьмите список цветов из примера или придумайте свой список цветов.

Напишите функцию **sqn(size, d, n)**. 

* Она рисует **n** квадратов разными цветами. 
* Первый квадрат со стороной **size**. 
* Каждый следующий на **d** меньше.
* Не рисовать, если `size < 0`

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
