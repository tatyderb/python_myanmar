# Аргументы и возвращаемое значение

lesson = 1108241

## Аргументы метода

Так как метод - это функция, определенная внутри класса, то для него действуют все правила для позиционных и именованных аргументов и значения по умолчанию.

Мы написали класс `Segment1`:

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
Добавим в класс метод `has_point(x)`, который проверяет, содержит ли отрезок точку `x`, по умолчанию считаем `x=0`:


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
        
    def has_point(self, x=0):
        """ Проверяет, принадлежит ли точка х отрезку """
        return self.start <= x <= self.finish 

# тут объявление класса закончено, можно его использовать

# использование класса:    

a = Segment1(2, 10)
d = a.length()
print(f'Отрезок a {a} длиной {d}')   # Отрезок a [2, 10] длиной 8
if a.has_point(4):
    print(f'отрезок {a} содержит точку 4')          # отрезок [2, 10] содержит точку 4
else:
    print(f'отрезок {a} НЕ содержит точку 4')
    
b = Segment1(-3, 1)
x1 = 20
if b.has_point(x1):
    print(f'отрезок {b} содержит точку {x1}')
else:
    print(f'отрезок {b} НЕ содержит точку {x1}')    # отрезок [-3, 1] НЕ содержит точку 20
    
x2 = -1
if b.has_point(x2):
    print(f'отрезок {b} содержит точку {x2}')       # отрезок [-3, 1] содержит точку -1
else:
    print(f'отрезок {b} НЕ содержит точку {x2}')

# значение по умолчанию 0
if b.has_point():
    print(f'отрезок {b} содержит точку 0')          # отрезок [-3, 1] содержит точку 0
else:
    print(f'отрезок {b} НЕ содержит точку 0')
```

## QUIZ 

Что будет напечатано?

```python
class Bag:
    def __init__(self, money=0):
        self.money = money
        
    def add_money(self, delta):
        self.money += delta
        
sumka = Bag(100)
wallet = Bag(300)
print(sumka.money, wallet.money)
```

A. 100 300
B. money money
C. 300 300
D. 100 100
E. 0 0
F. произойдет ошибка

ANSWER: A

## QUIZ вызов метода с аргументом

Выберите все корректные вызовы метода `add_money` у объекта класса `Bag`.

```python
class Bag:
    def __init__(self, money=0):
        self.money = money
        
    def add_money(self, delta):
        self.money += delta
        
sumka = Bag(100)
```

A. `sumka.add_money(200)`
B. `sumka.add_money(-40)`
C. `sumka.add_money()`

ANSWER: A,B

## NUMBER 

Что будет напечатано?

```python
class Bag:
    def __init__(self, money=0):
        self.money = money
        
    def __repr__(self):
        return str(self.money)
        
    def add_money(self, delta):
        self.money += delta
        
sumka = Bag(100)
sumka.add_money(200)
print(sumka)
```

ANSWER: 300

## NUMBER 

Что будет напечатано?

```python
class Bag:
    def __init__(self, money=0):
        self.money = money
        
    def __repr__(self):
        return str(self.money)
        
    def add_money(self, delta):
        self.money += delta
        
sumka = Bag()
sumka.add_money(200)
print(sumka)
```

ANSWER: 200


## Объекты в аргументах

Всё, что в питоне существует - это объекты. Числа - объекты типа `int` или `float`, строки - объекты типа `str`. Функции - тоже объекты (но про это расскажем гораздо позже). Поэтому всё, что мы можем передать в аргументы функции или вернуть из нее - ссылки на объекты.

### Объект как аргумент функции

Ничего нового. Мы узнаем, что все время раньше передавали в аргументы функции ссылки на объекты.

```python
class Segment1:
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

a = Segment1(2, 10)
d = a.length()
print(f'Отрезок a {a} длиной {d}')   # Отрезок a [2, 10] длиной 8
```


Напишем функцию, `is_crossed(a, b)`, которая возвращает, пересекаются ли отрезки `a` и `b` или нет. 
Сначала опишем использование этой функции:

```python
a = Segment1(-2, 10)
b = Segment1(5, 12)
c = Segment1(11, 15)

print(a, b, is_crossed(a, b))   # [-2, 10] [5, 12] True
print(b, a, is_crossed(b, a))   # [5, 12] [-2, 10] True
print(a, c, is_crossed(a, c))   # [-2, 10] [11, 15] False
print(c, a, is_crossed(c, a))   # [11, 15] [-2, 10] False
```
Пусть у нас два отрезка, *one* и *other*. Отрезки НЕ пересекаются, если второй отрезок или строго правее, или строго правее левее отрезка.

```
          one                          other
    |-----------|               |--------------|
one.start    one.finish    other.start    other.finish
```
или
```
              other                 one      
     |--------------|          |-----------|  
other.start    other.finish one.start    one.finish
```
То есть `one.finish < other.start` или `other.finish < one.start`

Во всех остальных случаях отрезки пересекаются.

```python
def is_crossed(one, other):
    """ Возвращает пересекаются ли отрезки one и other"""
    if one.finish < other.start or other.finish < one.start:
        return False
    return True
```
Заметим, что аргументы функции - ссылки на объекты. Ссылки на объекты класса `Segment1` записаны в переменных `one` и `other`.

*Числа типа `int` или `float`, строки - все в питоне является объектами. Раньше мы передавали в функции ссылку на объект, но не знали об этом*:
```python
s = 'Hello!'    # 'Hello' - объект класса str, в переменной s хранится ссылка на этот объект
print(s)        # в функцию print передаем ссылку на объект, которая хранится в переменной s
```

### Bнутри класса

Внесем функцию пересечения отрезков в класс. Назовем её, чтобы не путаться в названиях, `is_crossed_method`. Можно оставить у них одинаковые названия. Интерпретатор питона различает эти функции, потому что одна - вне классов, а вторая принадлежит классу `Segment1`.

Заменим параметры `one` и `other` на `self` и `other`.

Обратите внимание, что в вызове функции в точечной нотации передаём единственный параметр `other`:

```python
a.is_crossed_method(b)
```
Получится:
```python
class Segment1:
    """ Одномерный отрезок."""

    # инициализация объекта класса (конструктор объекта класса)
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish
        dist = self.length()
        self.dist = dist

    def __repr__(self):
        s = f'[{self.start}, {self.finish}]'
        return s

    def is_crossed_method(self, other):
        """ Возвращает пересекаются ли отрезки one и other"""
        if self.finish < other.start or other.finish < self.start:
            return False
         
# здесь закончилось описание класса
         
a = Segment1(-2, 10)
b = Segment1(5, 12)
c = Segment1(11, 15)
           
print(a, b, a.is_crossed_method(b))    # [-2, 10] [5, 12] True
print(a, c, c.is_crossed_method(a))    # [-2, 10] [11, 15] False
```

### Объект изменяется

Напишем метод `shift`, который сдвигает оба конца отрезка на `dx`

```python
class Segment1:
    """ Одномерный отрезок."""

    # инициализация объекта класса (конструктор объекта класса)
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __repr__(self):
        s = f'[{self.start}, {self.finish}]'
        return s

    def shift(self, dx):
        self.start = self.start + dx    # читаем старое значение self.start и записываем в этот атрибут новое значение
        self.finish += dx               # то же самое, но в краткой форме
         
# здесь закончилось описание класса
         
a = Segment1(-2, 10)
           
print(a)    # [-2, 10]
a.shift(3)  # сдвинули отрезок a на 3 вправо
print(a)    # [1, 13]
```

Заметим, объект изменился.

### Возвращаем ссылку на новый объект

Напишем метод `move`, который возвращает *новый отрезок*, лежащий на `dx` правее этого.

```python
class Segment1:
    """ Одномерный отрезок."""

    # инициализация объекта класса (конструктор объекта класса)
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __repr__(self):
        s = f'[{self.start}, {self.finish}]'
        return s

    def shift(self, dx):
        """ сдвигает этот отрезок на dx """
        self.start = self.start + dx    # читаем старое значение self.start и записываем в этот атрибут новое значение
        self.finish += dx               # то же самое, но в краткой форме
        
    def move(self, dx):
        """ возвращает новый отрезок на dx правее """
        tmp = Segment1(self.start + dx, self.finish + dx)   # создали новый объект
        return tmp                                          # вернули на него ссылку
         
# здесь закончилось описание класса
         
a = Segment1(-2, 10)
           
print(a)    # [-2, 10]
b = a.move(3)
print(a)    # [-2, 10]  отрезок не изменился
print(b)    # [1, 13]   новый отрезок на нужном месте
```
Заметим, сам объект не изменился. Создали новый объект с нужными атрибутами и вернули на него ссылку.

### Добавить

1. a.is_crossed(Segment(1, 2))
2. Реализовать Segment().shift().shift()
3. Лучше сказать, что метод может ничего не возвращать, возвращать результат, возвращать копию (может быть с изменениями) и self
