# Дата и время

* **Epoch** - 1 января 1970, с этого момента ведется летоисчисление в компьютерах.
* **timestamp** - всего секунд с 1 января 1970.

## модуль `datetime`

* Получить текущие дату и время
* Сравнение и арифметические операции
* Преобразование в строку и из строки

| Тип данных | Для чего                                    |
|----|---------------------------------------------|
| `data` | Дата (без времени), Грегорианский календарь |
| `time` | Время (без даты)                            |
| `datetime` | Дата и время, Грегорианский календарь       |
| `timedelta` | Разница между двумя моментами               |
| `tzinfo` | Часовой пояс                                |
| `timezone` | Время по UTC |

### datetime.date - дата (без времени) по Григорианскому календарю

```python
from datetime import date

my_date = date(2023, 9, 1)    # тип date: год + месяц + день, все обязательные, валидация
# date(day=1, month=9, year=2023)

print(my_date)          # 2023-09-01
print(type(my_date))    # <class 'datetime.date'>
print(my_date.year)     # 2023
print(my_date.month)    # 9
print(my_date.day)      # 1
```
* `date.today()` - cегодня
* `d.weekday()` - номер дня недели, 0 - понедельник, 6 - воскресенье
* `d.isoweekday()` - номер дня недели, 1 - понедельник, 7 - воскресенье
* `date.min()`  - 1 января 1 года, `MINYEAR=1`
* `date.max()` - 31 декабря 9999 года, `MAXYEAR=9999`
* `d.toordinal()` - int, дней с `date.min()`
* `date.fromordinal(days: int)` - дата из дней с `date.min()`
* 
```python
from datetime import date

d = date.today()        # datetime.date(2024, 5, 28) дата, сегодня
print(d)                # 2024-05-28
print(d.weekday())      # 1 (вторник)
print(d.isoweekday())   # 2 (вторник)

print(d.toordinal())    # 739034

d1 = date.fromordinal(356)
print(d1)               # 0001-12-31
```

#### Сравнение

Работают все операторы сравнения, `min`, `max`, сортировка.

```python
d1 = date(2023, 10, 30)
d2 = date(2024, 6, 11)
d3 = date(2024, 5, 28)
a = [d1, d2, d3]

print(d1 < d2)      # True
print(d1 > d3)      # False
print(min(a))       # 2023-10-30
print(max(a))       # 2024-06-11
print(sorted(a))    # [datetime.date(2023, 10, 30), datetime.date(2024, 5, 28), datetime.date(2024, 6, 11)]
print(*sorted(a))   # 2023-10-30 2024-05-28 2024-06-11
```

* `str(d1)` - `2023-10-30`
* `repr(d1)` - `datetime.date(2023, 10, 30)`

#### unmutable - неизменяемое

Может быть ключами в словаре.

```python
holidays = {
    date(2024, 1, 1): "Новый год",
    date(2024, 1, 7): "Рожество",
    date(2024, 2, 23): "День Советской армии и военно-морского флота",
    date(2024, 3, 8): "Международный женский день"  
}
```

### datetime.time - время (без даты)

* **Микросекунда** = $1 \cdot 10^{-6}$ секунды
* `time(hour=0, minute=0, second=0, microsecond=0)`, валидация
* Атрибуты `hour`, `minute`, `second`, `microsecond`
* сравнение
* неизменяемые (могут быть ключами в словаре)

```python
from datetime import time

t1 = time(11, 40, 37, 12345)     # 11:40:37.012345
t2 = time(minute=32, second=1)   # 00:32:01
print(t2.minute)                 # 32
print(t1)                        # 11:40:37.012345
print(t2)                        # 00:32:01        (да, без микросекунд)

t3 = t2.replace(minute=45)       # заменяет поля, создает новый объект
print(t2)                        # 00:32:01
print(t3)                        # 00:45:01
```

### datetime.datetime

* Дата по Григорианскому календарю вместе со временем. Объединение двух классов `date` и `time`.
* Конструктор `datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0)` и атрибуты.
* `datetime.combine(d: date, t: time) -> datetime`
* `datetime.now()` - локальное время, Москва - UTC+3
* `datetime.utcnow()` - UTC (Coordinated Universal Time) время (Гринвич)
* `x.timestamp()` - таймстемп - секунд с эпохи 1 января 1970 года (00:00:00 UTC), float
* `datetime.fromtimestamp` - из таймстемпа, локальное время, но можно указать таймзону

```python
from datetime import datetime
n = datetime.now()          # datetime.datetime(2024, 5, 28, 9, 28, 43, 339682)
nutc = datetime.utcnow()    # datetime.datetime(2024, 5, 28, 6, 29, 47, 929692)
ts = n.timestamp()          # 1716877723.339682
n2 = datetime.fromtimestamp(ts)     # datetime.datetime(2024, 5, 28, 9, 28, 43, 339682) 
```
* `replace` работает со всеми полями

```python
# TODO переписать, потырен пример
from datetime import datetime

datetime1 = datetime(2024, 10, 6, 10, 12, 45)               # используйте именованные параметры 
datetime2 = datetime1.replace(year=1995, month=12)         
datetime3 = datetime1.replace(day=17, hour=14, minute=37)

print(datetime1)
print(datetime2)
print(datetime3)
```

### Форматы даты и времени 

* По умолчанию дату и время печатают в ISO 8601 формате `YYYY-MM-DD` и `HH:MM:SS` или `HH:MM:SS.ffffff`
* x.`strftime(format)` - из даты/время в строку по формату, **f** - format для date, time, datetime
* cls.`strptime()` - из строки в дату/время, **p** - parse
* x.`isoformat()` - напечатать в формате ISO (и не вспоминать формат какой)
* cls.`fromisoformat(format: str)` - из строки в ISO формате получить дату или время, начиная с 3.7

[Формат](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)

```python
from datetime import date, time, datetime
d = date(2024, 5, 28)
t = time(11, 40, 37, 12345)
f = datetime(year=2024, month=5, day=28, hour=11, minute=40, second=37, microsecond=12345)

d.strftime('%d/%m/%y')      # '28/05/2024'
d.strftime('%A %d, %B %Y')  # 'Tuesday 28, May 2024'
t.strftime('%H.%M.%S')      # '11.40.37'
t.strftime('%H hours, %M minutes, %S seconds')  # '11 hours, 40 minutes, 37 seconds'
f.strftime('%A %d, %B %Y %H-%M')    # 'Tuesday 28, May 2024 11-40'
```
Для печати русских названий сначала надо установить русскую [локаль](https://docs-python.ru/standart-library/modul-locale-python/):
```python
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')      # 'en_EN.UTF-8' - английская
d.strftime('%A %d, %B %Y')  # 'вторник 28, Май 2024'
```

### Из строки в дату и время

```python
my_date = date.fromisoformat('2024-02-28')
my_time = time.fromisoformat('11:40:30')
```
Локаль должна быть соответствующая. 
```python
from datetime import datetime

datetime0 = datetime.strptime('10.08.2034 13:55:59', '%d.%m.%Y %H:%M:%S')
datetime1 = datetime.strptime('10/08/21', '%d/%m/%y')
datetime2 = datetime.strptime('Tuesday 10, August 2021', '%A %d, %B %Y')
datetime3 = datetime.strptime('18.20.34', '%H.%M.%S')
datetime4 = datetime.strptime('2021/08/10', '%Y/%m/%d')
datetime5 = datetime.strptime('10.08.2021 (Tuesday, August)', '%d.%m.%Y (%A, %B)')
datetime6 = datetime.strptime('Year: 2021, Month: 08, Day: 10, Hour: 18.', 'Year: %Y, Month: %m, Day: %d, Hour: %H.')

print(datetime0, datetime1, datetime2, datetime3, datetime4, datetime5, datetime6, sep='\n')
```

В отличие от конструктора, можно сделать `datetime` объект через `strptime` без указания части даты:
```python
from datetime import datetime

d = datetime.strptime('9:00', '%H:%M')
print(d)                                    # 1900-01-01 09:00:00
```

# timedelta - арифметические операции над датой и временем.

* конструктор принимает параметры (по умолчанию все 0)
  * недели (weeks) 
  * дни (days)
  * часы (hours)
  * минуты (minutes)
  * секунды (seconds)
  * миллисекунды (milliseconds)
  * микросекунды (microseconds)
* Аргументы могут быть **отрицательными**
* Атрибуты
  * days, seconds, microseconds - других нет, 0 < seconds < 24*60*60 = 86400
  * x.`total_seconds()`
  
```python
from datetime import timedelta

delta = timedelta(days=7, hours=20, minutes=7, seconds=17)  # datetime.timedelta(days=7, seconds=72437)

print(delta)            # 7 days, 20:07:17
print(type(delta))      # <class 'datetime.timedelta'>
```
Отрицательная дельта
```python
>>> delta1 = timedelta(minutes=-1)
>>> delta1
datetime.timedelta(days=-1, seconds=86340)   # 86400 - 60 sec
>>> print(delta1)
-1 day, 23:59:00

>>> delta2 = timedelta(weeks = -1, seconds = -1)
>>> delta2
datetime.timedelta(days=-8, seconds=86399)
>>> print(delta2)
-8 days, 23:59:59
```
Арифметические операции

```python
>>> d1 = datetime.fromisoformat('2024-05-28 01:02:03')
>>> d2 = datetime.fromisoformat('2024-05-28 01:02:13')
>>> d1 < d2
True
>>> d2 - d1
datetime.timedelta(seconds=10)
>>> d1 - d2
datetime.timedelta(days=-1, seconds=86390)
```
* Складывать, вычитать timedelta и timedelta, timedelta и datetime
* Умножать и делить timedelta на число
* abs(timedelta)