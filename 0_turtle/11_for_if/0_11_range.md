# Условия в циклах

lesson = 479602

## range(5) - это числа от 0 до 4

В коде
```python
for i in range(5):
```
Создается переменная i и в нее записываются по очереди числа 0, 1, 2, 3, 4

Напишем число и перейдем к следующему
```python
for i in range(5):
    write(i)
    t.fd(50)
```

![0..4](https://stepik.org/media/attachments/lesson/479602/ex0.png)

Вся программа:

```python
import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))


t = turtle.Turtle()
t.shape("turtle")
t.width(3)

for i in range(5):
    write(i)
    t.fd(50)

turtle.done()
```

### Задача: числа от 0 до 6

Нарисовать так:

![0..6](https://stepik.org/media/attachments/lesson/479602/ex0t.png)

## range(2, 5)

**range(2, 5)** дает числа 2, 3, 4. 

**Числа 5 нет.**

Нарисуем числа
```python
for i in range(2, 5):
    write(i)
    t.fd(50)
```

![2..4](https://stepik.org/media/attachments/lesson/479602/ex0_1.png)

### Задача: числа от 3 до 7

Нарисовать

![3..7](https://stepik.org/media/attachments/lesson/479602/ex0_1t.png)

## range(0, 200, 50)

**range(0, 200, 50)** дает числа 0, 50, 100, 150

Числа 200 нет.

От 0 до 200, увеличивать на 50.

```python
for x in range(0, 200, 50):
    t.goto(x, 0)
    write(x)
```

* Будем числа записывать в переменную х. 
* Иди черепахой в (x, 0) и пиши x.

Получится
![range(0, 200, 50)](https://stepik.org/media/attachments/lesson/479602/ex0_3.png)

### Задача

Нарисовать
![-30..170](https://stepik.org/media/attachments/lesson/479602/ex0_3t.png)

## Меняем цвет - 1

Нарисуем
![0..4](https://stepik.org/media/attachments/lesson/479602/dashes_1.png)

Менять цвет можно по-разному. 
Напишем функцию get_color(i). 
Где i - это число 0 или 1 или 2 или 3 или 4.
Если i это 0 или 2 или 4, то цвет желтый. Иначе цвет красный. Напишем это:

```python
def get_color(i):
    if i == 0 or i == 2 or i == 4:  # если i равен 0, 2 или 4
        col = 'gold'                # цвет желтый
    else :                          # иначе (i равен 1 или 3)
        col = 'red'                 # цвет красный
    return col
    
def dashes():    
    for i in range(5):
        col = get_color(i)
        t.color(col)
        write(i)
        t.fd(50)
```

Вся программа:
```python
import turtle           

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

def get_color(i):
    if i == 0 or i == 2 or i == 4:  # если i равен 0, 2 или 4
        col = 'gold'                # цвет желтый
    else :                          # иначе (i равен 1 или 3)
        col = 'red'                 # цвет красный
    return col
    
def dashes():    
    for i in range(5):
        col = get_color(i)
        t.color(col)
        write(i)
        t.fd(50)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

dashes()

turtle.done()
```

## Числа до 6

Хотим числа от 0 до 6. Изменим dashes(n), где n - сколько чисел

```python
def dashes(n):    
    for i in range(n):
        col = get_color(i)
        t.color(col)
        write(i)
        t.fd(50)
```
Тогда
```python
dashes(7)
```
нарисует
![0..4..6](https://stepik.org/media/attachments/lesson/479602/dashes_2.png)

Плохо. Цвет 6 - ошибка. Хочу для любых n.

Подумайте, как можно написать код для любых n.

## Меняем цвет - 2

Нарисуем
![0..4](https://stepik.org/media/attachments/lesson/479602/dashes_1.png)

* После желтого красный.
* После красного желтый.

Напишем это на python. Функция nextColor(col). Возвращает следующий цвет.

```python
# цвет col поменять на другой
def next_color(col):  
    if col == 'red':  # после красного
        col = 'gold'  # цвет желтый
    else :            # иначе (не красный)
        col = 'red'   # цвет красный
    return col
```

Рисуем n линий. Первая цвет col.
```python
def dashes(n, col): 
    for i in range(n):
        t.color(col)
        write(i)
        t.fd(50)
        col = next_color(col) # меняем цвет  
```
код
```python
dashes(5, 'gold')  # 5 чисел, первый цвет желтый
```
нарисует
![0..4](https://stepik.org/media/attachments/lesson/479602/dashes_1.png)

Вся программа:
```python
import turtle           

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

# цвет col поменять на другой
def nextColor(col):  
    if col == 'red':  # после красного
        col = 'gold'  # цвет желтый
    else :            # иначе (не красный)
        col = 'red'   # цвет красный
    return col
    
def dashes(n, col): 
    for i in range(n):
        t.color(col)
        write(i)
        t.fd(50)
        col = nextColor(col) # меняем цвет  

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

dashes(5, 'gold')  # 5 чисел, первый цвет желтый

turtle.done()
```

* Вопрос студента: "Я назвал функцию не nextColor, а next. У меня не работает. Почему?"
* Ответ преподавателя: "next - специальное слово в языке".

## TASKTEXT Задача: полоса квадратов

* Напишите функцию  csq(size, col). Она рисует квадрат со стороной size цвета col.
* Напишите функцию  csq_row(size, n, col),  Она рисует n квадратов со стороной size. Цвет первого квадрата col.
* Нарисуйте 

![полоса](https://stepik.org/media/attachments/lesson/479602/t91.png)

## Меняем цвет - 3

Найдем формулу для цвета

TODO: не было понятия "остаток от деления и не знают %"

```
Число                    это i        равно 0  1  2  3  4  5
Остаток от деления на 2  это i % 2    равно 0  1  0  1  0  1
```
Числа 0, 2, 4, 6  и так далее называют **четные числа".

-10 - тоже четное число.

Напишем функцию getColor(i).
```python
# по числу i определить цвет
def getColor(i):  
    if i % 2 == 0:    # i четное
        col = 'gold'  # цвет желтый
    else :            # иначе (нечетное)
        col = 'red'   # цвет красный
    return col        # вернуть цвет
```
используем так:
```python
def dashes(n): 
    for i in range(n):
        col = getColor(i)   # по числу получить цвет
        t.color(col)
        write(i)
        t.fd(50)
```
Нарисуем
![0..4](https://stepik.org/media/attachments/lesson/479602/dashes_1.png)

Вся программа:
```python
import turtle           

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

# по числу i определить цвет
def getColor(i):  
    if i % 2 == 0:   # i четное
        col = 'gold'  # цвет желтый
    else :            # иначе (не красный)
        col = 'red'   # цвет красный
    return col
    
def dashes(n): 
    for i in range(n):
        col = getColor(i)
        t.color(col)
        write(i)
        t.fd(50)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

dashes(5)

turtle.done()
```

## TASKTEXT Задача: столбец квадратов

Напишите функцию getColor(i, col1, col2)
Для четных i она возвращает col1, для нечетных col2.
 
Возьмите функцию csq(size, col), которая рисует квадрат со стороной size цветом col.

Напишите функцию csq_col(size, n, col1, col2), которая рисует столбец (column) из n квадратов размера size, меняя цвет. Цвет первого квадрата col1.

Нарисуйте
![столбец](https://stepik.org/media/attachments/lesson/479602/t92.png)

## TASKTEXT Задача: ковер из столбцов

* Напишите функцию hcarpet(size, n, m). 
* Она рисует прямоугольник из квадратов размера size. 
* n строк, m столбцов.

Нарисуйте

![ковер](https://stepik.org/media/attachments/lesson/479602/t93.png)

## TASKTEXT Задача: ковер из строк

* Напишите функцию vcarpet(size, n, m). 
* Она рисует прямоугольник из квадратов размера size. 
* n строк, m столбцов.

Нарисуйте

![ковер](https://stepik.org/media/attachments/lesson/479602/t94.png)

## TASKTEXT Задача: ковер шахматный

* Напишите функцию chess(size, n, m). 
* Она рисует прямоугольник из квадратов размера size. 
* n строк, m столбцов.

Нарисуйте

![ковер](https://stepik.org/media/attachments/lesson/479602/t95.png)

## TASKTEXT Задача: светофор

* Напишите функцию csq3(size, n)
* Она рисует из квадратов размера size строку размера n столбцов. 
* Цвета квадратов меняются красный - желтый - зеленый.

```python
сsq3 (40, 8)
```
нарисует
![светофор](https://stepik.org/media/attachments/lesson/479602/t96.png)


## Вложенные квадраты

* Написать функцию sqin (size, d, n).
* Она рисует первый квадрат размера size.
* Следующий квадрат на d меньше.
* Хочет нарисовать n квадратов.
    * Если размер 0 или меньше, то стоп.
* Написать сколько квадратов нарисовали (число).

```python
sqin (150, 20, 14)
```
нарисует

![sqin (150, 20, 14)](https://stepik.org/media/attachments/lesson/479602/carreinf.png)

```python
sqin (150, 20, 5)
```
нарисует

![sqin (150, 20, 5)](https://stepik.org/media/attachments/lesson/479602/carreinf2.png)

**Черепаху можно спрятать.**
```python
t.hideturtle()
```

## Спираль без цвета

* Напишите функцию spi(size, n)
* Она рисует из квадратов размера size спираль, у которой в первом отрезке n квадратов. 
* Отрезки спирали уменьшаются. Используйте while 

```python
spi (20, 8)
```
нарисует

![спираль](https://stepik.org/media/attachments/lesson/479602/t97.png)

## Спираль c цветом

* Напишите функцию spi(size, n)
* Она рисует из квадратов размера size спираль, у которой в первом отрезке n квадратов. 
* Цвета квадратов меняются красный - желтый.
* Отрезки спирали уменьшаются. Используйте while 

```python
spi (20, 8)
```
нарисует

![спираль](https://stepik.org/media/attachments/lesson/479602/t98.png)

## Задача: два квадрата

* sq(size, col)
* Рисует квадрат размера size цвета col.

* sq2(size1, col1, size2, col2)
* Рисует 2 квадрата. Сначала большой, потом маленький.

```python
sq2(150, 'yellow', 100, 'red')
```
Нарисует
![yellow + red](https://stepik.org/media/attachments/lesson/479602/sq2_1.png)

Если цвета одинаковые, второй квадрат не видно
```python
sq2(150, 'yellow', 100, 'yellow')
```
* Надо сделать цвета разные.
* Если цвета одинаковые, то col1 сделаем yellow.
* Но если col1 и co2 равны yellow? Тогда цвета останутся yellow. Плохо.

![yellow + yellow](https://stepik.org/media/attachments/lesson/479602/sq2_2.png)

По-другому:
* Если цвета равны
    * Если цвет1 желтый
          * пусть цвет1 красный
    * иначе
          * пусть цвет1 желтый
          
```python
def sq2(size1, col1, size2, col2):
    if col1 == col2:
        if col1 == 'yellow':   # значит col2 тоже yellow
            col1 = 'red'       # col1 = 'red',   col2='yellow'
        else:
            col1 = 'yellow'    # col1 = 'yellow'  col2 = НЕ желтый
    # конец выбора цвета
    sq(size1, col1)
    sq(size2, col2)
```

Проверим 1.
```python
sq2(150, 'yellow', 100, 'yellow')
``` 
![yellow + yellow](https://stepik.org/media/attachments/lesson/479602/sq2_3.png)

Проверим 2.
```python
sq2(150, 'blue', 100, 'yellow')
``` 
![blue + yellow](https://stepik.org/media/attachments/lesson/479602/sq2_4.png)

Проверим 3.
```python
sq2(50, 'blue', 100, 'yellow')   # первый квадрат маленький
``` 
Если первый квадрат маленький, его не видно.
Нужно исправить. Надо рисовать:

![blue + yellow](https://stepik.org/media/attachments/lesson/479602/sq2_5.png)

## TASKTEXT Задача

* Написать функцию sq2(size1, col1, size2, col2)
* Она рисует сначала большой квадрат. 
* Потом маленький квадрат.
* Если цвета одинаковые, то 
    * Если col1 желтый
          * пусть col1 красный
    * иначе
          * пусть col1 желтый

Надо исправить программу:
```python
import turtle           

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

def sq(size, col):
    t.color('gold', col)
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()
    
def sq2(size1, col1, size2, col2):
    if col1 == col2:
        if col1 == 'yellow':   # значит col2 тоже yellow
            col1 = 'red'       # col1 = 'red',   col2='yellow'
        else:
            col1 = 'yellow'    # col1 = 'yellow'  col2 = НЕ желтый
    # конец выбора цвета
    sq(size1, col1)
    sq(size2, col2)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

# Проверим 1
sq2(100, 'yellow', 50, 'blue')
# Проверим 2
#sq2(150, 'blue', 100, 'yellow')
# Проверим 3
# тут добавить что еще нужно проверить

turtle.done()
```    
