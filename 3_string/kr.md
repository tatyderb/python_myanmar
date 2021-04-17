# Задачи на контрольную

lesson = 515807

## Почему это в курсе?

Задачи в курсе, а не в ejudge. Потом будут там.

## TASKINLINE Расширение файла

Напишите функцию **get_ext(filename)**

Она по имени файла `filename` вернет расширение файла. 

В имени файла могут тоже быть точки. Так пишут версии. Например, `Anaconda3-2019.03-Windows-x86_64.exe` расширение `exe`

Если расширения нет, то вернет пустую строку `''`.

Внимание! В UNIX некоторые файлы начинаются с точки. Например `.ssh` или `.gitignore`. У них расширения нет.

Читайте имя файла и печатайте результат так:
```python
filename = input().strip()   # не нужны пробелы в конце!
ext = get_ext(filename)
print('['+ext+']')
```

TEST
hello.py
----
[py]
====
Anaconda3-2019.03-Windows-x86_64.exe
----
[exe]
====
Makefile
----
[]
====
.ssh
----
[]
====
.git
----
[]
====
lesson.2021.02.14.pptx
----
[pptx]
====

## TASKINLINE Имя диска

Напишите функцию **get_disk(path)**

Она по пути в Windows `path` вернет имя диска. 

```cpp
C:\work\python_myanmar
```
Имя диска `С`. 

Если имени диска нет, то вернет пустую строку `''`.

Читайте имя файла и печатайте результат так:
```python
path = input().strip()   # не нужны пробелы в конце!
disk = get_disk(path)
print('['+disk+']')
```

TEST
C:\work\python_myanmar
----
[C]
====
D:\work\lesson\hello.py
----
[D]
====
hello.py
----
[]
====
\work\lesson\hello.py
----
[]
====
lesson\hello.py
----
[]
====
Z:\work\lesson\hello.py
----
[Z]
====

## TASKINLINE URL - протокол

В браузере мы открываем страницы. У каждого объекта (страницы, изображения) есть адрес. Это URL - Universal Resource Locator.

Примеры URL:
```
http://acm.mipt.ru/twiki/bin/view/Cintro/PythonList4#___qmc_join_rq_ngfq_c_gn_pq_____
https://mipt.ru/education/foreign/
https://developer.mozilla.org/ru/docs/Learn/Common_questions/What_is_a_URL
ftp://192.168.1.11:2021/Downloads/solution.py
```
URL состоит из:

* protocol - протокол (http, https, ftp, mailto и других)
* domain name - имя домена (mipt.ru, developer.mozilla.org)
* port - порт (2021) - не обязательное поле
* path (to file) - путь (к файлу) - не обязательное
* parameters - параметры - не обязательно
* anchor - якорь - не обязательно 

Рассмотрим
```cpp
http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument
```

![protocol](https://stepik.org/media/attachments/lesson/515807/protocol.png)

![domain](https://stepik.org/media/attachments/lesson/515807/domain.png)

![port](https://stepik.org/media/attachments/lesson/515807/port.png)

![path](https://stepik.org/media/attachments/lesson/515807/path.png)

![parameters](https://stepik.org/media/attachments/lesson/515807/parameters.png)

![anchor](https://stepik.org/media/attachments/lesson/515807/anchor.png)

Напишите функцию **get_protocol(url)**. Она из **url** возвращает протокол.

Считать, что **протокол всегда есть в URL.**

Читайте URL и печатайте результат так:
```python
url = input().strip()   # не нужны пробелы в конце!
protocol = get_protocol(url)
print('['+protocol+']')
```

Рисунки и объяснения взяты из [developer.mozilla.org](https://developer.mozilla.org/ru/docs/Learn/Common_questions/What_is_a_URL)
Это очень полезный сайт.

CODE
def get_protocol(url):
    # тут нужно написать код

url = input().strip()   # не нужны пробелы в конце!
protocol = get_protocol(url)
print('['+protocol+']')

TEST
https://stepik.org/media/attachments/lesson/515807/parameters.png
----
[https]
====
http://acm.mipt.ru/twiki/bin/view/Cintro/PythonList4#___qmc_join_rq_ngfq_c_gn_pq_____
----
[http]
====
ftp://192.168.1.11:2021/Downloads/solution.py
----
[ftp]
====
http://judge2.vdi.mipt.ru/cgi-bin/new-master?SID=3fc61087336ebefe&action=2
----
[http]
====
https://stepik.org/edit-lesson/515807/step/3
----
[https]
====
ftp://acm.mipt.ru/twiki/pub/Cintro/WebHome/C_beginff.pdf
----
[ftp]
====

## TASKINLINE URL - якорь

тут будет задача

TEST
1
----
1
====

## TASKINLINE URL - аргументы

тут будет задача

TEST
1
----
1
====

## TASKINLINE URL разбор

тут будет задача

TEST
1
----
1
====
