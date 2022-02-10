# Turtle

lesson = 479498

## Компьютер понимает свой язык

Человек понимает язык, который знает (русский, английский, китайский...)

Я говорю, что надо делать. Если вы не понимаете язык, вы не можете сделать.

У компьютера свой язык. Программа - это текст на языке компьютера.

## Первая программа

 Напишем программу, которая рисует линию. Черепаха (turtle) идет и рисует линию. 
 
![отрезок](https://stepik.org/media/attachments/lesson/479498/1_1_fd.png)
 
```python
import turtle        # познакомили программу с библиотекой turtle

t = turtle.Turtle()  # сделали черепаху, назвали черепаху t
t.shape('turtle')    # как выглядит черепаха

t.forward(75)        # вперед на 75 шагов

turtle.done()	     # для repl.it НЕ нужно. Иначе закроет окно.
```

* Команды выполняются одна за другой. Сверху вниз.
* Черепаха может делать команды
    * t.forward(75) - вперед на 75 шагов
* команды могут быть короткими
    * t.fd(75) - вперед на 75 шагов.
* Число шагов может быть < 0.
    * "Иди назад на 50 шагов" можно написать `t.backward(50)` или `t.fd(-50)`
    
## Задача: Запустите программу


* Нажмите на кнопку Run - запустите программу.
* Измените программу. Пусть черепаха идет вперед на 100 шагов.
* Нажмите на кнопку Run. Проверьте, что программа работает правильно.
* Нажмите на кнопку Submit. Пошлите программу на проверку.

![отрезок](https://stepik.org/media/attachments/lesson/479498/1_1_fd.png)


## Цвет

Надо нарисовать синюю (blue) линию.

```python
t.color('blue')   # черепаха рисует синим цветом
```    

Цвет - это текст.

Текст пишем в 'кавычках' или в "двойных кавычках".

![цвета](https://stepik.org/media/attachments/lesson/479498/color_bar.png)

```python
import turtle       # познакомили с пакетом turtle (черепаха)

t = turtle.Turtle() # сделали черепаху, назвали t
t.shape('turtle')
t.width(5)

t.color('green')    # цвет зеленый
t.forward(75)       # вперед 75 шагов

turtle.done()       # конец
```

Нарисует 

![зеленый отрезок](https://stepik.org/media/attachments/lesson/479498/1_2_color.png)

## TASKTEXT Задача: зеленый и красный

Нарисовать:

* цвет зеленый, 75 шагов
* цвет красный, 75 шагов

Послать решение (submit).

![зеленый и красный](https://stepik.org/media/attachments/lesson/479498/1_2_task.png)

## Налево и направо

```python
t.right(angle)
t.rt(angle)
```
Повернуть **направо** на *angle* градусов.

Turn turtle right by angle units. (Units are by default degrees, but can be set via the degrees() and radians() functions.) 

```python
t.left(angle)
t.lt(angle)
```
Повернуть **налево** на *angle* градусов.

Turn turtle left by angle units. (Units are by default degrees, but can be set via the degrees() and radians() functions.) 

* Угол (angle) задается в градусах
* Угол может быть < 0.   Одинаково: `t.left(90)` и `t.right(-90)`

## Пример: налево и направо

![угол](https://stepik.org/media/attachments/lesson/479498/t3_ex.png)


```python
import turtle         # познакомили с пакетом turtle (черепаха)

t = turtle.Turtle()   # сделали черепаху, назвали черепаху t
t.shape("turtle")
t.width(3)            # ширина кисти

t.forward(75)         # вперед 75 
t.left(90)            # налево на 90 градусов
t.forward(75)         # вперед 75

turtle.done() 
```

## TASKTEXT Задача: ступеньки

Нарисовать:

![ступеньки](https://stepik.org/media/attachments/lesson/479498/t3.png)

```python
import turtle         # познакомили с пакетом turtle (черепаха)

t = turtle.Turtle()   # сделали черепаху, назвали черепаху t
t.shape("turtle")
t.width(3)            # ширина кисти

t.forward(75)         # вперед 75 
t.left(90)            # налево на 90 градусов
t.forward(75)         # вперед 75

# тут нужно написать код

turtle.done() 
```

## TASKTEXT Задача: квадрат

Нарисовать квадрат со стороной 100.

![квадрат](https://stepik.org/media/attachments/lesson/479498/t4.png)

## TASKTEXT Задача: треугольник

Нарисовать равносторонний треугольник со стороной 100.

![треугольник](https://stepik.org/media/attachments/lesson/479498/t6_1.png)

Математика:

* Все углы равностороннего треугольника одинаковые. Углы равны 60 градусам.
* Сумма смежных углов 180 градусов

![формула](https://stepik.org/media/attachments/lesson/479498/formula.png)

## TASKTEXT Задача: T

Каждый студент решает свой вариант.

Номер варианта дает преподаватель.

В начале программы надо написать:
```python
# Вариант: номер варианта
```

| Вариант | Нарисовать |
|----|-----|
| Вариант 1 | ![вариант 1](https://stepik.org/media/attachments/lesson/479498/t211.png) |
| Вариант 2 | ![вариант 2](https://stepik.org/media/attachments/lesson/479498/t212.png) |
| Вариант 3 | ![вариант 3](https://stepik.org/media/attachments/lesson/479498/t213.png) |

## TASKTEXT Задача: веер

Каждый студент решает свой вариант.

Номер варианта дает преподаватель.

В начале программы надо написать:

```python
# Вариант: номер варианта
```

| Вариант | Нарисовать |
|----|-----|
| Вариант 1 | ![вариант 1](https://stepik.org/media/attachments/lesson/479498/t241.png) |
| Вариант 2 | ![вариант 2](https://stepik.org/media/attachments/lesson/479498/t242.png) |
| Вариант 3 | ![вариант 3](https://stepik.org/media/attachments/lesson/479498/t243.png) |



