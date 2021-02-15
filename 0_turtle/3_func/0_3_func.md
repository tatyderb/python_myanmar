# Функции

lesson = 479594

## Видео

Видео  https://www.youtube.com/watch?v=T0C52MCd8os 
от 0:00 до 9:15

Текст - на следующих шагах.

## Новые слова

* **команда** - что нужно делать.

Тут нужно видео что такое команда.


## Функция - создать и использовать

TODO: сделать заменить на определить. Они должны знать слово определение.

Можно научить черепаху новой команде (функции).
Напишем имя новой функции и напишем в ней код. 

```python
def имя():
    команды
```

* **def** - специальное слово в python, от английского слова "definition" - определение.
* *triangle* - мы придумали название функции. Это *имя функции*.

У вас есть имя. Вам родители придумали хорошее имя.

Вы объявляете функцию. Нужно придумать хорошее имя функции.

Плохо: придумать разным функциям имена `func1`, `func2` или `aaa`. Имя функции говорит нам, что делает функция.

## Функция 

Нарисуем

![3 треугольника](https://stepik.org/media/attachments/lesson/479594/01_tri3.png)

Будем делать новую команду. Команда будет рисовать 1 треугольник. Назовем ее `triangle`. Сделаем новую функцию `triangle`.

| Сколько раз | Что делаем | Python |
|----|-----|----|
| 1 и только 1 раз | **сделаем функцию**   | `def triangle():` |
| много раз (тут 3) | **выполним функцию**  | `triangle()` |

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

# Здесь закончилась новая команда triangle.
# Закончилось определение функции - закончились отступы TAB.

# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

t.color('red')
# выполняется новая команда triangle
triangle()      
t.lt(45)

t.color('green')
# еще раз выполняется новая команда triangle
triangle()      
t.lt(45)

t.color('blue')
# вызывать (выполнять) новые команды можно много раз
triangle()      

turtle.done()
```

## Определение и вызов функции

Есть программа. Функция `triangle()` рисует 1 треугольник. Вызовем 3 раза функцию, черепаха нарисует 3 треугольника.

![3 треугольника](https://stepik.org/media/attachments/lesson/479594/01_tri3.png)


* **Методы**
    * Старые команды черепахи: `имя черепахи` **точка** `команда черепахи`
    * `t.fd(100)` - это "Черепаха с именем t, иди вперед на 100 шагов".
    * Команды черепахи называют **методы**. Методы черепахи пишут через `.` (точку)
    * Вызов метода черепахи `t`:
    
```python
t.fd(100)     # команда черепахи, начинается с t.
```    
    
* **Функции**
    * Новые команды - функции.
    * `triangle()` - "Нарисовать треугольник"
    * Новая команда `triangle` пишется без `t.`
    * **вызов** функции `triangle`:
    
```python
triangle()    # новая команда, t. не нужно
```

* **Определение функции**
    * **def** - специальное слово. От definition (определение).
    * *имя функции* `triangle` - придумали сами
    * `( )` - функции нужны скобки как в математике
    * `:` -  после `()` нужно поставить двоеточие (column)
    * команды в функции пишем с **отступом** (TAB)

```python
def triangle():
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
```    

## TASKTEXT Квадрат

* Написать функцию **sq( )**. 
* Функция `sq( )` рисует 1 квадрат. 
* Вызвать функцию `sq()` 3 раза и нарисовать

![3 квадрата](https://stepik.org/media/attachments/lesson/479594/func_t3.png)

**Обязательно определить функцию!**

## TASKTEXT Крест

* Определите функцию **cross()**
* Функция `cross()` рисует крест.
* Вызовите 1 раз `cross()` и нарисуйте

![cross](https://stepik.org/media/attachments/lesson/479594/t243.png)

* Вызовите много раз `cross()` и нарисуйте

| Вариант | Нарисовать |
|----|-----|
| Вариант 1 | ![вариант 1](https://stepik.org/media/attachments/lesson/479594/cross1.png) |
| Вариант 2 | ![вариант 2](https://stepik.org/media/attachments/lesson/479594/cross2.png) |

## Видео

Видео: http://youtube.com/watch?v=T0C52MCd8os
от 9:15 до 13:25

## Функция в функции

В функции можно писать функции черепахи и другие новые функции.

![3 треугольника](https://stepik.org/media/attachments/lesson/479594/01_tri3.png)

Мы определили функцию `triangle()`. Она рисует 1 треугольник.

```python
# Определим функцию triangle. Она рисует 1 треугольник.
def triangle():
    # здесь пишем команды - рисовать треугольник
    # команды надо начать с <TAB> (отступа)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
```

Определим другую функцию `ornament()`. Она рисует 3 треугольника.

**Вызовем функцию `triangle()` внутри функции `ornament()`**.

```python
# Определим функцию ornament. Она рисует 3 треугольника.
def ornament():
    # код в функции пишем с отступом <TAB>

    t.color('red')
    # выполнить новую команду triangle
    triangle()      
    t.lt(45)

    t.color('green')
    # еще раз выполнить новую команду triangle
    triangle()      
    t.lt(45)

    t.color('blue')
    # вызывать (выполнять) новые команды можно много раз
    triangle()  
```

Теперь можно вызвать функцию ornament():

```python
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
