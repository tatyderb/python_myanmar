# with .. as

lesson = 509846

## Читаем входной поток

Обычно мы читаем данные из консоли (с клавиатуры или при перенаправлении из файла)

Программа `linenum.py` печатает входной поток и номер каждой строки.

```python
import sys

fin = sys.stdin     # входной поток - из консоли
i = 1
for line in fin:
    print(f'{i:3d}: {line}')
    i += 1
```
Если нужно так распечатать файл `a.txt`, то перенаправляем его 
```cpp
python linenum.py < a.txt
```
`a.txt` содержит
```cpp
Hello, world!
Good bye.
```
Output:
```cpp
  1: Hello, world!
  2: Good bye.
```

## Читаем из файла

Читать можно без перенаправления. Указать имя файла в коде программы.

Программа `linenum2.py` печатает по строкам файл `a.txt` и номер каждой строки.

```python
fin = open('a.txt')         # открыли файл a.txt в поток fin
i = 1
for line in fin:
    print(f'{i:3d}: {line}')
    i += 1
    
fin.close()                 # закрыли поток
```
Запуск 
```cpp
python linenum2.py
```
Указывать имя файла в ходе не хорошо. Лучше прочитать его из командной строки. Про это будет отдельный урок.

## with .. as

Плохо:

* забыли вызвать функцию `close`
* ошибка при чтении или записи в файл, не смогли вызвать функцию `close`

Новый синтаксис  **with .. as:**:
```python
with open('a.txt') as fin:       # открыли файл a.txt в поток fin
    i = 1
    for line in fin:
        print(f'{i:3d}: {line}')
        i += 1
```

* внутри `with .. as ` отступ,
* `close` не нужно, он вызовется автоматически в любом случае.

## Функция open

**open** (path, mode='r')

* path - это имя файла;
* mode - как отрывать файл (чтение, запись, добавление)

| Мода | Как открывает |
|-|---|
| 'r' | открыть на чтение (является значением по умолчанию). | 
| 'w' | открыть на запись, содержимое файла удаляется, если файла не существует, создается новый. | 
| 'x' | открыть на запись, если файла не существует, иначе исключение. | 
| 'a' | открыть на запись, информация добавляется в конец файла. | 
| 'b' | открыть в двоичном режиме. | 
| 't' | открыть в текстовом режиме (является значением по умолчанию). | 
| '+' | открыть на чтение и запись | 

**Если открываем файлы, которые содержат бинарные данные, то открывать с `b`**. Это картинки, музыка, видео, форматы pdf, docx, fb2 и прочие.

### Примеры

* `open('data.txt')` - открыть файл `data.txt` на чтение в текстовом режиме.
* `open('img/cat.png', 'rb')` - открыть файл `img/cat.png` на чтение в бинарном режиме.
* `open('result.txt', 'w')` - открыть файл `result.txt` на запись в текстовом режиме.


## Вставь аргументы

Нужно открыть файл 'dog.jpg' на запись. Заполните пропуски.

## read и write

Все варианты, [которые мы знаем](https://stepik.org/lesson/496523/step/7?unit=487918), работают не только для `sys.stdin`, но и для открытого файла.

```python
with open('data.txt') as fin:
    text = fin.readlines()
    print(text)
```
или
```python
with open('data.txt') as fin:
    for line in fin:
        print(line)
```

## Запись в файл

* `data = file.read()` - читает все данные из потока `file`
* file.**write(data)** - записывает данные data в поток `file`. 

```python
text = '''
Paul Miller
Christopher Johnson
Jennifer Suarez
Cheryl Wang
Ashley Jackson
'''

with open('res.txt', 'w') as fout:
    fout.write(text)
```

## print в файл

У функции **print** есть аргумент `file`. Можно указать в какой файл писать.

Не забывайте в Windows экранировать `\`

```python
with open('C:\\Users\\tatyd\\Downloads\\res.txt', 'w') as fout:
        print(3, 5, 66, file=fout)
```
 

## Хорошие ссылки

* `*` и `**` https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/

* https://www.programiz.com/ - тьюториалы, примеры, объяснение описаний функций (питон, с, и прочее)

* https://younglinux.info/python/feature/zip  - вот тут zip шикарно была описана с примерами и есть тьюториал по башу, pygame, tkinter и тп