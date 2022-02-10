# Методы класса str (продолжение)

lesson = 488122



## Часть строки проверить

*   Проверки (подстрока в строке)
    * str.**count**(sub) - сколько раз входит (без пересечений)
    * **in** - поиск подстроки в строке
    * str.**endswith**(sub) - str оканчивается на sub
    * str.**startswith**(sub) - str начинается на sub
    
```python
"alalabla".count("la")      # 3
"alalabla".count("ala")     # 1

"hello".startswith("hel")   # True
"hello".startswith("el")    # False

"hello".endswith("lo")      # True
"hello".endswith("el")      # False

"el" in "hello"             # True           
"hel" in "hello"            # True
"Hel" in "hello"            # False - большая буква!
```    

## Номер начала подстроки   

* **Индекс** начала подстроки в строке, (иначе проверяем как 'el' in 'Hello')
    * str.**find**(sub\[, start\[, end\]\]) - возвращает -1, если подстроки нет
    * str.**index**(sub\[, start\[, end\]\]) - кидает ValueError, если подстроки нет
    * str.**rfind**(sub\[, start\[, end\]\])
    * str.**rindex**(sub\[, start\[, end\]\])
    
```python
"balalabla".find("la")  # 2
"alalabla".find("zx")   # -1

"balalabla".rfind("la") # 7
"alalabla".rfind("zx")  # -1

"balalabla".index("la")     # 2
"balalabla".rindex("la")    # 7
"balalabla".rindex("zx")    # Oops! ValueError
```

Как работать с `index` узнаем потом. Узнаем `try` и `except`.

## Замена

* Найти и заменить
    * str.**replace**(old, new) - заменяет в str все части old на new 
    * str.**replace**(old, new, count) - заменяет в str все части old на new не более count раз
    
```python
"balalabla".replace("la", "xyz")    # "baxyzxyzbxyz"
"balalabla".replace("la", "xyz", 2) # "baxyzxyzbla"
```  

```python
>>>'AAAAAA'.replace('AA', 'A')
'AAA'
>>> S = 'xxxxSPAMxxxxSPAMxxxx'
>>> S.replace('SPAM', 'EGGS')    # Заменить все найденные подстроки
‘xxxxEGGSxxxxEGGSxxxx’
>>> S.replace('SPAM', 'EGGS', 1) # Заменить одну подстроку
'xxxxEGGSxxxxSPAMxxxx'
```  

## Разбить и склеить

* str.**partition**(sep) - 3 строки: до, sep, после
* str.**rpartition**(sep) - 3 строки: до, sep, после. Ищем sep справа

* находим первую bomb слева
```python
my_str = "I have 2 small bombs and big bomb"
before, s, after = my_str.partition("bomb")
print(before)   # "I have 2 small "
print(s)        # "bomb"
print(after)    # "s and big bomb"
```

* находим первую bomb справа
```python
my_str = "I have 2 small bombs and big bomb"
before, s, after = my_str.rpartition("bomb")
print(before)   # "I have 2 small bombs and big "
print(s)        # "bomb"
print(after)    # ""
```

* ищем dog, его нет
```python
my_str = "I have 2 small bombs and big bomb"
before, s, after = my_str.partition("dog")
print(before)   # "I have 2 small bombs and big bomb"
print(s)        # ""
print(after)    # ""
```

## Разбить и склеить (повторение)

* строка.**split**(разделитель) - разделить 1 строку на много строк.
* разделитель.**join**(много строк) - из много строк сделать 1 строку.

Мы знаем, что split разделит строку по пробелам.
```python
a = "I have dog.".split() # a = ['I', 'have', 'dog.']
b = '-=-'.join(a)                # b = 'I-=-have-=-dog.'
```

Можно указать, чтобы split делила по разделителю.
```python
'1;2;3;hello'.split(';')        # ['1', '2', '3', 'hello']
'I-=-have-=-dog.'.split('-=-')  # ['I', 'have', 'dog.']
'1,2,,3,'.split(',')            # ['1', '2', '', '3']
```

Можно указать, **сколько** (не больше) раз делить. Если maxsplit очень большое, то делим сколько есть разделителей.
```python
'1,2,3'.split(',', maxsplit=1)  # ['1', '2,3']
'1,2,3'.split(',', maxsplit=10) # ['1', '2', '3']
```

Склеиваем только строки. Если не строки, то делаем строки и склеиваем

* `' '.join([1, 2, 3])` - ошибка, должны быть строки, а не числа.
* `' '.join(map(str, [1, 2, 3]))` - применить с помощью map функцию str к каждому элементу из списка `[1, 2, 3]`. 

## Разделить по строкам

В конце строки стоят специальные символы

* `\n` - в Linux, UNIX
* `\r` - в MAC
* `\r\n` - сразу 2 символа в Windows

Можно делить по строкам функцией **split**. 

Можно делить по строкам функцией **splitlines**

```python
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines()
['ab c', '', 'de fg', 'kl']
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
['ab c\n', '\n', 'de fg\r', 'kl\r\n']
```
