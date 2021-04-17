# Методы словарей

lesson = 

## Циклы со словарем

Методы словаря:

* **keys()** - список ключей
* **values()** - список значений
* **items()** - список пар (ключ, значение)

Словарь перебираем по ключам:
```python
for student in grades.keys():
    print(student, grades[student])
```
То же самое:
```python
for student in grades:          # словарь перебираем по ключам
    print(student, grades[student])
```
По значениям:
```python
for score in grades.values():   # только оценки, имена студентов не доступны
    print(score)
```
Это цикл работает быстрее остальных:
```python
for student, score in grades.items():   # получаем сразу пару ключ и значение
    print(student, score)
```

## Методы keys(), values(), items()

Словарь:
```python
>>> print(grades)
print(grades, type(grades))
{'Hein': 10, 'Arkar': 8, 'Sai': 9, 'Thaw': 7, 'Lin': 8}
>>> print(type(grades))
<class 'dict'>
```
Ключи:
```python
>>> print(grades.keys())
dict_keys(['Hein', 'Arkar', 'Sai', 'Thaw', 'Lin'])
>>> print(type(grades.keys()))
<class 'dict_keys'>
```
Значения:
```python
print(grades.values())
dict_values([10, 8, 9, 7, 8])
print(type(grades.values()))
<class 'dict_values'>
```
Пары (ключ, значение):
```python
print(grades.items())
dict_items([('Hein', 10), ('Arkar', 8), ('Sai', 9), ('Thaw', 7), ('Lin', 8)])
print(type(grades.items()))
<class 'dict_items'>
```

## Свойства ключей и значений

* **ключ** - должен быть **уникальным** и **неизменяемым** (на самом деле хешируемым, но об этом термине узнаем позже).
* **значение** - может быть любое

* Неизменяемые (unmutable) типы: строки `'Moscow'`, числа `12`, кортеж `(1, 3, 17)` и другие.
* Изменяемые типы (mutable) типы: списки `[1, 3, 17]`
