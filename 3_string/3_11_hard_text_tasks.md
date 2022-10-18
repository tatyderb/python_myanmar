# Задачи на обработку текста

lesson = 509847

## TASKINLINE сколько бомб

В файле **mail.txt** дан текст. Напечатайте сколько раз в нем встретилась подстрока (слово или часть слова) `bomb`.

HEADER
import sys
text = sys.stdin.read()
filename = 'mail.txt'
with open(filename, 'w') as fd:
    fd.write(text)

TEST
a high explosive bomb is one that employs a process called detonation to rapidly release its chemical energy
the seven islands that came to constitute mumbai were home to communities of fishing colonies
the simplest and oldest type of bombs store energy in the form of a low explosive
mumbai also known as bombay is the capital city of the indian state of maharashtra
BOMBS
----
3
====
the simplest and oldest type of bombs store energy 
in the form of a low explosive
mumbai also known as bombay is the capital city 
of the indian state of maharashtra
----
2
====
I have a dog and a cat.
----
0
====

## TASKINLINE заменить бомбы на арбузы

В файле `bomb.txt` дан текст. Замените все подстроки `bomb` на `watermelon`.

* В классе оффлайн с учителем: сохраните полученный текст в файл `out.txt`.
* В stepik результат выведите на `sys.stdout`.

HEADER
import sys
text = sys.stdin.read()
filename = 'bomb.txt'
with open(filename, 'w') as fd:
    fd.write(text)

TEST
A high explosive bomb is one that employs a process called detonation to rapidly release its chemical energy
The seven islands that came to constitute Mumbai were home to communities of fishing colonies
The simplest and oldest type of bombs store energy in the form of a low explosive. 
Mumbai also known as Bombay is the capital city of the Indian state of Maharashtra.
BOMBS
----
A high explosive watermelon is one that employs a process called detonation to rapidly release its chemical energy
The seven islands that came to constitute Mumbai were home to communities of fishing colonies
The simplest and oldest type of watermelons store energy in the form of a low explosive. 
Mumbai also known as Bombay is the capital city of the Indian state of Maharashtra.
BOMBS
====
the simplest and oldest type of bombs store energy 
in the form of a low explosive
mumbai also known as bombay is the capital city 
of the indian state of maharashtra
----
the simplest and oldest type of watermelons store energy 
in the form of a low explosive
mumbai also known as watermelonay is the capital city 
of the indian state of maharashtra
====
I have a dog and a cat.
----
I have a dog and a cat.
====


## TASKINLINE basename - промежуточная задача

Напишите функцию **basename(path)**.

* **path** - путь к файлу или директории
* функция возвращает 
    * имя файла, 
    * или пустую строку `''`, если path имя директории (последний символ /) или пустая строка
    
```python
print(basename('hello.py'))              # hello.py
print(basename('./hello.py'))            # hello.py
print(basename('../lesson3/hello.py'))   # hello.py
print(basename('/hello.py'))             # hello.py
print(basename('cat.jpg'))               # cat.jpg
print(basename('hello/'))                # пустая строка
print(basename('/home/taty/hello/'))     # пустая строка
print(basename('/home/taty/hello'))      # hello
print(basename('/home/taty/.gitignore')) # .gitignore
print(basename(''))                      # пустая строка
```
Удобно проверять функцию c [assert](https://stepik.org/lesson/408394/step/3?unit=397697):
```python
assert basename('hello.py') == 'hello.py'
assert basename('./hello.py') == 'hello.py'
assert basename('../lesson3/hello.py') == 'hello.py'
assert basename('/hello.py') == 'hello.py'
assert basename('cat.jpg') == 'cat.jpg'
assert basename('hello/') == ''
assert basename('/home/taty/hello/') == ''
assert basename('/home/taty/hello') == 'hello'
assert basename('/home/taty/.gitignore') == '.gitignore'
assert basename('') == ''
```

Подсказка: печатать результат можно как
```python
pathname = input().rstrip()
print('['+basename(pathname)+']')
```

TEST
hello.py
----
[hello.py]
====
./hello.py
----
[hello.py]
====
../lesson3/hello.py
----
[hello.py]
====
/hello.py
----
[hello.py]
====
cat.jpg
----
[cat.jpg]
====
/hello
----
[hello]
====
hello/
----
[]
====
hello/
----
[]
====
/home/taty/hello/
----
[]
====
/home/taty/hello
----
[hello]
====
/home/taty/.gitignore
----
[.gitignore]
====

## TASKINLINE extension - промежуточная задача

Напишите функцию **splitpath(path)**. Она отделяет расширение файла.

* разделяет path на части `(dirname, filename, ext)`, <br/> где `dirname + filename + ext == path`
* возвращает `(dirname, filename, ext)`
* `ext` или начинается с `.` или пустая строка

Подсказка: печатать результат можно как
```python
pathname = input().rstrip()
d, filename, ext = splitpath(path)
print('['+d+']')
print('['+filename+']')
print('['+ext+']')
```
Проверка:
```python
assert splitpath('./hello.py') == ('./', 'hello', '.py')
assert splitpath('python') == ('', 'python', '')
```

**Внимание! НЕ делайте переменную dir. `dir()` - это специальная функция python.**

TEST
./hello.py
----
[./]
[hello]
[.py]
====
hello.py
----
[]
[hello]
[.py]
====
/home/taty/hello/
----
[/home/taty/hello/]
[]
[]
====
../lesson2/sun.jpg
----
[../lesson2/]
[sun]
[.jpg]
====


## TASKINLINE сколько .py файлов

В файле `lesson.txt` написаны пути к файлам этого урока. 

По 1 пути на строку. 

Напечатайте сколько файлов с расширением `.py`

HEADER
import sys
text = sys.stdin.read()
filename = 'lesson.txt'
with open(filename, 'w') as fd:
    fd.write(text)

TEST
/3_string/tasks/first_line.py
/add/nature.png
/property/station.html
../3_string/tasks/ex_readlines.py
./3_string/tasks/flint.py
3_string/tasks/names.txt
/3_string/tasks/first_line.py
/3_string/tasks/first_line.pyc
----
4
====
../0_turtle/4_arguments/0_4_argument.md
../1_repeat/9_while.md
../2_list/13_slice.md
../3_string/3_2_str.md
../3_string/3_8_readline.md
../3_string/3_9_text_tasks.md
/3_string/tasks/first_line.py
../3_string/tasks/ex_readlines.pyc
./3_string/tasks/flint.py
3_string/tasks/names.txt
../3_string/tasks/vizhner.py
../3a_file/
./
../5_dict_set/
../out.log
../tasks/0_1_forward/
/else/inside.webm
/field/six.pptx
/measure/traditional.ods
/economy/peace.png
/total/special.webm
/range/together.png
/particularly/its.docx
/tend/local.webm
/add/nature.png
/property/station.html
----
3
====
/add/nature.png
----
0
====

## TASKINLINE сколько файлов с решениями

Курс состоит из разных файлов. В файле `filelist.txt` написан список путей к файлам или директориям.

Файл с решением задачи имеет расширение `.py` и имя файла начинается с `task`.

* Что делать в классе (решение проверяется учителем):
    * Запишите все пути к файлам решений задач в выходной файл `tasklist.txt`.
    * Выведите на `sys.stdout` **сколько** задач в списке.
* Что делать этой задаче на stepik.org:
    * пути к файлам решений задач печатайте на `sys.stdout`.
    * Выведите на `sys.stdout` **сколько** задач в списке.

Примеры путей:

* `./3_string/task_flint.py` - задача
* `/add/nature.png` - НЕ задача
* `./3_string/tasks/flint.py` - НЕ задача (нет слова task в имени файла)
* `./3_string/tasks/flint_task.py` - НЕ задача (не начинается имя файла с task)
* `./3_string/task_lesson.md` - НЕ задача, расширение `.md`
* `./3_string/task_flint.pyc` - НЕ задача, расширение `.pyc`
* `/task_sun.py` - задача

HEADER
import sys
text = sys.stdin.read()
filename = 'filelist.txt'
with open(filename, 'w') as fd:
    fd.write(text)

TEST
./3_string/task_flint.py
/add/nature.png
./3_string/tasks/flint.py
./3_string/tasks/flint_task.py
./3_string/task_lesson.md
./3_string/task_flint.pyc
/task_sun.py
----
./3_string/task_flint.py
/task_sun.py
2
====
../0_turtle/4_arguments/0_4_argument.md
../1_repeat/9_while.md
../2_list/13_slice.md
../3_string/3_2_str.md
../3_string/3_8_readline.md
../3_string/3_9_text_tasks.md
/3_string/task_first_line.py
../3_string/tasks/ex_readlines.py
./3_string/tasks/flint.py
3_string/tasks/names.txt
../3_string/task_vizhner.py
../3_string/task_vizhner.pyc
../3a_file/
./
../5_dict_set/
../out.log
../tasks/0_1_forward/
/else/inside.webm
/field/six.pptx
/measure/traditional.ods
/economy/peace.png
/total/special.webm
/range/together.png
/particularly/its.docx
/tend/local.webm
/add/nature.png
/property/station.html
----
/3_string/task_first_line.py
../3_string/task_vizhner.py
2
====
/particularly/its.docx
/tend/local.webm
/add/nature.png
/property/station.html
task_sum.py
----
task_sum.py
1
====

## TASKINLINE filesize

В файле `filelist.txt` напечатан результат работы команды Linux

```cpp
ls -lsh /mnt/c/Users/tatyd/Downloads/
```
Получили:
```
 662M -rwxrwxrwx 1 tatyderb tatyderb 662M Jun  1  2019  Anaconda3-2019.03-Windows-x86_64.exe
 467M -rwxrwxrwx 1 tatyderb tatyderb 467M Jul  1  2020  Anaconda3-2020.02-Windows-x86_64.exe
 391M -rwxrwxrwx 1 tatyderb tatyderb 391M Jun 30  2020 'Docker Desktop Installer.exe'
 304M -rwxrwxrwx 1 tatyderb tatyderb 304M Jan  2  2020  LibreOffice_6.3.4_Win_x64.msi
  60M -rwxrwxrwx 1 tatyderb tatyderb  60M Mar 18  2020  DiscordSetup.exe
  58M -rwxrwxrwx 1 tatyderb tatyderb  58M Mar 17  2020  MovaviVideoEditorSetupC.exe
  58M -rwxrwxrwx 1 tatyderb tatyderb  58M Jun 25  2019  pandoc-2.7.3-windows-x86_64.msi
 1.1M -rwxrwxrwx 1 tatyderb tatyderb 1.1M Jul 22  2020 'PayApp 2020-07-22 18-13-35.png'
1000K -rwxrwxrwx 1 tatyderb tatyderb 997K Nov 18 15:07  7001173624_1605701140381.zip
 996K -rwxrwxrwx 1 tatyderb tatyderb 996K Nov 18 14:57  7001173624_1605700280816.zip
 320K -rwxrwxrwx 1 tatyderb tatyderb 319K Mar  1  2020  download.html
 320K -rwxrwxrwx 1 tatyderb tatyderb 319K Sep 20  2019 'c2019_3 (1).pdf'
  80K -rwxrwxrwx 1 tatyderb tatyderb  77K Nov  4  2019  uved-232718004.pdf
  76K -rwxrwxrwx 1 tatyderb tatyderb  76K Nov  4  2019  tu-37111005.pdf
  76K -rwxrwxrwx 1 tatyderb tatyderb  75K Nov 29  2019 'pay_rub (1).pdf'
  36K -rwxrwxrwx 1 tatyderb tatyderb  35K Jun  1  2020  164.doc
  16K -rwxrwxrwx 1 tatyderb tatyderb  13K Nov 24 17:10 'photo_2020-11-24 17.06.21.jpeg'
 4.0K -rwxrwxrwx 1 tatyderb tatyderb 3.3K May 24  2020  project.c
 4.0K -rwxrwxrwx 1 tatyderb tatyderb 3.3K May 24  2020 'troblem (1).c'
 4.0K -rwxrwxrwx 1 tatyderb tatyderb 3.2K Jun 26  2019  239366_11_text.step
  512 -rwxrwxrwx 1 tatyderb tatyderb  508 Mar 27 12:49  4.2.8.py
    0 -rwxrwxrwx 1 tatyderb tatyderb    8 Mar 28 23:24  res.txt
```

**Напечатайте только те строки (без изменений), где размер файла больше 100К.**

Размер файла - первое число. Буквы обозначают:

* K - kilobyte, 1К = 1024
* M - megabyte, 1M = 1024K
* G - gigabyte, 1G = 1024M

Первый столбец - размер файла.

Подсказка:

* str.**split(maxsplit=-1, sep=None)**
    * `sep` - по какой строке делим. `None` - по пробельным символам (пробел, новая строка, табуляция и так далее).
    * `maxsplit` - делить не более maxsplit раз
    
* **print(аргументы, sep=' ', end='\n')**
        * `sep` что печатаем между аргументами
        * `end` - что печатаем в конце

HEADER
import sys
text = sys.stdin.read()
filename = 'filelist.txt'
with open(filename, 'w') as fd:
    fd.write(text)

TEST
  36K -rwxrwxrwx 1 tatyderb tatyderb  35K Jun  1  2020  164.doc
  58M -rwxrwxrwx 1 tatyderb tatyderb  58M Jun 25  2019  pandoc-2.7.3-windows-x86_64.msi
  76K -rwxrwxrwx 1 tatyderb tatyderb  75K Nov 29  2019 'pay_rub (1).pdf'
1000K -rwxrwxrwx 1 tatyderb tatyderb 997K Nov 18 15:07  7001173624_1605701140381.zip
  16K -rwxrwxrwx 1 tatyderb tatyderb  13K Nov 24 17:10 'photo_2020-11-24 17.06.21.jpeg'
  512 -rwxrwxrwx 1 tatyderb tatyderb  508 Mar 27 12:49  4.2.8.py
 662M -rwxrwxrwx 1 tatyderb tatyderb 662M Jun  1  2019  Anaconda3-2019.03-Windows-x86_64.exe
 320K -rwxrwxrwx 1 tatyderb tatyderb 319K Sep 20  2019 'c2019_3 (1).pdf'
  58M -rwxrwxrwx 1 tatyderb tatyderb  58M Mar 17  2020  MovaviVideoEditorSetupC.exe
  60M -rwxrwxrwx 1 tatyderb tatyderb  60M Mar 18  2020  DiscordSetup.exe
 391M -rwxrwxrwx 1 tatyderb tatyderb 391M Jun 30  2020 'Docker Desktop Installer.exe'
    0 -rwxrwxrwx 1 tatyderb tatyderb    8 Mar 28 23:24  res.txt
 320K -rwxrwxrwx 1 tatyderb tatyderb 319K Mar  1  2020  download.html
 1.1M -rwxrwxrwx 1 tatyderb tatyderb 1.1M Jul 22  2020 'PayApp 2020-07-22 18-13-35.png'
 304M -rwxrwxrwx 1 tatyderb tatyderb 304M Jan  2  2020  LibreOffice_6.3.4_Win_x64.msi
 4.0K -rwxrwxrwx 1 tatyderb tatyderb 3.2K Jun 26  2019  239366_11_text.step
  80K -rwxrwxrwx 1 tatyderb tatyderb  77K Nov  4  2019  uved-232718004.pdf
 4.0K -rwxrwxrwx 1 tatyderb tatyderb 3.3K May 24  2020 'troblem (1).c'
 467M -rwxrwxrwx 1 tatyderb tatyderb 467M Jul  1  2020  Anaconda3-2020.02-Windows-x86_64.exe
 996K -rwxrwxrwx 1 tatyderb tatyderb 996K Nov 18 14:57  7001173624_1605700280816.zip
 4.0K -rwxrwxrwx 1 tatyderb tatyderb 3.3K May 24  2020  project.c
  76K -rwxrwxrwx 1 tatyderb tatyderb  76K Nov  4  2019  tu-37111005.pdf
----
58M pandoc-2.7.3-windows-x86_64.msi
1000K 7001173624_1605701140381.zip
662M Anaconda3-2019.03-Windows-x86_64.exe
320K 'c2019_3 (1).pdf'
58M MovaviVideoEditorSetupC.exe
60M DiscordSetup.exe
391M 'Docker Desktop Installer.exe'
320K download.html
1.1M 'PayApp 2020-07-22 18-13-35.png'
304M LibreOffice_6.3.4_Win_x64.msi
467M Anaconda3-2020.02-Windows-x86_64.exe
996K 7001173624_1605700280816.zip
====
 996K -rwxrwxrwx 1 tatyderb tatyderb 996K Nov 18 14:57  7001173624_1605700280816.zip
 4.0K -rwxrwxrwx 1 tatyderb tatyderb 3.3K May 24  2020  project.c
  76K -rwxrwxrwx 1 tatyderb tatyderb  76K Nov  4  2019  tu-37111005.pdf
----
996K 7001173624_1605700280816.zip
====

## TASKINLINE add_path

Задача в разработке

TEST
1
----
1
====

## TASKINLINE Разбор URL

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
* path (to file) - путь (к файлу) - не обязательное поле
* parameters - параметры - не обязательное поле
* anchor - якорь - не обязательное поле

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

Напишите функцию **parse_url(url)**. Она разбирает **url** и возвращает кортеж (протокол, доменное имя, порт, путь к файлу, параметры, якорь).

Якорь хранится вместе с `#` в начале строки.

```python
url = 'http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument'
protocol, host, port, path, parameters, anchor = parse_url(url)
assert protocol == 'http'
assert host == 'www.example.com'
assert port == '80'             # this is string now!
assert path == '/path/to/myfile.html'
assert parameters = 'key1=value1&key2=value2'
assert anchor == 'SomewhereInTheDocument'
```

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
def parse_url(url):
    # тут нужно написать код

url = input().strip()   # не нужны пробелы в конце!
protocol, host, port, path, parameters, anchor = parse_url(url)
print(f'protocol=[{protocol}]')
print(f'host    =[{host}]')
print(f'port    =[{port}]')
print(f'path    =[{path}]')
print(f'params  =[{parameters}]')
print(f'anchor  =[{anchor}]')

TEST
http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument
----
protocol=[http]
host    =[www.example.com]
port    =[80]
path    =[/path/to/myfile.html]
params  =[key1=value1&key2=value2]
anchor  =[SomewhereInTheDocument]
====
http://acm.mipt.ru/twiki/bin/view/Cintro/PythonList4#___qmc_join_rq_ngfq_c_gn_pq_____
----
protocol=[http]
host    =[acm.mipt.ru]
port    =[]
path    =[/twiki/bin/view/Cintro/PythonList4]
params  =[]
anchor  =[___qmc_join_rq_ngfq_c_gn_pq_____]
====
ftp://192.168.1.11:2021/Downloads/solution.py
----
protocol=[ftp]
host    =[192.168.1.11]
port    =[2021]
path    =[/Downloads/solution.py]
params  =[]
anchor  =[]
====
http://judge2.vdi.mipt.ru/cgi-bin/new-master?SID=3fc61087336ebefe&action=2
----
protocol=[http]
host    =[judge2.vdi.mipt.ru]
port    =[]
path    =[/cgi-bin/new-master]
params  =[SID=3fc61087336ebefe&action=2]
anchor  =[]
====
https://stepik.org/edit-lesson/515807/step/3
----
protocol=[https]
host    =[stepik.org]
port    =[]
path    =[/edit-lesson/515807/step/3]
params  =[]
anchor  =[]
====
ftp://acm.mipt.ru/twiki/pub/Cintro/WebHome/C_beginff.pdf
----
protocol=[ftp]
host    =[acm.mipt.ru]
port    =[]
path    =[/twiki/pub/Cintro/WebHome/C_beginff.pdf]
params  =[]
anchor  =[]
====
http://stepik.org/
----
protocol=[http]
host    =[stepik.org]
port    =[]
path    =[/]
params  =[]
anchor  =[]
====


