# Шифры (продолжение)

lesson = 484417

## Делаем шрифт сложнее

Чтобы шифр было труднее взломать, новый алфавит делается с ключевой фразой.

Буквы из ключевой фразы берутся по 1 разу, остальные буквы берутся из алфавита.

```cpp
apple + abcdefghijklmnopqrstuvwxyz 
```
Буквы в `()` не войдут в алфавит, потому что каждая буква должна входить в алфавит только 1 раз.
```
ap(p)le + (a)bcd(e)fghijk(l)mno(p)qrstuvwxyz 
```
Удалим лишние буквы. Получим алфавит.

```cpp
Исходный алфавит: abcdefghijklmnopqrstuvwxyz
Новый алфавит:    aplebcdfghijkmnoqrstuvwxyz
```
Часть алфавита не шифруется. Буквы `qrstuvwxyz` остаются как есть. Это плохо.

Возьмем не 1 слово, а много слов. Например, [The quick brown fox jumps over the lazy dog](https://ru.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog). 

Берем из предложения только буквы и строим хороший алфавит.

## TASKINLINE Убрать лишние числа

Даны числа. Убрать повторения.

TEST
2 14 2 5 7 5 -3 2 1 7
---- 
2 14 5 7 -3 1
====
1 1 1 1 1 1
----
1
====
12 3 -4 56 7 890 123
----
12 3 -4 56 7 890 123
====


## TASKINLINE Алфавит по слову

* Дана строка (только маленькие буквы) key_text.
* Дан алфавит alphabet.
* Напечатайте новый алфавит для шифра Цезаря.

Напишите функцию **new_alphabet(key_text, alphabet)** 

* Из предложения `key_text`
* и алфавита `alphabet`
* делает новый алфавит
* возвращает новый алфавит

TEST
apple
abcdefghijklmnopqrstuvwxyz
----
aplebcdfghijkmnoqrstuvwxyz
====
the quick brown fox jumps over the lazy dog
abcdefghijklmnopqrstuvwxyz
----
thequickbrownfxjmpsvlazydg
====

## Шифр Вижнера 

[Статья в wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

Добавляем ключевое слово (key word) для шифрования. Например, 'lemon'. Тогда для шифровки каждой буквы текста 'hello' используется свой сдвиг для построение алфавита цезаря.

* Буква 'h' шифруется алфавитом, где 'a' переходит в 'l'
* Буква 'e' шифруется алфавитом, где 'a' переходит в 'e'
* Буква 'l' шифруется алфавитом, где 'a' переходит в 'm'
* Буква 'l' шифруется алфавитом, где 'a' переходит в 'o'
* Буква 'o' шифруется алфавитом, где 'a' переходит в 'n'

Если текст больше, то слово 'lemon' повторяется столько раз, сколько нужно:

```cpp
Исходный текст:       ATTACKATDAWN
Ключ:                 LEMONLEMONLE
Зашифрованный текст:  LXFOPVEFRNHR
```

Для шифрования руками делают 1 раз квадрат Виженера (tabula recta):

```cpp
 0 a abcde fghij klmno pqrst uvwxyz
 1 b bcdef ghijk lmnop qrstu vwxyza
 2 c cdefg hijkl mnopq rstuv wxyzab
 3 d defgh ijklm nopqr stuvw xyzabc
 4 e efghi jklmn opqrs tuvwx yzabcd
 5 f fghij klmno pqrst uvwxy zabcde
 6 g ghijk lmnop qrstu vwxyz abcdef
 7 h hijkl mnopq rstuv wxyza bcdefg
 8 i ijklm nopqr stuvw xyzab cdefgh
 9 j jklmn opqrs tuvwx yzabc defghi
10 k klmno pqrst uvwxy zabcd efghij
11 l lmnop qrstu vwxyz abcde fghijk
12 m mnopq rstuv wxyza bcdef ghijkl
13 n nopqr stuvw xyzab cdefg hijklm
14 o opqrs tuvwx yzabc defgh ijklmn
15 p pqrst uvwxy zabcd efghi jklmno
16 q qrstu vwxyz abcde fghij klmnop
17 r rstuv wxyza bcdef ghijk lmnopq
18 s stuvw xyzab cdefg hijkl mnopqr
19 t tuvwx yzabc defgh ijklm nopqrs
20 u uvwxy zabcd efghi jklmn opqrst
21 v vwxyz abcde fghij klmno pqrstu
22 w wxyza bcdef ghijk lmnop qrstuv
23 x xyzab cdefg hijkl mnopq rstuvw
24 y yzabc defgh ijklm nopqr stuvwx
25 z zabcd efghi jklmn opqrs tuvwxy
```

Кто расшифровывает, тоже знает ключевое слово.

Этот шифр легко расшифровывается подбором длины ключевого слова. 

Защита лучше, если используется не ключевое слово, а ключевой текст, который равен длине шифруемого текста (не повторяется, а все время новый). 

Новая шифровка - новый ключевой текст. Для этого (дипломатическая переписка) у отправителя и у получателя были одинаковые шифровальные блокноты, которые содержали только ключевой текст. После использования текста страница блокнота вырывалась и уничтожалась.

## TASKINLINE

Эту задачу можно не делать.

* Дано ключевое слово для шифра Виженера.
* Дан текст.
* Зашифруйте текст с этим ключевым словом. Напечатайте результат

TEST
lemon
attack at dawn
----
lxfopv ef rnhr
====
