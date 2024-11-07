# Разбор аргументов командной строки с помощью пакета click
## Что такое аргументы командной строки и зачем они нужны

**CLI** - command line interface - интерфейс для запуска программы из командной строки.

Команда `ls` в терминале UNIX (wsl) - показать содержимое директории или информации о файле. У нее могут быть параметры.

```python
$ ls
cpython  devguide  prog.py  pypy  rm-unused-function.patch
$ ls pypy
ctypes_configure  demo  dotviewer  include  lib_pypy  lib-python ...
$ ls -l
total 20
drwxr-xr-x 19 wena wena 4096 Feb 18 18:51 cpython
drwxr-xr-x  4 wena wena 4096 Feb  8 12:04 devguide
-rwxr-xr-x  1 wena wena  535 Feb 19 00:05 prog.py
drwxr-xr-x 14 wena wena 4096 Feb  7 00:59 pypy
-rw-r--r--  1 wena wena  741 Feb 18 01:01 rm-unused-function.patch
$ ls --help
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
...
```

* Можно запускать команду без параметров, она покажет содержимое текущей директории. То есть **значение по умолчанию** - текущая директория.
* **Позиционный аргумент** - имя директории, которую мы просматриваем. Программа решает что делать с аргументом на основе того, _где_ он появился в командной строке. Так в команде `cp src dst` первый аргумент - что копируем, второй аргумент - куда копируем.
* `-l` может появиться, а может и нет. **Опциональный аргумент** (option). 
  * Возможна склейка аргументов, т.е. либо вызов `ls -l -a`, либо `ls -la`.
  * опциональные аргументы возможно записать в короткой `-s` или полной `--size` форме.
* есть хелп, запускается `ls --help`

У `git` есть возможность работы в командной строке. Например, commit указанных файлов с сообщением задается так:
```
git commit -m 'Несколько лам в руке считаются как одна лама' rules.md hand.py
```
Взять данные из удаленного репозитория:
```
git checkout https://github.com/tatyderb/3415_uno.git uno
```
В этом случае дальнейшие аргументы зависят от выбранной команды git, то есть от первого аргумента.

### Аргументы командной строки в вычислительных задачах

В вычислительных задачах аргументов обычно два: файл с данными и файл конфигурации, потому что аргументов можно задавать много и хорошо бы хранить историю с какими аргументами был запущен рассчет, то есть сохранять данные, результат и полностью конфигурацию запуска, что удобно, если вся конфигурация описана в файле.

## Пакеты для разбора аргументов командной строки

* [argparse](https://docs.python.org/3/library/argparse.html)
    * Плюс: содержится в стандартной библиотеке, то есть не надо дополнительно ставить.
    * https://github.com/tatyderb/python_express_course/blob/master/chapter_stdlib/argparse.md - лекция про argparse
* [click](https://click.palletsprojects.com/) - урок про него
    * [Глава "Модуль click"](https://advpyneng.readthedocs.io/ru/latest/book/04_click/index.html) из книги "Advanced Python для сетевых инженеров" (на русском).
* [Сравнение популярных CLI-библиотек для Python: click, cement, fire и другие](https://habr.com/ru/articles/466999/) - статья на habr.

## Тестирование CLI с помощью pytest (без click)

1. вызывать программу с аргументами командной строки
2. проверять, что она печатает на stdout и stderr
3. проверять код возврата программы

### Программа, которую будем тестировать (пока без разбора аргументов)

Напишем простую программу, которая будет печатать все аргументы командной строки. И еще какой-нибудь текст. Например:

```python
# файл hello.py
import sys

def main(args):
    first, *params = args
    
    print(f'Выполнили команду {first} с аргументами {params}')

if __name__ == '__main__':
    main(sys.argv[1:])   # sys.argv[0] это hello.py
```
Запустим ее вручную с аргументами:
```
python hello.py mytest 123 4.12
```
Напечатает
```
Выполнили команду mytest с аргументами ['123', '4.12']
```

### Тестирование, что печатает программа с помощью pytest. capsys

Для перехвата печати тестируемой программы на stdout и stderr во время тестов используют фикстуру **capsys**.

```python
# файл test_hello.py
import hello

EXPECTED = "Выполнили команду mytest с аргументами ['123', '4.12']\n"

def test_hello_arguments(capsys):
    hello.main(['mytest', '123', '4.12'])  # все аргументы должны быть строками
    out, _ = capsys.readouterr()
    assert out == EXPECTED
```
Запуск
`pytest --capture=sys test_hello.py`

**С click тестировать будет проще!**

## click быстрый старт

Напишем программу, которая здоровается с указанным именем `name`, повторяет приветствие `count` раз. Пока без click.

```python
def hi(name: str, count: int):
    """Печатаем приветствие count раз"""
    for _ in range(count):
        print(f"Здравствуй, {name}!")

if __name__ == '__main__':
    name = 'Tanya'
    hi(name, count=3)
```
Пока никакого разбора аргументов. Все прибито гвоздями.

**Click работает через декораторы**.

* У программы автоматически появляется help.
* Есть значение по умолчанию, заданное в `default`.
* Без аргументов вводится приглашение на ввод имени, используется параметр `prompt`.
* Порядок опциональных аргументов `--count` и `--name` может быть любой.
* Есть полная форма `--count` и краткая `-c`.

```python
import click

@click.command()
@click.option('--count', '-c', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
```
Запускаем и проверяем.

У программы автоматически появляется help.
```
>python hi_click.py --help
Usage: hi_click.py [OPTIONS]

  Simple program that greets NAME for a total of COUNT times.

Options:
  --count INTEGER  Number of greetings.
  --name TEXT      The person to greet.
  --help           Show this message and exit.
```

Есть значение по умолчанию, заданное в `default`.

Без аргументов вводится приглашение на ввод имени, используется параметр `prompt`.
```
python hi_click.py
Your name: Bob
Hello Bob!
```

Опциональные аргументы идут в любом порядке, для count задана полная и краткая форма. То есть все эти варианты напечатают `Hello Bob!` два раза:

* `python hi_click.py --name Bob --count 2`
* `python hi_click.py --count 2 --name Bob`
* `python hi_click.py -c 2 --name Bob`

### Опции или аргументы?

Если мы хотим, чтобы имя всегда указывали в командной строке без всяких `--name`, то это не опция, а аргумент.

```python
@click.command()
@click.option('--count', '-c', default=1, help='Number of greetings.')
@click.argument('name')
def hello(count, name):
    """
    Печатает Hello, NAME! повторяя это count раз.
    """
    ...
```
Изменится вызов, мы не указываем `--name`, а указываем сразу имя

`python hi_click.py --count 2 Bob`

Изменится так же help:
```
>python hi_click.py --help
Usage: hi_click.py [OPTIONS] NAME

  Печатает Hello, NAME! повторяя это count раз.

Options:
  -c, --count INTEGER  Number of greetings.
  --help               Show this message and exit.
```

#### Доступно только опциям

* апрос ввода значения опции у пользователя
* опции могут использоваться как флаги
* значения опций можно считывать из переменных окружения с автоматическим префиксом
* опциям можно писать help

Возможности доступные только в аргументах:

* передача любого количества значений

### click.echo или print?

Чем отличается `click.echo` от `print`?

* `click.echo` пытается работать корректно даже в недоопределенном окружении. То есть сам скорректирует вывод, а не кинет, например, ошибку UnicodeError.
* поддержка цветов и стилей, на Windows она автоматически включена и используется. См. больше в [ANSI colors](https://click.palletsprojects.com/en/stable/utils/#ansi-colors)

## Аргументы, класс click.Argument

* Рекомендуется использовать для команд (commit, add и тп в git), имен файлов (пути), URL.
* [Документация](https://click.palletsprojects.com/en/stable/documentation/#documenting-arguments)

`@click.argument(name, type=None, required=True, default=None, nargs=None)`

* **name** - название аргумента, его можно дальше использовать в коде
* **type** - о типах поговорим позже, можно поставить ограничение, что указывать только целые числа, например
* **required** - обязательный аргумент или нет (В `ls` имя директории - не обязательный аргумент)
* **default** - значение по умолчанию, если аргумент не задан
* **nagrs** - ожидаемое количество аргументов,
    *  `-1` - специальное значение, означает "произвольное количество аргументов".

`@click.argument("name", nargs=-1, required=True)` - можно задать много аргументов, но хотя бы один задать надо. То есть 1 или более аргументов.

## Опции, класс click.Option

Все, что не аргумент, делайте опцией.

```
class click.Option(
    param_decls=None,
    show_default=False,
    prompt=False,
    confirmation_prompt=False,
    hide_input=False,
    is_flag=None,
    flag_value=None,
    multiple=False,
    count=False,
    allow_from_autoenv=True,
    type=None,
    help=None,
    hidden=False,
    show_choices=True,
    show_envvar=False,
    **attrs
)
```

### Имена опций

* `@click.option("-f", "--foo-bar")`, имя параметра функции будет `"foo_bar"`
* `@click.option("-x")`, имя `"x"`
* `@click.option("-f", "--filename", "dest")`, имя `"dest"`
* `@click.option("--CamelCase")`, имя `"camelcase"`
* `@click.option("-f", "-fb")`, имя `"f"`
* `@click.option("--f", "--foo-bar")`, имя `"f"`
* `@click.option("---f")`, имя `"_f"`

### prompt - запрос значения у пользователя

* Запрос выполняется только если в опции не указано значение
* Параметр `hide_input` позволяет скрывать вводимое значение.

```
@click.command()
@click.option("--username", "-u", prompt="Your name")
@click.option("--password", "-p", prompt=True, hide_input=True)
@click.option("--secret", "-s", prompt=True, hide_input=True)
def cli(username, password, secret):
    pass
```

### Переменные окружения

* Если не указано в аргументах, значение берется из переменной окружения (см. `MERCHANT_KEY`)
* Если вместе с `prompt`, то если нет ни в аргументах, ни в переменных окружения, запрашивается у пользователя (см. `username`)
    * `hide_input` так же позволяет скрыть вводимое значение

```
@click.command()
@click.option("--merchantkey", "-k", envvar="MERCHANT_KEY")
@click.option("--username", "-u", envvar="NET_USER", prompt=True)
@click.option("--password", "-p", envvar="NET_PASSWORD", prompt=True, hide_input=True)
@click.option("--secret", "-s", envvar="NET_SECRET", prompt=True, hide_input=True)
def cli(username, password, secret):
    pass
```

### Флаг

`@click.option("--show-all", "-a", is_flag=True, help="show db content")`

### Подтверждение ввода

Второй раз просят ввести те же данные и введенные значения сравниваются. Должны быть идентичными.

**Для ввода пароля используйте `@click.password_option`, а не `@click.option`**

То же самое, что `@click.password_option`:
```python
@click.option("--password", "-p", prompt=True, hide_input=True, confirmation_prompt=True)
```
Использование:
```python
@click.command()
@click.option("--username", "-u", prompt=True)
@click.password_option()
def cli(username, password):
    print(username, password)
```

## Type

* Кроме поддерживаемых типов, можно описать [свои типы данных](https://click.palletsprojects.com/en/7.x/parameters/#implementing-custom-types)
* базовые типы: `str`, `int`, `float`, `bool`
* `click.File` - специальный тип, который автоматически открывает и закрывает файл. Возвращает открытый файл
* `click.Path` - тип для проверки пути, файл это или каталог и подобного. Возвращает строку, не открытый файл
* `click.Choice` - набор допустимых значений
* `click.IntRange` - диапазон числовых значений
* `click.DateTime` - преобразует строку с датой в объект datetime

### Базовые типы: str, int, float, bool

Указываем, что опция `-c` должна быть строго целым числом. (Сами будете проверять, что оно не отрицательное.)

`@click.option("--count", "-c", type=int, help="Number of greetings")`

### click.File - возвращает открытый файл

`click.File(mode='r', encoding=None, errors='strict', lazy=None, atomic=False)`

* Поддерживает значение `-`, которое `stdin` или `stdout`, в зависимости от значения `mode`
* `lazy` - открывать сразу же или только при первой попытке I/O.
* `atomic` - версия Click 2.0 и выше, пишем в другой файл в той же директории, что и оригинальный, и только по окончанию записи оригинальный файл одномоментно заменяется этим другим файлом; другой файл уничтожается (то есть не copy, а move).
* [документация](https://click.palletsprojects.com/en/stable/arguments/#file-args) 

### click.Path - строка, а не открытый файл

`click.Path(exists=False, file_okay=True, dir_okay=True, writable=False, readable=True, resolve_path=False, allow_dash=False, path_type=None, executable=False)`

* `exists (bool)` – Файл или директория существуют. Если `exists=False`, то остальные проверки молча пропускаются.
* `file_okay (bool)` – Allow a file as a value.
* `dir_okay (bool)` – Allow a directory as a value.
* `readable (bool)` – if true, a readable check is performed.
* `writable (bool)` – if true, a writable check is performed.
* `executable (bool)` – if true, an executable check is performed.
* `resolve_path (bool)` – Make the value absolute and resolve any symlinks. A `~` is not expanded, as this is supposed to be done by the shell only.
* `allow_dash (bool)` – Allow a single dash as a value, which indicates a standard stream (but does not open it). Use `open_file()` to handle opening this value.
* `path_type (Type[Any] | None)` – Convert the incoming path value to this type. If None, keep Python’s default, which is `str`. Useful to convert to `pathlib.Path`.

### click.Choice - выбор из списка опций

`click.Choice(choices, case_sensitive=True)`

Пример выбора из 'MD5' или 'SHA1' без учета регистра:
```
@click.option('--hash-type',
              type=click.Choice(['MD5', 'SHA1'], case_sensitive=False))
```

### click.IntRange, click.FloatRange - диапазоны чисел

```
click.IntRange(min=None, max=None, min_open=False, max_open=False, clamp=False)
click.FloatRange(min=None, max=None, min_open=False, max_open=False, clamp=False)
```
* `min`, `max` - границы снизу и сверху, включая указанные
* `min_open`, `max_open` - границы снизу и сверху, НЕ включая указанные
* если ограничение не указано, то любые числа в этом направлении
* `clamp=True` - если число вышло за границу, то не ошибка, а используем граничное значение

Пример:
```python
@click.command()
@click.option("--count", type=click.IntRange(0, 20, clamp=True))
@click.option("--digit", type=click.IntRange(0, 9))
def repeat(count, digit):
    click.echo(str(digit) * count)
```
Аргументы и результат (при count=100 используется граница 20):
```
repeat --count=100 --digit=5
55555555555555555555
repeat --count=6 --digit=12
Usage: repeat [OPTIONS]
Try 'repeat --help' for help.

Error: Invalid value for '--digit': 12 is not in the range 0<=x<=9.
```

## Валидация входных данных или как задавать кубики 1d6

[Документация](https://click.palletsprojects.com/en/stable/options/#callbacks-for-validation)

```python
def validate_rolls(ctx, param, value):
    if isinstance(value, tuple):
        return value

    try:
        rolls, _, dice = value.partition("d")
        return int(dice), int(rolls)
    except ValueError:
        raise click.BadParameter("format must be 'NdM'")

@click.command()
@click.option(
    "--rolls", type=click.UNPROCESSED, callback=validate_rolls,
    default="1d6", prompt=True,
)
def roll(rolls):
    sides, times = rolls
    click.echo(f"Rolling a {sides}-sided dice {times} time(s)")
```
Пример вызова:
```
roll --rolls=42
Usage: roll [OPTIONS]
Try 'roll --help' for help.

Error: Invalid value for '--rolls': format must be 'NdM'

roll --rolls=2d12
Rolling a 12-sided dice 2 time(s)

roll
Rolls [1d6]: 42
Error: format must be 'NdM'
Rolls [1d6]: 2d12
Rolling a 12-sided dice 2 time(s)
```

## Большие приложения (команды и пересечение аргументов команд)

Если у нас в параметрах программы есть понятие "команда и ее аргументы". Например, CLI git.

```
git config –global user.name "Ivanov Ivan"
git clone git@github.com:tatyderb/3415_uno.git uno
```
и так далее, аргументы с одной стороны зависят от команды, с другой стороны, у двух разных команд могут быть аргументы с одинаковым именем.

### click.group

Как организовать описание аргументов в этом случае? Это называется [nesting commands](https://click.palletsprojects.com/en/stable/quickstart/#nesting-commands) (вложенные команды).

* Пишем группу `@click.group`, имя функции - это название группы.
* `@группа.command` пишем с этим именем группы. Имя функции - это название команды.

В примере ниже группа `pomodoro_cli` с командами `stats` и `work`.

```python
import click

@click.group()
def pomodoro_cli():
    pass

@pomodoro_cli.command()
@click.option("--day", "-d", is_flag=True)
@click.option("--week", "-w", is_flag=True)
@click.option("--month", "-m", is_flag=True)
def stats(day, week, month):
    print("STATS")

@pomodoro_cli.command()
@click.option("--pomodoros_to_run", "-r", default=5, show_default=True, type=int)
@click.option("--work_minutes", "-w", default=25, show_default=True, type=int)
@click.option("--short_break", "-s", default=5, show_default=True, type=int)
@click.option("--long_break", "-l", default=30, show_default=True, type=int)
@click.option("--set_size", "-p", default=4, show_default=True, type=int)
def work(pomodoros_to_run, work_minutes, short_break, long_break, set_size):
    pass

if __name__ == "__main__":
    pomodoro_cli()
```
В общем хэлпе перечисляются команды, и у каждой команды есть свой хелп для рассказа об её аргументах.

Хэлп всей программы:
```
$ python example_10_click_group_basics.py --help
Usage: example_10_click_group_basics.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  stats
  work
```
Хэлп одной команды `stats`:
```
$ python example_10_click_group_basics.py stats --help
Usage: example_10_click_group_basics.py stats [OPTIONS]

Options:
  -d, --day
  -w, --week
  -m, --month
  --help       Show this message and exit.
```

#### Отложенная регистрация команды

В примере сначала описывалась группа, потом описывалась команда как принадлежащая этой группе.

Можно сначала описать команды, потом с помощью `группа.add_command(команда)` зарегистрировать команду в группе:
```python
@click.command()
def greet():
    click.echo("Hello, World!")

@click.group()
def group():
    pass

group.add_command(greet)
```

### click.pass_context - общие аргументы у разных команд

[click.pass_context](https://advpyneng.readthedocs.io/ru/latest/book/04_click/complex.html#click-pass-context)

Общие параметры можно объединить в группу. Передать значение этих параметров в разные команды можно через контекст, используя `click.pass_context`.

Обратите внимание на порядок аргументов и их названия.
```python
import click


@click.group()
@click.option("--db-filename", "-n", help="db filename")
@click.pass_context
def dhcp_db(context, db_filename):
    context.obj = {"db_filename": db_filename}


@dhcp_db.command()
@click.option("--db-schema", "-s", help="db schema filename")
@click.pass_context
def create(context, db_schema):
    """
    create DB
    """


@dhcp_db.command()
@click.argument("filename", nargs=-1, required=True)
@click.option("--switch-data", "-s", default=False, is_flag=True)
@click.pass_context
def add(context, filename, switch_data):
    """
    add data to db from FILENAME
    """


@dhcp_db.command()
@click.option("--key", "-k", type=click.Choice(["mac", "ip", "vlan"]))
@click.option("--value", "-v", help="value of key")
@click.option("--show-all", "-a", is_flag=True, help="show db content")
@click.pass_context
def get(context, key, value, show_all):
    """
    get data from db
    """


if __name__ == "__dhcp_db__":
    dhcp_db()
```