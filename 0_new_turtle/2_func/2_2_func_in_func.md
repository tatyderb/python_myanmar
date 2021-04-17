# Функция вызывает функцию

lesson = 501268

## SKIP VIDEO https://youtu.be/189BA5AmQLw

Video от 9:15 до 13:25


## Функция вызвает функцию

[Видео](https://youtu.be/189BA5AmQLw)

Есть функция `triangle()`. Она рисует 1 треугольник.

Сделаем новую команду. Она рисует 3 треугольника.

Объявим функцию. Назовем функцию `ornament`.

**Другая функция должна иметь другое имя.** Нельзя в 1 файле 2 функции с одинаковым именем.

**Вызовем функцию `triangle()` внутри функции `ornament()`**.

```python
def ornament():
    # функция рисует 3 треугольника
    
    t.pencolor('red')
    triangle()          # вызов функции triange
    t.lt(45)
    
    t.pencolor('green')
    triangle()          # вызов функции triange
    t.lt(45)
    
    t.pencolor('blue')
    triangle()          # вызов функции triange    
```

Теперь можно вызвать функцию ornament():

```python
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

ornament()          # вызов функции ornament

turtle.done()
```

## Вся программа

Пример рисует:

![3 треугольника](https://stepik.org/media/attachments/lesson/479594/01_tri3.png)

**python сначала должен определить новую функцию. ПОТОМ использовать эту функцию.**

```python
import turtle

# Это новая команда - функция
# Назовем ее triangle()
# def пишем с начала строки без пробелов
def triangle():
    # здесь пишем команды - рисовать треугольник
    # команды надо начать с <TAB> (отступа)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
# Здесь закончилась новая команда triangle

# Новая функция ornament()
# triangle() можно вызвать внутри функции ornament()
def ornament():
    # код в функции пишем с отступом <TAB>

    t.color('red')
    # выполняется новая команда triangle
    triangle()      
    t.lt(45)

    t.color('green')
    # еще раз выполняется новая команда triangle
    triangle()      
    t.lt(45)

    t.color('blue')
    # вызывать (выполнять) новые команды можно сколько хочешь
    triangle()      
# Здесь закончилась функция ornament

# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

ornament()          # вызов функции ornament

turtle.done()
```



## TASKTEXT 6 треугольников

Пример рисует:

![3 треугольника](https://stepik.org/media/attachments/lesson/479594/01_tri3.png)

Нарисовать:

![6 треугольников](https://stepik.org/media/attachments/lesson/479594/04_tri2.png)

* Выполнить программу. Сколько она рисует треугольников?
* написать +1 строку в программе. Нужно 6 треугольников.

```python
import turtle

# Это новая команда - функция
# Назовем ее triangle()
# def пишем с начала строки без пробелов
def triangle():
    # здесь пишем команды - рисовать треугольник
    # команды надо начать с <TAB> (отступа)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
# Здесь закончилась новая команда triangle

# Новая функция ornament()
# triangle() можно вызвать внутри функции ornament()
def ornament():
    # код в функции пишем с отступом <TAB>

    t.color('red')
    # выполняется новая команда triangle
    triangle()      
    t.lt(45)

    t.color('green')
    # еще раз выполняется новая команда triangle
    triangle()      
    t.lt(45)

    t.color('blue')
    # вызывать (выполнять) новые команды можно сколько хочешь
    triangle()      
# тут закончилась функция ornament

# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

ornament()          # вызов функции ornament
# тут нужно написать код

turtle.done()
```

## TASKTEXT Горы

Горы - это

![горы](https://stepik.org/media/attachments/lesson/479594/kogr_small.jpg)

Нужно научиться писать функции.

Хорошо: Пишем мало кода. Проверяем программу. Исправляем ошибки. Пишем еще мало кода, проверяем и исправляем.

Плохо: Пишем сразу всю программу. Много кода. Много ошибок. Трудно найти ошибку.

Надо писать 1 функцию и проверить 1 функцию. Потом писать следующую функцию.

* определить функцию `pik()`
* вызвать функцию `pik()`, проверить функцию
* найти и исправить ошибки в программе
* определить функцию `gory()`
* вызвать функцию `gory()`
* найти и исправить ошибки в программе
* послать решение


* Объявить функцию **pik()** и вызвать ее. Функция `pik()` рисует 1 пик:

![pik](https://stepik.org/media/attachments/lesson/479594/gory1.png)

* Объявить функцию **gory()** и вызвать ее. Функция `gory()` рисует 3 пика:

![gory](https://stepik.org/media/attachments/lesson/479594/gory3.png)

## TASKTEXT 2 квадрата

* Написать и проверить функцию **sq()**. Она рисует квадрат:

![квадрат](https://stepik.org/media/attachments/lesson/479498/t4.png)

* Написать функцию **sq2()**. Она рисует 2 квадрата:

![gory](https://stepik.org/media/attachments/lesson/479594/func_e6.png)

## TASKTEXT снежинка

* Написать и проверить функцию **snowline()**. Она рисует:

![snow line](https://stepik.org/media/attachments/lesson/479594/func_t5a.png)

* Написать функцию **snowflake()**. Она рисует:

![snow flake](https://stepik.org/media/attachments/lesson/479594/func_t5.png)

## TASKTEXT Узор

* Написать функцию **spileft()**. Она рисует

![spileft](https://stepik.org/media/attachments/lesson/479594/sll.png)

* Написать функцию **spiright()**. Она рисует

![spiright](https://stepik.org/media/attachments/lesson/479594/spp.png)

* Написать функцию **uzorup()**. Используйте функции `spileft()` и `spiright()`. `uzorup()` рисует

![uzorup](https://stepik.org/media/attachments/lesson/479594/uzz2.png)

* Написать функцию **spidownleft()**. Она рисует

![spidownleft](https://stepik.org/media/attachments/lesson/479594/slo.png)

* Написать функцию **spidownright()**. Она рисует

![spidownright](https://stepik.org/media/attachments/lesson/479594/spo.png)

* Написать функцию **uzordown()**. Используйте функции `spidownleft()` и `spidownright()`. `uzordown()` рисует

![uzordown](https://stepik.org/media/attachments/lesson/479594/uzz1.png)

* Написать функцию **uzor()**. Используйте функции `uzorup()` и `uzordown()`. `uzor()` рисует

![uzor](https://stepik.org/media/attachments/lesson/479594/uz.png)

* Написать функцию **uzor2()**. Используйте функцию `uzor()`. `uzor2()` рисует

![full uzor](https://stepik.org/media/attachments/lesson/479594/spiral.png)
