# json

lesson = 527242

## TASKINLINE Сколько разных чисел

Даны числа. Напечатать сколько всего чисел и сколько разных чисел.

Если числа `1 7 5 3 5 5`, то чисел всего 6, а разных 4 (это 1, 7, 5, 3)

TEST
1 7 5 3 5 5
----
6 4
====
1 4 6 2 3 6 3 0 2 2 2 4
----
12 6
====
1 1 1 1 1 11
----
6 2
====
-3 124 82 90123
----
4 4
====

## TASKINLINE Ключи по возрастанию

Даны числа, напечатать число (по возрастанию) и сколько раз оно встречалось.

TEST
1 4 6 2 3 6 3 0 2 2 2 4
----
0 1
1 1
2 4
3 2
4 2
6 2
====
1 1 1 1 1
----
1 5
====
-3 124 82 90123
----
-3 1
82 1
124 1
90123 1
====

## TASKINLINE Сложная сортировка

Даны числа, напечатать число и сколько раз оно встретилось.

Список отсортировать по убыванию сколько раз встретилось. При одинаковом количестве чисел, сначала печатать меньшее число.

TEST
1 4 6 2 3 6 3 0 2 2 2 4
----
2 4
3 2
4 2
6 2
0 1
1 1
====
1 1 1 1 1
----
1 5
====
-3 124 82 90123
----
-3 1
82 1
124 1
90123 1
====

## json

Можно хранить сложные объекты. Опишем человека.

```python
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
```

Такая сложная структура, где смешаны словари, списки, строки и числа называется JSON.

## json functions

Для работы с json используют пакет **json** и функции этого пакета.

```python
import json
```

* **dumps(d, indent=0)** - превратить d в строку
* **dump(d, file, indent=0)** - записать d в файл
* **loads(text)** - прочитать json из строки
* **load(file)** - прочитать json из файла

**s** в конце названия функции говорит, что будет строка.

## json: печатаем

Пусть есть словарь оценок студентов по разным предметам:
```python
data = {
	[
		{
			"name": "Alexey Ivanov",
			"courses" : [
				{
					"title": "mathematics",
					"grades": [8, 9, 9, 6]
				}, 
				{
					"title": "physics",
					"grades": [5, 7]
				}, 
			]
		},
		{
			"name": "Jhon Smith",
			"courses" : [
				{
					"title": "russian language",
					"grades": [8, 9, 9, 6]
				}
			]
		}
	]
}
```

Печатаем этот сложный объект по формату json:
```python
print(data)
print(json.dumps(data))
print(json.dumps(data, indent=4))
```
Печатать в файл. Все 3 способа печатают в файл. Выберите один:
```python
with open('grades.json', 'w') as fout:
	print(data, file=fout)
	json.dump(data, fout)
	json.dump(data, fout, indent=4)
```

## json: читаем

Пусть в файле `grades.json` у нас данные:
```python
[{'name': 'Alexey Ivanov', 'courses': [{'title': 'mathematics', 'grades': [8, 9, 9, 6]}, {'title': 'physics', 'grades': [5, 7]}]}, {'name': 'Jhon Smith', 'courses': [{'title': 'russian language', 'grades': [8, 9, 9, 6]}]}]
```
Прочитаем их по формату json:
```python
import json
with open('grades.json', 'r') as fin:
	data = json.load(fin)
```
Если у нас json уже в виде строки, то используем **loads**:
```python
import json

text = "[{'name': 'Alexey Ivanov', 'courses': [{'title': 'mathematics', 'grades': [8, 9, 9, 6]}, {'title': 'physics', 'grades': [5, 7]}]}, {'name': 'Jhon Smith', 'courses': [{'title': 'russian language', 'grades': [8, 9, 9, 6]}]}]" 

data = json.loads(text)
```
Заметим, чтобы удобно писать json в программе, мы писали его в `".."` и внутри использовали `'`.

## Сравнение словарей

Словари можно сравнить `==` и `!=`.

Порядок ключей может быть любой:
```python
>>> d1 = {'a':10, 'b':20}
>>> d2 = {'b':20, 'a': 10}
>>> d1 == d2
True
>>> d3 = {'a': 33}
>>> d1 == d3
False
>>> d1 != d3
True
```

Если нужно сравнить и порядок ключей, используйте json.dumps() и сравните строки:
```python
>>> import json
>>> s1 = json.dumps(d1)
>>> s2 = json.dumps(d2)
>>> s1 == s2
False
>>> d1 == d2
True
```

## TASKINLINE loads и dumps

В файле `exam.json` задан список: студент и его оценка. Построить словарь оценка - сколько человек ее получили. Напечайте словарь красиво.

HEADER
import sys
text = sys.stdin.read()
filename = 'exam.json'
fd = open(filename, 'w')
fd.write(text)
fd.close()

TEST
{
    "Ivanov": 6,
    "Petrov": 8,
    "Lan Han": 10,
    "Jhon Smith": 4,
    "Arkar Kyaw": 8
}
----
{
    "6": 1,
    "8": 2,
    "10": 1,
    "4": 1
}
====
{
	"Gorshkov": 7,
	"Vasiliev": 5,
	"Sirko": 7
}
----
{
	"7": 2,
	"5": 1
}
====	


## TASKINLINE Оценка и список студентов

В файле `exam.json` задан список: студент и его оценка. Построить словарь оценка - список студентов, которые ее получили. Напечайте словарь красиво.

HEADER
import sys
text = sys.stdin.read()
filename = 'exam.json'
fd = open(filename, 'w')
fd.write(text)
fd.close()

TEST
{
    "Ivanov": 6,
    "Petrov": 8,
    "Lan Han": 10,
    "Jhon Smith": 4,
    "Arkar Kyaw": 8
}
----
{
    "6": [
        "Ivanov"
    ],
    "8": [
        "Petrov",
        "Arkar Kyaw"
    ],
    "10": [
        "Lan Han"
    ],
    "4": [
        "Jhon Smith"
    ]
}
====
{
	"Gorshkov": 7,
	"Vasiliev": 5,
	"Sirko": 7
}
----
{
	"7": [
        "Gorshkov",
        "Sirko"
    ],
	"5": [
		"Vasiliev"
	]
}
====	

## TASKINLINE Оценки по кафедрам

В файле `all_exams.json` написаны предмет, студент, оценка.

Нужно построить списки по студентам.
Студент, предмет, оценка.
И красиво напечатать.

HEADER
import sys
text = sys.stdin.read()
filename = 'all_exams.json'
fd = open(filename, 'w')
fd.write(text)
fd.close()

TEST
{
    "mathematics": {
    "Ivanov": 6,
    "Petrov": 8,
    "Lan Han": 10,
    "Jhon Smith": 4,
    "Arkar Kyaw": 8
    },
    "russian language": {
         "Jhon Smith": 7,
         "Lan Han": 6,
         "Arkar Kyaw": 7
    },
    "physics": {
        "Ivanov": 8,
        "Petrov": 6,
        "Jhon Smith": 6
    },
    "informatica": {
    }
}
----
{
    "Ivanov": {
        "mathematics": 6,
        "physics": 8
    },
    "Petrov": {
        "mathematics": 8,
        "physics": 6
    },
    "Lan Han": {
        "mathematics": 10,
        "russian language": 6
    },
    "Jhon Smith": {
        "mathematics": 4,
        "russian language": 7,
        "physics": 6
    },
    "Arkar Kyaw": {
        "mathematics": 8,
        "russian language": 7
    }
}
====
{
	"informatica": {
		"Kozlova": 5,
		"Morozov": 9,
		"Bekboev": 5
	}
}
----
{
    "Kozlova": {
        "informatica": 5
    },
    "Morozov": {
        "informatica": 9
    },
    "Bekboev": {
        "informatica": 5
    }
}
====		
	