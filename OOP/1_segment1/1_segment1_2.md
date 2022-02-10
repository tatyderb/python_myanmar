# Класс Segment1 (продолжение)

lesson = 532649

## Добавляем новый метод

Следующий метод будет двигать отрезок на **dx**. Назовем его **move**.  Должен изменяться сам отрезок.

Сначала напишем тесты.
```python
def test_move():
    """Проверяем сдвиг отрезка на dx"""
    s1 = Segment1(-120, 50)
    assert str(s1) == '[-120, 50]:170'

    s1.move(40)                     # сдвиг на 40 вправо
    print(s1)
    assert str(s1) == '[-80, 90]:170'
    
    s1.move(-100)                   # сдвиг на 100 влево
    print(s1)
    assert str(s1) == '[-180, -10]:170'
```

Теперь я понимаю что должен делать метод. Пишу метод.

```python
def test_move():
    """Проверяем сдвиг отрезка на dx"""
    s1 = Segment1(-120, 50)
    assert str(s1) == '[-120, 50]:170'

    s1.move(40)                     # сдвиг на 40 вправо
    assert str(s1) == '[-80, 90]:170'
    
    s1.move(-100)                   # сдвиг на 100 влево
    assert str(s1) == '[-180, 190]:170'
```

Вся программа:
```python
# определение класса Segment1
class Segment1:
    """Класс Segment1 описывает отрезки на оси Х"""
    
    def __init__(self, start=0, finish=0):
        # Эта функция вызывается, когда мы создаем новый объект класса.
        # self - это название переменной, которая указвает на сам объект.
        self.start = start      # переменная объекта 
        self.finish = finish

    def __repr__(self):
        mylen = self.length()
        return f'[{self.start}, {self.finish}]:{mylen}'     # не забудьте f перед строкой
        
    def length(self):
        """Возвращает длину отрезка"""
        return abs(self.start - self.finish)

    def move(self, dx):
        """Сдвигает сам отрезок на dx вправо"""
        self.start += dx
        self.finish += dx
        
# закончились отступы - закончился класс
# дальше можно класс использовать

# напишем функцию проверки:
def test_create():
    """Тест проверяет создание отрезков и их атрибуты"""
    
    # Создадим два отрезка [-150, 50] и [100, 230]
    s1 = Segment1(-150, 50)     # создали объект класса Segment1, на него ссылается переменная s1 - первый отрезок
    s2 = Segment1(100, 230)     # создали объект класса Segment1, на него ссылается переменная s2 - второй отрезок

    print(s1.start, s1.finish)  # -150 50
    assert s1.start == -150
    assert s1.finish == 50
    print(s2.start, s2.finish)  # 100 230
    assert s2.start == 100
    assert s2.finish == 230

    s1.start = -120             # первый отрезок теперь [-120, -30]
    s1.finish = -30

    print(s1.start, s1.finish)  # -120 -30
    assert s1.start == -120
    assert s1.finish == -30

def test_length():
    """Тест проверяет функцию length"""
    
    # Создадим отрезок
    s1 = Segment1(-100, 20)

    # добавим проверку метода length()
    len1 = s1.length()
    # печать должна показывать всю информацию, если длина считается неправильно
    print(s1.start, s1.finish, len1)  # -100 20 120
    assert len1 == 120


def test_str():
    """Проверяем печатать отрезка"""
    # Создадим два отрезка [-120, 50] и [100, 230]
    s1 = Segment1(-120, 50)     # создали объект класса Segment1, на него ссылается переменная s1 - первый отрезок
    s2 = Segment1(100, 230)     # создали объект класса Segment1, на него ссылается переменная s2 - второй отрезок
    
    print(s1)   # [-120, 50]:170
    print(s2)   # [100, 230]:130

    # str(s1) возвращает строку. Эту строку сравниваем с образцом.
    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[100, 230]:130'

def test_move():
    """Проверяем сдвиг отрезка на dx"""
    s1 = Segment1(-120, 50)
    assert str(s1) == '[-120, 50]:170'

    s1.move(40)                     # сдвиг на 40 вправо
    print(s1)
    assert str(s1) == '[-80, 90]:170'
    
    s1.move(-100)                   # сдвиг на 100 влево
    print(s1)
    assert str(s1) == '[-180, -10]:170'
    

# вызовем функции проверки
test_create()
test_length()
test_str()
test_move()
```

## Метод изменяет объект, ничего не возвращает

Метод `move` меняет сам объект.

* Метод двигает объект на `dx`. 
* Первый аргумент `self`
* Меняет атрибуты объекта. 
* Ничего не возвращает.

Пишем его **внутри класса**:
```python
    def move(self, dx):
        """Сдвигает отрезок на dx. Ничего не возвращает"""
        self.start += dx
        self.finish += dx
```
Проверили метод. Удобно, когда печатается длина. При move длина отрезка не должна измениться.

## Метод класса. Возвращает новый объект класса.

Метод `copymove` можно написать так, чтобы он не изменял отрезок (объект класса), а создавал **новый объект** класса `Segment1`

Напишем проверку:
```python
def test_copymove():    
    """Проверяем получение нового отрезка со сдвигом на dx"""
    s1 = Segment1(-120, 50) # исходный отрезок, он не должен измениться
    s2 = s1.copymove(40)    # новый отрезок
    print(s1)               # s1 не должно измениться
    print(s2)               # s2 - новый отрезок на другом месте

    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[-80, 90]:170'
```

## Реализуем метод copymove

Внутри класса:
```python
    def copymove(self, dx):
        """Возвращает копию отрезка, сдвинутого на dx"""
        new_start = self.start + dx
        new_finish = self.finish + dx
        new_segment = Segment1(new_start, new_finish)
        return new_segment
```
или короче:
```python
    def copymove(self, dx):
        """Возвращает копию отрезка, сдвинутого на dx"""
        new_segment = Segment1(self.start + dx, self.finish + dx)
        return new_segment
```
еще короче:
```python
    def copymove(self, dx):
        """Возвращает копию отрезка, сдвинутого на dx"""
        return Segment1(self.start + dx, self.finish + dx)
```

Вся программа:

```python
# определение класса Segment1
class Segment1:
    """Класс Segment1 описывает отрезки на оси Х"""
    
    def __init__(self, start=0, finish=0):
        # Эта функция вызывается, когда мы создаем новый объект класса.
        # self - это название переменной, которая указвает на сам объект.
        self.start = start      # переменная объекта 
        self.finish = finish

    def __repr__(self):
        mylen = self.length()
        return f'[{self.start}, {self.finish}]:{mylen}'     # не забудьте f перед строкой
        
    def length(self):
        """Возвращает длину отрезка"""
        return abs(self.start - self.finish)

    def move(self, dx):
        """Сдвигает сам отрезок на dx вправо"""
        self.start += dx
        self.finish += dx

    def copymove(self, dx):
        """Возвращает копию отрезка, сдвинутого на dx"""
        new_start = self.start + dx
        new_finish = self.finish + dx
        new_segment = Segment1(new_start, new_finish)
        return new_segment
        # return Segment1(self.start + dx, self.finish + dx) 
        
# закончились отступы - закончился класс
# дальше можно класс использовать

# напишем функцию проверки:
def test_create():
    """Тест проверяет создание отрезков и их атрибуты"""
    
    # Создадим два отрезка [-150, 50] и [100, 230]
    s1 = Segment1(-150, 50)     # создали объект класса Segment1, на него ссылается переменная s1 - первый отрезок
    s2 = Segment1(100, 230)     # создали объект класса Segment1, на него ссылается переменная s2 - второй отрезок

    print(s1.start, s1.finish)  # -150 50
    assert s1.start == -150
    assert s1.finish == 50
    print(s2.start, s2.finish)  # 100 230
    assert s2.start == 100
    assert s2.finish == 230

    s1.start = -120             # первый отрезок теперь [-120, -30]
    s1.finish = -30

    print(s1.start, s1.finish)  # -120 -30
    assert s1.start == -120
    assert s1.finish == -30

def test_length():
    """Тест проверяет функцию length"""
    
    # Создадим отрезок
    s1 = Segment1(-100, 20)

    # добавим проверку метода length()
    len1 = s1.length()
    # печать должна показывать всю информацию, если длина считается неправильно
    print(s1.start, s1.finish, len1)  # -100 20 120
    assert len1 == 120


def test_str():
    """Проверяем печатать отрезка"""
    # Создадим два отрезка [-120, 50] и [100, 230]
    s1 = Segment1(-120, 50)     # создали объект класса Segment1, на него ссылается переменная s1 - первый отрезок
    s2 = Segment1(100, 230)     # создали объект класса Segment1, на него ссылается переменная s2 - второй отрезок
    
    print(s1)   # [-120, 50]:170
    print(s2)   # [100, 230]:130

    # str(s1) возвращает строку. Эту строку сравниваем с образцом.
    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[100, 230]:130'

def test_move():
    """Проверяем сдвиг отрезка на dx"""
    s1 = Segment1(-120, 50)
    assert str(s1) == '[-120, 50]:170'

    s1.move(40)                     # сдвиг на 40 вправо
    print(s1)
    assert str(s1) == '[-80, 90]:170'
    
    s1.move(-100)                   # сдвиг на 100 влево
    print(s1)
    assert str(s1) == '[-180, -10]:170'

def test_copymove():    
    """Проверяем получение нового отрезка со сдвигом на dx"""
    s1 = Segment1(-120, 50)
    s2 = s1.copymove(40)
    print(s1)               # s1 не должно измениться
    print(s2)               # s2 - новый отрезок на другом месте

    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[-80, 90]:170'
   

# вызовем функции проверки
test_create()
test_length()
test_str()
test_move()
test_copymove()
```

## "Плохой отрезок"

Когда создаем отрезок, можем перепутать концы и написать
```python
s = Segment1(200, -30)
```

Можно в конструкторе сразу правильно присвоить концы:
```python
def __init__(self, start, finish):
    if start < finish:
        self.start = start
        self.finish = finish
    else:
        self.start = finish
        self.finish = start    
```

Но что будет, если start и finish перепутаются при трансформации отрезка или кто-то выставит self.start равное правому концу отрезка. Нужен метод, который будет правильно устанавливать начало и конец отрезка. 

Напишем метод класса, который правильно устанавливает start и finish. Назовем метод `normalize`. Сначала тесты:
```python
def test_normalize():
    """Концы отрезка в правильном порядке"""
    
    # правильный порядок не изменяется
    s1 = Segment1(-120, 50)
    print(s1)
    assert str(s1) == '[-120, 50]:170'

    # неправильный порядок становится правильным
    s2 = Segment1(50, -120)
    print(s2)
    assert str(s2) == '[-120, 50]:170'

    # normalize не меняет правильный порядок
    s1.normalize()
    print(s1)
    assert str(s1) == '[-120, 50]:170'

    # normalize устанавливает правильный порядок
    s2.start = 200
    s2.finish = 50
    s2.normalize()
    print(s2)
    assert str(s2) == '[50, 200]:150' 
```

В конструкторе вызовем метод `normalize`. Так как это метод это же объекта, то вызов будет `self.normalize()`.

* **s1.**normalize() - вызов по внешней ссылке `s1` в функции `test_normalize`.
* **self.**normalize() - вызов по _внутренней_ ссылке на сам объект `self` в конструкторе `__init__`
```python
    def __init__(self, start=0, finish=0):
        # Эта функция вызывается, когда мы создаем новый объект класса.
        # self - это название переменной, которая указвает на сам объект.
        self.start = start      # переменная объекта 
        self.finish = finish
        self.normalize()
        
    def normalize(self):
        """Концы отрезка хранятся в правильном порядке,
            self.start <= self.finish
        """
        if self.start > self.finish:
            self.start, self.finish = self.finish, self.start     
```

Вся программа:
```python
# определение класса Segment1
class Segment1:
    """Класс Segment1 описывает отрезки на оси Х"""
    
    def __init__(self, start=0, finish=0):
        # Эта функция вызывается, когда мы создаем новый объект класса.
        # self - это название переменной, которая указвает на сам объект.
        self.start = start      # переменная объекта 
        self.finish = finish
        self.normalize()

    def __repr__(self):
        mylen = self.length()
        return f'[{self.start}, {self.finish}]:{mylen}'     # не забудьте f перед строкой
        
    def length(self):
        """Возвращает длину отрезка"""
        return abs(self.start - self.finish)

    def move(self, dx):
        """Сдвигает сам отрезок на dx вправо"""
        self.start += dx
        self.finish += dx

    def copymove(self, dx):
        """Возвращает копию отрезка, сдвинутого на dx"""
        new_start = self.start + dx
        new_finish = self.finish + dx
        new_segment = Segment1(new_start, new_finish)
        return new_segment
        # return Segment1(self.start + dx, self.finish + dx)

    def normalize(self):
        """Концы отрезка хранятся в правильном порядке,
            self.start <= self.finish
        """
        if self.start > self.finish:
            self.start, self.finish = self.finish, self.start

        
# закончились отступы - закончился класс
# дальше можно класс использовать

# напишем функцию проверки:
def test_create():
    """Тест проверяет создание отрезков и их атрибуты"""
    
    # Создадим два отрезка [-150, 50] и [100, 230]
    s1 = Segment1(-150, 50)     # создали объект класса Segment1, на него ссылается переменная s1 - первый отрезок
    s2 = Segment1(100, 230)     # создали объект класса Segment1, на него ссылается переменная s2 - второй отрезок

    print(s1.start, s1.finish)  # -150 50
    assert s1.start == -150
    assert s1.finish == 50
    print(s2.start, s2.finish)  # 100 230
    assert s2.start == 100
    assert s2.finish == 230

    s1.start = -120             # первый отрезок теперь [-120, -30]
    s1.finish = -30

    print(s1.start, s1.finish)  # -120 -30
    assert s1.start == -120
    assert s1.finish == -30

def test_length():
    """Тест проверяет функцию length"""
    
    # Создадим отрезок
    s1 = Segment1(-100, 20)

    # добавим проверку метода length()
    len1 = s1.length()
    # печать должна показывать всю информацию, если длина считается неправильно
    print(s1.start, s1.finish, len1)  # -100 20 120
    assert len1 == 120


def test_str():
    """Проверяем печатать отрезка"""
    # Создадим два отрезка [-120, 50] и [100, 230]
    s1 = Segment1(-120, 50)     # создали объект класса Segment1, на него ссылается переменная s1 - первый отрезок
    s2 = Segment1(100, 230)     # создали объект класса Segment1, на него ссылается переменная s2 - второй отрезок
    
    print(s1)   # [-120, 50]:170
    print(s2)   # [100, 230]:130

    # str(s1) возвращает строку. Эту строку сравниваем с образцом.
    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[100, 230]:130'

def test_move():
    """Проверяем сдвиг отрезка на dx"""
    s1 = Segment1(-120, 50)
    assert str(s1) == '[-120, 50]:170'

    s1.move(40)                     # сдвиг на 40 вправо
    print(s1)
    assert str(s1) == '[-80, 90]:170'
    
    s1.move(-100)                   # сдвиг на 100 влево
    print(s1)
    assert str(s1) == '[-180, -10]:170'

def test_copymove():    
    """Проверяем получение нового отрезка со сдвигом на dx"""
    s1 = Segment1(-120, 50)
    s2 = s1.copymove(40)
    print(s1)               # s1 не должно измениться
    print(s2)               # s2 - новый отрезок на другом месте

    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[-80, 90]:170'

def test_normalize():
    """Концы отрезка в правильном порядке"""
    
    # правильный порядок не изменяется
    s1 = Segment1(-120, 50)
    print(s1)
    assert str(s1) == '[-120, 50]:170'

    # неправильный порядок становится правильным
    s2 = Segment1(50, -120)
    print(s2)
    assert str(s2) == '[-120, 50]:170'

    # normalize не меняет правильный порядок
    s1.normalize()
    print(s1)
    assert str(s1) == '[-120, 50]:170'

    # normalize устанавливает правильный порядок
    s2.start = 200
    s2.finish = 50
    s2.normalize()
    print(s2)
    assert str(s2) == '[50, 200]:150'
    

# вызовем функции проверки
test_create()
test_length()
test_str()
test_move()
test_copymove()
test_normalize()
```

## Итоги:

* Общие:
    * умеем объявлять класс `class ИмяКласса:`
    * тело класса пишем с отступом в 1 табуляцию.
    * функции внутри класса называются **методы**
    * первый аргумент метода класса **self** - ссылка на сам объект.
    
* Методы
    * первый аргумент метода экземепляра класса всегда **self**.
    * метод `__init__` - конструктор, он инициализирует объект класса.
        * переменные объекта называются **атрибуты** объекта и доступаются по ссылка на объект.
    * метод `__repr__` из объекта получает строку, вызывается при печати.
    * возвращает число или строку (это тоже экземепляры классов, но других, не Segment1.
        * `length()`
        * `__repr()__`
    * изменяет объект, ничего не возвращает
        * `move(dx)`
        * `normalize()`
    * возвращает измененную копию объекта, объект не изменяется:
        * `copymove(dx)`
       
