# Задачи на обработку файлов

lesson = 492343

## Пример: сколько килограмм фруктов

Студент сходил в магазин и купил фрукты. 

Он написал в файл что купил и сколько килограмм весит каждая покупка.

Сколько всего килограмм фруктов купил студент?

Файл `data.txt`

```cpp
apple 5
orange 3.5
grapes 1.2
apple 7
```
Заметим, студент купил apple два раза. Одних яблок 5 кг, других яблок 7 кг.

Напишем программу, которая читает любое количество покупок. 
Программу напишем в файле `fruit.py`:

```python
import sys

total = 0                       # в total будет сумма килограмм

fin = sys.stdin

for line in fin:                # для каждой строки с клавиатуры
    fruit, kg = line.split()    # разделим строку по пробелу на фрукт и вес
    kg = float(kg)              # вес - это число
    total = total + kg
    print(f'{fruit} weight={kg} total={total}')
    
print(total)
```
Запустим программу с входными данными:
```
python fruit.py < data.txt
```
Она напечатает:
```
apple weight=5.0 total=5.0
orange weight=3.5 total=8.5
grapes weight=1.2 total=9.7
apple weight=7.0 total=16.7
16.7
```
Для входных данных
```cpp
garlic 0.1
carrot 2
```
напечатает
```cpp
garlic weight=0.1 total=0.1
carrot weight=2.0 total=2.1
2.1
```

## TASKINLINE Сколько денег потратил студент?

Студент сходил в магазин и купил фрукты и овощи. 

Он написал в файл для каждой покупки:

* что купил 
* сколько килограмм весит эта покупка
* цена за 1 кг

Сколько всего денег потратил студент?

Если студент записал:
```python
apple 5*200
orange 3.5*100
```
то он купил:

* 5 кг яблок по 200 рублей за килограмм
* 3.5 кг апельсинов по 100 рублей за килограмм

Все покупки стоят $5 \cdot 200 + 3.5 \cdot 100 = 1350$ рублей

TEST
apple 5*200
orange 3.5*100
----
1350.0
====
apple 5*2
orange 3.5*1
grapes 1.2*3
apple 7*1
----
24.1
====

## TASKINLINE Самая тяжелая покупка

Студент записывал свои покупки так:

* сколько килограмм весит покупка
* `=`
* что купил

Найдите самую тяжелую покупку (больше всего килограмм).

TEST
5=apple
3.5=orange
1.2=grapes
7=apple
-----
7.0
=====
1.3=pineapple
5.7=rice
3.2=orange
12.4=potato
2.5=bananas
----
12.4
=====

## TASKINLINE email студентов

Есть список email.

Нужно напечатать эти же имена, но с `@phystech.edu`

TEST
khakimzhonov.ub@phystech.edu
derbysheva.tn@mipt.ru
tatyderb@gmail.com
----
khakimzhonov.ub@phystech.edu
derbysheva.tn@phystech.edu
tatyderb@phystech.edu
=====
muzafarov.ae@bk.ru
----
muzafarov.ae@phystech.edu
====

## TASKINLINE отличные оценки


Даны оценки студентов. Сначала фамилия, потом оценки через запятую.
Например, `Ivanov,3,9,6,7`

Отлично - это 8, 9 или 10.

Дан список студентов. Напечатать фамилии студентов, у которых есть отличные оценки.

Напишите функцию **excellent(grades)**. Она возвращает True, если в списке `grades` есть 8 или 9 или 10. Иначе она возвращает False.

TEST
Ivanov,6,8,5,6
Petrov,4,3
Sidorova,7,9,8
Kolos,8
Petrova,7,5
----
Ivanov
Sidorova
Kolos
====
Lunev,10,9,10
Podlesnyh,5,7
Golubev,8
----
Lunev
Golubev
====

## Прочитать первую строку отдельно

Даны оценки студентов. Сначала фамилия, потом оценки через запятую.
Например, `Ivanov,3,9,6,7`

**Сначала написана одна фамилия.**

Потом список студентов. Напечатать средний балл студента с этой фамилией.

```cpp
Petrov
Ivanov,6,8,5,6
Petrov,4,3
Sidorova,7,9,8
Kolos,8
Petrova,7,5
```
Напишем программу.

Нужно отдельно прочитать первую строку. Можно **input()**. Можно **readline()**.

```python
import sys

fin = sys.stdin

name = fin.readline()           # отдельно читаем первую строку
name = name.rstrip()            # удаляем пробелы в конце строки

for line in fin:                # для каждой ОСТАЛЬНОЙ строки
    data = line.split(',')      # разделим строку по ,
    if name == data[0]:         # нам нужен только один студент
        grades = list(map(int, data[1:]))
        print(sum(grades) / len(grades))
        break                   # нашли, дальше студентов можно не читать.
```

## TASKINLINE стипендия

Даны оценки студентов. Сначала фамилия, потом оценки через запятую.
Например, `Ivanov,3,9,6,7`

Сначала дано число. У кого **средняя оценка больше этого числа, получают зачет.**

Дано число и список студентов с оценками. 

Напечатать через пробел фамилию студента, его средний балл и слово `zachet`, если студент получил зачет.

TEST
3.7
Sidorova,7,9,8
Petrov,4,3
Kolos,6
Petrova,7,4
----
Sidorova 8.0 zachet
Petrov 3.5
Kolos 6.0 zachet
Petrova 5.5 zachet
====
8
Lunev,10,9
Podlesnyh,5,7
Golubev,9,2
----
Lunev 9.5 zachet
Podlesnyh 6.0
Golubev 5.5
====




