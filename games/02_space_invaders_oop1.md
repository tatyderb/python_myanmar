# SI и классы

lesson = 791928

## Что будет в этом уроке

Мы уже написали вариант [Space Invaders без ООП](https://stepik.org/edit-lesson/784099?auth=login&unit_id=786701). Обнаружили, что трудно реализовать несколько enemy или пуль. Нужен другой подход.

Перепишем код через классы (пока без наследования), чтобы игра легко масштабировалась.

## Ресурсы отдельно

В проектах важно, чтобы ваши ресурсы не были раскиданы по коду. Опишем их в одном месте. В дальнейшем можем переместить описание где лежат ресурсы в отдельный конфигурационный файл.

```python
RSC = {
    'title': 'Space Invaders',
    'img': {
        'background': 'resources/img/background.png',
        'icon': 'resources/img/ufo.png',
        'player': 'resources/img/player.png',
        'enemy': 'resources/img/enemy.png',
        'bullet': 'resources/img/bullet.png'
    },
    'sound': {
        'background': 'audio/background.wav',
        'explosion': 'audio/explosion.wav',
        'laser': 'audio/laser.wav',
        'endless_big': 'audio/Time-to-Spare-An-Jone.wav'
    },
    'font': {

    }
}
```

## Черное окно и закрытие по Х

Отдельно пропишем каркас приложения - черное окно с иконкой и названием "Space Invaders", которое закрывается по нажатию X.

Создадим класс Application так, чтобы разделить создание в конструкторе и работу приложения. Он у нас будет в единственном экземпляре. Пока не будем заострять на нем внимание.
Использование класса:
```python
app = Application()
app.run()
```
или без дополнительной переменной app, в одну строку:
```python
Application().run()
```
Заметьте, `running` - локальная переменная, так как используется только в методе `run`. Нет необходимости делать её атрибутом класса.

```python
class Application:
    def __init__(self):
        pygame.init()
        self.size = (self.width, self.height) = (800, 600)
        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption(RSC['title'])
        icon_img = pygame.image.load(RSC['img']['icon'])
        pygame.display.set_icon(icon_img)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

```

* [commit](https://github.com/tatyderb/games_in_pygame/commit/2dbf6e41049912a58ca129782d7d54628a36a7c8)
* [view](https://github.com/tatyderb/games_in_pygame/blob/2dbf6e41049912a58ca129782d7d54628a36a7c8/space_invaders_live)

## Какие классы нужны

* Game - в этом классе мы определим всех участников игры и этот класс будет контролировать создание и удаление игровых объектов.
* Player - игрок
* Bullet - пуля
* Enemy - враг

Объект класса Game должен существовать при запуске игры в `Application.run()`, он должен на каждом шаге цикла пересчитать модель, отрисоваться и обработать события. Пока все в кучу.

Метод `Application.run` изменится:
```python
    def run(self):
        running = True
        game = Game(self.size)
        while running:
            game.model_update()
            game.redraw(self.display)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                game.event_process(event)
```
Заготовка под класс `Game`, пока все методы `pass`, ничего не делают.

```python
class Game:
    def __init__(self, display_size):
        pass

    def model_update(self):
        pass

    def redraw(self, display):
        pass

    def event_process(self, event):
        pass
```

Приложение по-прежнему запускается, рисует черный экран и закрывается по Х.

* [commit](https://github.com/tatyderb/games_in_pygame/commit/4b1bff68e2ee0d933ddf6c66c64ddef485c3de9c)
* [файл](https://github.com/tatyderb/games_in_pygame/blob/4b1bff68e2ee0d933ddf6c66c64ddef485c3de9c/space_invaders_live)

## class Player

При добавлении игрока (player) в игру (класс Game) изменятся методы игры:
```python
class Game:
    def __init__(self, display_size):
        self.display_size = display_size
        self.player = Player(display_size)

    def model_update(self):
        self.player.model_update()

    def redraw(self, display):
        # заливаем фон
        w, h = self.display_size
        display.fill((0, 0, 0), (0, 0, w, h))
        # рисуем игровые элементы
        self.player.redraw(display)
        # запрашиваем обновление экрана
        pygame.display.update()

    def event_process(self, event):
        self.player.event_process(event)
```

Перенесем код игрока из старого варианта в класс. `player_x` заменим на `self.x` и тп.

Константы, которые не менялись, вынесем в переменные класса.

* `YGAP` - расстояние между игроком и границей экрана,
* `SPEED` - скорость перемещения при нажатой клавише.

Не забудем, что игрок не должен выходить за границы экрана. Для этого сохраним размеры границы.
```python
self.bound_size = self.bound_width, self.bound_height = display_size
```
Итого:
```python
class Player:
    YGAP = 10
    SPEED = 0.5

    def __init__(self, display_size):
        self.bound_size = self.bound_width, self.bound_height = display_size
        self.img = pygame.image.load(RSC['img']['player'])
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = self.bound_width // 2 - self.width // 2
        self.y = self.bound_height - self.height - self.YGAP
        self.dx = 0

    def model_update(self):
        self.x += self.dx
        # не дадим игроку выходить за пределы окна
        if self.x < 0:
            self.x = 0
        if self.x > self.bound_width - self.width:
            self.x = self.bound_width - self.width

    def redraw(self, display):
        display.blit(self.img, (self.x, self.y))

    def event_process(self, event):
        # нажали клавишу
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.dx = -self.SPEED
            elif event.key == pygame.K_RIGHT:
                self.dx = self.SPEED
        # отпустили клавишу
        if event.type == pygame.KEYUP:
            self.dx = 0
```

* [commit](https://github.com/tatyderb/games_in_pygame/commit/a93605347c9f0af909c270185ce7d4318ffdbd77)
* [файлы](https://github.com/tatyderb/games_in_pygame/blob/a93605347c9f0af909c270185ce7d4318ffdbd77/space_invaders_live)

## class Bullet - пуля

Заметьте, что изначально в игре ее нет. Она создается по клику мыши и должна исчезать по вылету за границу экрана.

Пока никакого взаимодействия пули и врага не делаем (врага еще нет).

Точно так же добавим методы пули в Game.model_update и Game.redraw. В обработке событий у нас возвращается - жмем на гашетку (fire) или нет. Если жмем на гашетку и пули еще не было, создаем ее.

```python
class Game:
    def __init__(self, display_size):
        self.display_size = display_size
        w, h = self.display_size
        self.bound_rect = pygame.Rect(0, 0, w, h)
        self.player = Player(display_size)
        self.bullet = None

    def model_update(self):
        self.player.model_update()
        if self.bullet:
            # если пуля есть, надо ее двигать
            self.bullet.model_update()
            if not self.in_bound(self.bullet.rect()):
                # если пуля вылетела за границы экрана, удаляем ее
                self.bullet = None

    def redraw(self, display):
        # заливаем фон
        display.fill((0, 0, 0), self.bound_rect)
        # рисуем игровые элементы
        self.player.redraw(display)
        if self.bullet:
            self.bullet.redraw(display)
        # запрашиваем обновление экрана
        pygame.display.update()

    def event_process(self, event):
        self.player.event_process(event)
        if Bullet.fire(event) and self.bullet is None:
            self.bullet = Bullet(self.player.rect())

    def in_bound(self, rect):
        """Возвращает True если rect в границах экрана"""
        return self.bound_rect.contains(rect)
```
Класс Bullet похож на класс Player. Обратите внимание, нам нужно проверять нажата клавиша "огонь!" или нет, когда пули еще нет. Поэтому метод `fire(event)` статический, а не метод объекта (объекта "пуля" может еще не существовать).

```python
class Bullet:
    SPEED = 0.5     # скорость пули (абсолютная величина)

    def __init__(self, player_rect):
        self.img = pygame.image.load(RSC['img']['bullet'])
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        px, py, pw, ph = player_rect
        self.x = px + pw // 2 - self.width // 2
        self.y = py - self.height
        self.dy = -Bullet.SPEED

    def model_update(self):
        self.y += self.dy

    def redraw(self, display):
        display.blit(self.img, (self.x, self.y))

    def rect(self):
        return self.x, self.y, self.width, self.height

    @staticmethod
    def fire(event):
        """ Return True, if press FIRE!!! button. """
        if event.type == pygame.MOUSEBUTTONDOWN:
            key = pygame.mouse.get_pressed()
            if key[0]:
                return True
        return False
```

Пуль можно добавлять несколько. Обработка движения и отрисовка одной пули никак не влияет на другие.

* [commit](https://github.com/tatyderb/games_in_pygame/commit/ff097c1816ad3f371c4b38589644236d80fc73ab)
* [файл](https://github.com/tatyderb/games_in_pygame/blob/ff097c1816ad3f371c4b38589644236d80fc73ab/space_invaders_live)

## class Enemy

* Сначала врага нет.
* Если врага нет, то он появляется.
    * в случайном месте,
    * но для отладки лучше посередине экрана
* При выходе за границы экрана враг исчезает.
* у врагов нет реакции на события.

Опишем эти фразы в методах класса `Game`:

```python
class Game:
    def __init__(self, display_size):
        self.display_size = display_size
        w, h = self.display_size
        self.bound_rect = pygame.Rect(0, 0, w, h)
        self.player = Player(display_size)
        self.bullet = None
        self.enemy = None

    def model_update(self):
        self.player.model_update()
        if self.bullet:
            # если пуля есть, надо ее двигать
            self.bullet.model_update()
            if not self.in_bound(self.bullet.rect()):
                # если пуля вылетела за границы экрана, удаляем ее
                self.bullet = None

        if self.enemy is None:
            # если врага нет, его надо сделать
            self.enemy = Enemy(self.display_size)
        self.enemy.model_update()
        if not self.in_bound(self.enemy.rect()):
            # если враг вылетел за экран, он исчез
            self.enemy = None

    def redraw(self, display):
        # заливаем фон
        display.fill((0, 0, 0), self.bound_rect)
        # рисуем игровые элементы
        self.player.redraw(display)
        if self.bullet:
            self.bullet.redraw(display)
        if self.enemy:
            self.enemy.redraw(display)
        # запрашиваем обновление экрана
        pygame.display.update()

    # другие методы этого класса не изменились
```

class Enemy очень похож на класс Bullet.

```python
class Enemy:
    DEFAULT_DX = 0
    DEFAULT_DY = 0.1
    DEFAULT_Y = 30

    def __init__(self, display_size):
        self.bound_size = self.bound_width, self.bound_height = display_size
        self.img = pygame.image.load(RSC['img']['enemy'])
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        # self.x, self.y, self.dx, self.dy = self.create_at_random_position()
        self.x, self.y, self.dx, self.dy = self.create_at_center()

    def rect(self):
        return self.x, self.y, self.width, self.height

    def create_at_center(self):
        x = self.bound_width // 2 - self.width // 2
        y = self.DEFAULT_Y
        dx = self.DEFAULT_DX
        dy = self.DEFAULT_DY
        return x, y, dx, dy

    def create_at_random_position(self):
        x = random.randint(0, self.bound_width)
        y = self.DEFAULT_Y
        dx = random.randint(-2, 3) / 10
        dy = random.randint(1, 3) / 20
        return x, y, dx, dy

    def model_update(self):
        self.x += self.dx
        self.y += self.dy

    def redraw(self, display):
        display.blit(self.img, (self.x, self.y))
```

* [commit](https://github.com/tatyderb/games_in_pygame/commit/ad53328d8a192fe67630398838af141c18975b03)
* [файл](https://github.com/tatyderb/games_in_pygame/blob/ad53328d8a192fe67630398838af141c18975b03/space_invaders_live)

## Взаимодействие Enemy и Bullet

Взаимодействие игровых объектов происходит в игре. Два объекта пересекаются, оба уничтожаются.

Это взаимодействие можно описать только снаружи классов Enemy и Bullet, то есть в классе Game, который отвечает за всю игровую модель целиком.

```python
if self.intersection(self.enemy, self.bullet):
    self.enemy = None
    self.bullet = None
```
Метод Game.intersection напишем используя метод pygame.Rect.collidetect.

В метод передаем ссылки на объекты. Если у них можно вызвать методы `rect()` и эти прямоугольники пересекаются, возвращается True.

```python
@staticmethod
def intersection(orect1, orect2):
    if orect1 is None or orect2 is None:
        return False
    return pygame.Rect(orect1.rect()).colliderect(orect2.rect())
```

* [commit](https://github.com/tatyderb/games_in_pygame/commit/ae8eb71ea47f7d438011a677da55a3b3fbb25761)
* [файлы](https://github.com/tatyderb/games_in_pygame/blob/ae8eb71ea47f7d438011a677da55a3b3fbb25761/space_invaders_live)

## Что дальше?

* Реализуйте столкновение игрока и врага.
* Сделайте очередь из пуль.
    * можно максимум 5 пуль.
    * можно бесконечную очередь.

Счет, жизни, game over и тп.