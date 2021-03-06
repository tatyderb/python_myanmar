# for и range

lesson = 414777

# Повторить

Мы черепахой рисовали квадрат размером ``. В квадрате нужно 4 раз повторить: "вперед на `size` и поверни на 90 градусов".

```python
def sq(size):           # функция рисует квадрат
    for i in range(4):  # повторить 4 раза
        t.fd(size)      # вперед на size шагов
        t.lt(90)        # повернуть налево на 90 градусов
```
Хотим нарисовать квадраты. Самый большой 200, следующий на 50 меньше. Рисуем сколько сможем.
```python
size = 200                  # сначала size 200
while size > 0:             # пока size > 0
    print(f'square {size}') # печатаем размер квадрата  
    sq(size)                # рисовать квадрат размера size
    size = size - 50        # уменьшить size на 50
```
Программа напечатает
```cpp
square 200
square 150
square 100
square 50
```
Когда size = 0, условие `size > 0` - ложь (False). Квадрат не рисуем, print не печатает.

![Тут нужна картика этих квадратов]()

## Как работает `for i in range(4)`

* `range(4)` дает числа 0, 1, 2, 3 (число 4 не дает!).
* переменная `i` равна сначала 0, потом 1, потом 2, потом 3.

```python
for i in range(4):
    print(i)
```
Напечатает:
```cpp
0
1
2
3
```

## range

`range` - функция. Она возвращает:

| Код | Возвращает | Объяснение |
|----|-----|--------|
|`range(4)` | 0 1 2 3 | от 0 до 4 (без 4) |
|`range(2, 7)` | 2 3 4  5 6 | от 2 до 7 (без 7) |
|`range(2, 20, 3)` | 2 5 8 11 14 17 | от 2 до 20 (без 20), +3 каждый раз |
|`range(20, 2, -3)` | 20 17 14 11 8 5 | от 20 до 2 (без 2), -3 каждый раз |

**range(from, to, step)** - от **from** до **to**, каждый раз **+step**.

## сортировка

* `range(5)`
* `range(5, 11)`
* `range(5, 11, 2)`
* `range(0, 5, 2)`

## QUIZ

Нужно нарисовать квадраты от 200 до 0. Следующий на 50 меньше.

Для этого написали код:
```python
for size in ??? :
    sq(size)
```
Какой код нужно поставить на место `???`

A. `range(200, 0, -50)`

B. `range(200, 0)`

C. `range(200)`

D. `range(0, 200, 50)`

ANSWER: A
