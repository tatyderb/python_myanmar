# slice

lesson = 730289

## Часть строки - slice

![строка и индексы](https://stepik.org/media/attachments/lesson/418189/string_slicing.png)

* **s[от:до]** - часть строки от (включая) до (НЕ включая)
* **s[от:до:шаг]** - часть строки от (включая) до (НЕ включая), + шаг

```python
s = 'Monty Python'
```
| Код | Равен | Что делает |
|----|----|--------|
| `s[9]` | `'h'` | 1 символ с **начала** строки с номером 9 |
| `s[-3]` | `'h'` | 1 символ с **конца** строки с номером -3 |
| `s[6:10]` | `'Pyth'` | часть строки от 6 до 10 (БЕЗ 10, последний символ `s[9]`) |
| `s[-12:-7]` | `'Monty'` | часть строки от -12 до -7 (БЕЗ -7, последний символ `s[-8]`) |
| `s[1:11:2]` | `'ot yh'` | от 1 (включая) до 11 (не включая), с шагом 2 (каждый раз индекс +2) |
| `s[11:1:-2]` | `'nhy t'` | от 11 (включая) до 1 (не включая), с шагом -2 (каждый раз индекс -2) |
| `s[:5]` | `'Monty'` | от **начала** ( часть *от* - пустая) до 5 |
| `s[6:]` | `'Python'` | от 6 до **конца** ( часть *до* - пустая) |
| `s[:]` | `'Monty Python'` | от **начала** до **конца** (копия строки) |
| `s[::-1]` | `'nohtyP ytnoM'` | от **конца** до **начала** с шагом -1 (строка с последней буквы до первой) |


## QUIZ Индекс

![](https://stepik.org/media/attachments/lesson/418189/string_slicing.png)

```python
s = 'Monty Python'
```

Отметьте выражения, которые дадут `M`

A. `s[0]`

B. `s[-12]`

C. `s[0:0]`

D. `s[0:1]`

E. `s[:1]`

F. `s[:0]`

ANSWER: A, B, D, E

## QUIZ Индекс минус

![](https://stepik.org/media/attachments/lesson/418189/string_slicing.png)

```python
s = 'Monty Python'
```

Отметьте выражения, которые дадут последний символ.

A. `s[-1]`

B. `s[11]`

C. `s[len(s)]`

D. `s[len(s)-1]`

ANSWER: A, B, D

## QUIZ Slice

![](https://stepik.org/media/attachments/lesson/418189/string_slicing.png)

```python
s = 'Monty Python'
```

Отметьте выражения, которые дадут строку без первых 3 символов 'ty Python'.

A. `s[2:]`

B. `s[3:]`

C. `s[2:len(s)]`

D. `s[3:len(s)]`

E. `s[2:-1]`

F. `s[3:-1]`

SHUFFLE: false
ANSWER: B, D

## QUIZ Slice minus

![](https://stepik.org/media/attachments/lesson/418189/string_slicing.png)

```python
s = 'Monty Python'
```

Отметьте выражения, которые дадут строку без последних 2 символов 'Monty Pyth'.

A. `s[:3]`

B. `s[:2]`

C. `s[:-3]`

D. `s[:-2]`

E. `s[0:-2]`

E. `s[0:-3]`

F. `s[0:3]`

G. `s[0:2]`

ANSWER: D, E

## TASKINLINE Без www

Дан сайт с `www.` в начале. Напечатайте его без `www.`

TEST
www.mipt.ru
----
mipt.ru
====
www.stepik.org
----
stepik.org
====
www.acm.mipt.ru
----
acm.mipt.ru
====
www.acm.vdi.mipt.ru/twiki/bin/view/Cintro/CoffeeQsort
----
acm.vdi.mipt.ru/twiki/bin/view/Cintro/CoffeeQsort
====

## TASKINLINE Из pystech.edu в mipt.ru

Челове имеет email в домене mipt.ru и phystech.edu. 

Дан email в mipt.ru, надо напечатать email в phystech.edu.

TEST
ivanov.as@mipt.ru
----
ivanov.as@phystech.edu
====
chaox@mipt.ru
----
chaox@phystech.edu
====
smith.john@mipt.ru
----
smith.john@phystech.edu
====


