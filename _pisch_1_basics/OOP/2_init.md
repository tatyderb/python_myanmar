# `__init__` и `__repr__`

lesson = 1108238

## Конструктор

Мы написали класс `Segment1`:
```python
class Segment1:
    """ Одномерный отрезок. """
    
    def length(self):
        """ Возвращает длину отрезка. """
        return self.finish - self.start
       
a = Segment1()
a.start = 2
a.finish = 10

d = a.length()
print(f'Отрезок a от {a.start} до {a.finish} длиной {d}')   # Отрезок a от 2 до 10 длиной 8
```

### Инициализация объекта `__init__`

1. Как будет работать метод `length`, если после создания объекта, ему забудут создать нужный атрибут или ошибутся в его имени?

2. Можно ли написать короче код создания одного объекта (отрезка от 2 до 10)?

Принято определять все атрибуты объекта сразу при его создании. Для этого в классе определяют метод со специальным "магическим" именем `__init__`. Этот метод называют **конструктором** объекта или "метод init".

При создании экземпляра класса:

1. Выделяется память для этого объекта (автоматически! программисты на С++, Java и тем более на С, завидуют вам)
2. Для инициализации данных этого объекта вызывается метод `__init__`, первый аргумент `self` - ссылка на этот объект. 

Так как метод - это та же функция, то можно передать в нее аргументы и установить, если нужно, **значения по умолчанию**.

```python
class Segment1:
    """ Одномерный отрезок. """
    
    def __init__(self, mstart, mfinish):
        """ Отрезок от start до finish. """
        self.start = mstart
        self.finish = mfinish
    
    def length(self):
        """ Возвращает длину отрезка. """
        return self.finish - self.start

# тут объявление класса закончено, можно его использовать

# использование класса:    
a = Segment1(2, 10)
d = a.length()
print(f'Отрезок a от {a.start} до {a.finish} длиной {d}')   # Отрезок a от 2 до 10 длиной 8
```
Заметим, что в конструкторе параметры `mstart` и `mfinish` - это одни переменные, а атрибуты `self.start` и `self.finish` - совершенно другие. И python их не путает, даже если использовать для них одинаковые идентификаторы:
```python
    def __init__(self, start, finish):
        """ Отрезок от start до finish. """
        self.start = start      # self.start и start - разные переменные
        self.finish = finish
```

Что будет, если при создании объекта класса в конструктор передать меньше аргументов? Вы уже знаете, что будет, если передать функции меньше аргументов, чем нужно. Будет ошибка.

```python
b = Segment1(-5)
```
Получим сообщение об ошибке.
```python
TypeError: Segment1.__init__() missing 1 required positional argument: 'finish'
```
Заметьте, 

* **в `__init__` у нас описано 3 параметра: `self`, `start`, `finish`, а передаем в скобках явно 2 аргумента.**
* метод `__init__` ничего не возвращает (то есть возвращает `None`), иначе получим ошибку.

## Значения по умолчанию

Метод - это функция. Параметры метода могут иметь значения по умолчанию. Опишем класс `Circle`, который хранит окружности на плоскости XY с центром в точке с координатами `x` и `y` и радиусом `r`. По умолчанию координаты равны 0, а радиус 1.
```python
class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r
        
a = Circle(2, 3, 4)     # окружность радиуса 4 с центром в точке (2,3)
g = Circle(x=2, y=3, r=4) 

b = Circle(2, 3)        # окружность радиуса 1 с центром в точке (2,3)
c = Circle(2)           # окружность радиуса 1 с центром в точке (2,0)
d = Circle()            # окружность радиуса 1 с центром в точке (0,0)

f = Circle(r=5)         # окружность радиуса 5 с центром в точке (0,0)
```
Рекомендуем указывать именованные аргументы, `Circle(x=2, y=3, r=4)`, ибо такой вызов

* позволяет поменять порядок аргументов в функции, добавив или удалив значение по умолчанию (вспомним, что они должны быть в конце списка параметров, после них не может идти параметр без значения по умолчанию);
* можно добавить параметры;
* код более читаем, в `Circle(2, 3, 4)` задумаешься, радиус идет первым или последним аргументом.

## QUIZ init-0

Выберите корректный способ создания объекта класса `Bag`.

```python
class Bag:
    def __init__(self):
        self.money = 0
```

A. `sumka = Bag()`
B. `sumka = Bag.__init__()`
C. `sumka = Bag.__init__(self)`
D. `sumka = Bag(self)`
E. `sumka = Bag.self()`

ANSWER: A

## QUIZ init-1

Выберите корректные способы создания объекта класса `Bag`.

```python
class Bag:
    def __init__(self, money):
        self.money = money
```

A. `sumka = Bag()`
B. `sumka = Bag(100)`
C. `sumka = Bag(money=50)`

ANSWER: B,C


## QUIZ init-2

Выберите корректные способы создания объекта класса `Bag`.

```python
class Bag:
    def __init__(self, money=0):
        self.money = money
```

A. `sumka = Bag()`
B. `sumka = Bag(100)`
C. `sumka = Bag(money=50)`

ANSWER: A,B,C

## QUIZ init-3

Выберите корректные способы создания объекта класса `Bag`.

```python
class Bag:
    def __init__(self, money=0, book='Общая физика'):
        self.money = money
        self.book = book
```

A. `sumka = Bag()`
B. `sumka = Bag(100)`
C. `sumka = Bag(money=50)`
D. `sumka = Bag(money=60, book='Математика')`
E. `sumka = Bag(book='Биология', money=70)`
F. `sumka = Bag(book='История')`

ANSWER: A,B,C,D,E,F

## QUIZ init-4

Что будет напечатано?

```python
class Bag:
    def __init__(self):
        print('Вызвана функция __init__')
        
b1 = Bag()
b2 = Bag()
```

Сколько раз будет напечатано `Вызвана функция __init__`

A. 2
B. 4
C. 1
D. 0
E. будет сообщение об ошибке

ANSWER: A

## Печать объекта `__repr__`

```python
a = Segment1(start=2, finish=10)
```

При попытке напечатать `print(a)` получаем строку `<__main__.Segment1 object at 0x000001A8E3D900D0>` (у вас последнее число будет другим). Печатают полное название типа объекта, и начиная с какого адреса в памяти он расположен.

Хочется иметь удобную отладочную печать, чтобы `print(a)` печатало координату начала и конца отрезка по формату `[start,finish]`. При вызове `print(a)` происходит преобразование объекта к типу `str`, которое вызывает метод со специальным именем `__repr__(self)`, если он есть. Метод должен **вернуть строку**. Напишем его.

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

# тут объявление класса закончено, можно его использовать

# использование класса:    
      
a = Segment1(2, 10)
d = a.length()
print(f'Отрезок a {a} длиной {d}')   # Отрезок a [2, 10] длиной 8
```

### Правильная печать информации об объекте

Мы вызывали метод в точечной нотации по ссылке на объект:
```python
a = Segment1(2, 10)
d = a.length()      # a содержит ссылку на объект, для этого объекта вызываем метод length
print(f'Отрезок a {a} длиной {d}')   # Отрезок a [2, 10] длиной 8
```
Если нужно вызвать метод объекта изнутри метода класса, то используем ту же точечную нотацию `объект.метод`. В данном случае это будет ЭТОТ объект, то есть параметр `self`.

```python
self.length()
```

Добавим в функцию `__repr__` вывод длины отрезка:

```python
class Segment1:
    """ Одномерный отрезок. """
    
    def __init__(self, start, finish):
        """ Отрезок от start до finish. """
        self.start = start
        self.finish = finish
        
    def __repr__(self):
        d = self.length()       # длина ЭТОГО отрезка
        return f'[{self.start}, {self.finish}] длиной {d}'
    
    def length(self):
        """ Возвращает длину отрезка. """
        return self.finish - self.start
        
a = Segment1(2, 10)
d = a.length()
print(a)   # [2, 10] длиной 8

```

## QUIZ печать объекта

Чтобы `print(sumka)` напечатала 100, что нужно написать вместо `???`

```python
class Bag:
    def __init__(self, money=0):
        self.money = money
        
    def ???(self):
        return str(self.money)
        
      
sumka = Bag(100)
print(sumka)        # 100
```

A. `__repr__`
B. `repr`
C. `print`
D. `__print__`
E. любое название функции, главное, чтобы она возвращала строку.

ANSWER: A


