# pathlib

* `os` - старый подход к работе с путями
* `pathlib` - новый подход, через класс `Path`
* [документация на русском](https://docs-python.ru/standart-library/modul-pathlib-python/)

## Проблема - зависимость от ОС

|      | Windows                                                    | Unix/Mac                                             |
|------|------------------------------------------------------------|------------------------------------------------------|
| путь | `C:\Users\taty\PycharmProjects\demo_import`                | `/home/taty/PycharmProjects/demo_import`             |
| PATH | `C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem`  | `/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin` | |

* Путь, корень (с него начинается абсолютный путь)
  * `C:`
  * `/`
* Путь, разделитель
  * `\`
  * `/`
* Переменная PATH (список путей для поиска в них)
  * через `;`
  * через `:`
* Общее:
  * `.` - текущая директория
  * `..` - директория уровнем выше

Python - кроссплатформенный язык, нужно уметь работать с любыми путями.

**Не хардкордте в коде абсолютные пути!** На другом компьютере может не быть `C:\Users\taty\myproject`

## Иерархия классов

![Path](https://docs.python.org/3/_images/pathlib-inheritance.png)

![Path](https://www.freecodecamp.org/news/content/images/2022/04/pathlib-diagram.png)

* `Pure*Path` - класс для манипуляции с путями, при этом сама директория или файл не создается (идея директории или файла)
* `*Path` - добавили операции для чтения/записи, то есть изменения объекта на диске.

В зависимости от того, на какой ОС работает этот код, он вернет объект `PureWindowsPath` или `PurePosixPath`

`pathlib.PurePath('setup.py')`

| ОС       | Результат |
|----------|----|
| Windows  | `PureWindowsPath('myfile.txt')`   |
| Unix/Mac |  `PurePosixPath('myfile.txt')`    |

То есть вы используете "общие классы" `PurePath` или `Path`. 
И при выполнении, в зависимости от текущей ОС, создаются экземпляры для данной ОС.

Можно создавать экземпляры классов `PureWindowsPath` и `PurePosixPath` самому? Можно. Но если вы ошибетесь с текущей ОС, получите исключение.

`NotImplementedError: cannot instantiate 'WindowsPath' on your system`

## Методы класса

### cwd() - current working directory (текущая рабочая директория)

```python
# pathlib_part\cwd.py
from pathlib import Path
print(Path.cwd())
```
Директория, откуда запускали скрипт.
```
C:\Users\taty\PycharmProjects\demo_import>python pathlib_part\cwd.py
C:\Users\taty\PycharmProjects\demo_import
```

### home() - домашняя директория

```python
# pathlib_part\cwd.py
from pathlib import Path

print('cwd', Path.cwd())
print('home', Path.home())
```

```commandline
C:\work\courses_my\_python_myanmar\lectures>python C:\Users\taty\PycharmProjects\demo_import\pathlib_part\cwd.py
cwd C:\work\courses_my\_python_myanmar\lectures
home C:\Users\taty
```

## Передаем строку как путь

`\n` и `\t` - escape последовательности (новая строка и табуляция). Поэтому написать

* `'C:\Users\natasha\tasks\t1.py'` - будут части пути трактоваться как `\n` и `\t`
* `r'C:\Users\natasha\tasks\t1.py'` - так не будут трактоваться
* `'C:\\Users\\natasha\\tasks\\t1.py'` - и так мы экранируем каждую `\`

```python
>>> import pathlib
>>> p = pathlib.Path(r'C:\Users\taty\PycharmProjects\demo_import\pathlib_part\cwd.py')
>>> p
WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part/cwd.py')
>>> str(p)
'C:\\Users\\taty\\PycharmProjects\\demo_import\\pathlib_part\\cwd.py'
```
Можно ли такой путь передать в Path сразу? Да.
```python
>>> p1 = pathlib.Path('C:/Users/taty/PycharmProjects/demo_import/pathlib_part/cwd.py')
>>> p1
WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part/cwd.py')
```

[POSIX](https://en.wikipedia.org/wiki/POSIX) - Portable Operating System Interface - стандарт поддержки совместимости между ОС.

## Собираем путь из частей

Переопределен оператор `/`

* `Path.home().joinpath("python", "scripts", "test.py")`
* `Path.home() / 'python' / "scripts" / "test.py"`

Пример:
```python
>>> h = pathlib.Path.home()
>>> h / 'PycharmProjects/demo_import'
WindowsPath('C:/Users/taty/PycharmProjects/demo_import')
>>> h / 'PycharmProjects' / 'demo_import'
WindowsPath('C:/Users/taty/PycharmProjects/demo_import')
>>> h / 'PycharmProjects\\demo_import'
WindowsPath('C:/Users/taty/PycharmProjects/demo_import')
```

## `resolve()` - выкинуть из пути лишнее

* `..` и `.` в середине пути
* симлинки

```python
>>> pp
WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part')
>>> p3 = pp / '..' / '..' / 'myfile.txt'
>>> p3
WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part/../../myfile.txt')
>>> p3.resolve()
WindowsPath('C:/Users/taty/PycharmProjects/myfile.txt')
```

## Разбираем на пути

* `__file__` - путь в виде строки к файлу с кодом
* `p.parent` - директория (если `p` - файл) или директория уровнем выше (если `p` - директория)
* `list(p.parents)` - список директорий от самой полной до корня

```python
>>> p
WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part/cwd.py')
>>> p.parent
WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part')
>>> p.parents
<WindowsPath.parents>
>>> list(p.parents)
[WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part'), 
 WindowsPath('C:/Users/taty/PycharmProjects/demo_import'), 
 WindowsPath('C:/Users/taty/PycharmProjects'), 
 WindowsPath('C:/Users/taty'), 
 WindowsPath('C:/Users'), 
 WindowsPath('C:/')]
>>> p.parts
('C:\\', 'Users', 'taty', 'PycharmProjects', 'demo_import', 'pathlib_part', 'cwd.py')
```

## Части пути

```python
>>> p
WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part/cwd.py')
>>> p.drive
'C:'
>>> p.root
'\\'
>>> p.anchor   # p.drive + p.root
'C:\\'
>>> p.name
'cwd.py'
>>> p.suffix
'.py'
>>> p.suffixes
['.py']
>>> p.stem
'cwd'
```

## Проверки

### `is_absolute_path` - абсолютный путь

```python
>>> PurePosixPath('/a/b').is_absolute()
True
>>> PurePosixPath('a/b').is_absolute()
False

>>> PureWindowsPath('c:/a/b').is_absolute()
True
>>> PureWindowsPath('/a/b').is_absolute()
False
>>> PureWindowsPath('c:').is_absolute()
False
>>> PureWindowsPath('//some/share').is_absolute()
True
```

### `is_relative_to(path)` - относительно пути

```python
>>> p
WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part/cwd.py')
>>> p.is_relative_to('taty')
False
>>> p.is_relative_to('C:/Users/taty')
True
>>> p.is_relative_to('C:/work')
False
```

### `match(шаблон)` - соответствие шаблону 

```python
>>> PurePath('/src/goo/scripts/main.py').match('*.py')
True
>>> PurePath('/src/goo/scripts/main.py').match('goo/*.py')
True
>>> PurePath('src/goo/scripts/main.py').match('/*.py')
False
```

### Существует, файл, директория

```python
>>> p
WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part/cwd.py')
>>> p.exists()
True
>>> p.is_file()
True
>>> p.is_dir()
False
```

## Замена имени, суффикса

```python
>>> p
WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part/cwd.py')
>>> p.with_name('new_file.md')
WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part/new_file.md')
>>> p.with_suffix('.txt')
WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part/cwd.txt')
>>> p.with_stem('commands')
WindowsPath('C:/Users/taty/PycharmProjects/demo_import/pathlib_part/commands.py')
```

## `os` и `pathlib`

| os and os.path | pathlib                                  |
|----|------------------------------------------|
| os.path.abspath() | Path.absolute() за исключением симлинков |
| os.path.realpath() | Path.resolve() |
| os.chmod() | Path.chmod() |
| os.mkdir() | Path.mkdir() |
| os.makedirs() | Path.mkdir() |
| os.rename() | Path.rename() |
| os.replace() | Path.replace() |
| os.rmdir() | Path.rmdir() |
| os.remove(), os.unlink() | Path.unlink() |
| os.getcwd() | Path.cwd() |
| os.path.exists() | Path.exists() |
| os.path.expanduser() | Path.expanduser() and Path.home() |
| os.listdir() | Path.iterdir() |
| os.walk() | Path.walk() |
| os.path.isdir() | Path.is_dir() |
| os.path.isfile() | Path.is_file() |
| os.path.islink() | Path.is_symlink() |
| os.link() | Path.hardlink_to() |
| os.symlink() | Path.symlink_to() |
| os.readlink() | Path.readlink() |
| os.path.relpath() | PurePath.relative_to() |
| os.stat() | Path.stat(), Path.owner(), Path.group() |
| os.path.isabs() | PurePath.is_absolute() |
| os.path.join() | PurePath.joinpath() |
| os.path.basename() | PurePath.name |
| os.path.dirname() | PurePath.parent |
| os.path.samefile() | Path.samefile() |
| os.path.splitext() | PurePath.stem and PurePath.suffix |

## Чтение и запись в файл

* Чтение: `Path.read_text()` и `Path.read_bytes()`;
* Запись: `Path.write_text()` и `Path.write_bytes()`;

## Создание файла и директорий

**Создание экземпляра класса `Pure*Path` или `Path` не означает, что создается такой файл или директория**. 
Их надо создавать отдельно.

* Параметры `mkdir`:
  * Если значение `parents = True`, то метод создаст родительские каталоги (при их отсутствии). Если False, то вернет ошибку при их отсутствии.
  * If `exist_ok` is false (the default), FileExistsError is raised if the target directory already exists.

```python
>>> CreateExample 
WindowsPath('C:/Users/Blog/Timeweb/Cloud/Pathlib/file.txt')
>>> CreateExample.is_dir()   # Есть ли такая директория?
False
>>> CreateExample.mkdir(parents = True, exist_ok = True)         
>>> CreateExample.is_dir()   # теперь есть такая директория, ее можно увидеть в других программах     
True
>>> CreateExample.rmdir()    # удалили диреторию                       
>>> CreateExample.touch()    # создали файл с таким именем (существует на диске)                           
>>> CreateExample.is_file()  # это файл?
True
```

## `__file__` - текущий файл

У каждого файла эта переменная имеет свое значение.

```python
import sys, pathlib

sys.path.append(str(pathlib.Path(__file__).resolve()))      # insert(0)
```



