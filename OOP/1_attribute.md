# Атрибуты и методы объекта

lesson = 1108157


## Атрибуты объекта и методы

```python
class Segment1:
    """ Одномерный отрезок. """
    pass
```

Создадим объект `a` класса `Segment1` (то есть отрезок).

```python
a = Segment1()  # переменная a ссылается на объект класса Segment1
```
У отрезка должно быть начало и конец. Назовем их `start` и `finish` (мы придумали такие названия). Это атрибуты данного объекта. Зададим их так, чтобы мы описывали отрезок от 2 до 10.
```python
a.start = 2
a.finish = 10
```
Можно напечатать значение атрибутов объекта:
```python
print(a.start, a.finish)    # 2 10
print(f'Отрезок a от {a.start} до {a.finish}')
```
Создадим еще один объект того же класса `Segment1` и запишем ссылку на него в переменную `b`. Зададим у него атрибуты `start` и `finish` так, чтобы они описывали отрезок от -5 до 1. Напечатаем эти значения.

```python
b = Segment1()  # переменная b ссылается на объект класса Segment1
b.start = -5
b.finish = 1

print(f'Отрезок b от {b.start} до {b.finish}')
```

Атрибуты - это переменные. Они тоже ссылаются на данные (числа -5 и 1). Их значения можно менять.

```python
b.finish = 6    # теперь это отрезок от -5 до 6
b.start += 1    # теперь это отрезок от -4 до 6
``` 

Схематично нарисуем переменные, объекты и их атрибуты на **диаграмме объектов**.

**Рисунок a ссылается на объект с атрибутами, атрибуты ссылаются на числа, аналогично b** , диаграмма объектов, как на стр. 142

Полный код программы:
```python
class Segment1:
    """ Одномерный отрезок. """
    pass
# тут объявление класса закончено, можно его использовать

# использование класса:    
a = Segment1()  # переменная a ссылается на созданный объект класса Segment1
a.start = 2
a.finish = 10

print(a.start, a.finish)    # 2 10
print(f'Отрезок a от {a.start} до {a.finish}')      # Отрезок a от 2 до 10

b = Segment1()  # переменная b ссылается на объект класса Segment1
b.start = -5
b.finish = 1

print(f'Отрезок b от {b.start} до {b.finish}')      # Отрезок b от -5 до 1

b.finish = 6    # теперь это отрезок от -5 до 6
b.start += 1    # теперь это отрезок от -4 до 6

print(f'Отрезок b от {b.start} до {b.finish}')      # Отрезок b от -4 до 6
```

### Методы

Чтобы действия с данными не были оторваны от данных, можно добавить в класс функцию.

Напишем обычную функцию (вне класса), которая вычисляет длину отрезка:
```python
def length(seg):
    """ Возвращает длину отрезка seg. """
    d = seg.finish - seg.start
    return d
    
# вызовем эту функцию для объектов, на которые ссылаются переменные a и b
d = length(a)
print(f'Отрезок a от {a.start} до {a.finish} длиной {d}')   # Отрезок a от 2 до 10 длиной 8

d = length(b)
print(f'Отрезок b от {b.start} до {b.finish} длиной {d}')   # Отрезок b от -4 до 6 длиной 10
```

Перенесем эту функцию внутрь класса `Segment1` и вызовем ее по полному имени (имя класса и имя функции в нем). *Предупреждение: данный синтаксис может привести к крикам "так никто не пишет!!!" у знатоков питона. Подождите чуть-чуть и мы перепишем этот фрагмент привычным образом.*

**Функции внутри класса пишут с дополнительным отступом, чтобы интерпретатор понял, что этот код принадлежит классу.**

```python
class Segment1:
    """ Одномерный отрезок. """
    def length(seg):
        """ Возвращает длину отрезка seg. """
        d = seg.finish - seg.start
        return d
# тут объявление класса закончено, можно его использовать

# использование класса:    
a = Segment1()
a.start = 2
a.finish = 10

d = Segment1.length(a)
print(f'Отрезок a от {a.start} до {a.finish} длиной {d}')   # Отрезок a от 2 до 10 длиной 8
```
Этот код работает. Но его можно записать короче, через синтаксис с точкой. `переменная.метод()`

Вместо
```python
d = Segment1.length(a)
```
Напишем
```python
d = a.length()
```
Так как переменная `a` ссылается на объект класса `Segment1`, то вызовется функция `length` этого класса. Чтобы не писать дважды одну и ту же ссылку, первый аргумент функции, ссылку на ЭТОТ объект, при вызове не пишут. Потому что мы написали ее раньше. Вызовется функция именно для этого объекта, на который ссылается `a`. То есть у объекта есть и атрибуты `start` и `finish` и функция `length`.

**Функция, определенная внутри класса, называется методом.** Далее мы будем употреблять то слово "метод", то "функция".

Вы уже работали с методами объектов. 
```python
text = input()          # вызвали функцию input, она создала объект класса str, на объект ссылается переменная text
words = text.split()    # у объекта класса str вызвали метод split
```
При создании игры мы писали `display.blit(player_img, (0, 0))`. В выражении `display` - ссылка на объект одного из классов `pygame`, у этого класса есть метод `blit` с аргументами.

### self

**Первым аргументом метода объекта должна быть ссылка на этот объект.** 

Принято параметр для этой ссылки называть **self** (ссылка на ЭТОТ объект). Мы в методе `length` назвали этот параметр `seg`. Как видите, синтаксически это корректная запись, но **все программисты используют название self**. 

Перепишем наш код:

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
Можно вызов метода объекта сделать прямо в форматной строке:
```python
print(f'Отрезок a от {a.start} до {a.finish} длиной {a.length()}')   # Отрезок a от 2 до 10 длиной 8
```

### инициализация объекта `__init__`

Как будет работать метод `length`, если после создания объекта, ему забудут создать нужный атрибут или ошибутся в его имени?

Чтобы не мучиться этим вопросом, принято определять все атрибуты объекта сразу при его создании. Для этого в классе определяют метод со специальным "магическим" именем `__init__`. Этот метод называют **конструктором** объекта или "метод init".

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
Заметьте, в `__init__` у нас описано 3 параметра: `self`, `start`, `finish`, а передаем в скобках явно 2 аргумента.

### Печать объекта `__repr__`

При попытке напечатать `print(a)` получаем строку `<__main__.Segment1 object at 0x000001A8E3D900D0>` (у вас последнее число будет другим). Печатают полное название типа объекта, и начиная с какого адреса в памяти он расположен.

Хочется иметь удобную отладочную печать, чтобы `print(a)` печатало координату начала и конца отрезка по формату `[start,finish]`. При вызове `print(a)` происходит преобразование объекта к типу `str`, которое вызывает метод со специальным именем `__repr__(self)`, если он есть. Метод должен вернуть строку. Напишем его.

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

### Вызов метода того же объекта в классе

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
        return f'[{self.start}, {self.finish}] длины {d}'
    
    def length(self):
        """ Возвращает длину отрезка. """
        return self.finish - self.start
```


## QUIZ Параметры методов - 1

Какой параметр должен иметь каждый метод объекта (экземпляра) класса `Point`?

A. `self`
B. `myself`
C. `this`
D. `Point`
E. `point`
F. `__init__`

ANSWER: A

## QUIZ Параметры методов - 2

В методе экземпляра класса параметр `self` :

A. должен быть первым параметром
B. должен быть последним параметром
C. должен быть одним из параметров, в любом месте
D. может быть, а может не быть, это не обязательный параметр

ANSWER: A

## QUIZ место

Отметьте все правильные объявления метода `foo` экземпляров класса `A`, которому передают два целых числа через параметры `n` и `m`.

A. `def foo(self, n, m):`
B. `def foo(n, m, self):`
C. `def foo(n, self, m):`
D. `def foo(n, m):`

ANSWER: A

## QUIZ вызов метода

Выберите все корректные вызовы метода `voice` у объекта класса `Cat`.

```python
class Cat:
    def voice(self):
        print('Мяу')
        
barsik = Cat()
```

A. `barsik.voice()`
B. `Cat.voice(barsik)`
C. `barsik.voice(self)`
D. `barsik.voice(barsik)`
E. `Cat.voice(self)`
F. `voice(barsik)`
G. `voice(Cat)`

ANSWER: A,B

## QUIZ поезд

Выберите все корректные вызовы метода `tutu` у объекта класса `Train`.

```python
class Train:
    def tutu(self, station):
        print(f'Поезд следует до станции {station}')
        
t = Train()
```

A. `t.tutu('Новодачная')`
B. `t.tutu()`
C. `t.tutu(17, 'Новодачная')`
D. `t.tutu(self, 'Новодачная')`
E. `Train.tutu(t, 'Новодачная')`
F. `Train.tutu(self, t, 'Новодачная')`

ANSWER: A,E

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

## QUIZ 

Что будет напечатано?

```python
class Bag:
    def __init__(self, money=0):
        self.money = money
        
    def add_money(self, delta):
        self.money += delta
        
sumka = Bag(100)
valet = Bag(300)
print(sumka.money, valet.money)
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


