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

## Заполните пробелы создание словаря

Создайте словарь страна и ее столица для 2 стран.

```python
countries = {'Russia' ____ 'Moscow'____ 'China': 'Beijing'____
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
{'apple': 61, 'banana': 67, 'orange': 80, 'grape': 100, 'lemon': 120}
{
    "apple": 61,
    "banana": 67,
    "orange": 80,
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

## dictionary comprehensions

Краткая запись создания словаря.

Ключ - число, значение - квадрат числа. Сделаем словарь для чисел от 0 до 10.

```python
# dict comprehensions:
square1 = {x : x*x for x in range(10) }                              
# задаем явно пары ключ=значение
square2 = {0=0, 1=1, 2=4, 3=9, 4=16, 5=25, 6=36, 7=49, 8=64, 9=81}  
```
или словарь $\sqrt{x}$ для целых квадратов:
```python
sqrtn1 = {x*x : x for x in range(10) }
sqrtn2 = {0=0, 1=1, 4=2, 9=3, 16=4, 25=5, 36=6, 49=7, 64=8, 81=9}  
```

## Если значения нет

Если ключа в словаре нет, то будет ошибка. В списке нет студента 'Mike'. Попробуем узнать его оценку.
```python
x = grades['Mike']
```
получим
```cpp
Traceback (most recent call last):
  File "C:\Users\tatyd\Downloads\my.py", line 15, in <module>
    x = grades['Mike']
KeyError: 'Mike'
```
В ошибке написано, какого ключа нет. 

## Чему равно

```python
capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington', 'Myanmar':'Naypyidaw', 'Mongolia':'Ulaanbaatar', 'China':'Beijing'}
print(capitals[0])
```
Какой результат?

A. 'Russia'
B. 'Moscow'
C. 0
D. KeyError

ANSWER: D

## in и get

Кто пришел на зачет, оценку записали в словарь. Кто не пришел, нужно поставить 2.

Можно проверять **in** есть такой ключ в словаре или нет:
```python
if student in grades:
    score = grades[student]
else:
    score = 2                # кто не пришел на зачет, получил 2
```

Можно взять значение функцией **get(key, default_value=None)**.

* `key` - ключ
* `default_value` - значение, если ключа нет
	* по умолчанию `None`
	
```python
score = grades.get(student, 2)
```	

## Пример get

```python
d = {
    'Bob': 7,
    'Alex': 5,
    'David': 8,
    'Charly': 2
}
```
| Код | Результат |
|----|----|
| `d['Alex']` | 5 |
| `d.get('Alex')]` | 5 |
| `d.get('Alex', 2)]` | 5 |
| `d['Charly']` | 2 |
| `d.get('Charly')]` | 2 |
| `d['Mike']` | KeyError |
| `d.get('Mike')]` | None |
| `d.get('Mike', 2)]` | 2 |

## TASKINLINE дешевые фрукты

Дан список фрукт и его цена за 1 кг (целое число).

Сделайте из списка словарь. Если фрукт повторяется, хранить минимальную цену.

TEST
apple 150
orange 87
apple 90
apple 100
----
{
    "apple": 90,
    "orange": "87"
}
====
apple 50
banana 90
orange 60
grape 100
mango 80
banana 84
apple 110
lemon 120
----
{
    "apple": 50,
    "banana": 84,
    "orange": 60,
    "grape": 100,
    "mango": 80,
    "lemon": 120
}
====
