# or, and, not

lesson = 1160427

## Пример: Вложенные `if` и `else` (координатные четверти)

На координатной плоскости $XY$ номера координатных четвертей определены так:

* x > 0 и y > 0 - четверть 1,
* x < 0 и y > 0 - четверть 2,
* x < 0 и y < 0 - четверть 3,
* x > 0 и y < 0 - четверть 4.

```python
if x > 0:
    if y > 0:
        print('x > 0 и y > 0 - первая четверть')
    else:
        # к какому if относится else определяем по отступам, этот определяет y <= 0
        print('x > 0 и y <= 0 - четвертая четверть (и часть оси Y)')
else:
    # этот else относится к x <= 0
    if y > 0:
        print('x <= 0 и y > 0 - вторая четверть (и часть оси X)')
    else:
        # к какому if относится else определяем по отступам, этот определяет y <= 0
        print('x <= 0 и y <= 0 - третья четверть (и часть осей X и Y)')
```
Если мы захотим отдельно обрабатывать случаи с `x == 0` или `y == 0` с помощью вложенных операторов `if` и `else`, то получим сложный код. Как писать проще?

Хочется написать так:

* Если `x == 0` **или** `y == 0`, то это точка на оси.
* Иначе если `x > 0` **и** `y > 0`, то это первая координатная четверть.
* Иначе если `x < 0` **и** `y > 0`, то это вторая координатная четверть.
* Иначе если `x < 0` **и** `y < 0`, то это третья координатная четверть.
* Иначе если `x > 0` **и** `y < 0`, то это четвертая координатная четверть.

То есть нам нужны оператор **или** и оператор **и**.

## Логические операторы

* `and` - логическое **И** (конъюнкция)
* `or` - логическое **ИЛИ** (дизъюнкция)
* `not` - логическое отрицание

### Оператор `not`

| Выражение | Результат |
|----|----|
| `not True` | `False` |
| `not False` | `True` |

** `not x` - превращает ложь в истину и истину в ложь. **

*Россия* - страна, *not Россия* - всё вне этой страны.

### Оператор `and`

<table>
	<thead>
		<tr>
			<th>Выражение </th>
			<th>Результат</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>True and True</code></td>
			<td style="background-color:#dae8ff"><code>True</code></td>
		</tr>
		<tr>
			<td><code>True and False</code></td>
			<td style="background-color:#f8cecc"><code>False</code></td>
		</tr>
		<tr>
			<td><code>False and True</code></td>
			<td style="background-color:#f8cecc"><code>False</code></td>
		</tr>
		<tr>
			<td><code>False and False</code></td>
			<td style="background-color:#f8cecc"><code>False</code></td>
		</tr>
	</tbody>
</table>

** `x and y` истина, только когда оба аргумента - истина. В остальных случаях - ложь. **

### Оператор `or`

<table>
	<thead>
		<tr>
			<th>Выражение </th>
			<th>Результат</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>True or True</code></td>
			<td style="background-color:#dae8ff"><code>True</code></td>
		</tr>
		<tr>
			<td><code>True or False</code></td>
			<td style="background-color:#dae8ff"><code>True</code></td>
		</tr>
		<tr>
			<td><code>False or True</code></td>
			<td style="background-color:#dae8ff"><code>True</code></td>
		</tr>
		<tr>
			<td><code>False or False</code></td>
			<td style="background-color:#f8cecc"><code>False</code></td>
		</tr>
	</tbody>
</table>


** `x or y` ложь, только когда оба аргумента - ложь. В остальных случаях - истина. **

### Пьём чай с логическими операторами

В теории множеств `and` (конъюнкция) - это **пересечение** множеств.

Я хочу выпить чай. У меня есть чашка воды `x` и пакет чая `y`. Могу выпить чай, только если у меня есть и чашка, и пакетик **одновременно**. 

`вода and заварка`

![and](https://stepik.org/media/attachments/lesson/1160427/and_tea.png)


В теории множеств `or` (дизъюнкция) - это **объединение** множеств.

К чаю я хочу сладкого. У меня есть печенье `x` и конфета `y`. Сладкое у меня будет, если есть печенье или конфета или и печенье и конфета. **Хоть что-нибудь**. Только если у меня нет ни печенья, ни конфеты, я сижу без сладкого.

`печенье or конфета`

![or](https://stepik.org/media/attachments/lesson/1160427/or_tea.png)


## SKIP MATCH

Поставьте в соответствие эквивалентное выражение.

| Выражение | Еще выражение |
|----|----|
| not x == 5 | x != 5 |
| not x < 5 | x >= 5 |
| not x <= 5 | x > 5 |

## SKIP TABLE 

Чему равно значение выражения?

not True
not False
not not True
not not False

## SKIP TABLE 

Чему равно значение выражения?

True and True
True and False
False and True
False and False
True or True
True or False
False or True
False or False

## QUIZ 

Столовая работает с 8 до 22 часов. Сейчас `h` часов.

Какое выражение правильно проверяет, что сейчас столовая работает?

A. `8 <= h <= 22`

B. `8 <= h and h <= 22`

C. `8 <= h or h <= 22`

D. `8 <= h not h <= 22`

ANSWER: A, B

## Порядок вычислений

Порядок вычислений выражений с логическими операторами похож на порядок вычислений с арифметическими операторами.

Порядок вычисления операций в выражении определен **приоритетом операций**. Для арифметических операций таблица приоритетов и ассоциативности операций такая:

| Приоритет | Операторы | Описание | Ассоциативность |
|----|----|----|----|
| 1 | `()` | Скобки | Cлева направо |
| 2 | `**` | Степень | **Справа налево** |
| 3 | `-x` | Унарный минус | **Справа налево** |
| 4 | `*`, `/`, `//`, `%` | Умножение, деление, целочисленное деление, остаток | Слева направо |
| 5 | `+`, `–` | Сложение, вычитание  | Слева направо |	
| 6 | `=` | Присвоить  | **Справа налево** |

### Приоритет

**Приоритет** - какая операция выполнится раньше. Самая высокоприоритетная операция `()`, поэтому ими можно изменить последовательность выполнения любых операций.

`2 + 3 * 4` - сначала выполнится `3 * 4`, потом `2 + 12`. Результат `14`.

`(2 + 3) * 4` - сначала выполнится `(2 + 3)`, то есть вычислится `2 + 3`, потом `5 * 4`. Результат `20`.

### Ассоциативность

**Ассоциативность** (слева направо или справа налево). Из группы операторов **одинакового приоритета** какой будет выполняться раньше.

* Слева направо: `12 // 5 * 5` - сначала вычислится `12 // 5` (получим 2), потом `2 * 5`. Результат `10`.

* Справа налево: `4 ** 3 ** 2` вычислится как `4 ** (3 ** 2)`, то есть `4 ** 9`. Результат `262144`.

### Таблица приоритетов для логических операций и операций сравнения

| Приоритет | Операторы | Описание | Ассоциативность |
|----|----|----|----|
| 1 | `()` | Скобки | Cлева направо |
| 2 | `<`, `<=`, `>`, `>=`, `!=`, `==` | Сравнения  | Слева направо |		
| 3 | `not x` | Логическое NOT  | **Справа налево** |
| 4 | `and` | Логическое AND | Слева направо |	
| 5 | `or` | Логическое OR | Слева направо |

То есть, `not` - "как минус", `and` - "как умножить", `or` - "как сложить". И скобки меняют порядок вычислений.	

* `x < 2 and y > 3` - как `(x < 2) and (y > 3)`
* `x or y and z` - как `x or (y and z)`
* `not x or y and not z` - как `(not x) or (y and (not z))`

## SKIP TABLE

Чему равны значения выражений?

* not(True or False)
* not True or False
* not True and False
* not (True and not False)
* not True and not False
* not True or not False

## QUIZ 

| Номер месяца | Месяц | Время года |
|----|----|----|
| 1 | январь | зима |
| 2 | февраль | зима |
| 3 | март | весна |
| 4 | апрель | весна |
| 5 | май | весна |
| 6 | июнь | лето |
| 7 | июль | лето |
| 8 | август | лето |
| 9 | сентябрь | осень |
| 10 | октябрь | осень |
| 11 | ноябрь | осень |
| 12 | декабрь | зима |

Сейчас месяц номер `m`.

Какая запись правильно проверяет, что сейчас зима?

A. `m == 1 and m == 2 and m == 12`

B. `m == 1 or m == 2 or m == 12`

C. `not (2 < m < 12)`

D. `2 < not m < 12`

ANSWER: B, C


## QUIZ 

Понедельник - это 1, вторник - это 2, воскресенье - это 7.

Врач принимает с понедельника по пятницу с 8 до 16, а в субботу с 10 до 14.

Сейчас день `d` час `h`. Какое выражение правильно проверяет, принимает ли сейчас врач?

A. `1 <= d <= 5 and 8 <= h < 16 or d == 6 and 10 <= h < 14`

B. `1 <= d <= 5 or 8 <= h < 16 and d == 6 or 10 <= h < 14`

C. `1 <= d <= 5 or 8 <= h < 16 or d == 6 or 10 <= h < 14`

D. `1 <= d <= 5 and 8 <= h < 16 and d == 6 and 10 <= h < 14`

E. `1 <= d <= 5 or d == 6 and 8 <= h < 16 or 10 <= h < 14`

ANSWER: A


## SKIP TABLE

Чему равны значения выражений?

* not(True and True)
* not True or not True
повторить для всех пар

## SKIP TABLE

Чему равны значения выражений?

* not(True or True)
* not True and not True
повторить для всех пар

## Правила де Моргана

Поздравляем! Только что вы экспериментально вывели правила де Моргана для логических выражений.

Для логических выражений `a` и `b` верны следующие равенства:

* `not(a and b)` равно `not a or not b` 
* `not(a or b)` равно `not a and not b` 

Если у вас в решении задачи получается слишком сложное логическое выражение, посмотрите, можно ли его упростить  с помощью этих правил.

## QUIZ

Отметьте выражение, которое правильно проверяет, что год високосный.

Год `year` считается високосным, если он делится на 4, но не делится на 100. Каждый 400 год все равно является високосным.

A. year % 400 == 0 or year % 4 == 0 and year % 100 != 0
B. (year % 400 == 0 or year % 4 == 0) and year % 100 != 0
C. year % 4 == 0 and year % 100 != 0 or year % 400 == 0
D. year % 4 == 0 and year % 100 != 0 and year % 400 == 0
E. year % 4 == 0 or year % 100 != 0 or year % 400 == 0

ANSWER: A, C

## TASKINLINE Делится на 3 или 5, но не на 15

Напишите программу, которая печатает YES, если число делится на 3 или 5, но не делится на 15. Иначе напечатайте NO.

| Число | Напечатать | Почему |
|----|----|----|
| 6 | YES | делится на 3 |
| 10 | YES | делится на 5 |
| 150 | NO | делится на 15 |
| 4 | NO | не делится ни на 3, ни на 5 |

TEST
6
---
YES
====
10
---
YES
====
30
---
NO
====
11
---
NO
====
3
---
YES
====
5
---
YES
====
15
---
NO
====
150
---
NO
====
45
---
NO
====


## Ленивый питон

Правило: как только значение всего выражения можно определить, **дальше не считаем**.

```python
x < 5 and y != 3 or z == 0
```
Порядок вычислений при x = 10, y = 10, z = 0:

* `x < 5` False, значит `x < 5 and y != 3` все False
* поэтому `y != 3` не проверяем
* `z == 0` True
* `x < 5 and y != 3 or z == 0` это `False or True` равно `True`

Можете это не запоминать. Потому что для констант это практически не влияет на эффективность (быстроту выполнения кода).

А если вы написали так с функциями, которые не только проверяют, но и делают что-то нужное ещё, то не надо так писать!!!

```python
def ok():
    print('OK')     # делает что-то ещё
    return True
    
def foo():
    print('foooooo')
    return False
    
# не превращайте код в головоломку:
foo() and ok()      # напечатает только foooooo
foo() or ok()       # напечатает foooooo OK
```