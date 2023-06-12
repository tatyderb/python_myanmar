# Space invaders

C:\work\stud\2023_podfac\space_invider_draft

## Подготовка к коду

* Послать студентам
    * src.zip - архив с картинками, шрифтом и музыкой, распаковать в директорию со структурой
```
src/
    background.png
    bullet.png
    enemy.png
    player.png
```
    * https://meet.google.com/pzv-smtf-qbu - встреча
    * https://replit.com/join/zunvzwitqi-tatyderb - код буду посылать сюда.
    
## Знакомство с repl.it

* Создаем новый pygame repl.it - можете писать тут, если у вас на компьютере нет pygame или python.

* Сюда буду копировать свой код. Можете его брать.

## Pycharm. Создаем проект

* создать новый проект
* создать новый файл
* `import pygame as pg`
* установить pygame, если нужно
* проверка pygame: `print(pg.version.ver)`
```python
import pygame as pg
print(pg.version.ver)
```

## Основы создания любого оконного приложения в pygame

### Черное окно (в pyCharm - ничего)

```python
# Размеры окна, repl.it берем 500 и 400
display_width = 800
display_height = 600
display_size = (display_width, display_height)

# создаем окно
display = pg.display.set_mode(display_size)
```
Pycharm: окно появляется и мгновенно исчезает
replit: есть окно и оно не исчезает

### Синее окно

```python
display.fill('blue', (0, 0, display_width, display_height))
```

### окно не исчезает

События. 
```python
while True:
    display.fill('blue', (0, 0, display_width, display_height))
    pg.display.update()
```

### окно закрывается

В цикл добавим обработку событий
```python
running = True
while running == True:
    # рисуем
    # обрабатываем события
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

# после окончания цикла
pg.quit()   
```

### Даем программе отдыхать, 100% CPU

```python
# создали часы
FPS = 24  # frame per second
clock = pg.time.Clock()
```
в цикле
```python
    clock.tick(FPS)
```

### Заголовок окна и иконка

```python
pg.display.set_caption('Space Invaders')
```
копируем файлы ресурсов, пока копируем только ufo.pngб drag-n-drop в pycharm в дерево файлов и в replit.
показываем относительный и абсолютный путь.

### Рисуем фон игры

Как в иконе - сначала объект один раз создаем, потом много раз рисуем

```python
background_img = pg.image.load('src/background.png')
```
```python
    display.blit(background_img, (0, 0))
```

## Перерыв 5 минут

Копируете рисунки, дописываете все, что не успели.
Поднимаем руку, когда все получилось.

## Рисуем игрока

```python
player_img = pg.image.load('resources/img/player.png')
```

### Система координат и рисуем изображение в нужном месте

Рассказ о системе координат
Хотим нарисовать посередине, 10 пикселей от низа окна.

До цикла один раз
```python
player_width = player_img.get_width()
player_height = player_img.get_height()
player_gap = 10                                     # расстояние от игрока до низа окна
player_x = display_width // 2 - player_width // 2   # будет потом меняться
player_y = display_height - player_height - player_gap
print(f'{player_x=} {player_y=}')
```
В цикле и **не забыть про update!!!**
```python
    display.blit(player_img, (player_x, player_y))
```

### Движение вправо

```python
player_speed = 1
```
В цикле до отрисовки изменение модели
```python
    player_x += player_speed
```
**Показать, что будет без перерисовки бэкграунда**.

## Рефакторинг

Хотим
```python
while running:
    model_update()
    display_redraw()
    running = event_process()
```
Модель - это игрок, потом пуля и враг.
```python
def model_update():
    player_update()
```
и
```python
def player_update():
    global player_x
    player_x += player_speed
```
**global** player_x

```python
def display_redraw():
    display.fill('dark blue', (0, 0, display_width, display_height))
    # display.blit(background_img, (0, 0))
    display.blit(player_img, (player_x, player_y))
    pg.display.update()

def event_process():
    for event in pg.event.get():
        # press X button - quit
        if event.type == pg.QUIT:
            return False
    return True
```

### Движение влево, вправо

У нажатия клавиш на клавиатуре event.type должен быть pygame.KEYDOWN.

event.key:
pygame.K_LEFT - стрелка ВЛЕВО
pygame.K_RIGHT - стрелка ВПРАВО
pygame.K_a и pygame.K_d - клавиши a и d.

```python
if event.type == pg.KEYDOWN:
    if event.key == pg.K_LEFT or event.key == pg.K_a:
        player_dx = -player_speed
    if event.key == pg.K_RIGHT or event.key == pg.K_d:
        player_dx = player_speed
```
Хотим двигаться только когда кнопка НАЖАТА, а когда отпустили, то остановиться
```python
    if event.type == pg.KEYUP:
        if event.key == pg.K_LEFT or event.key == pg.K_a or event.key == pg.K_RIGHT or event.key == pg.K_d:
            player_dx = 0
```

### Не выходим за границы экрана

```python
    # игрок не должен выходить за пределы экрана
    if player_x < 0:
        player_x = 0
    if player_x + player_width > display_width:
        player_x = display_width - player_width
```

## Пуля

Загрузим изображение и возьмем из него константы ширины и высоты.

```python
bullet_img = pg.image.load('src/bullet.png')
bullet_width = bullet_img.get_width()
bullet_height = bullet_img.get_height()
bullet_x = 0
bullet_y = 0
bullet_dy = -5
```

### Создаем пулю

Хотим проверить создание. Поэтому она не двигается. Создали сразу перед циклом и вызвали функцию

```python
def bullet_create():
    """Создает пулю над игроком, середина игрока равна середине пули.
    bullet_x + bullet_width / 2 = player_x + player_width / 2
    bullet_x = player_x + player_width / 2 - bullet_width / 2
    """
    global bullet_x, bullet_y, bullet_alive
    bullet_x = player_x + player_width / 2 - bullet_width / 2
    # низ пули равен верху игрока
    bullet_y = player_y - bullet_height
```

### Пуля летит

Изменяем model_update, дописываем bullet_update

```python
def bullet_update():
    global bullet_y
    bullet_y += bullet_dy
```

### По левому клику мыши пулей стреляем

События нажатия кнопки мыши имеют тип pygame.MOUSEBUTTONDOWN.

pygame.mouse.get_pressed() возвращают набор True/False значений, который соответствует кнопкам мыши.

* `key[0]` - левая кнопка,
* `key[1]` - средняя кнопка,
* `key[2]` - правая кнопка,

```python
if event.type == pg.MOUSEBUTTONDOWN:
    key = pg.mouse.get_pressed()
    print(f'{key=} {bullet_alive=}')
    if key[0] and not bullet_alive:
        bullet_create()
```

### Нельзя стрелять, пока пуля не улетела за экран

```python
bullet_alive = False
```
добавим в создание пули проверку. 
в bullet_update убиение пули.

Сделать ошибку - не убирается по достижению потолка.

Пофиксить ошибку.

## Перерыв, 5 минут

Если не устали, то можете начать писать противника, который появляется посередине экрана и начинает двигаться вниз и влево.

## Противник

Похож на пулю, но летит сверху вниз и появляется новый, когда исчезает старый.

### Создаем и он стоит на месте

```python
# противник
enemy_img = pg.image.load('src/enemy.png')
enemy_width = enemy_img.get_width()
enemy_height = enemy_img.get_height()
enemy_x, enemy_y, enemy_dx, enemy_dy = 0, 0, 0, 0
enemy_alive = False

def enemy_create():
    """Создает противника посередине экрана вверху."""
    global enemy_x, enemy_y, enemy_alive
    enemy_x = display_width // 2 - enemy_width // 2
    enemy_y = 0
    enemy_alive = True
```
Не забываем про отрисовку!

### Попадание в противника, противник уничтожается

Если пуля пересекает противника, то попала.

```python
    # пересекает ли пуля противника?
    rect_bullet = pg.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
    rect_enemy = pg.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    if rect_enemy.colliderect(rect_bullet):
        # пуля попала в противника
        bullet_alive = False
        enemy_alive = False
        print('Bang!')
```
Смотрите сколько раз напечатали Bang и можно ли еще раз выпустить пулю.

### Случайное поведение противника

```python
import random

def enemy_random_create():
    global enemy_x, enemy_y, enemy_dx, enemy_dy, enemy_alive
    enemy_x = random.randint(0, display_width)
    enemy_y = default_enemy_y
    enemy_dx = random.randint(-2, 2)
    enemy_dy = random.randint(1, 3)
    enemy_alive = True
```

## Текст (счет, game over, и тп)

Один раз создаем фонт.
```python
font = pg.font.Font('src/04B_19.TTF', 32)
hihg_score_font = pg.font.Font('src/04B_19.TTF', 64)
restart_font = pg.font.SysFont('None', 48)
```

В функции display_redraw рисуем надписи
```python
# надпись
score_surface = font.render(f'Score: 123', True, 'red')
display.blit(score_surface, (10, 10))

other_surface = restart_font.render('Game Over', True, (255, 255, 255))
w = other_surface.get_width()
display.blit(other_surface, ((display_width - w)/2, display_height/2))
```

## Звук 

### Однократный

Однократно создаем Sound
```python
sound_bullet = pg.mixer.Sound('src/laser.wav')
sound_bullet.set_volume(0.5)
```
Когда нужно, запускаем звук
```python
sound_bullet.play()
```
### В фоне бесконечно

Один раз запускаем музыку
```python
pygame.mixer.music.load('src/background.wav')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
```

# Модификации

1. Выпускать пулю так же по нажатию клавиши ПРОБЕЛ.
2. изменить код, разбить функцию event_process на функции 
    event_player_process, event_bullet_process
3. Если противник прошел за игрока, game over.
4. Пишем количество сбитых противников.




