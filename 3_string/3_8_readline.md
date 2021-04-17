# Весь текст

lesson = 492342

## Читали раньше

### Прочитать 1 строку

```python
s = input()
```

### Дано N, потом N строк

В группе N студентов. Дано N. Потом по 1 студенту на строку:

* фамилия
* его оценки за экзамены

Напечатать:

* фамилия студента
* самая большая оценка за экзамены

Это файл `data.txt`
```cpp
3
Ivanov 6 8 5 6
Petrov 4 3
Sidorova 7 9 8
```
Это файл `student1.py`:
```python
n = int(input())                    # прочитали сколько студентов

for i in range(n):                  # для каждого студента
    s = input().split()             # прочитали 1 строку, разбили на слова
    first_name = s[0]               # фамилия - первое слово
    grades = list(map(int, s[1:]))  # остальные слова - числа
    print(s[0], max(grades))        # печатать фамилию и максимальное число
```

Можно запустить программу так и ввести данные студентов с клавиатуры:
```cpp
python student1.py
```

Можно запустить программу так и передать данные студентов из файла `data.txt` на вход с клавиатуры:
```cpp
python student1.py < data.txt
```
Очень удобно. Попробуйте сделать так. Получится

```python
Ivanov 8
Petrov 4
Sidorova 9
```

## sys.stdin

Как работает?
```cpp
python student1.py < data.txt
```

Когда запускаем любую программу на python, у нее есть:

* **sys.stdin** - standard input (стандартный входной поток данных)
    * что вводим с клавиатуры, 
    * отсюда читает **input()**
* **sys.stdout** - standard output (стандартный выходной поток данных)
    * выводит на экран
    * сюда печатает **print()**


```cpp
python student1.py < data.txt
```

Данные из файла `data.txt` перенаправили на **sys.stdin** программы `student1.py`.

## Читаем студентов до слова END

N не дано. Нужно прочитать всех студентов. Не знаю, сколько студентов.

После студентов слово `END` на строке.

Файл `data2.txt`:
```cpp
Ivanov 6 8 5 6
Petrov 4 3
Sidorova 7 9 8
END
```

* **while True:** - бесконечный цикл. 
* **continue** - перейти к следующей итерации цикла
* **break** - выйти из цикла

[Повторить про break, continue, ворон и яблоки](https://stepik.org/lesson/427312/step/5?unit=417169)

Это файл `student2.py`:
```python
while True:                         # всегда
    line = input()                  # прочитать строку
    if line.startswith('END')       # если строка начинается с END
        break                       #   выйти из цикла
                                    # если тут, то END не было
    s = line.split()                # разбили строку на слова
    first_name = s[0]               # фамилия - первое слово
    grades = list(map(int, s[1:]))  # остальные слова - числа
    print(s[0], max(grades))        # печатать фамилию и максимальное число
```

Можно запустить программу так и ввести данные студентов с клавиатуры:
```cpp
python student2.py < data2.txt
```
Напечатает

```python
Ivanov 8
Petrov 4
Sidorova 9
```

## NUMBER студенты END студенты

Файл `data3.txt`:
```cpp
Ivanov 6 8 5 6
Petrov 4 3
Sidorova 7 9 8
END
Kuznetsov 2 2 5
Popova 3 3 2 4
Ibragimov 5
Hrol 8 8 6
```

Это файл `student2.py` (не изменился):
```python
while True:                         # всегда
    line = input()                  # прочитать строку
    if line.startswith('END')       # если строка начинается с END
        break                       #   выйти из цикла
                                    # если тут, то END не было
    s = line.split()                # разбили строку на слова
    first_name = s[0]               # фамилия - первое слово
    grades = list(map(int, s[1:]))  # остальные слова - числа
    print(s[0], max(grades))        # печатать фамилию и максимальное число
```

Сколько строк напечатает
```cpp
python student2.py < data3.txt
```

ANSWER: 3

## NUMBER студенты END студенты END

Файл `data4.txt`:
```cpp
Ivanov 6 8 5 6
Petrov 4 3
Sidorova 7 9 8
END
Kuznetsov 2 2 5
Popova 3 3 2 4
Ibragimov 5
Hrol 8 8 6
END
```

Это файл `student2.py` (не изменился):
```python
while True:                         # всегда
    line = input()                  # прочитать строку
    if line.startswith('END')       # если строка начинается с END
        break                       #   выйти из цикла
                                    # если тут, то END не было
    s = line.split()                # разбили строку на слова
    first_name = s[0]               # фамилия - первое слово
    grades = list(map(int, s[1:]))  # остальные слова - числа
    print(s[0], max(grades))        # печатать фамилию и максимальное число
```

Сколько строк напечатает
```cpp
python student2.py < data4.txt
```

ANSWER: 3

## TASKINLINE Клад Флинта

Капитан Флинт зарыл клад на Острове сокровищ. Он оставил описание, как найти клад. 

![Пиратская карта](https://stepik.org/media/attachments/lesson/443937/pirate_map.jpg)
<a href="http://www.freepik.com">Designed by Freepik</a>

Описание состоит из строк вида: "куда 5", 

* куда – одно из: 
    * north (север), 
    * south (юг), 
    * east (восток), 
    * west (запад), 
* второе число – сколько шагов идем в направлении *куда*

В конце пути есть клад 'Treasure!`

Путь 5 шагов на север, 3 шага на восток, 1 шаг на юг это

```
north 5
east 3
south 1
Treasure!
```
Начинаем путь в точке (0, 0). По осям Х и Y считаем шаги.

Ось OX направлена на восток, ось OY – на север.

![Путь к кладу](https://stepik.org/media/attachments/lesson/443937/flint_coords.png)

Программа получает на вход последовательность строк указанного вида, завершающуюся строкой со словом "Treasure!". Программа должна вывести два целых числа: координаты клада.

TEST
north 6
east 6
south 4
east 1
Treasure!
----
7 2
====
north 5
east 3
south 1
Treasure!
----
3 4
====
Treasure!
----
0 0
====
west 5
south 3
Treasure!
----
-5 -3
====
west 5
south 3
east 1
south 4
Treasure!
----
-4 -7
====


## Интерпретатор python

Когда вы запускаете любую программу на питоне `python students.py`, то

* сначала запускается сам python. Это очень большая программа.
* Она читает и понимает (интерпретирует) вашу маленькую программу `students.py`. Поэтому большую программу `python` называют **интерпретатор языка python**.
* **sys** - пакет (модуль). Он дает информацию об интерпретаторе python, его переменных и функциях.
    * **sys.version** - номер версии вашей программы python.
    
```python
import sys

print(sys.version)      # Напечатать версию python
```  

**sys.stdin** поможет прочитать все строки в файле.  

## Читаем всех студентов

N не дано. Нужно прочитать всех студентов. Не знаю, сколько студентов.

Файл `data.txt`:
```cpp
Ivanov 6 8 5 6
Petrov 4 3
Sidorova 7 9 8
```
или другое количество строк:
```cpp
Ivanov 6 8 5 6
Petrov 4 3
Sidorova 7 9 8
Kolos 8
```
Прочитать по 1 строке **все** строки можно так:
```python
import sys

for line in sys.stdin:  # для каждой строки из sys.stdin, прочитаем строку в line
    print(line)
```

* **input()** не нужен. 
* Читаем строку в переменную `line`. 
* Имя переменной придумаем сами. В этой программе придумали имя `line`.

## Читаем и печатаем всех студентов

Файл `data.txt`:
```cpp
Ivanov 6 8 5 6
Petrov 4 3
Sidorova 7 9 8
```
Читаем все строки, печатаем студента и его максимальную оценку:

Это файл `student_all.py` (не изменился):
```python
import sys

fin = sys.stdin                     # данные будем читать с клавиатуры

for line in fin:                    # для каждой строки с клавиатуры
    s = line.split()                # разбили строку на слова
    first_name = s[0]               # фамилия - первое слово
    grades = list(map(int, s[1:]))  # остальные слова - числа
    print(s[0], max(grades))        # печатать фамилию и максимальное число
```
Запустим программу и передадим ей данные:
```cpp
python student_all.py < data.txt
```
Напечатает:
```cpp
Ivanov 8
Petrov 4
Sidorova 9
```

## Вводим данные руками с клавиатуры

```cpp
python student_all.py < data.txt
```
Данные заканчиваются и поток данных из `data.txt` закрывается.

Можно запустить и вводить информацию о студентах руками.
```cpp
python student_all.py
```

Как сказать, что данные закончились? После всех данных нажмите 

* **Ctrl+Z** - Windows
* **Ctrl+D** - Linux, Mac
