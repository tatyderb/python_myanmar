# Задачи на строки

lesson = 488123

## Некоторые методы класса str

Тут удобно искать нужный для задачи метод.

*   Проверки (подстрока в строке)
    * str.**count**(sub) - сколько раз входит (без пересечений)
    * **in** - поиск подстроки в строке
    * str.**endswith**(sub) - str оканчивается на sub
    * str.**startswith**(sub) - str начинается на sub

* **Индекс** начала подстроки в строке, (иначе проверяем как 'el' in 'Hello')
    * str.**find**(sub\[, start\[, end\]\]) - возвращает -1, если подстроки нет
    * str.**index**(sub\[, start\[, end\]\]) - кидает ValueError, если подстроки нет
    * str.**rfind**(sub\[, start\[, end\]\])
    * str.**rindex**(sub\[, start\[, end\]\])

* Найти и заменить
    * str.**replace**(old, new) - заменяет в str все части old на new 
    * str.**replace**(old, new, count) - заменяет в str все части old на new не более count раз

* Разбить на 3 части
    * str.**partition**(sep) - 3 строки: до, sep, после
    * str.**rpartition**(sep) - 3 строки: до, sep, после. Ищем sep справа

* Разбить на много частей и склеить
    * строка.**split**(разделитель) - разделить 1 строку на много строк.
    * разделитель.**join**(много строк) - из много строк сделать 1 строку.

*   Убрать символы (пробелы)
    * str.**lstrip**()
    * str.**rstrip**()
    * str.**strip**()

Пример: Разбиваем по ,
```python
'1 2 3'.split()                 # ['1', '2', '3']
'1,2,3'.split(',')              # ['1', '2', '3']
'1,2,3'.split(',', maxsplit=1)  # ['1', '2,3']
'1,2,,3,'.split(',')            # ['1', '2', '', '3', '']
```
Пример: склеиваем
```python
'-'.join(['abc', 'de', 'xyz'])  # 'abc-de-xyz'
' '.join(map(str, [3, -7, 11])) # '3 -7 11'
```

## TASKINLINE найди бомбу

Дана строка.

Напечатать YES, если в тексте есть подстрока bomb, иначе напечатать NO.

TEST
a high explosive bomb is one that employs a process called detonation to rapidly release its chemical energy
----
YES
====
the simplest and oldest type of bombs store energy in the form of a low explosive
----
YES
====
mumbai also known as bombay is the capital city of the indian state of maharashtra
----
YES
====
BOMBS
----
NO
====
the seven islands that came to constitute mumbai were home to communities of fishing colonies
----
NO
====

## TASKINLINE бомба большая и маленькая

Дана строка.

Напечатать YES, если в тексте есть подстрока bomb **без учета большие буквы или маленькие**, иначе напечатать NO.

Подсказка: используйте метод `upper()` или `lower()`

TEST
A high explosive bomb is one that employs a process called detonation to rapidly release its chemical energy
----
YES
====
The simplest and oldest type of bombs store energy in the form of a low explosive
----
YES
====
Mumbai also known as Bombay is the capital city of the indian state of maharashtra
----
YES
====
BOMBS
----
YES
====
the seven islands that came to constitute mumbai were home to communities of fishing colonies
----
NO
====

## TASKINLINE сколько бомб

Дана строка.

Напечатать сколько бомб в строке. Бомбы могут быть большими или маленькими буквами.

TEST
i have a bomb. you have a bomb too.
----
2
====
A high explosive bomb is one that employs a process called detonation to rapidly release its chemical energy
----
1
====
The simplest and oldest type of bombs store energy in the form of a low explosive
----
1
====
Mumbai also known as Bombay is the capital city of the indian state of maharashtra
----
1
====
BOMBS
----
1
====
the seven islands that came to constitute mumbai were home to communities of fishing colonies
----
0
====

## TASKINLINE обезвредь бомбу

Дана строка.

Заменить все подстроки `bomb` (маленькими буквами) на `watermelon`.

TEST
i have a bomb. you have bombs.	
----
i have a watermelon. you have watermelons.	
====
the simplest and oldest type of bombs store energy in the form of a low explosive
----
the simplest and oldest type of watermelons store energy in the form of a low explosive
====
mumbai also known as bombay is the capital city of the indian state of maharashtra
----
mumbai also known as watermelonay is the capital city of the indian state of maharashtra
====
BOMBS
----
BOMBS
====
bomb or not
----
watermelon or not
====
dog and cat
----
dog and cat
====
