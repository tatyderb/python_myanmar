# read, readline, readlines

lesson = 496523


## Что делаем

Файл `names.txt` со списком людей:
```cpp
Paul Miller
Christopher Johnson
Jennifer Suarez
Cheryl Wang
Ashley Jackson
```
Выполняем программу:
```python
python readnames.py < names.txt
```
Прочитаем данные разными способами. 

## for .. in fin

Уже знаем:

```python
import sys

fin = sys.stdin                    # данные будем читать с клавиатуры

for line in fin:                   # для каждой строки с клавиатуры
    print('['+line+']')
``` 
Напечатает `[` в начале и `]` в конце **каждой строки** с именем.
```cpp
[Paul Miller
]
[Christopher Johnson
]
[Jennifer Suarez
]
[Cheryl Wang
]
[Ashley Jackson
]
```
Вывод: каждая строка содержит символ новой строки `\n`. Используйте метод **str.rstrip()**, чтобы их убрать.

## read

Метод **read()** - читает все данные в 1 строку python.

```python
import sys
fin = sys.stdin                    # данные будем читать с клавиатуры

text = fin.read()

print('['+text+']')
```
Напечатает `[` в начале и `]` в конце **всего текста**.
```cpp
[Paul Miller
Christopher Johnson
Jennifer Suarez
Cheryl Wang
Ashley Jackson
]
```

## readlines

Метод **readlines()** - читает все строки в **список** строк python.

```python
import sys
fin = sys.stdin

text = fin.readlines()

print(text)
```
напечатает
```cpp
['Paul Miller\r\n', 'Christopher Johnson\r\n', 'Jennifer Suarez\r\n', 'Cheryl Wang\r\n', 'Ashley Jackson\r\n']
```
В конце каждой строки есть `\r\n` - признак конца строки (EOL, end of line).

Конец строки обычно делают:

* `\n` - UNIX
* `\r` - Mac
* `\r\n` - Windows

### Не больше n строк

Если нужно прочитать не больше n строк, укажите n в параметрах

```python
text = fin.readlines(3) # прочитать не больше 3 строк
```
* Если строк много, то прочитает 3. Дальше читать не будет.
* Если строк дано меньше 3, то прочитать все строки.
* `readlines(-1)` или `readlines()` - прочитать все строки.

### Нет \n после Ashley Jackson

Пример печатает 

`['Paul Miller\n', 'Christopher Johnson\n', 'Jennifer Suarez\n', 'Cheryl Wang\n', 'Ashley Jackson']`

Вместо `'Ashley Jackson\n'` получаю `'Ashley Jackson'`. Что делать?

Нужно исправить файл `names.txt`. 

![нет \r\n](https://stepik.org/media/attachments/lesson/496523/rn_NO.png)

Встаньте в конец файла и нажмите Enter.

![есть \r\n](https://stepik.org/media/attachments/lesson/496523/rn_YES.png)

## readline

Метод **readline()** - читает 1 строку.

Программа
```python
import sys
fin = sys.stdin

s = fin.readline()         # читаем первую строку
print(f'First: [{s}]')

s = fin.readline()         # читаем следующую строку 
print(f'Second: [{s}]')

for s in fin:              # каждую оставшуюся строку
    print(f'Other: [{s}]')
```
напечатает
```cpp
First: [Paul Miller
]
Second: [Christopher Johnson
]
Other: [Jennifer Suarez
]
Other: [Cheryl Wang
]
Other: [Ashley Jackson
]
```

## Читаем весь файл через readline

* в конце файла `readline` вернет `''` пустую строку.

```python
import sys
fin = sys.stdin

while True:
    s = fin.readline()
    if s == '':
        break
    print(f'[{s}]')
```

Input:
```cpp
Paul Miller
Christopher Johnson
Jennifer Suarez
Cheryl Wang
Ashley Jackson
```
Output:
```cpp
[Paul Miller
]
[Christopher Johnson
]
[Jennifer Suarez
]
[Cheryl Wang
]
[Ashley Jackson
]
```

## Все варианты

* **read()** - читаем весь файл в 1 строку python.
* **readline()** - прочитать 1 строку.
* **readlines()** - читаем файл в список (list) строк.
    * **readlines(n)** - читать не больше `n` строк.
* **for** line **in** fin - читать в цикле по 1 строке.

Самый простой вариант **получить из файла список строк**

```python
import sys
fin = sys.stdin

text = fin.readlines()
print(text)
```

Самый простой вариант **обработать каждую строку**:
```python
import sys
fin = sys.stdin

for line in fin:
    print(line)
```