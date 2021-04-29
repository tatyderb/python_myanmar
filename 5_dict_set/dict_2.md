# dict.get

lesson = 522726

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

## QUIZ Чему равно

```python
capitals = {
    'Russia': 'Moscow', 
    'Ukraine': 'Kiev', 
    'USA': 'Washington', 
    'Myanmar':'Naypyidaw', 
    'Mongolia':'Ulaanbaatar', 
    'China':'Beijing'
}
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

Дан текст. На каждой строке фрукт и его цена за 1 кг (целое число).

Сделайте из текста словарь. Если фрукт повторяется, хранить минимальную цену.

Напечатайте словарь красиво.

TEST
apple 150
orange 87
apple 90
apple 100
----
{
    "apple": 90,
    "orange": 87
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
