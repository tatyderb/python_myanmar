# Функции

lesson = 501267

## SKIP VIDEO https://www.youtube.com/embed/iOgdQPYBSsI

Тут видео загруженное в шаг

## 2 треугольника

[Видео](https://www.youtube.com/embed/iOgdQPYBSsI)

Нарисуем 2 треугольника.

![](https://stepik.org/media/attachments/lesson/501267/2tri.png)

Хорошо: код работает. 

Плохо: большой код.

Код повторяется. Можно одинаковый код писать короче.

```python
import turtle

t = turtle.Turtle()
t.pensize(4)
t.pencolor('red')

t.fd(100)   # рисуем 1 треугольник
t.lt(120)

t.fd(100)
t.lt(120)

t.fd(100)
t.lt(120)

t.lt(45)    # повернулись
t.pencolor('green')

t.fd(100)   # рисуем 2 треугольник
t.lt(120)

t.fd(100)
t.lt(120)

t.fd(100)
t.lt(120)

turtle.done()
```

## SKIP VIDEO https://youtu.be/u3MzjAhgFkA

Встроенное видео

## Определение функции

[Видео](https://youtu.be/u3MzjAhgFkA)

* Команды черепахи:
    * forward
    * backward
    * left
    * right
    
Научим черепаху новой команде:
```python
def tri():
    t.fd(100)
    t.lt(120)

    t.fd(100)
    t.lt(120)

    t.fd(100)
    t.lt(120)
```

Пишем новую команду в python:
```python
def имя():
    старые команды
```

* **def** - слово языка python, от английского слова "define" (определить)

Определение в математике: **Равносторонний треугольник** - это треугольник, у которого все стороны равны.

Определение в python: команда `tri` - это прямо 100, налево 120, прямо 100, налево 120, прямо 100, налево 120.

Новая команда черепахи называется **функция**. 

* **def** - слово языка python
* `triangle` - имя функции. Придумали сами. Я придумала `triangle`.
* `( )` - функции нужны скобки как в математике
* `:` - обязательно. Это **двоеточие** ("две точки").

Мы перевели на язык python "triangle это функция. Она делает:"

Что делает новая функция? Пишем ниже. Нужен отступ (анг. "indent") 1 табуляция 
![клавиша табуляции](https://stepik.org/media/attachments/lesson/501267/tab_key.jpg)

Закончился отступ - закончилось определение новой функции `triangle`.

## SKIP VIDEO https://youtu.be/1snAjTm_I7U

Видео

## Вызов функции

[Видео](https://youtu.be/1snAjTm_I7U)

Исполнение функции - это **вызов** функции.

```python
triangle()
```

Вся программа:
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
t.pensize(3)
t.color('red')

# выполняется новая команда triangle
triangle()      

turtle.done()
```

## SKIP VIDEO https://youtu.be/YAhMGJXDfx4

https://youtu.be/YAhMGJXDfx4

## Много вызовов

[Видео](https://youtu.be/YAhMGJXDfx4)

Нарисуем 3 треугольника. У нас есть новая функция `triange()`.

```python
t.pencolor('red')
triangle()      # вызов функции triange
t.lt(45)
t.pencolor('green')
triangle()      # вызов функции triange
t.lt(45)
t.pencolor('blue')
triangle()      # вызов функции triange
```

![3 треугольника](https://stepik.org/media/attachments/lesson/479594/01_tri3.png)

Код короткий и понятный.

Функцию назвали `triangle`. Читаем и понимаем, что делает `triangle`. Понятное имя функции.

Плохо: назвать функцию `tttttttttttttttttqqqqqqqqqqqq` вместо `triangle`. Она работает. Плохо читать. Непонятно.

Вся программа:
```python
import turtle

t = turtle.Turtle()
t.pensize(4)

# определение новой функции triangle
def triangle():
    t.fd(100)
    t.lt(120)

    t.fd(100)
    t.lt(120)

    t.fd(100)
    t.lt(120)
# здесь функция triangle закончилась

t.pencolor('red')
triangle()          # вызов функции triange
t.lt(45)
t.pencolor('green')
triangle()          # вызов функции triange
t.lt(45)
t.pencolor('blue')
triangle()          # вызов функции triange
    
turtle.done()
```

## Определение до вызова

В школе сначала учим, потом используем. TODO: нужен пример!

В программе сначала определяем новую функцию. Потом ее используем.

Нельзя сначала использовать, потом определить. Ошибка.
```python
import turtle

t = turtle.Turtle()
t.pensize(4)
t.pencolor('red')

triangle()      # Ошибка! Не знаю triangle

# определение новой функции triangle
def triangle():
    t.fd(100)
    t.lt(120)

    t.fd(100)
    t.lt(120)

    t.fd(100)
    t.lt(120)
# здесь функция triangle закончилась

turtle.done()
```
получим:
```cpp
NameError: name 'triangle' is not defined
```

## Методы и функции

```python
t.fd(100)     # команда черепахи, начинается с t.
```    

* **Метод** - это функция черепахи. Уже знаем.
    * `t.fd(100)` - "черепаха вперед 100 шагов"
    * `имя черепахи` **точка** `что делать`

```python
triangle()    # новая команда, t. не нужно
```
    
* **Функция** - 
    * `triangle()` - "нарисовать треугольник"
    * `что делать`
    
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
    
    





