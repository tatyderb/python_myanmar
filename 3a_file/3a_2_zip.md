# zip() и *

lesson = 509966

## Оператор `*`

`*` распаковывает список. То есть из  `[5, 17, -3]` делает `5, 17, -3`

```python
a = [5, 17, -3]
print(a)            # [5, 17, -3]
print(*a)           # 5 17 -3
```

## Функция zip

Функция **zip()** - собирает из нескольких итерируемых объектов (списков, строк, генераторов) один:

```python
>>> numbers = [1, 2, 3]
>>> strings = ['one', 'two', 'three']
>>> a = zip(numbers, strings)
>>> list(a)
[(1, 'one'), (2, 'two'), (3, 'three')]        
```

Если размеры не совпадают, то берется самый короткий.

```python
>>> numbers = [1, 2, 3, 4, 5]             # 5 элементов
>>> strings = ['one', 'two', 'three']     # 3 элемента
>>> a = zip(numbers, strings)
>>> list(a)
[(1, 'one'), (2, 'two'), (3, 'three')]    # 3 кортежа       
```

## Транспонируем матрицу. Чтение матриц

Используем `*` и `zip`. Напишем функцию транспонирования матрицы.

Сначала напишем функцию чтения матрицы.

Матрица задается:

* n - сколько в матрице строк
* далее строки с числами

```cpp
3
1 2 3 4
5 6 7 8
9 10 11 12
``` 
Надо транспонировать матрицу и напечатать ее:
```cpp
1 5 9
2 6 10
3 7 11
4 8 12
```

Читаем матрицу:
```python
def read_matrix():
    n = int(input())
    m = []
    for i in range(n):
        line = input()
        m.append(list(map(int, line.split())))
    return m
    
m = read_matrix()    
print(m)            # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
```
или через генерацию списков
```python
def read_matrix():
    n = int(input())
    m = [list(map(int, line.split())) for i in range(n)]
    return m
```
избавимся от переменных n и m, подставив вместо них выражения
```python
def read_matrix():
    return [list(map(int, line.split())) for i in range(int(input()))]
```

Напишем данные в файле `a.txt`:
```cpp
3
1 2 3 4
5 6 7 8
9 10 11 12
``` 

## Транспонируем матрицу

Будем печатать исходную матрицу и этапы транспонирования.

### Вариант 1. Делаем матрицу размером с транспонированную из 0 и дальше в нее пишем числа

$$tm_{ij} = m_{ji}$$

```python
def read_matrix():
    return [list(map(int, input().split())) for i in range(int(input()))]
    
def trans(m):
    print(m)                            # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    nrow = len(m)                       # сколько строк в матрице
    ncol = len(m[0])                    # сколько столбцов в матрице
    tm = [[0]*nrow for i in range(ncol)]
    print(tm)                           # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for irow in range(nrow):
        for icol in range(ncol):
            tm[icol][irow] = m[irow][icol]

    print(tm)                           # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    return tm
    
m = read_matrix()
tr = trans(m)
```

## Перепишем на добавление списков

```python
def read_matrix():
    return [list(map(int, input().split())) for i in range(int(input()))]
    
def trans(m):
    print(m)                            # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    nrow = len(m)                       # сколько строк в матрице
    ncol = len(m[0])                    # сколько столбцов в матрице
    tm = [[] for i in range(ncol)]
    print(tm)                           # [[], [], [], []]
    for irow in range(nrow):
        for icol in range(ncol):
            tm[icol].append(m[irow][icol])
        print(m)                        # [[1], [2], [3], [4]]
                                        # [[1, 5], [2, 6], [3, 7], [4, 8]]
                                        # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    return tm
    
m = read_matrix()
tr = trans(m)
```

## Перепишем на генерацию списков

```python
def read_matrix():
    return [list(map(int, input().split())) for i in range(int(input()))]
    
def trans(m):
    print(m)                            # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    nrow = len(m)                       # сколько строк в матрице
    ncol = len(m[0])                    # сколько столбцов в матрице
    tm = [[m[irow][icol] for irow in range(nrow)] for icol in range(ncol)]
    print(tm)                           # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    return tm
    
m = read_matrix()
tr = trans(m)
```

## Перепишем через zip и *

```python
def read_matrix():
    return [list(map(int, input().split())) for i in range(int(input()))]
    
def trans(m):
    print(m)                            # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(*m)                           # [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]
    print(list(zip(*m)))                # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
    tm = [list(row) for row in zip(*m)]
    print(tm)                           # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    return tm
    
m = read_matrix()
tr = trans(m)
```
Вынесем print и получим:
```python
def read_matrix():
    return [list(map(int, input().split())) for i in range(int(input()))]
    
def trans(m):
    tm = [list(row) for row in zip(*m)]
    return tm
    
m = read_matrix()
print(m)                            # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
tr = trans(m)
print(tr)                           # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
