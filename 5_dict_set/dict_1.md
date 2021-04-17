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

## Читаем и изменяем значение

**Создать словарь** `grades` (студент и его оценка на зачете):
```python
grades = {
    'Hein': 10,
    'Arkar': 8,
    'Sai': 9,
    'Thaw': 6
}
```
Взять значение по ключу:
```python
x = grades['Sai']   # x = 9
```
Изменить значение по ключу:
```python
grades['Thaw'] = 7  # было 6, стало 7
```
Добавить новую пару:
```python
grades['Lin'] = 8   # добавить и изменить пишем одинаково
```
Печатать:
```python
print(grades)
```
получим
```python
{'Hein': 10, 'Arkar': 8, 'Sai': 9, 'Thaw': 7, 'Lin': 8}
```

* печатаем и перебираем в цикле в том порядке, в котором добавляли в словарь
* в старых версиях питона порядок в словаре может быть произвольный

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
d = capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington', 'Myanmar':'Naypyidaw', 'Mongolia':'Ulaanbaatar', 'China':'Beijing'}
print(d[0])
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





