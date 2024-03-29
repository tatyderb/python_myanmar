# Стек на основе списка

lesson = 660396

## Правильная скобочная последовательность, несколько типов скобок

Добавим к скобкам `(` и `)` еще `<` и `>`.

| Последовательность | Корректная? |
|----|----|
| `(<>)<()<>>` | Да |
| `(<>())` | Да |
| `<)(>` | Нет |
| `<(>)` | Нет |

Счетчики не решают задачу! Что делать?

## Интерфейс стек

Стек - структура данных, в которой реализован принцип **LIFO** (last input, first output), последним пришел, первым ушел. 

Пример стека - стопка тарелок или книг, детская пирамидка из колец, вагон метро в час пик. Тарелку можно поставить только на верх стопки и снять тоже - только верхнюю тарелку. Нельзя выдернуть тарелку из середины.

<img src="https://stepik.org/media/attachments/lesson/300286/toy.png"/> 
<img src="https://stepik.org/media/attachments/lesson/300286/stones.jpg"/> 

Основа интерфейса - это метод **push** (добавить элемент на вершину стека) и **pop** (удалить элемент с вершины стека).

<img src="https://stepik.org/media/attachments/lesson/300286/push_pop.png"/> 

## Стек - стакан с красками

Пусть наш стек - это стакан, в который наливают **push** и выливают **pop** слой краски. Эти  слои не смешиваются. 

**top** - посмотреть на вершину стека и сказать, какая сверху краска, но не изменять содержимое стека. (**pop** - изменяет стек).

Введем дополнительные функции:

**is_empty** - проверить, что стек пуст. Из него нельзя достать краску. Ее там нет.

**is_full** - проверить, что стек (стакан) полный. В него больше не получится наливать краску (она прольется через край).

**create** - создать (взять) стакан. Сначала стакан пустой.

Возьмем стакан и начнем наливать туда краски (**push**).

<table>
    <tr>
        <td>
        <img src="https://stepik.org/media/attachments/lesson/300286/stackan0.png"/><br/>
        <b>create</span><br/>
        <b>is_empty: true</b>
        </td>

        <td>
        <img src="https://stepik.org/media/attachments/lesson/300286/stackan1.png"/><br/>
        <b>push (<span style="color:#64b0f4">blue</span>)</b><br/>
        <b>top: <span style="color:#64b0f4">blue</span></b>
        </td>

        <td>
        <img src="https://stepik.org/media/attachments/lesson/300286/stackan2.png"/><br/>
        <b>push (<span style="color:#ff4363">red</span>)</b><br/>
        <b>top: <span style="color:#ff4363">red</span></b>
        </td>

        <td>
        <img src="https://stepik.org/media/attachments/lesson/300286/stackan3.png"/><br/>
        <b>push (<span style="color:#66cc66">green</span>)</b><br/>
        <b>top: <span style="color:#66cc66">green</span></b>
        </td>

        <td>
        <img src="https://stepik.org/media/attachments/lesson/300286/stackan4.png"/><br/>
        <b>push (<span style="color:#ff9900">yellow</span>)</b><br/>
        <b>top: <span style="color:#ff9900">yellow</span></b>
        </td>

        <td>
        <img src="https://stepik.org/media/attachments/lesson/300286/stackan5.png"/><br/>
        <b>push (<span style="color:#ff00cc">magenta</span>)</b><br/>
        <b>top: <span style="color:#ff00cc">magenta</span></b>
        </td>
    </tr>
</table>

Стакан полный. В него больше ничего нельзя налить до тех пор, пока не выльем хотя бы 1 слой. Иначе будет **переполнение стека** (stack overflow).

Начнем выливать из стакана функцией **pop**.

<table>
    <tr>
        <td>
        <img src="https://stepik.org/media/attachments/lesson/300286/stackan5.png"/><br/>
        <b>is_full: true</b><br/>
        <b>top: <span style="color:#ff00cc">magenta</span></b>
        </td>

        <td>
        <img src="https://stepik.org/media/attachments/lesson/300286/stackan4.png"/><br/>
        <b>pop: <span style="color:#ff00cc">magenta</span></b><br/>
        <b>top: <span style="color:#ff9900">yellow</span></b>
        </td>

        <td>
        <img src="https://stepik.org/media/attachments/lesson/300286/stackan3.png"/><br/>
        <b>pop: <span style="color:#ff9900">yellow</span></b><br/>
        <b>top: <span style="color:#66cc66">green</span></b>
        </td>

        <td>
        <img src="https://stepik.org/media/attachments/lesson/300286/stackan2.png"/><br/>
        <b>pop: <span style="color:#66cc66">green</span></b><br/>
        <b>top: <span style="color:#ff4363">red</span></b>
        </td>

        <td>
        <img src="https://stepik.org/media/attachments/lesson/300286/stackan1.png"/><br/>
        <b>pop: <span style="color:#ff4363">red</span></b><br/>
        <b>top: <span style="color:#64b0f4">blue</span></b>
        </td>

        <td>
        <img src="https://stepik.org/media/attachments/lesson/300286/stackan0.png"/><br/>
        <b>pop: <span style="color:#64b0f4">blue</span></b><br/>
        <b>is_empty: true</b>
        </td>
    </tr>
</table>

Когда стек пустой из него нельзя сделать **pop** - нечего доставать, стек может испортиться.

## Проверяем скобки, используем стек

```cpp
Пока есть скобки
    если скобка открывающая
        положить ее в стек push
    если скобка закрывающая
        достать скобку из стека pop
        если достать не можем — плохо
		если эти скобки не пара — плохо

В конце проверить, что стек пустой
Последовательность корректная
```

* читаем новую скобку в переменную `с` (current bracket), 
* из стека достается в переменную `p` (popped bracket)

Последовательность `(<><()>)`

| `c` | `p` | стек после операции | что делали |
|----|-------|----|-----|
| `(` |  | `(` | `c` открывающая, `push(c)` |
| `<` |   | `(<` | `c` открывающая, `push(c)` |
| `>` | `<` | `(` | `c` закрывающая, `p = pop()` <br/>  `с` и `p` пара, идем дальше |
| `<` | `<` |  `(<` | `c` открывающая, `push(c)` |
| `(` | `<` | `(<(` | `c` открывающая, `push(c)` |
| `)` | `)` | `(<` | `c` закрывающая, `p = pop()` <br/>  `с` и `p` пара, идем дальше |
| `>` | `<` | `(` | `c` закрывающая, `p = pop()` <br/>  `с` и `p` пара, идем дальше |
| `)` | `(` | стек пуст | `c` закрывающая, `p = pop()` <br/>  `с` и `p` пара, идем дальше |
| нет | `(` | стек пуст |  последовательность закончилась,<br/> стек пуст, значит <br/>последовательность корректна |

Последовательность `(<)>`

| `c` | `p` | стек после операции | что делали |
|----|-------|----|-----|
| `(` |  | `(` | `c` открывающая, `push(c)` |
| `<` |   | `(<` | `c` открывающая, `push(c)` |
| `)` | `<` | `(` | `c` закрывающая, `p = pop()` <br/>  `с` и `p`  НЕ пара.<br/> СТОП, последовательность не корректна |

## Как решать?

Удобно сделать списки:
```python
bra_open  = ['(', '{', '[', '<']
bra_close = [')', '}', ']', '>']
```

Как проверить, что символ в переменной **с** открывающая скобка?

### метод index возвращает номер элемента

```python
a = [3, 7, -4, 11]
i = a.index(-4)          # i = 2
i = a.index(88)          # ошибка ValueError: 88 is not in list
```

## TASKINLINE Правильная скобочная последовательность - 2

Дана последовательность из скобок `( ) { } [ ] < >`.

Напечатайте, правильная она (YES) она или нет (NO).

| Последовательность | Правильная? |
|----|----|
| `{)` | NO |
| `[({<>})]` | YES |
| `)(` | NO |
| `()()` | YES | 
| `[(])` | NO |


TEST
{)
----
NO
====
[({<>})]
----
YES
====
)(
----
NO
====
()()
----
YES
====
[(])
----
NO
====
[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[
----
NO
====
[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
----
YES
====
{[(<{[(<[}>)]}>)]}
----
NO
====
