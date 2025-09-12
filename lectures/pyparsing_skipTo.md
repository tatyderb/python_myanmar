# pyparsing.skipTo
https://chat.deepseek.com/a/chat/s/f1254e42-5d30-4858-8c46-b802110437c4
## Пример 1: Пропуск до определенного токена
```python
from pyparsing import Word, alphas, skipTo, restOfLine, pythonStyleComment

# Пример 1: Пропуск до ключевого слова
text = "Неважный текст KEYWORD важные данные"

# Пропускаем всё до слова "KEYWORD"
parser = skipTo("KEYWORD") + "KEYWORD" + restOfLine
result = parser.parseString(text)
print(result)  # Вывод: ['Неважный текст ', 'KEYWORD', ' важные данные']
```

## Пример 2: Извлечение данных между маркерами
```python
from pyparsing import Word, alphas, skipTo, Suppress

# Пример: Извлечение содержимого между тегами
text = "Начало <data>Здесь важная информация</data> Конец"

# Пропускаем до открывающего тега, затем извлекаем содержимое
open_tag = Suppress("<data>")
close_tag = Suppress("</data>")
content = Word(alphas + " ")

parser = skipTo(open_tag) + open_tag + skipTo(close_tag)("content") + close_tag
result = parser.parseString(text)
print(result.content)  # Вывод: 'Здесь важная информация'
```
## Пример 3: Парсинг конфигурационных файлов

```python
from pyparsing import Word, alphas, nums, skipTo, Literal, restOfLine

# Парсинг конфигурационного файла
config_text = """
# Комментарий
server = example.com
port = 8080
# Еще комментарий
timeout = 30
"""

# Пропускаем комментарии и извлекаем пары ключ-значение
comment = Literal("#") + restOfLine
key = Word(alphas)
value = Word(alphas + nums + ".")
assignment = key + Literal("=") + value

# Парсер, который пропускает всё до следующего присваивания
parser = skipTo(assignment) | assignment

for match in parser.searchString(config_text):
    if len(match) == 3:  # key, =, value
        print(f"{match[0]} = {match[2]}")
```
## Пример 4: Обработка логов
```python
from pyparsing import Word, alphas, nums, skipTo, Literal, Regex

log_data = """
ERROR 2023-12-15 10:30:25 Database connection failed
INFO 2023-12-15 10:30:26 Retrying connection
ERROR 2023-12-15 10:30:27 Connection timeout
"""

# Извлекаем только ERROR сообщения
error_line = Literal("ERROR") + skipTo(Literal("INFO") | Literal("ERROR") | Literal("WARNING"))
error_parser = Literal("ERROR") + restOfLine

for match in error_parser.searchString(log_data):
    print("Ошибка:", match[1])
```

## Пример 5: Парсинг многострочных структур
```python
from pyparsing import Word, alphas, nums, skipTo, Literal, LineEnd, OneOrMore

text = """
Заголовок:
===========
Строка 1
Строка 2
Строка 3
Конец
"""

# Пропускаем заголовок и извлекаем содержимое
header = Literal("Заголовок:") + skipTo(Literal("==========="))
content = OneOrMore(Word(alphas + nums) + LineEnd())

parser = header + skipTo(Literal("===========")) + Literal("===========") + content
result = parser.parseString(text)
print("Содержимое:", result)
```

## Пример 6: С обработкой исключений
```python
from pyparsing import Word, alphas, skipTo, ParseException

text = "Текст без искомого ключевого слова"

try:
    # Попытка найти несуществующий маркер
    parser = skipTo("NONEXISTENT") + "NONEXISTENT"
    result = parser.parseString(text)
    print(result)
except ParseException as e:
    print(f"Маркер не найден: {e}")
```
## Пример 7: Комбинирование с другими парсерами
```python
from pyparsing import Word, alphas, nums, skipTo, Group, OneOrMore

data = """
Name: John Doe
Age: 30
City: New York
---
Name: Jane Smith
Age: 25
City: London
"""

# Парсинг нескольких записей, разделенных ---
record_separator = Literal("---")
name_parser = Literal("Name:") + Word(alphas + " ")
age_parser = Literal("Age:") + Word(nums)
city_parser = Literal("City:") + Word(alphas + " ")

record = Group(
    skipTo("Name:") + 
    name_parser("name") + 
    skipTo("Age:") + 
    age_parser("age") + 
    skipTo("City:") + 
    city_parser("city")
)

parser = OneOrMore(record + skipTo(record_separator | Literal("")))

for rec in parser.parseString(data):
    print(f"Имя: {rec.name[1]}, Возраст: {rec.age[1]}, Город: {rec.city[1]}")
```
## Пример 8: Пропуск нежелательных секций
```python
from pyparsing import Word, alphas, nums, skipTo, Suppress

text = """
Мусорный текст
Ненужная информация
=== НАЧАЛО ===
Важные данные: 12345
=== КОНЕЦ ===
Еще мусор
"""

# Пропускаем всё до начала важной секции и после нее
start_marker = Suppress("=== НАЧАЛО ===")
end_marker = Suppress("=== КОНЕЦ ===")
important_data = Word(nums)

parser = skipTo(start_marker) + start_marker + important_data("data") + skipTo(end_marker) + end_marker
result = parser.parseString(text)
print("Важные данные:", result.data)
```
## Ключевые особенности `skipTo`:

1. **Пропускает все токены** до указанного маркера
2. **Включает сам маркер** в результат, если не использовать `Suppress`
3. **Может вызвать исключение**, если маркер не найден
4. **Полезен для** пропуска нерелевантных частей текста
5. **Часто комбинируется** с другими парсерами для извлечения конкретных данных
    
`skipTo` особенно полезен при работе с неструктурированными или частично структурированными данными, где нужно пропустить "шум" и извлечь только нужную информацию.