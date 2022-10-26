# Space invaders (simple)

lesson = 784099
lang = python

## О чем модуль

Опишем этапы разработки игры space invaders, используя библиотеку pygame.

Закрепим базовый синтаксис и рассмотрим как **улучшает код его разбивка на функции**.

*Один игрок. Один враг. Одна пуля.*

Подробную информацию о pygame на русском языке можно найти в курсе [Pygame. Введение в разработку игр на Python](https://younglinux.info/pygame/). В нашем курсе игры не цель, а средство изучения языка. Поэтому мы не будем углубляться в работу функций и методов, а кратко описывать только нужную нам функциональность.

### План, если вы проводите live coding.

1. Подготовка.
2. Черное окно
   * import pygame
   * pygame.init()
   * размеры окна и запуск черного окна.
   * реакция на нажатие `Х`
   * декорация окна - заголовок и иконка.
3. Игрок
    * загружаем изображение,
    * x, y, width, height
    

## Подготовка

Если вы *показываете* live coding, то позаботьтесь, чтобы ваш код могли взять с задержкой максимум 10-20 строк. Не полагайтесь на хороший интернет у всех сторон.

1. Создадим проект games_pygame на github и клонируем его локально.
2. Создали папку space_invaders_simple
3. Создаем проект в Pycharm
    * добавляем папку games_pygame в проект 
        * Files / Settings / Project [games_pygame] / Project structure
        * Добавляем папку с репозиторием (жмем на +)
        * Удаляем другую ненужную папку.
4. Преподаватель: создаем директорию 
    * space_invaders_simple/resource
    * space_invaders_simple/resource/img
    * space_invaders_simple/resource/audio
    * копируем туда файлы
    * git add, commit, push
4. Студенты: кладем файлы ресурсов из [zip файла](https://stepik.org/media/attachments/lesson/784099/resources_silent.zip) или из директории `space_invaders_simple` запускаем `git pull`.

5. Установка модуля pygame (выберите один из вариантов).
    1. написать import pygame, оно подсветится красным
    2. File / Settings / вкладка проекта / Python interpreter / + install / ищем pygame / install package.
    3. В терминале, где будете запускать программу, набрать `pip3 pygame`
6. Проверка, что модуль нормально установился
    1. Добавили `print(pg.version.ver)`, потом эту строку можно закоментировать
    
Надо выставить корректные EOL настройки
https://www.jetbrains.com/help/pycharm/configuring-line-endings-and-line-separators.html
В статус баре меняем внизу окна pycharm для текущего файла.

## Окно, которое закрывается

### Импорт пакета и инициализация

```python
import pygame

pg.init()
```

Запускаем, не должно ничего происходить. Код должен запускаться без ошибок.

### Черное окно, которое не умеет закрываться

```python
# Размеры окна
display_width = 800
display_height = 600
display_size = (display_width, display_height)

# создаем окно
pygame.display.set_mode(display_size)
```
При запуске появляется черное окно 800х600, которое по нажатию на `X` не закрывается. Приходится прерывать выполнение программы.

### Добавляем закрытие приложения по нажатию на `Х`

Организуем цикл с флагом `running` - продолжать работу или нет.
```python
# флаг, что приложение работает
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```
Как это работает? Работа с клавиатурой и мышью реализована через события (event). События накапливаются в очереди. Их по порядку достают в цикле 
```python
    for event in pygame.event.get():
```
Подробнее как работают подобные циклы увидим в модуле про коллекции.

У события есть поля тип `event.type` и ключ `event.key`. Нажатие на `Х` порождает событие типа `pygame.QUIT`.

Проверяем, что после запуска можно нажать на `Х` и приложение закроется без ошибок.

### Декорации окна - заголовок и иконка

Еще одни методы pygame.

Меняем заголовок окна
```python
pygame.display.set_caption('Space Invaders')
```
Для загрузки иконки нужно сначала прочитать файл с картинкой и преобразовать его в Surface. Потом полученный объект передать в метод `set_icon`.
```python
# секция изображений
icon_img = pygame.image.load('resources/img/ufo.png')   
pygame.display.set_icon(icon_img)
```

### Полный код программы

Лучше посмотреть версию программы для [этого коммита](https://github.com/tatyderb/games_in_pygame/tree/8ca7f77a1a3a8a0661263c3a1c0416413c969fed) на github. Далее будут приводиться только коммиты и ссылки на конкретные состояния репозитория.

```python
import pygame

pygame.init()

# загружаем изображения
icon_img = pygame.image.load('resources/img/ufo.png')

# размеры окна
display_width = 800
display_height = 600
display_size = (display_width, display_height)
# print(f'{display_width=} {display_height=} {display_size=}')

# создаем окно
pygame.display.set_mode(display_size)
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(icon_img)

# флаг, что приложение работает
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

## Добавим игрока в поле

### Загрузка изображения

Загрузим изображение из файла `resources/img/player.png`
```python
player_img = pygame.image.load('resources/img/player.png')
```

### Размеры и позиция игрока

Из изображения получим ширину и высоту игрока.
```python
# позиция игрока
player_width = player_img.get_width()
player_height = player_img.get_height()
```
Расположим игрока внизу посередине, на расстоянии 10 пикселей от низа окна.

Оси координат в окне идут так же, как луч развертки в телевизоре. Исторически эти оси возникли от развертки и прижились в графических пакетах.

Луч идет слева направо. **Ось Х идет слева направо, как в математике**.

Линии идут сверху вниз. **Ось Y идет сверху вниз**. (0, 0) находится в левом верхнем углу.

![Оси на экране](https://stepik.org/media/attachments/lesson/784099/axis.png)

При рисовании изображения указываются (x, y) координаты его **левого верхнего угла**. Инициируем игрока так, чтобы он был внизу посередине на расстоянии 10 пикселей (player_gap) от низа окна.

```python
player_gap = 10                                     # расстояние от игрока до низа окна
player_x = display_width // 2 - player_width // 2   # будет потом меняться
player_y = display_height - player_height - player_gap
# print(f'{player_x=} {player_y=}')
```

### Рисуем неподвижного игрока

Изменяем строку создания окна игры, запоминая полученный из функции Surface для рисования в переменную `display`.
```python
display = pygame.display.set_mode(display_size)
```
* Используя этот `display` нарисуем изображение в указанных координатах.
* Чтобы увидеть этот "заказ на рисование", обязательно должен быть вызов метода `update`.
* Этот код должен работать в главном цикле `while running:`
```python
    display.blit(player_img, (player_x, player_y))
    pygame.display.update() #!!!!!!
```

Проверяем: при запуске приложения видно изображение игрока. Оно находится в правильном месте.

* [commit](https://github.com/tatyderb/games_in_pygame/commit/8f235e92677aa117399e81b41d62473eb110502c)
* [файлы этой версии](https://github.com/tatyderb/games_in_pygame/tree/8f235e92677aa117399e81b41d62473eb110502c)

### Движение игрока вправо

Отладим анимацию игрока при движении вправо.

* `player_dx` - на сколько изменяется `x` координата игрока, то есть его скорость;
* `player_speed` - модуль скорости.

Определим константы и переменные:
```python
player_speed = 1
player_dx = player_speed
```

проблема: игрок полосой размазывается по низу.
Решение: надо перерисовывать фон.

### Заливаем на каждом шаге глобального цикла фон

Заливаем бэк каждый раз черным. Потом можно будет рисовать картинку.
```python
display.fill('black', (0, 0, display_width, display_height))
```
* первый аргумент - цвет, его можно задать как цвет в tkinter, например, `'black'` или `'red'`. Можно задать тройкой чисел от 0 до 255 - значения красного, синего и зеленого. `(0, 0, 0)` - тоже черный цвет.
* второй аргумент - прямоугольник, внутри которого заливаем (x, y, ширина, высота), где x и y - координаты левой верхней точки.

Проверяем: игрок движется вправо, не оставляя "следа".

* [движение игрока влево](https://github.com/tatyderb/games_in_pygame/commit/ac35db2accc446cdee21b3fd132cae17f6c77f83), [убираем след](https://github.com/tatyderb/games_in_pygame/commit/e509616b0a0ad3a933a3ef52fd2e47d7baf1215c) - коммиты
* [файлы этой версии](https://github.com/tatyderb/games_in_pygame/tree/e509616b0a0ad3a933a3ef52fd2e47d7baf1215c)

## Разбиваем на функции

В этом коде плохо, что в одну кучу смешаны разные вещи: изменение математической модели (расположение игрока и далее прочих объектов), перерисовка объектов и обработка событий.

Есть:
```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # изменение положения объектов
    player_x += player_dx

    # рисуем на экране
    display.fill('black', (0, 0, display_width, display_height))
    display.blit(player_img, (player_x, player_y))
    pygame.display.update()
``` 
Хочется:
```python
running = True
while running:
    model_update()
    display_redraw()
    running = event_process()
```
Перепишем код в этом стиле, учитывая, что дальше нам добавлять врагов и пули.

### Модель

Обновление модели - это обновление игрока.
```python
def model_update():
    player_update()
```
Обновление игрока - это его смещение по `x`.
```python
def player_update():
    player_x += player_dx
```
Обратите внимание, что 

* функцию `player_update` нужно написать раньше, чем функцию `model_update`.
* код приводит к ошибке, хотя в цикле без функций строка изменения `player_x` работала:
```python
def player_update():
    player_x += player_dx
```
В функциях можно читать глобальные переменные, но нельзя их изменять. Присвоение привело к тому, что тут создается **локальная** переменная `player_x`. И в правой части читается значение из еще не инициализированной локальной переменной.

Чтобы **изменять** именно глобальную переменную, нужно использовать ключевое слово **global**:
```python
def player_update():
    global player_x
    player_x += player_dx
```
Такое изменение глобальных переменных приводит к тому, что трудно отследить где именно изменилось ее значение, если мы ищем ошибку в коде. В нашей небольшой игре будем использовать глобальные переменные. Если передавать нужные объекты в аргументах функций и возвращать их наборы по цепочке вызова функций, текст станет плохо читаемым.

С другим подходом к решению этой проблемы мы познакомимся в следующем модуле по разработке игр. Пока попробуем писать код, используя глобальные переменные.

### Перерисовка объектов

Напишем ее единой функцией:
```python
# перерисовка объектов
def display_redraw():
    # рисуем на экране
    display.fill('black', (0, 0, display_width, display_height))
    display.blit(player_img, (player_x, player_y))
    pygame.display.update()
```

### Обработка событий

Разбираем очередь событий. Напишем отдельные функции, которые обрабатывают отдельное событие.
```python
def event_process():
    """Обрабатывает события клавиатуры и мыши, возвращает False, если приложение хотят закрыть."""
    for event in pygame.event.get():
        event_player(event)
        if event_close_application(event):
            return False
    return True
```
События игрока мы еще не писали, поставим функцию-заглушку:
```python
def event_player(event):
    pass
```
Обработка нажатия на `Х` на окне:
```python
def event_close_application(event):
    close = False
    if event.type == pygame.QUIT:
        close = True
    return close
```
Вместо глобальной переменной `running` создается локальная переменная `close`, значение которой возвращают по цепочке вызова функций.

Этот код можно упростить:
```python
def event_close_application(event):
    return event.type == pygame.QUIT
``` 

Проверка: код работает так же, как на предыдущем шаге. Новой функциональности нет. Мы проводили **рефакторинг** (переработку) кода.

* [коммит](https://github.com/tatyderb/games_in_pygame/commit/af965c76f4011f76e96e0b5757757a4c0b47a628)
* [код](https://github.com/tatyderb/games_in_pygame/tree/af965c76f4011f76e96e0b5757757a4c0b47a628)

## Продолжим разработку игрока

### По нажатию клавиш ВЛЕВО и ВПРАВО будем двигаться влево и вправо

У нажатия клавиш на клавиатуре `event.type` должен быть `pygame.KEYDOWN`.

* `event.key`:
    * `pygame.K_LEFT` - стрелка ВЛЕВО
    * `pygame.K_RIGHT` - стрелка ВПРАВО
    * `pygame.K_a` и `pygame.K_d` - клавиши `a` и `d`.
    
По нажатию клавиши ВЛЕВО или `a` будем двигаться влево, а ВПРАВО или `d` - вправо.

```python
ef event_player(event):
    """Вправо-влево по нажатию стрелок и a, d;"""
    global player_dx
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            player_dx = -player_speed
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            player_dx = player_speed
```
Проверяем: запускаем приложение и нажимаем стрелки влево/вправо и клавиши a и d. Игрок движется влево и вправо, меняя направление от нажатых клавиш.

* [коммит](https://github.com/tatyderb/games_in_pygame/commit/0c2e29c5a8e16ad2490c02192c5e0edb36842ec4)
* [код](https://github.com/tatyderb/games_in_pygame/tree/0c2e29c5a8e16ad2490c02192c5e0edb36842ec4)

Забегая вперед, код 
```python
if event.key == pygame.K_LEFT or event.key == pygame.K_a:
```
можно переписать как
```python
if event.key in (pygame.K_LEFT, pygame.K_a):
```

### И останавливается

Игрок замечательно бегает. Вести с такого положения стрельбу очень трудно. Хочется остановиться и прицелиться. Изменим поведение игрока, двигаясь только при нажатых клавишах. Если клавиша отпущена, то будем сразу останавливаться.

```python
def event_player(event):
    """Вправо-влево по нажатию стрелок и a, d;"""
    global player_dx
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            player_dx = -player_speed
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            player_dx = player_speed

    # отпускаем эти кнопки и останавливаемся
    if event.type == pygame.KEYUP:
        if event.key in (pygame.K_LEFT, pygame.K_RIGHT,
                         pygame.K_a, pygame.K_d):
            player_dx = 0
```
* [коммит](https://github.com/tatyderb/games_in_pygame/commit/570c4fc4f8df62f0b7480f93446fecdbfdf6b676)
* [файлы](https://github.com/tatyderb/games_in_pygame/tree/570c4fc4f8df62f0b7480f93446fecdbfdf6b676)

### Не даем игроку выходить за пределы окна

Это относится к модели, изменение игрока. Допишем функцию `player_update`.

С левым краем просто, нужно чтобы `player_x > 0`. На левом крае нужно учесть ширину игрока.

```python
def player_update():
    """Обновляет позицию игрока."""
    global player_x
    player_x += player_dx
    
    # не дадим игроку выходить за пределы экрана
    if player_x < 0:
        player_x = 0

    if player_x + player_width > display_width:
        player_x = display_width - player_width
```
Проверка: Запускаем и жмем стрелку сначала в одну строну, потом в другую. Игрок доходит до края экрана и дальше не идет.

* [коммит](https://github.com/tatyderb/games_in_pygame/commit/af55ad8fcc0d76a0788d7f31aa03951a19aa24da)
* [файлы](https://github.com/tatyderb/games_in_pygame/tree/af55ad8fcc0d76a0788d7f31aa03951a19aa24da)

Задание: Измените код так, чтобы при запуске приложения игрок стоял, а не бежал вправо.

## Пуля

Научимся создавать пулю и двигать её.

### Загрузим изображение

```python
bullet_img = pygame.image.load('resources/img/bullet.png')
```

### Определим переменные

Определим ширину и координаты, почти как в игроке. Но пуля, в отличие от игрока, существует не всегда. Переменная `bullet_alive` будет `True`, если пуля есть. Только в этом случае нужно изменять положение пули и перерисовывать.

Пуля двигается только по вертикали, поэтому `bullet_dy`. Изначально никакой пули нет.
```python
# пуля
bullet_alive = False
bullet_width = bullet_img.get_width()
bullet_height = bullet_img.get_height()
bullet_x, bullet_y, bullet_dy = 0, 0, 0
bullet_speed = 5
```

### Изменим модель

Изменение модели пули начнем с отдельной функции создания пули. Она нам будет часто нужна. Создаем пулю над игроком:
```python
def bullet_create():
    """Возвращает координаты пули"""
    x = player_x + player_width / 2 - bullet_width / 2
    y = player_y - bullet_height
    dy = -bullet_speed
```
и изменение модели:
```python
def bullet_update():
    global bullet_y
    if bullet_alive:
        bullet_y += bullet_dy
```

### Нарисуем пулю

Не забудем про перерисовку, иначе наша пуля будет не видна.
```python
    if bullet_alive:
        display.blit(bullet_img, (bullet_x, bullet_y))
```

### Обработка событий

По нажатию левой кнопки мыши будем стрелять пулей, **если она еще не существует**

События нажатия кнопки мыши имеют тип `pygame.MOUSEBUTTONDOWN` (не нашла клик, море возможностей нажать на кнопке, потянуть, отпустить вне кнопки, тестер негодует уже заранее).

`pygame.mouse.get_pressed()` возвращают набор True/False значений, который соответствует [кнопкам мыши](https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pressed). 

    * `key[0]` - левая кнопка, 
    * `key[1]` - средняя кнопка, 
    * `key[2]` - правая кнопка, 
    
Если нажата левая кнопка мыши и пули еще не существует, делаем пулю.

```python
def event_bullet(event):
    """Стреляет по нажатию левой кнопки мыши."""
    global bullet_alive, bullet_x, bullet_y, bullet_dy
    if event.type == pygame.MOUSEBUTTONDOWN:
        key = pygame.mouse.get_pressed()
        print(f'{key=} {bullet_alive=}')
        if key[0] and not bullet_alive:
            bullet_x, bullet_y, bullet_dy = bullet_create()
            bullet_alive = True
```

Проверка: запустим приложение. По левому клику мыши появляется пуля над игроком. Она никуда не движется.

* [коммит](https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pressed)
* [файлы](https://github.com/tatyderb/games_in_pygame/tree/d82c4a3c5be810f9def0d3e2dfbc57a9b1b67096)

Если пули нет на нужном месте, проверьте, не забыли ли вы добавить перерисовку пули. Распечатайте координаты пули при её создании.

Все еще не видно пули? Если вы уже добавили апдейт пули в модель, может у вас слишком большая скорость и пуля вылетает за пределы окна. Установите скорость 0 при создании пули. и попробуйте запустить еще раз. 

### Пуля начинает лететь вверх

Для этого добавим обновление модели. Перерисовка у нас уже есть.

```cpp
def model_update():
    player_update()
    bullet_update()
```

Чтобы стрелять второй раз, нужно удалять пулю при выходе за границу окна (или потом при попадании во врага). Напишите это самостоятельно.

* [коммит](https://github.com/tatyderb/games_in_pygame/commit/4065a96aef90ddb76e328ca0d7c385f98446fe62)
* [файлы](https://github.com/tatyderb/games_in_pygame/tree/4065a96aef90ddb76e328ca0d7c385f98446fe62)

## Враг (enemy)

Создаем вверху посередине. Скорость и ее направление делаем случайной.

### Загружаем изображение 

```python
enemy_img = pygame.image.load('resources/img/enemy.png')
```
### Создаем переменные и заполняем значениями

Враг летит вниз со скоростью `enemy_dy` и немного вбок со скоростью `enemy_dx`.

```python
# позиция врага
enemy_width = enemy_img.get_width()
enemy_height = enemy_img.get_height()
enemy_x, enemy_y, enemy_dx, enemy_dy = 0, 0, 0, 0
enemy_alive = False
```
### Модель

Функция `random.randrange(от, до, сколько)` создает последовательность из `сколько` целых значений в диапазоне `от` и `до`, включая `от` и не включая `до`, как в `range`. По умолчанию `сколько` равно 1.

`random.randrange(-2, 3)` создает одно целое число от -2 включительно до 3 не включительно. Т.е. может быть создано -2, -1, 0, 1, 2. Число 3 никогда не получится.

Вместо `random.randrange(-2, 3)` можно использовать `random.randint(-2, 2)`, которое создает одно число, обе границы включены в диапазон.

```python
def enemy_create():
    """Возвращает случайные координаты и скорость для создания врага"""

    x = random.randrange(0, display_width - enemy_width)
    y = enemy_y_gap

    dx = random.randrange(-2, 3)
    dy = random.randrange(1, 3) / 2

    return x, y, dx, dy

def enemy_update():
    global enemy_x, enemy_y, enemy_dx, enemy_dy
    enemy_x += enemy_dx
    enemy_y += enemy_dy
    
    # когда выходим за границы окна, убираем текущего
    # и сразу создаем нового
    if enemy_x < 0 \
            or enemy_x + enemy_width > display_width\
            or enemy_y + enemy_height > display_height:
        enemy_x, enemy_y, enemy_dx, enemy_dy = enemy_create()
 

def model_update():
    player_update()
    bullet_update()
    enemy_update()
```

### Перерисовка

Не забудьте добавить в `display_redraw()`

```python
    if enemy_alive:
        display.blit(enemy_img, (enemy_x, enemy_y))
```

### События

Врагом мы не управляем, поэтому его событий нет.

Проверка: запускаем приложение и смотрим, что враги появляются и пролетают, как только исчезнет один враг, сразу же появляется новый.

* [коммит](https://github.com/tatyderb/games_in_pygame/commit/a690bfc282f5396301ad84fd3bef242d3d6c9783)
* [файлы](https://github.com/tatyderb/games_in_pygame/tree/a690bfc282f5396301ad84fd3bef242d3d6c9783)

## Взаимодействие с врагом

Реализуем столкновение пули и врага. Чтобы не мучиться с отладкой, *временно* поставим при создании

```python
enemy_dx = 0
enemy_dy = 0.1
```
