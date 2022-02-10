# Команды turtle (продолжение)

lesson = 499642

## Не рисовать

Надо нарисовать 

![2 отрезка](https://stepik.org/media/attachments/lesson/479499/t2_2e.png)

Новые команды: `penup` и `pendown`.

### pendown

**Рисовать**, когда движется.

Pull the pen down – drawing when moving.

```python
t.pendown()    # полная форма
t.pd()         # короткая форма
t.down()       # короткая форма
```

![pendown](https://stepik.org/media/attachments/lesson/479499/pen_down.png)

### penup

**НЕ Рисовать**, когда движется.

Pull the pen down – NO drawing when moving.

```python
t.penup()       # полная форма
t.pu()          # короткая форма
t.up()          # короткая форма
```

![pendown](https://stepik.org/media/attachments/lesson/479499/pen_up.png)

## Пример: 2 отрезка

Рисуем

![2 отрезка](https://stepik.org/media/attachments/lesson/479499/t2_2e.png)

```python
import turtle         # познакомили программу с пакетом turtle (черепаха)

t = turtle.Turtle()   # сделали черепаху, назвали черепаху t

t.forward(75)         # вперед 75
t.up()                # поднять карандаш
t.forward(75)         # вперед 75 (линии не видно)
t.down()              # опустить карандаш
t.forward(75)         # вперед 75

turtle.done()         # чтобы окно не закрывалось, на repl.it не нужно
```

## TASKTEXT Задача: отрезки

Каждый студент решает свой вариант.

Номер варианта дает преподаватель.

В начале программы надо написать:
```python
# Вариант: номер варианта
```

| Вариант | Нарисовать |
|----|-----|
| Вариант 1 | ![вариант 1](https://stepik.org/media/attachments/lesson/479499/t221.png) |
| Вариант 2 | ![вариант 2](https://stepik.org/media/attachments/lesson/479499/t222.png) |
| Вариант 3 | ![вариант 3](https://stepik.org/media/attachments/lesson/479499/t223.png) |

## Цвет линии и цвет внутри

Рисуем

![квадрат](https://stepik.org/media/attachments/lesson/479499/t2_3e.png)

Разный **цвет линии** (красный) и **цвет внутри** (желтый)

TODO: видео с крупной черепахой, которая меняет цвет

```python
t.color('red', 'yellow') # red - цвет линии, yellow - цвет внутри
t.color('blue')          # blue - цвет линии, blue - цвет внутри
t.pencolor('green')      # green - цвет линии, цвет внутри не изменился
t.fillcolor('gold')      # gold - цвет внутри, цвет линии не изменился
```

### Цвет внутри

t.**begin_fill()**    # начали рисовать с цветом внутри
рисуем квадрат        
t.**end_fill()**      # закончили рисовать с цветом внутри

Фигура должна быть **замкнутой**. Например: квадрат, треугольник, круг, многоугольник.

```python
import turtle

t = turtle.Turtle()

t.color('red', 'yellow')  # линия - красный, внутри - желтый

t.begin_fill()        # начинаем рисовать замкнутую фигуру

t.forward(75)         # нарисуем квадрат
t.left(90)            
t.forward(75)         
t.left(90)            
t.forward(75)         
t.left(90)            
t.forward(75)         
t.left(90)      

t.end_fill()          # заканчиваем рисовать фигуру

turtle.done()
```

## TASKTEXT Задача: треугольник

Нарисовать

![треугольник](https://stepik.org/media/attachments/lesson/479499/t2_4.png)

## TASKTEXT Задача: ромб

Нарисовать

![ромб](https://stepik.org/media/attachments/lesson/479499/t2_3t.png)

## TASKTEXT Задача: радуга (rainbow)

Нарисовать

![радуга](https://stepik.org/media/attachments/lesson/479499/rainbow.png)

Цвет:  blue, violet, green, red, yellow.

## TASKTEXT Задача: 2 квадрата

Нарисовать

![2 квадрата](https://stepik.org/media/attachments/lesson/479499/sq2.png)

## TASKTEXT Задача: 2 квадрата на расстоянии

Нарисовать

![2 квадрата](https://stepik.org/media/attachments/lesson/479499/sq2_dist.png)

## TASKTEXT Задача: пентаграмма или звезда

**Вариант выберите какой вы хотите**. В "вариант 1" математика проще. В "вариант 2" математика сложнее.

В начале программы надо написать:
```python
# Вариант: номер варианта
```

| Вариант | Нарисовать |
|----|-----|
| Вариант 1 | ![вариант 1](https://stepik.org/media/attachments/lesson/479499/pent.png) |
| Вариант 2 | ![вариант 2](https://stepik.org/media/attachments/lesson/479499/star.png) |

Свойства пятиугольника:

* Угол звезды 36 градусов.
* Угол пятиугольника 108 градусов.

![углы пятиугольника](https://stepik.org/media/attachments/lesson/479499/pentagramm.png)


## TASKTEXT Задача не обязательная

Задачу можно **НЕ делать**.

Цифры можно писать так:

![цифры](https://stepik.org/media/attachments/lesson/479499/post_index_small.png)

Выберите сами один вариант:

* Вариант 1. Напишите год. Сейчас или год рождения.
* Вариант 2. Напишите время. Например, `12:34`
* Вариант 3. Напишите ваше имя.

