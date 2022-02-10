# Создание словаря

lesson = 492969

## Словарь

**Пара - это 2 предмета**. Пара рук - это 2 руки. Семейная пара - это муж и жена. Чайная пара - это чашка и блюдце.

**Словарь** (dictionary) - это набор пар **ключ** и **значение** (**key** и **value**).


Пример словаря:

* список студент (ключ) и его оценка за зачет (значение)
* список страна (ключ) и ее столица (значение)
* список столица (ключ) и страна (значение)
* список страна (ключ) и список городов страны (значение)

Создать словарь студент и его оценка на зачете:
```python
grades = {
    'Hein': 10,
    'Arkar': 8,
    'Sai': 9,
    'Thaw': 6
}
```

## Создаем словарь

Пустой словарь:
```python
d1 = dict()
d2 = {}         # это словарь
```

Словарь страна-столица:
```python
capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington', 'Myanmar':'Naypyidaw', 'Mongolia':'Ulaanbaatar', 'China':'Beijing'}
capitals = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington', )
capitals = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])
capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))
```
Пишем красиво:
```python
capitals = {
    'Russia': 'Moscow', 
    'Ukraine': 'Kiev', 
    'USA': 'Washington', 
    'Myanmar':'Naypyidaw', 
    'Mongolia':'Ulaanbaatar', 
    'China':'Beijing'
}
```

## Печатать красиво

```python
capitals = {
    'Russia': 'Moscow', 
    'Ukraine': 'Kiev', 
    'USA': 'Washington', 
    'Myanmar':'Naypyidaw', 
    'Mongolia':'Ulaanbaatar', 
    'China':'Beijing'
}
```

Печатать обычно:
```python
print(capitals)
```
Получим все значения (хорошо). Неудобно читать (плохо).
```python
{'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington', 'Myanmar': 'Naypyidaw', 'Mongolia': 'Ulaanbaatar', 'China': 'Beijing'}
```
Печатать красиво. Библиотека json. Функция **json.dumps**
```python
import json
print(json.dumps(capitals, indent=4))
```
Без `indent=4` печатает как обычно.
```python
{
    "Russia": "Moscow",
    "Ukraine": "Kiev",
    "USA": "Washington",
    "Myanmar": "Naypyidaw",
    "Mongolia": "Ulaanbaatar",
    "China": "Beijing"
}
```

## Читаем и изменяем значение

* **Создать словарь** `grades` (студент и его оценка на зачете):
```python
grades = {
    'Hein': 10,
    'Arkar': 8,
    'Sai': 9,
    'Thaw': 6
}
```
* Взять значение по ключу:
```python
x = grades['Sai']   # x = 9
```
* Изменить значение по ключу:
```python
grades['Thaw'] = 7  # было 6, стало 7
```
* Добавить новую пару:
```python
grades['Lin'] = 8   # добавить и изменить пишем одинаково
```
* Печатать:
```python
print(grades)
```
получим
```python
{'Hein': 10, 'Arkar': 8, 'Sai': 9, 'Thaw': 7, 'Lin': 8}
```

* печатаем и перебираем в цикле в том порядке, в котором добавляли в словарь
* в старых версиях питона порядок в словаре может быть произвольный

* **удалить** пару по ключу
```python
del grades['Arkar']
```

* **длина** словаря (сколько ключей)
```python
len(grades)
```

## QUIZ У кого какая оценка

Преподаватель записал оценки в словарь. Потом изменил оценки. Выберите, какой список оценок правильный.

```python
d = {
    'Bob': 7,
    'Alex': 5,
    'David': 8,
    'Charly': 2
}
d['Bob'] = 10
x = d['David']
d['Harry'] = 9

print(d)
```
A. `{'Bob': 10, 'Alex': 5, 'David': 8, 'Charly': 2, 'Harry': 9}`

B. `{'Bob': 7, 'Alex': 5, 'David': 8, 'Charly': 2, 'Harry': 9}`

C. `{'Bob': 10, 'Alex': 5, 'David': 8, 'Charly': 2}`

D. `{'Bob': 7, 'Alex': 5, 'David': 8, 'Charly': 2}`

E. `{'Bob': 7, 'Alex': 5, 'David': 8, 'Charly': 2, 'Bob':10, 'Harry': 9}`

ANSWER: A


## TASKINLINE Работа со словарем

Купили фрукты. Сделали словарь фрукт (ключ) и цена за 1 килограмм (значение).

Допишите код:

CODE
import json

# создаем словарь
fruit = {
    'apple': 50,
    'banana': 90,
    'orange': 60,
    'grape': 100,
    'mango': 110
}
# печатаем словарь
print(fruit)

# lemon стоит 120 рублей за 1 кг

# есть дешевые бананы 67 рублей за 1 кг, запомним их

# удалим из словаря mango

# яблоки apple стали на x рублей дороже
x = int(input())

# печатаем словарь

# печатаем словарь красиво

TEST
11
----
{'apple': 50, 'banana': 90, 'orange': 60, 'grape': 100, 'mango': 110}
{'apple': 61, 'banana': 67, 'orange': 60, 'grape': 100, 'lemon': 120}
{
    "apple": 61,
    "banana": 67,
    "orange": 60,
    "grape": 100,
    "lemon": 120
}
====

## Читаем словарь

С клавиатуры ввели:
```python
apple 50
banana 90
orange 60
grape 100
mango 80
```
Прочитаем эти данные в словарь fruit
```python
import sys
fin = sys.stdin
fruit = {}
for line in fin:
	name, cost = line.split()
	fruit[name] = int(cost)
	
print(fruit)
```

## TASKINLINE

Дан список страна и столица. По 1 стране на строку. 

Сделайте словарь country. Ключ - страна, значение - столица. Напечатайте словарь красиво.

TEST
Russia Moscow
Ukraine Kiev
----
{
    "Russia": "Moscow",
    "Ukraine": "Kiev"
}
====
Russia Moscow 
Ukraine Kiev 
USA Washington 
Myanmar Naypyidaw 
Mongolia Ulaanbaatar 
China Beijing 
----
{
    "Russia": "Moscow",
    "Ukraine": "Kiev",
    "USA": "Washington",
    "Myanmar": "Naypyidaw",
    "Mongolia": "Ulaanbaatar",
    "China": "Beijing"
}
====
Germany Berlin
----
{
    "Germany": "Berlin"
}
====
