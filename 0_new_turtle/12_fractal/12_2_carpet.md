# Ковры и деревья

lesson = 530690

## TASKTEXT Задача. Крест Висека - 2

Вместо 1 квадрата рисуют много квадратов.
Глубина увеличивается

![этапы](https://stepik.org/media/attachments/lesson/479604/cross_iter1.png)

Написать функцию **cross(size, n)** и нарисовать

![задача](https://stepik.org/media/attachments/lesson/479604/t12_cross2.png)

## TASKTEXT Задача. Крест Висека - 1

Вместо 1 квадрата рисуют много квадратов.
Глубина увеличивается

![этапы](https://stepik.org/media/attachments/lesson/479604/cross_iter2.png)

Написать функцию **cross(size, n)** и нарисовать

![задача](https://stepik.org/media/attachments/lesson/479604/t12_cross1.png)


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
