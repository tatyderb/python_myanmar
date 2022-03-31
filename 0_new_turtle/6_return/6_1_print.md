# print

lesson = 515007

## Черепаха умеет писать текст

Уже знаем.

Черепаха умеет писать текст.

```python
t.write('Hello')
```
Напишет текст `Hello` в том месте, где стоит черепаха.

Написать текст размера 18:
```python
t.write(text, font=('Arial', 18, 'normal'))
```
## Пример write и print

В python есть функция **print**. Она печатает текст. 

```python
print('Start')
```

В программе:
```python
import turtle

t = turtle.Turtle()
t.shape('turtle')
t.color('blue')

t.write('Hello', font=('Arial', 18, 'normal'))  # поле черепахи
print('start')                                  # console
print('stop')                                   # console

t.fd(150)
t.rt(90)
t.color('red')
t.write('End', font=('Arial', 18, 'normal'))    # поле черепахи
```

## консоль (console)

Что такое консоль и где ее найти?

### replit.com

![replit console](https://stepik.org/media/attachments/lesson/515007/replit_console.png)

### IDLE

![IDLE console](https://stepik.org/media/attachments/lesson/515007/idle_console.png)

### PyCharm

![PyCharm console]()

### Другая?

Не нашли свой пример? Пошлите снимок своего экрана и покажите в нем консоль.

## Разница между print и write

| | write | print |
|----|----|----|
| пример вызова | <b>t.</b>`write('abc')` | `print('abc')` |
| чья функция? | Функция черепахи | функция python |
| где? | графическое окно | консоль |
| передаем данные | делаем 1 аргумент | можно много аргументов |
| пример | `t.write((x, y))` | `print(x, y)` |
| import | нужно `import turtle` | import не нужно |

Функция `print` есть всегда. import для нее не нужен. Такие функции называют **встроенные функции** (build-in functions).

## TASKTEXT Имя и страна

* Напишите синими буквами на **поле с черепахой** ваше **имя**.
* Напишите **в консоли** название вашей **страны**.

Мое имя Tanya. Моя страна Russia. Моя программа пишет:
![name_country.png](https://stepik.org/media/attachments/lesson/515007/name_country.png)

## Без черепахи

Можно написать программу на python без черепахи. 

Программа печатает `Hello!` на консоль.

Вся программа:
```python
print('Hello!')
```

### replit.com

Если черепаха не нужна, можно использовать replit для python без черепахи.

![Hello на replit](https://stepik.org/media/attachments/lesson/515007/repl_hello.png)

### IDLE

![Hello на IDLE](https://stepik.org/media/attachments/lesson/515007/idle_hello.png)

### PyCharm

![Hello на PyCharm]()

## печатать красиво

Можно сделать красивую строку в print или write. Нужно указать формат.

Буква **f** перед строкой означает, что это *форматная строка*.

В форматной строке `{x}` означает "вместо переменной х поставить ее значение".

Примеры что напечатает:
```python
x = 12
y = 34
col = 'blue'
print(x, y, col)				 # 12 34 blue
print(f'{x}, {y}, {col}')		 # 12, 34, blue
print(f'x={x} y={y} цвет {col}') # x=12 y=34 цвет blue
print(f'{x} + {y} = {x+y}') 	 # 12 + 34 = 46
```

## TASKINLINE Задача с проверкой

stepik умеет сам проверять задачи без черепахи.

**Напишите программу. Она должна печатать `MIPT` (большими буквами).**

* Напишите код.
* Нажмите **Run**. Запустите код локально у вас на компьютере или телефоне.
* Проверьте, что код работает правильно. Исправьте ошибки, если нужно.
* Нажмите **Submit**. Пошлите код на проверку.

![stepik](https://stepik.org/media/attachments/lesson/515007/stepik_task.png)

Как проверяет stepik? 

* Учитель в задаче написал правильный ответ. Это **образец** (example).
* stepik запускает вашу программу и сравнивает, что она печатает и образец.
	* Образец и печать программы одинаковые? Значит задача решена.
	* Образец и печать программы разные? Значит задача НЕ решена.
	
TEST
1
----
MIPT
====


