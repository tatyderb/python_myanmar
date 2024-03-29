# Арифметика и переменные

lesson = 1140056

## python как калькулятор

### Содержание

1. Интерактивная консоль
2. Арифметические операции
3. Приоритет операций

### Интерактивная консоль

Если у вас установлен python, у вас под рукой есть мощный калькулятор с математическими функциями. Удобный ввод, копирование, сохранение промежуточных результатов в памяти и последующее их использование, история команд.

Научимся **переводить математические формулы в вычисления**.

Если вы еще не поставили python, но уже хотите попробовать работать с ним, то воспользуйтесь **интерактивной консолью** ниже:

<p><iframe height="356" src="https://trinket.io/embed/python/33e5c3b81b?runOption=console&amp;start=result&amp;runMode=console&amp;showInstructions=true" width="400"></iframe></p>


Вычислим `2+3` с помощью консоли:

1. после приглашения на ввод (символов `>>>`) напишите `2+3` 
2. нажмите клавишу `Enter` на клавиатуре. Тогда интерпретатор поймет, что ввод выражения закончен, его надо исполнить.
3. напечатает `5`
4. на следующей строке появится новое приглашение на ввод (`>>>`)

```python
>>> 2+3
5
>>>
```
Клавиша Enter: ![enter](https://stepik.org/media/attachments/lesson/1140056/Oxygen480-actions-key-enter.svg)


### Арифметические операции

| Выражение | Результат | Что это |
|----|----|----|
| `7 + 2` | 9 | сложение |
| `7 - 2` | 5 | вычитание |
| `7 * 2` | 14 | умножение |
| `7 ** 2` | 49 | возведение в степень |
| `7 / 2`| 3.5 | деление (математическое), результат - дробное число `float` |
| `7 // 2` | 3 | деление целочисленное, результат - целое число |
| `7 % 2` | 1 | остаток от деления |

*Перепишите эту таблицу себе в конспект.*

* Символ `+` называют **код операции** сложения. Числа 2 и 3 - **операнды**. Если операндов два, то операция **бинарная**. Если операнд один, то **унарная**. Пример унарной операции: `-5`, к числу 5 применили операцию "унарный минус".

* **Десятичные дроби записываются с разделителем `.` (точка), а не запятая**. В курсе все десятичные дроби мы будем писать именно так.


Попробуйте сами посчитать что-то в этом поле. Вычислите несколько выражений. Стрелки вверх и вниз перемещают по истории выполненных команд. Можно использовать скобки `()`

<p><iframe height="356" src="https://trinket.io/embed/python/33e5c3b81b?runOption=console&amp;start=result&amp;runMode=console&amp;showInstructions=true" width="400"></iframe></p>


### Задание 1. Выясните экспериментально, как работают

* `//` для отрицательных операндов,
* `%` для отрицательных операндов,
* `%`, если второй операнд - не целое число,
* `**` для нецелых чисел, посчитайте $\sqrt{9}$ через возведение в дробную степень.

*Результат запишите в конспект.*

### Приоритет операций

Так же, как в математике, операции обладают **приоритетом** (например, умножение выполняется раньше, чем сложение). Приоритет можно изменить с помощью скобок.

```python
>>> (2 + 3) * (4 + 6)
50
>>> 
```

### Сокращенная запись

В математике можно писать сокращенно, пропуская знак *умножить*. $(2 + 3)(4 + 6)$ это $(2 + 3) \cdot (4 + 6)$. В программировании нужно писать знак умножения.

```python
>>> (2 + 3) * (4 + 6)
50
>>> 
```
Без знака умножения интерпретатор питона не поймет вас:
![error](https://stepik.org/media/attachments/lesson/1140056/error_screen.png)

*Сначала ошибки могут быть не понятными. Такая ошибка возникает, если пропустили знак умножения.*

### Ошибки - наши учителя

Не бойтесь совершать ошибки. Чем больше вы их сделаете, тем быстрее поймете, как исправить новую ошибку.

## SKIP сопоставление

Сопоставьте выражению его результат.

21 / 8 = 2.625
21 // 8 = 2
21 % 8 = 5
21 + 8 = 29
21 - 8 = 13
21 * 8 = 168

## NUMBER Умножение

1. Вычислите значение выражения, **используя python**. Ниже дана **интерактивная консоль**; если у вас не стоит python, воспользуйтесь ей.
2. Скопируйте результат в поле ввода ниже консоли.
3. Нажмите кнопку *Отправить*
4. Если решение с ошибками, решите снова, исправив ошибку.
5. Откроется форум решений. Сходите в него и *прочитайте* авторское решение и интересные решения других студентов. **Посылать свое НЕ НУЖНО.** Свое решение нужно послать в форум, если оно оригинальное. Если ваше решение похоже на уже опубликованные, не засоряйте форум клонами. Мы их будем минусовать. 

Чему равно $$123 \cdot 45$$

<p><iframe height="356" src="https://trinket.io/embed/python/33e5c3b81b?runOption=console&amp;start=result&amp;runMode=console&amp;showInstructions=true" width="400"></iframe></p>


ANSWER: 5535

## NUMBER Деление

Чему равно $$\frac{2}{5} + \frac{1}{8}$$

<p><iframe height="356" src="https://trinket.io/embed/python/33e5c3b81b?runOption=console&amp;start=result&amp;runMode=console&amp;showInstructions=true" width="400"></iframe></p>

ANSWER: 0.525

## NUMBER Скобки

Чему равно $$\frac{(82-78)(27 + 53)}{(3 + 7)(16 - 11)}$$

<p><iframe height="356" src="https://trinket.io/embed/python/33e5c3b81b?runOption=console&amp;start=result&amp;runMode=console&amp;showInstructions=true" width="400"></iframe></p>

ANSWER: 6.4

## NUMBER Дробные числа

Чему равно $$0.258 \cdot 12$$

<p><iframe height="356" src="https://trinket.io/embed/python/33e5c3b81b?runOption=console&amp;start=result&amp;runMode=console&amp;showInstructions=true" width="400"></iframe></p>

ANSWER: 3.096


## NUMBER Степень

Чему равно $$12^3 + 7^4$$

<p><iframe height="356" src="https://trinket.io/embed/python/33e5c3b81b?runOption=console&amp;start=result&amp;runMode=console&amp;showInstructions=true" width="400"></iframe></p>

ANSWER: 4129

## NUMBER Степени

Чему равно $$4^{3^2}$$

<p><iframe height="356" src="https://trinket.io/embed/python/33e5c3b81b?runOption=console&amp;start=result&amp;runMode=console&amp;showInstructions=true" width="400"></iframe></p>

ANSWER: 262144

