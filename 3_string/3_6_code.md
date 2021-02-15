# Шифрование

lesson = 483732

## Шифрование

Чтобы письма не могли прочитать чужие люди, текст шифруют (кодируют).

Кодирование - это получение из понятного текста (исходного) непонятного (зашифрованного).

Когда из "Hello, world!" получают "Кhoor, zruog!", то это **шифрование**.

Когда потом знают, как их из "Кhoor, zruog!" получить "Hello, world!", то это **дешифрование**.

Когда не знают, как получить "Hello, world!", но пытаются из "Кhoor, zruog!" получить текст, то это называется **взлом шифра**.

Шифрами занимается наука [криптография](https://en.wikipedia.org/wiki/Cryptography)

## Шифр Цезаря

Простой [шифр Цезаря](https://en.wikipedia.org/wiki/Caesar_cipher)

Очень старый шифр. Алфавит сдвигается на N букв и получается зашифрованный алфавит. Cдвинем на 3 буквы, получим:

```python
abcdefghijklmnopqrstuvwxyz - что было
    |  |   |  |            - меняем на
defghijklmnopqrstuvwxyzabc - зашифрованный алфавит
```
* Шифрование:
    * буква а меняется на d
    * буква b меняется на e
    * ...
    * буква z меняется на c

Слово "hello" по буквам меняется на "khoor".

Нужно получить из "khoor" правильное слово? Нужно поменять буквы обратно.

* Дешифрование
    * буква d меняется на a
    * буква e меняется на b
    * ...
    * буква c меняется на z
    
Тогда получим из "khoor" опять "hello".

## STRING Расшифруйте слово

Слов зашифровали с помощью шифра Цезаря.

```cpp
abcdefghijklmnopqrstuvwxyz - исходный алфавит
tuvwxyzabcdefghijklmnopqrs - зашифрованный алфавит
```
Есть зашифрованное слово `irmahg`. Какое слово зашифровали?

ANSWER: python

## Задача

Будем писать программу. Она из "hello, world!", будет делать "khoor, zruog!" и обратно.

* Функция **cezar_code(text, letters_src, letters_dst)**.
* Функция переводит `text` из алфавита `letters_src` в алфавит `letters_dst`.
* Возвращает текст в алфавите letters_dst

```python
a1 = 'abcdefghijklmnopqrstuvwxyz'
a2 = 'defghijklmnopqrstuvwxyzabc'

text = 'hello'
res = cezar_code(text, a1, a2)

print(f'Input  text: {text}')   # hello
print(f'Output text: {text}')   # khoor
```

## Шифруем 1 букву

Что нужно для получения из буквы 'h' зашифрованной буквы 'k'?

```python
0123456789...              - номер буквы
abcdefghijklmnopqrstuvwxyz - буквы старого слова
    |  |   |  |            - меняем на
defghijklmnopqrstuvwxyzabc - буквы нового слова
```

* ищем в алфавите номер буквы 'h'.
    * буква 'h' стоит на месте номер 7
    * напишем функцию **number**(буква, алфавит).<br/>Она по букве и алфавиту возвращает место буквы в алфавите.
    
* берем в новом алфавите по номеру букву.
    * в новом алфавите на месте номер 7 стоит буква 'k'
    * напишем функцию **letter**(номер, алфавит).<br/>Она по номеру и алфавиту возвращает новую букву.
    
## Вспомним индексы строк и slice

```python
>>> s = 'Hello!'
>>> s[0]
'H'
>>> s[-1]
'!'
>>> s[1:4]
'ell'
>>> s[2:]
'llo!'
>>> s[:2]
'He'
>>> s[1:5:2]
'el'
>>> s[0:5:2]
'Hlo'
>>> s[::2]
'Hlo'
>>> s[::-2]
'!le'
>>> s[::-1]
'!olleH'
```

* напишем функцию **letter**(номер, алфавит).<br/>Она по номеру и алфавиту возвращает новую букву.
```python
def letter(i, al):
    """
    По строке алфавиту и номеру i получить букву из этого алфавита.
    Вернуть букву.
    """
    res = al[i]
    return res
```

## TASKINLINE Из числа в букву

* Есть алфавит 'abcdefghijklmnopqrstuvwxyz'
* Дана последовательность чисел на одной строке через пробел
* Напишите функцию **letter(i, al)**, который по строке `al` и числу `i` возвращает букву.
* соберите из букв строку
* Напечатайте строку.

TEST
7 4 11 11 14
----
hello
====
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
---- 
abcdefghijklmnopqrstuvwxyz
====

## Из буквы в число

В python у строк есть метод str.**find**(s)

* Ищет строку s в строке str. 
* Если s есть в str, то возвращает номер, с которого начинается s в str 
* Если s в str нет, то возвращает -1

```python
>>> "balalabla".find("la")
2
>>> "balalabla".find("z")
-1
```

* напишем функцию **number**(буква, алфавит).<br/>Она по букве и алфавиту возвращает место буквы в алфавите.

```python
def number(x, al):
    """
    По строке алфавиту и букве x получить номер места этой буквы в алфавите 
    или -1, если такой буквы в алфавите нет.
    Вернуть полученное число.
    """
    i = al.find(x)
    return i
```

## TASKINLINE Из букв в числа

Вы решили задачу перевода из чисел в буквы. Решим обратную задачу.

Дана строка. Перевести буквы в числа (места букв в алфавите)

TEST
hello
----
7 4 11 11 14
====
abcdefghijklmnopqrstuvwxyz
---- 
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
====

## TASKINLINE Зашифруем слово

Даны:

* старый алфавит `old_al`
* новый алфавит `new_al`
* слово `text`

Напишем функцию **cezar_code(text, old_al, new_al)**. Она возвращает новый текст.

```python
# Пример использования функции cezar_code

a1 = 'abcdefghijklmnopqrstuvwxyz'
a2 = 'defghijklmnopqrstuvwxyzabc'

text = 'hello'
res = cezar_code(text, a1, a2)

print(f'Input  text: {text}')   # hello
print(f'Output text: {text}')   # khoor
```

Зашифровать слово из старого алфавита в новый шифром Цезаря и напечатать результат.

TEST
abcdefghijklmnopqrstuvwxyz
defghijklmnopqrstuvwxyzabc
hello
----
khoor
====
defghijklmnopqrstuvwxyzabc
abcdefghijklmnopqrstuvwxyz
khoor
----
hello
====
abcdefghijklmnopqrstuvwxyz
tuvwxyzabcdefghijklmnopqrs
python
----
irmahg
====
tuvwxyzabcdefghijklmnopqrs
abcdefghijklmnopqrstuvwxyz
irmahg
----
python
====

## TASKINLINE code

Попробуем зашифровать строку

```python
# Пример использования функции cezar_code

a1 = 'abcdefghijklmnopqrstuvwxyz'
a2 = 'defghijklmnopqrstuvwxyzabc'

text = 'hello, world!'
res = cezar_code(text, a1, a2)

print(f'Input  text: {text}')   # hello, world!
print(f'Output text: {text}')   # khoorcczruogc  - откуда буквы с?
```
В новом тексте `с` вместо пробела, запятой и восклицательного знака. Откуда?

* функция find ищет пробел (`,` или `!`) в алфавите
* этих символов в алфавите нет. Поэтому find вернет -1.
* `al[-1]` - это буква `c`. Поэтому будет `с` вместо любого символа, которого нет в алфавите.

Исправьте программу. Шифруйте только буквы из алфавита. Остальные символы оставьте без изменений.

Вспомним: *s* **in** *str* - проверяем, что s содержится в str.

| код | результат |
|----|----|
| `"el" in "hello"` | True |
| `"hel" in "hello"` | True |
| `"z" in "hello"` | False |
| `"Hel" in "hello"` | False |

TEST
abcdefghijklmnopqrstuvwxyz
defghijklmnopqrstuvwxyzabc
hello, world!
----
khoor, zruog!
====
defghijklmnopqrstuvwxyzabc
abcdefghijklmnopqrstuvwxyz
khoor, zruog!
----
hello, world!
====
abcdefghijklmnopqrstuvwxyz
tuvwxyzabcdefghijklmnopqrs
i like python!!!
----
b ebdx irmahg!!!
====
tuvwxyzabcdefghijklmnopqrs
abcdefghijklmnopqrstuvwxyz
b ebdx irmahg!!!
----
i like python!!!
====

## TASKINLINE Новый алфавит

Напишите функцию **shift(k, al)**.

Функция сдвигает алфавит `al` на `k` и возвращает новый алфавит.

Дан сдвиг и на следующей строке алфавит.

Напечатайте новый алфавит для шифра Цезаря с указанным сдвигом.

TEST
3
abcdefghijklmnopqrstuvwxyz
----
defghijklmnopqrstuvwxyzabc
====
-3
defghijklmnopqrstuvwxyzabc
----
abcdefghijklmnopqrstuvwxyz
====
-7
abcdefghijklmnopqrstuvwxyz
----
tuvwxyzabcdefghijklmnopqrs
====

## Взлом шифра

Этот шифр легко взломать.

Есть зашифрованный текст. Будем расшифровывать его алфавитами с разными сдвигами: 1, 2, 3, .. 25.

Один результат будет верный.

У каждого свой номер варианта. Возьмите строку для своего варианта. Взломайте шрифт. Напишите преподавателю правильный текст на английском и сдвиг алфавита.

```cpp
1 zcysrgdsj gq zcrrcp rfyl sejw.
2 ibtpmgmx mw fixxiv xler mqtpmgmx.
3 rhlokd hr adssdq sgzm bnlokdw.
4 tfdgcvo zj svkkvi kyre tfdgcztrkvu.
5 xdsl ak twllwj lzsf fwklwv.
6 wtevwi mw fixxiv xler hirwi.
7 cplolmtwtej nzfyed.
8 qncagyj ayqcq ypcl'r qncagyj clmsef rm zpcyi rfc psjcq.
9 itbpwcop xzikbqkitqbg jmiba xczqbg.
10 uhhehi ixekbt duluh fqii iybudjbo.
11 sljcqq cvnjgagrjw qgjclacb.
12 sx dro pkmo yp kwlsqesdi, bopeco dro dowzdkdsyx dy qeocc.
13 lzwjw kzgmdv tw gfw-- sfv hjwxwjstdq gfdq gfw --gtnagmk osq lg vg al.
14 grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.
15 dem yi rujjuh jxqd duluh.
16 fqymtzlm sjajw nx tkyjs gjyyjw ymfs *wnlmy* stb.
17 fc qeb fjmibjbkqxqflk fp exoa ql bumixfk, fq'p x yxa fabx.
18 xu iwt xbeatbtcipixdc xh tphn id tmeapxc, xi bpn qt p vdds xstp.
19 zmyqebmoqe mdq azq tazwuzs sdqmf upqm — xqf'e pa yadq ar ftaeq!
```

