# Атрибуты класса и статические методы

lesson = 1247797

## Класс Circle

Напишем класс, который описывает окружность с центром с координатами $x$ и $y$ и радиусом $r$.

В нем реализуем методы **экземпляров класса** `area` и `length` для вычисления площади круга и длины окружности.

```python
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
    def length(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2
```

Допустим, что мы забыли о `math.pi`, не знаем о `numpy.pi` <strike>и в гугле нас тоже забанили</strike>. Хотим объявить переменную `pi` в классе `Circle`.

Если мы напишем в конструкторе `self.pi = 3.1415`, то мы:

1. Будем использовать лишнюю память, храня $pi$ для каждой окружности.
2. Будет трудно перейти "на лету" к более точному значению $pi$, потому что у каждой окружности своя личная $pi$ и нужно найти все окружности и поменять значение у каждой из них.

По логике $pi$ - общая для всех окружностей величина. И принадлежит всем окружностям, как идеи. Хочется в классе иметь возможность определить атрибут (переменную), который принадлежит классу целиком, а не конкретному экземпляру класса.

Это можно сделать, если написать атрибут вне методов:

```python
class Circle:
    pi = 3.1415
    
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
    def length(self):
        return 2 * Circle.pi * self.radius

    def area(self):
        return Circle.pi * self.radius ** 2        
```

* **Атрибут класса** - это переменная, которая определена внутри класса, но вне любого метода (экземпляра класса)
* Обращение к атрибуту класса `имя_класса.атрибут`

На самом деле, все в языке - объекты. И сам класс целиком описывает так называемый "class object", один на каждый класс. Он содержит в себе все такие переменные класса. (Ничего нового: объект, в нем есть переменная, только синтаксис для доступа к этому объекту непривычный).

Создадим несколько экземпляров класса `Circle`:

```python
a = Circle(x=1, y=2, radius=4.5)
b = Circle(x=-6, y=-1.5, radius=10.7)

print(a.radius)     # 4.5
print(b.y)          # -1.5
print(Circle.pi)    # 3.1415
```
![class object](https://stepik.org/media/attachments/lesson/1247797/pi.png)

Так как каждый объект имеет доступ к описанию всего класса (то есть class object, на рисунке более темный объект). Class object один на весь класс. Все экземпляры класса имеют доступ к этому объекту. Поэтому обратиться к экземпляру класса можно как по ссылке на сам класс, так и по ссылке на любой объект этого класса:

```python
print(Circle.pi)    # 3.1415
print(a.pi)         # 3.1415
print(b.pi)         # 3.1415
```
**Изменить** значение атрибута класса тоже можно по ссылке на сам класс или на любой из объектов этого класса <strike>уберите от экрана математиков</strike>:

```python
Circle.pi = 100
print(a.pi)         # 100
b.pi = 777
print(a.pi)         # 777
```

Атрибут `pi` класса `Circle` - это **одно** место в памяти, общее для всех объектов этого класса, к которому можно доступиться или через имя класса, или через ссылку на любой объект.

Не путайте:

* **атрибут экземпляра класса** - характеризует один конкретный объект (радиус конкретной окружности, `a.x`).
* **атрибут класса** - характеризует весь класс целиком; нельзя сказать, что это характеристика одного экземпляра класса и у другого экземпляра этого же класса она будет другая, `Circle.pi`

## SKIP TABLE

Определите, какие атрибуты являются атрибутами класса, а какие - атрибутами экземпляра класса (объекта класса).

Доступен класс `Cat` и экземпляры этого класса `barsik` и `murka`.

```python
class Cat:
    leg_number = 4
    voice = 'мяу'
    
    def __init__(self, color, name, gender):
        self.color = color
        self.name = name
        self.gender = gender
    
barsik = Cat('black', 'Барсик', 'кот')
murka = Cat('white', 'Мурка', 'кошка')
```

TABLE

|    | атрибут класса | атрибут экземпляра класса |
|----|----|-----|
| `voice` | + | - |

## QUIZ

```python
class Cat:
    leg_number = 4
    voice = 'мяу'
    
    def __init__(self, color, name, gender):
        self.color = color
        self.name = name
        self.gender = gender
    
barsik = Cat('black', 'Барсик', 'кот')
murka = Cat('white', 'Мурка', 'кошка')
```
Дан класс и экземпляры этого класса. Отметьте, какие обращения к атрибутам являются корректными.

A. `Cat.voice`
B. `barsik.leg_number`
C. `Cat.color`
D. `murka.name`
E. `barsik.gender`

ANSWER: A, B, D, E

## NUMBER

```python
class Example:
    common = 5
    
    def __init__(self, x):
        self.x = x
        
a = Example(7)
print(a.x + Example.common)
```

ANSWER: 12

## NUMBER

```python
class Example:
    common = 5
    
    def __init__(self, x):
        self.x = x
        
a = Example(7)
b = Example(3)

print(a.x + b.common + Example.common)
```
Что будет напечатано?

ANSWER: 17

## NUMBER

```python
class Example:
    common = 5
    
    def __init__(self, x):
        self.x = x
        
a = Example(7)
b = Example(3)
Example.common = 1

print(a.x + b.common + Example.common)
```
Что будет напечатано?

ANSWER: 9

## Статические методы

Иногда функция относится к классу вообще, но нам трудно сказать, к какому экземпляру класса она относится. Вспомним наш одномерный отрезок и функцию, которая проверяет [пересекаются отрезки или нет](https://stepik.org/lesson/1108241/step/6).

```python
class Segment1:
    """ Одномерный отрезок. """
    
    def __init__(self, start, finish):
        """ Отрезок от start до finish. """
        self.start = start
        self.finish = finish
        
    def __repr__(self):
        return f'[{self.start}, {self.finish}]'
    
    def length(self):
        """ Возвращает длину отрезка. """
        return self.finish - self.start
```

Мы написали функцию `is_crossed`, которая проверяла, пересекаются ли отрезки или нет.

```python
def is_crossed(one, other):
    """ Возвращает пересекаются ли отрезки one и other"""
    if one.finish < other.start or other.finish < one.start:
        return False
    return True

a = Segment1(-2, 10)
b = Segment1(5, 12)
c = Segment1(11, 15)

print(a, b, is_crossed(a, b))   # [-2, 10] [5, 12] True
print(b, a, is_crossed(b, a))   # [5, 12] [-2, 10] True
print(a, c, is_crossed(a, c))   # [-2, 10] [11, 15] False
print(c, a, is_crossed(c, a))   # [11, 15] [-2, 10] False
```
Далее мы написали метод экземпляра класса `is_crossed_method`, который проверял, пересекает ли ЭТОТ отрезок другой отрезок и вызывали его как `a.is_crossed_method(b)`

Некоторым из вас форма "отдельной функции" `is_crossed(a, b)` показалась удобнее. Но эта функция идеологически относится к классу одномерных отрезков. Она считает только пересечениях таких отрезков и не работает для пересечения отрезка и объекта другого типа.

Напишем функцию `is_crossed` **внутри класса**. Но подчеркнем, что он не относится ни к одному объекту класса, а ко всему классу целиком. Объекты передаются в аргументах.

* Перед сигнатурой функции пишем `@staticmethod` (это декоратор, мы еще не знаем, что это такое, поэтому пользуемся, как магической формулой)
* **self не пишем**, потому что метод не относится ни к какому конкретному объекту, а всему классу целиком.
* Обращение к методу, так же как к атрибуту класса - по имени класса или ссылке на любой объект этого класса.

Метод, написанный с декоратором `@staticmethod` внутри класса называется **статический метод**.

```python
class Segment1:
    """ Одномерный отрезок. """
    
    def __init__(self, start, finish):
        """ Отрезок от start до finish. """
        self.start = start
        self.finish = finish
        
    def __repr__(self):
        return f'[{self.start}, {self.finish}]'
    
    def length(self):
        """ Возвращает длину отрезка. """
        return self.finish - self.start
    
    # это метод экземпляра класса, у него есть self
    def is_crossed_method(self, other):
        """ Возвращает пересекаются ли отрезки one и other"""
        if self.finish < other.start or other.finish < self.start:
            return False
            
    # это статический метод, у него нет self
    @staticmethod
    def is_crossed(one, other):
        """ Возвращает пересекаются ли отрезки one и other"""
        if one.finish < other.start or other.finish < one.start:
            return False
        return True
    
a = Segment1(-2, 10)
b = Segment1(5, 12)
c = Segment1(11, 15)

# вызов метода экземпляра класса
print(a, b, a.is_crossed_method(b))    # [-2, 10] [5, 12] True
print(a, c, c.is_crossed_method(a))    # [-2, 10] [11, 15] False

# вызов статического метода
print(a, b, Segment1.is_crossed(a, b))   # [-2, 10] [5, 12] True
print(a, c, b.is_crossed(a, c))          # [-2, 10] [11, 15] False
```
Заметим, что в последней строке `b.is_crossed(a, c)` считается пересечение отрезков `a` и `c`, отрезок `b` используется как ссылка для доступа к методу. Не надо писать такие головоломки в рабочем коде! Используйте для вызова имя класса. Подчеркните, что это метод относится к классу целиком, а не к конкретному объекту.

## Статический метод для создания объектов класса

В классе может быть только один метод `__init__`. Что делать, если мы хотим создавать объект класса `Point` (точка на плоскости $XY$) разными способами:

* передавая координаты как числа `p = Point(x=1, y=2)`
* передавая **строку** с набором координат $x$ и $y$ по определенному формату, например через пробел или `;`, этот вариант нужен, когда мы сохраняем через функцию `__repr__` объект, а потом хотим восстановить объект из строки.

Можно в конструктор добавить дополнительный аргумент `text` и конструировать из одних или других аргументов:
```python
def __init__(self, x=None, y=None, text=None):
    if (x is None or y is None) and text is None:
        # тут обрабатываем ошибку, что не все аргументы заданы, не можем сделать точку
    elif text is None:
        # из x и y
        self.x = x
        self.y = y
    else:
        # из text
        self.x, self.y = map(float, text.split())
```
Плохо: 

* дублируется код создания `self.x` и `self.y`, можно или потерять один атрибут, или назвать его по-другому, или ошибиться в определении. Классы могут быть гораздо сложнее.
* нельзя сделать значения по умолчанию `x=0` и `y=0`, мы не знаем, хотим создать точку $(0, 0)$ или у нас ошибка с недоопределенными аргументами при вызове конструктора.

Решение: конструктор пишем с параметрами `x` и `y`. Пишем дополнительно статический метод `create(text)`.

```python
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    @staticmethod
    def create(text):
        """ Создает точку по координатам, заданным через пробел, например '1.5 -6.3'"""
        x, y = map(float, text.split())
        p = Point(x, y)
        return p
        
p1 = Point(1.4, 2.3)
p2 = Point.create('2.7 9.0')
p3 = Point.create(input())
```

## Статический метод для инициализации атрибута класса

Допустим, в классе `Circle` мы хотим задать число $pi$ с конкретной точностью.

Для этого воспользуемся методом [вычисления](https://ru.wikipedia.org/wiki/%D0%9F%D0%B8_(%D1%87%D0%B8%D1%81%D0%BB%D0%BE)) с некоторой точностью. Например, будем считать очередной член ряда Нилаканта, пока он не станет меньше, чем требуемая точность. Тогда мы перестанем считать новые члены последовательности и ограничимся частичной суммой $S_n$ из $n$ членов.

$$S_n = 3 + \frac{4}{2 \cdot 3 \cdot 4} - \frac{4}{4 \cdot 5 \cdot 6} + \frac{4}{6 \cdot 7 \cdot 8} - \frac{4}{8 \cdot 9 \cdot 10} + ...$$$

Реализуем статический метод `pi_nilakantha` и вызовем его:

```python
class Circle:
    pi = Circle.pi_nilakantha(0.001)
    
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
    @staticmethod
    def pi_nilakantha(accuracy):
        # реализация метода
        res = 3   # первый член ряда
        ...
        return res
```

## Статический метод для валидации аргументов

Статические методы часто используют для валидации (проверки правильности) аргументов конструктора:

```python
class Circle:
    def __init__(self, x, y, radius):
        if not Circle.is_valid(x, y, radius):
            print(f'Ошибка! Невалидный набор аргументов Circle(x={x}, y={y}, radius={radius}')
            # гораздо лучше написать raise ValueError('радиус должен быть положительным') но мы пока не знаем об исключениях
        self.x = x
        self.y = y
        self.radius = radius
        
    @staticmethod
    is_valid(x, y, radius):
        if radius <= 0:
            return False
        return True        
```

## QUIZ

Отметьте верные утверждения.

A. Метод экземпляра класса должен иметь параметр `self`, который ссылается на экземпляр класса.
B. Метод экземпляра класса может не иметь ни одного параметра.
C. Статический метод класса должен иметь параметр `self`, который ссылается на экземпляр класса.
D. Статический метод класса может не иметь ни одного параметра.

SHUFFLE: false
ANSWER: A, D

## QUIZ

Отметьте корректные с точки зрения интерпретатора python вызовы метода.

```python
class Cat:
    leg_number = 4
    voice = 'мяу'
    
    def __init__(self, color, name, gender, chip_id=None):
        self.color = color
        self.name = name
        self.gender = gender
        self.chip_id = chip_id
        
    def set_chip(self, chip_id):
        self.chip_id = chip_id
        
    @staticmethod
    def is_valid(color, name, gender):
        if gender == 'кот' or gender == 'кошка':
            return True
        return False
        
    @staticmethod
    def create(csv_str):
        """ Создает из строки вида 'имя;цвет;пол', пол задается как 'самка' или 'самец'."""
        name, color, gender = csv_str.split(';')
        match gender:
            case 'самец': gender = 'кот'
            case 'самка': gender = 'кошка'
            case '_': raise ValueError(f'gender={gender}')       
```

A. `animal = Cat.create('серый;Пушок;самец')`
B. `Cat.is_valid('рыжий', 'Рыжик', 'кот')`
C. `kitty = animal.create('коричневый;Мурка;самка')`
D. `Cat.set_chip(123)`
E. `kitty.set_chip(45678)`

SHUFFLE: false
ANSWER: A, B, C, E

## TASKINLINE Вызов статического метода

НЕ РЕШАТЬ!!! ЗАДАЧА В РАЗРАБОТКЕ

Дан класс (этот код уже есть в проверяющей системе):

```python
class A:
    variable = 5
    
    @staticmethod
    def set_variable(value):
        A.variable = value
```
Вызовите метод `set_variable` с аргументом `77`

TEST
2
----
3
====
