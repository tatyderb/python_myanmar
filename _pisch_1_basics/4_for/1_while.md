# Цикл while

lesson = 414778

## Повторяющиеся действия в программе

В этом уроке будет рассказано о синтаксисе циклов (повторяющихся действий) с `while`.

Чтобы понять, почему для циклов придумали особый синтаксис, решим задачу.

### Задача про поход

Отряд туристов отправился в поход.  В первый день они прошли **L** км. 
Каждый следующий день проходили на **k** км больше
Сколько км они прошли за 3 дня?

Пусть дано:	`L = 4`, `k = 2`. Для конкретной задачи это константы.

Введем переменные:

* **i** - закончилось полных дней похода; сначала 0.
* **step** - прошли за 1 день похода; сначала **L**
* **path** - прошли за все время; сначала 0.

<img src="https://stepik.org/media/attachments/lesson/260536/path1_lines.svg" width=600></img>

### Таблица

Прежде чем писать код, рекомендуем составить таблицу, как изменялись переменные цикла. 

<img src="https://stepik.org/media/attachments/lesson/260536/path1_table.svg"></img>

На таблице нарисованы стрелки и операции - как изменялись переменные. Перед тем, как начать писать программу, напишите такую таблицу, нарисуйте стрелками и знаками операции и выпишите формулы. Глядя на стрелки проще понять, зависят изменения одних переменных от других или нет и в каком порядке писать их в коде.

Каждый день отряд:

* проходит путь 
* пишет в журнал сколько прошел сегодня и сколько прошел всего
* планирует сколько нужно пройти завтра

День похода в виде формул:

* Прошли путь: `path = path + step` - (новый путь - это старый путь плюс что прошли за последний день) зависит от `step`, нужно складывать в первый день именно с `L`
* Закончился день: `i = i + 1` - не зависит от изменения других переменных, можно писать в любом месте относительно других формул 
* Печатаем значения `i`, `step`, `path`. 
* Планируем сколько пройдем завтра: `step = step + k` -  (завтра пройдем на k больше, чем сегодня) не зависит от других переменных.

Значит, изменения `step` должны пройти позже изменения `path`.

### Напишем решение без циклов

**Если не понятно как писать цикл, надо написать код без цикла. Одинаковые части потом перенесем внутрь цикла.**

```python
# Дано
L = 4           # прошли в первый день
k = 2           # на сколько больше пройдем завтра

path = 0        # еще ничего не прошли
step = L        # в первый день пройдем L
i = 0           # еще не закончился первый день

# первый день
path = path + step  # прошли путь
i = i + 1           # закончился день
print(f'за день {i} прошли {step} км, всего {path} км')
step = step + k     # планируем, сколько пройдем завтра

# второй день
path = path + step  # прошли путь
i = i + 1           # закончился день
print(f'за день {i} прошли {step} км, всего {path} км')
step = step + k     # планируем, сколько пройдем завтра

# третий день
path = path + step  # прошли путь
i = i + 1           # закончился день
print(f'за день {i} прошли {step} км, всего {path} км')
step = step + k     # планируем, сколько пройдем завтра

# ответ
print(f'Всего прошли {path} км')
```

Программа напечатает:
```cpp
За день 1 прошли 4 км, всего 4 км
За день 2 прошли 6 км, всего 10 км
За день 3 прошли 8 км, всего 18 км
Всего прошли 18 км
```
## TASKINLINE 7 дней

Дано, по 1 числу на каждой строке:

* `L` - сколько отряд прошел в первый день
* `k` - на сколько больше пройдет завтра

Найти:

* Перепишите и запустите программу для **7 дней** похода. Проверьте ее.
* Трудно ли будет изменить программу, чтобы она подсчитала путь для 100 дней?

**Внимание! Печатать только одно число - сколько километров всего прошли за весь поход**

TEST
4
1
----
49
====
1
1
----
28
====
0
5
----
105
====

## Блок-схемы

### Блок-схема последовательная

Напишем эти шаги в виде блок-схемы:

<p style="text-align:center"><img alt="Блок-схема с последовательным выполнением" src="https://stepik.org/media/attachments/lesson/260536/b_step1.svg" /></p>

На схеме видны повторяющиеся блоки. Попробуем оптимизировать блок-схему, чтобы **один и тот же код выполнялся несколько раз**.

### Блок-схема с повторениями

Будем считать `i` - сколько дней уже прошли.

Добавим в схему условие: выполняем блок с изменением пути 3 дня. Пока условие истино (`True`), продолжаем выполнять блок, а как только станет ложным (`False`), выходим из повторения и идем дальше по коду программы - печатаем результат и заканчиваем программу.

Ромб означает условие.

<p style="text-align:center"><img alt="Блок-схема с циклом" src="https://stepik.org/media/attachments/lesson/260536/b_while1.svg" /></p>



## Код с циклом while

Используем оператор **while**

```cpp
while условие_продолжения_цикла:
	тело цикла
```

* Если *условие продолжения цикла* истина `True`, то выполняется тело цикла и опять проверяется условие.
* Если условие ложно `False`, то управление передается на первый оператор после цикла.

**Итерация цикла** - это одно выполнение тела цикла.

Синтаксис:

* специальное слово **while**
* условие **продолжения** цикла (как зеленый на светофоре)
* `:` двоеточие
* **Тело цикла надо выделить отступом.**

```python
# Дано
L = 4           # прошли в первый день
k = 2           # на сколько больше пройдем завтра

# готовимся к походу ДО цикла
path = 0        # еще ничего не прошли
step = L        # в первый день пройдем L
i = 0           # еще не закончился первый день

# цикл
while i < 3:    # пока i < 3, то есть i==0, i==1, i==2 
    path = path + step  # прошли путь
    i = i + 1           # закончился день
    print(f'за день {i} прошли {step} км, всего {path} км')
    step = step + k     # планируем, сколько пройдем завтра

# ответ ПОСЛЕ цикла
print(f'Всего прошли {path} км')
```
Цикл из 3 итераций.

* Подумайте, как изменить код, чтобы он посчитал путь для 100 дней. 
* Сравните количество изменений в коде с программой без цикла.

## Что где писать?

Правило "один-много-один":

* **До цикла** - выполняется 1 раз - инициализация переменных цикла;
* **Внутри цикла** - выполняется много раз (много - это 0 или более);
* **После цикла** - выполняется 1 раз (возвращаем результат, печатаем ответ и тп).

## QUIZ

Какое ключевое слово надо написать для цикла?

A. while
B. until
C. repeat
D. continue
E. every
F. always

ANSWER: A

## QUIZ

Как работает цикл `while`?

A. Сначала проверяется условие, потом выполняется тело цикла.
B. Сначала выполняется тело цикла, потом проверяется условие.

ANSWER: A

## QUIZ

В цикле `while` пишется условие:

A. Продолжения цикла.
B. Остановки цикла.

ANSWER: A

## NUMBER

```python
i = 2
while i < N:
    print('hello')
    i = i + 1
```

Чему должна быть равна переменная `N`, чтобы напечаталось

```python
hello
hello
hello
```

ANSWER: 5

## QUIZ 

```python
i = 2
while i < 7:
    print('hello')
```

Сколько раз будет напечатано `hello`?

A. 5
B. 6
C. 4
D. 7
E. код будет бесконечно печатать `hello`

ANSWER: E


## TASKINLINE За сколько дней дойдут до Дубны?

Очень похожая задача.

Отряд туристов отправился в поход.  В первый день они прошли **L** км. 
Каждый следующий день проходили на **k** км больше

До города Дубна **s** километров. За сколько дней отряд дойдет до города Дубна?

Входные данные, по 1 числу на каждой строке:

* L - сколько отряд прошел в первый день
* k - на сколько больше пройдет завтра,
* s - сколько нужно всего пройти

Объяснение: за 7 дней прошли 49 км, значит 50 км пройдут за 8 дней.

TEST
4
1
50
----
8
====
3
2
1
----
1
====
0
5
105
----
7
====

## TASKINLINE Сколько страниц прочитает студент за 20 дней?

Студент готовится к экзамену и читает учебник. В первый день он прочитал $L$ страниц, каждый следующий на $k$ **меньше**.

Если студент в день читает ≤ 0 страниц, то студент не читает (отдыхает).

Программа, которая вычисляет сколько студент прочитает страниц за 7 дней:

| День `day` | Страниц сегодня `per_day` | Всего прочитал `total` | Комментарий |
|----|----|----|----|
| 1 | 10 | 10 |   |
| 2 | 8 | 18 |   |
| 3 | 6 | 24 |   |
| 4 | 4 | 28 |   |
| 5 | 2 | 30 |   |
| 6 | 0 | 30 | устал и больше не читает  |
| 7 | 0 | 30 | устал и больше не читает |

```python
# возвращает сколько студент прочитает завтра
def tomorrow(per_day, k):
    per_day = per_day - k
    
    # студент не может прочитать отрицательное количество страниц 
    # (или съесть отрицательное количество котлет).
    if per_day < 0:
        per_day = 0

    return per_day
    

# Дано
L = 10          # сколько прочитал в первый день
k = 2           # на сколько меньше прочитает на следующий день

# начинаем учиться, до цикла 1 раз
total = 0       # сколько всего прочитали (еще не начали читать учебник)
per_day = L     # сколько читаем за 1 день (в первый день L страниц)
day = 0         # сколько дней уже прошло

# цикл
while day < 7:    
    total = total + per_day         # прочитали еще per_day страниц
    day = day + 1                   # день закончился
    print(f'день {day}: сегодня прочитали {per_day} страниц, всего {total} страниц')
    per_day = tomorrow(per_day, k)  # готовимся к следующему дню

# ответ ПОСЛЕ цикла
print(f'Всего прочитали {total} страниц')
```
Напечатает:
```
день 1: сегодня прочитали 10 страниц, всего 10 страниц
день 2: сегодня прочитали 8 страниц, всего 18 страниц
день 3: сегодня прочитали 6 страниц, всего 24 страниц
день 4: сегодня прочитали 4 страниц, всего 28 страниц
день 5: сегодня прочитали 2 страниц, всего 30 страниц
день 6: сегодня прочитали 0 страниц, всего 30 страниц
день 7: сегодня прочитали 0 страниц, всего 30 страниц
Всего прочитали 30 страниц
```

* Прочитать L и k.
* Переписать и отладить программу для **20 дней**.
* Программа должна печатать ТОЛЬКО ПОСЛЕДНИЙ total. Убрать ненужные print.

CODE
# возвращает сколько студент прочитает завтра
def tomorrow(per_day, k):
    per_day = per_day - k
    
    # студент не может прочитать отрицательное количество страниц 
    # (или съесть отрицательное количество котлет).
    if per_day < 0:
        per_day = 0

    return per_day
    

# Дано
L = 10          # сколько прочитал в первый день
k = 2           # на сколько меньше прочитает на следующий день

# начинаем учиться, до цикла 1 раз
total = 0       # сколько всего прочитали (еще не начали читать учебник)
per_day = L     # сколько читаем за 1 день (в первый день L страниц)
day = 0         # сколько дней уже прошло

# цикл
while day < 7:    
    total = total + per_day         # прочитали еще per_day страниц
    day = day + 1                   # день закончился
    print(f'день {day}: сегодня прочитали {per_day} страниц, всего {total} страниц')
    per_day = tomorrow(per_day, k)  # готовимся к следующему дню

# ответ ПОСЛЕ цикла
print(f'Всего прочитали {total} страниц')
TEST
30 1
---
410
====
25 5
---
75
====
2 0
---
40
====

## TASKINLINE Bloop_path4 Сколько вообще прочитал студент?

Студент готовится к экзамену и читает учебник. В первый день он прочитал `L` страниц, каждый следующий на `k` **меньше**.

Если студент в день читает ≤ 0 страниц, то студент не читает (больше не может учиться, устал).

Программа вычисляет сколько страниц всего прочитал студент.

```python
# возвращает сколько студент прочитает завтра
def tomorrow(per_day, k):
    per_day = per_day - k
    
    # студент не может прочитать отрицательное количество страниц 
    # (или съесть отрицательное количество котлет).
    if per_day < 0:
        per_day = 0

    return per_day
    

# Дано
L = 10          # сколько прочитал в первый день
k = 2           # на сколько меньше прочитает на следующий день

# начинаем учиться, до цикла 1 раз
total = 0       # сколько всего прочитали (еще не начали читать учебник)
per_day = L     # сколько читаем за 1 день (в первый день L страниц)
day = 0         # сколько прошло дней

# цикл
while per_day > 0:                  # пока студент может читать
    total = total + per_day         # прочитали еще per_day страниц
    print(f'сегодня прочитали {per_day} страниц, всего {total} страниц')
    per_day = tomorrow(per_day, k)  # готовимся к следующему дню

# ответ ПОСЛЕ цикла
print(f'Всего прочитали {total} страниц')
```

Написать программу, которая вычисляет сколько всего страниц прочитали и **за сколько дней**.

Программа должна печатать ТОЛЬКО **total** и **day**.

CODE
# возвращает сколько студент прочитает завтра
def tomorrow(per_day, k):
    per_day = per_day - k
    
    # студент не может прочитать отрицательное количество страниц 
    # (или съесть отрицательное количество котлет).
    if per_day < 0:
        per_day = 0

    return per_day
    

# Дано
L = 10          # сколько прочитал в первый день
k = 2           # на сколько меньше прочитает на следующий день

# начинаем учиться, до цикла 1 раз
total = 0       # сколько всего прочитали (еще не начали читать учебник)
per_day = L     # сколько читаем за 1 день (в первый день L страниц)
day = 0         # сколько прошло дней

# цикл
while per_day > 0:                  # пока студент читает
    total = total + per_day         # прочитали еще per_day страниц
    print(f'сегодня прочитали {per_day} страниц, всего {total} страниц')
    per_day = tomorrow(per_day, k)  # готовимся к следующему дню

# ответ ПОСЛЕ цикла
print(f'Всего прочитали {total} страниц')
TEST
25 5
---
75
5
====
10 10
---
10
1
====
0 1
---
0
0
====
25 15
---
35
2
====

## TASKINLINE Сколько прочесть в последний день учебы?

Студент готовится к экзамену и читает учебник. В первый день он прочитал **first** страниц, каждый следующий на **d** страниц **больше**.

Всего в учебнике **book** страниц.

В последний день в учебнике может остаться меньше страниц **remaining**, чем хочет прочитать студент. Напечатайте сколько **remaining** останется прочитать студенту в последний день учебы.

### Пример 1

В первый день прочитал `first = 10` страниц, каждый день на `d = 2` страницы больше. Всего в книге `book = 100` страниц.

| дней `day` | в день страниц `per_day` | осталось прочитать `remaining` |
|----|-----|----|
| 1 | 10 | 90 |
| 2 | 12 | 78 |
| 3 | 14 | 64 |
| 4 | 16 | 48 |
| 5 | 18 | 30 |
| 6 | 20 | 10 <--- это ответ |

Ответ: в последний неполный день осталось прочитать 10 страниц

### Пример 2

В первый день прочитал `first = 10` страниц, каждый день на `d = 2` страницы больше. Всего в книге `book = 112` страниц.

| дней `day` | в день страниц `per_day` | осталось прочитать `book - total` |
|----|-----|----|
| 1 | 10 | 102 |
| 2 | 12 | 90 |
| 3 | 14 | 76 |
| 4 | 16 | 60 |
| 5 | 18 | 42 |
| 6 | 20 | 22 <- это ответ |
| 7 | 22 | 0 |

Ответ: в последний день учебы студент прочел 22 страницы. *Потом он читал 0 страниц, то есть отдыхал.*

TEST
10
2
100
----
10
====
10
2
112
----
22
====
30
1
17
----
17
====
5
10
300
----
55
====

## TASKINLINE Задача про рис-1 - сколько потратит денег за N дней

Начиная с понедельника студент каждый день покупает в столовой рис.

В первую неделю рис стоит **price** рублей. Всю неделю цена не меняется. 

Каждую следующую неделю (в ночь с воскресенья на понедельник) цена риса увеличивается на **delta** рублей (`price = price + delta`). 

Студент покупал рис **days** дней.

Написать программу (с циклом `while`), которая вычисляет  сколько денег (**money**) потратил студент.

Нужны переменные:

* `d` - сколько дней уже покупал студент,
* `price` - сколько стоит сегодня рис,
* `money` - сколько всего денег потратил студент,
* `week_day` - номер дня недели, (week day, день недели от понедельника до воскресенья, потом идет опять понедельник).

Дано: **price delta days** на одной строке через пробел

Найти: **money** сколько студент потратил денег.

Подсказка: напишите сначала бесконечный цикл, который печатает дни недели 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, и так далее; потом сделайте так, чтобы печаталось ровно `days` дней.

### Пример

Рис стоил сначала 10 рублей, каждый понедельник становился на 1 рубль дороже. Студент покупал рис 9 дней.

| День `d` | День недели `wd` | Цена `price` | Всего потратил денег `money` |
|----|----|----|----|
| 1 | 1 | 10 | 10 |
| 2 | 2 | 10 | 20 |
| 3 | 3 | 10 | 30 |
| 4 | 4 | 10 | 40 |
| 5 | 5 | 10 | 50 |
| 6 | 6 | 10 | 60 |
| 7 | 7 | 10 | 70 |
| 8 | 1 | 11 | 81 |
| 9 | 2 | 11 | 92 |

Ответ: 92

TEST
10 1 9
---
92
====
1 5 19
---
104
====
12 0 2
---
24
====
12 0 48
---
576
====

## TASKINLINE Задача про рис-2 - на сколько дней хватит денег

Начиная с понедельника студент каждый день покупает в столовой рис.

В первую неделю рис стоит **price** рублей. Всю неделю цена не меняется. 

Каждую следующую неделю (в ночь с воскресенья на понедельник) цена риса увеличивается на **delta** рублей (`price = price + delta`). 

У студента **money** денег. **Сколько дней он может покупать рис?**

Дано: **price delta money** на одной строке через пробел.

Найти: сколько дней может покупать рис.

TEST
10 1 92
----
9
====
10 1 100
----
9
====
10 1 9
----
0
====
1 5 100
----
18
====
10 1 80
----
7
====
10 1 81
----
8
====
