# Координаты

lesson = 505568

## Координаты

* Математики знают:
    * координаты точки `(100, -30)`
    * координатные оси X и Y
* Черепаха знает координаты и оси.
    * черепаха сначала в точке (0, 0)
    * ось Х направлена вправо, как в математике.
    * ось Y направлена вверх, как в математике.

![координатная плоскость]()

## Методы черепахи с координатами

Можно двигать (move) черепаху по указанным координатам. Черепаха не поворачивается.

Это одинаковые команды: 
```python
t.setposition(x, y) # двигать в точку с координатами (x,y)
t.setpos(x, y)      # двигать в точку с координатами (x,y)
t.goto(x, y)        # двигать в точку с координатами (x,y)
```

Можно изменить только одну координату:
```python
t.setx(x)           # изменить х, не менять y
t.sety(y)           # изменить y, не менять x
```

Функция **t.write(текст)** рисует текст черепахой. Можно написать координаты черепахи

```python
t.write(t.pos())
```

Что делает пример?
```python
import turtle

t = turtle.Turtle()

t.write(t.pos())    # (0,0)

t.setpos(100, -50)
t.write(t.pos())    # (100,-50)

t.goto(100, 50)
t.write(t.pos())	# (100, 50)

turtle.done()
```

В replit.com и в IDLE может быть `100` целое число и `100.00`.

![пример](https://stepik.org/media/attachments/lesson/505568/write_small.png)

## Большие буквы

Можно сделать текст больше. Скопируйте в задачи эту функцию `write(text)`

```python
import turtle

# написать текст размером 18
def write(text):
        t.write(text, font=('Arial', 18, 'normal'))

t = turtle.Turtle()


write(t.pos())    # (0,0)


t.setpos(100, -50)
write(t.pos())    # (100,-50)


t.goto(100, 50)
write(t.pos())    # (100, 50)

turtle.done()
```

18 - высота текста. Можно сделать другим.

![большие буквы](https://stepik.org/media/attachments/lesson/505568/write_big.png)


## TASKTEXT Задача: функция line(x1, y1, x2, y2)

Напишите функцию **line(x1, y1, x2, y2)**. Она рисует линию и пишет координаты.

`line(-200, 50, 100, -50)` нарисует 

![отрезки](https://stepik.org/media/attachments/lesson/479595/line.png)

```python
import turtle

def write(text):
        t.write(text, font=('Arial', 18, 'normal'))

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('red')

def line(x1, y1, x2, y2):
    # тут нужно написать код функции
    
line(-200, 50, 100, -50)
    
turtle.done()
```

## TASKTEXT Задача: треугольник по координатам

Напишите функцию **tri(x1, y1, x2, y2, x3, y3)**. 

Она рисует треугольник с вершинами в точках (x1, y1), (x2, y2), (x3, y3) и пишет их координаты.

`tri(-200, 200, 100, 0, -200, 0)` нарисует 

![треугольник](https://stepik.org/media/attachments/lesson/479595/coord_tri.png)

```python
import turtle

def write(text):
        t.write(text, font=('Arial', 18, 'normal'))

# координаты черепахи, целые числа
def coord():
        x = int(t.xcor())
        y = int(t.ycor())
        write((x, y))

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')

def tri(x1, y1, x2, y2, x3, y3):
    # тут нужно написать код функции
    coord()
    
tri(-200, 200, 100, 0, -200, 0)
    
turtle.done()
```

## TASKTEXT Задача: прямоугольник по координатам

Напишите функцию **rect(x1, y1, x2, y2, rect_col, text_col)**. Она рисует прямоугольник.

* x1, y1, x2, y1 - координаты противоположных вершин
* rect_color - цвет внутри
* text_color - цвет текста и линий.


`rect(-10, -20, 200, 150, "green", "red")` нарисует 

![прямоугольник](https://stepik.org/media/attachments/lesson/479595/coord_rect.png)

```python
import turtle

def write(text):
        t.write(text, font=('Arial', 18, 'normal'))

# координаты черепахи, целые числа
def coord():
        x = int(t.xcor())
        y = int(t.ycor())
        write((x, y))


t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def rect(x1, y1, x2, y2, rect_col, text_col):
    # тут нужно написать код функции
    
rect(-10, -20, 200, 150, "green", "red")
    
turtle.done()
```

IDLE и replit.com рисуют по-разному. Любой из этих рисунков - хорошо.

![прямоугольник](https://stepik.org/media/attachments/lesson/505568/t_rect.png)

