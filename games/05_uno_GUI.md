# UNO: GUI на pygame

lesson = 809155

## Проблемы с написанием GUI

Вспомним, какая была структура GUI приложения в Space Invaders. Основа - функция `run`:

```python
def run(self):
    running = True
    clock = pygame.time.Clock()
    while running:
        self.application.model_update()
        self.application.redraw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            self.application.event_process(event)

        clock.tick(FPS)     # ждать 1/FPS секунды
``` 

Если в `model_update()` у нас будет один ход игрока, как в `turn()`, то вся игра пролетит перед нами в одно мгновение. И останется надпись, что "победил игрок ..."

Разделим `turn()` на небольшие части, например, играется карта, игрок берет карту, ход переходит к другому игроку и тп. Разделим так, чтобы запущенный в цикле он давал ту же игру до конца. Назовем метод `Game.model_update()`. Как добиться чтобы много раз работали маленькие куски и этот метод можно было вызвать в цикле?

Пусть у нас будет функция, которая печатает 4 строки за 1 вызов. Переделаем код так, чтобы она печатала те же 4 строки но за 4 вызова и при дальнейших вызовах код не печатала.
```python
def foo_old():
    print('AAA')
    print('BBB')
    print('CCC')
    print('ZZZ')
```
Пусть у нашей программы будут состояния `a`, `b`, `c`, `z` и `end`. При очередном состоянии мы печатаем строку и переходим в следующее состояние. Из `a` в `b`, из `b` в `c`, из `c` в `z`, из `z` в `end`. Из `end` мы никуда не переходим и ничего не делаем. Это состояние для того, чтобы остановить нашу программу.

Состояние программы храним в переменной `state`, функцию вызываем в цикле:
```python
state = 'a'
while(state != 'end'):
    foo()
```
Заменяем функцию `foo_old` на `foo`:
```python
def foo():
    if state == 'end':
        # ничего не делаем
        return 
        
    if state == 'a':
        print('AAA')
        state = 'b'
        return

    if state == 'b':
        print('BBB')
        state = 'c'
        return
        
    if state == 'c':
        print('CCC')
        state = 'z'
        return

    if state == 'z':
        print('ZZZ')
        state = 'end'
        return
```
Этот код длиннее, но позволил вызывать функцию много раз в цикле.

## Переписываем `Game.turn()` через состояния

Подумаем, какие будут состояния, что во время них нужно делать и в какое состояние и него можно перейти.

| Состояние | Переходит в | Что делаем |
|----|----|----|
| TURN_BEGIN | PLAY_CARD, DRAW_CARD  | Решает что может делать игрок - играть карту с руки или вынужден брать карту из колоды. |
| PLAY_CARD | NEXT_PLAYER | Играется карта в отбой.  |
| NEXT_PLAYER | TURN_BEGIN, END | Или игра закончена, или текущим игроком становится следующий игрок.  |
| END | - | Игра закончена. |

Добавим в класс Game подкласс State (состояния) и поле state - текущее состояние игры.

После переписывания убедитесь, что игра по-прежнему играет и играет правильно!

* [commit](https://github.com/tatyderb/games_in_pygame/commit/89cb8133355619cb4bb435b9729543e6c78b087c)
* [файлы](https://github.com/tatyderb/games_in_pygame/tree/89cb8133355619cb4bb435b9729543e6c78b087c)

## Про умных и красивых

Для реализации GUI возьмем за основу паттерн программирования [Model, View, Controller](https://ru.wikipedia.org/wiki/Model-View-Controller)

* Model - модель (игры), содержит логику игры.
* View - представление (визуализация игры) - как мы отрисовываем игру.
* Controller - обеспечивает взаимодействие пользователя и системы.

Иногда в простых системах контроллер соединяется с представлением.

Грубо говоря, в Space Invaders модель была реализована в `model_update`, view в `redraw`, контроллер в `event_process`.

Но у нас модель, представление и контроллер были смешаны в единое, потому что модель зависела от местоположения, как и контроллер.

Модель - это умные, представление - это красивые, а контроллер - это те, кто управляет как умные и красивые взаимодействуют с пользователем.

В Uno мы постараемся разнести классы на модель и представление. К классу `Card` напишем класс `CardView` и тп.

## Конфигурация приложения

Вынесем в отдельный файл данные (конфигурацию игры). В будущем можем написать чтение файла конфигурации.

Назовем этот файл `config.py`
```python
RSC = {
    'title': 'UNO',
    'FPS': 30,
    'img': {
        'background': 'resources/img/background.png',
        'back': 'resources/img/back.png',
        'card': 'resources/img/{}.png'
    },
    'sound': {
    },
    'font': {
    }
}

GEOM = {
    'display': (800, 600),
    'card': (109, 168),
    'dx_card': 30,
    'xgap': 10,
    'ygap': 10,
}
```
Будем импортировать его данные, перечисляя нужные словари:
```python
from uno_stepik.config import RSC, GEOM
```
Заметим, что ресурсы и параметры геометрии мы разнесли. Старайтесь держать их отдельно. 

* [commit](https://github.com/tatyderb/games_in_pygame/commit/d366954ea0dc96297d9c2e49385221d7aed92065)
* [файлы](https://github.com/tatyderb/games_in_pygame/tree/d366954ea0dc96297d9c2e49385221d7aed92065)

## Приложение и одна карта

Сделаем графическое приложение и нарисуем на нем одну карту. Пусть эта карта по клику на ней меняет открыта она или закрыта (нарисована картинкой или рубашкой вверх).

Сначала приложение, которое рисует большое зеленое поле. И закрывается по нажатию на крестик.

Сначала нарисуем черное окно, которое умет закрываться при нажатии на крестик.

* [commit](https://github.com/tatyderb/games_in_pygame/commit/80737dead05a4ddf891039e486debf9ad1b99bab)
* [файлы](https://github.com/tatyderb/games_in_pygame/tree/80737dead05a4ddf891039e486debf9ad1b99bab)

Добавим класс `CardView`, который умеет рисовать карту. Контроллером у нас будет класс `GameView`, в него пока поместим 1 карту и будем её рисовать. В приложении будет только один класс `GameView`. В будущем мы сможем заканчивать из класса `Application` одну игру и начинать другую.

В классе `CardView` я инкапсулирую поля. Т.е. вместо поля `x` определяю поле `__x` и прописываю через `@property` метод чтения и присвоения этому полю.

Извне класса (с точки зрения API) у объекта класса есть поле `х`.

```python
class CardView:

    back_img = None
    size = (width, height) = GEOM['card']

    def __init__(self, card: Card | None, x: int, y: int, opened: bool = True):
        self.__card = card
        self.__x = x
        self.__y = y
        # еще тут храним изображение карты и тп  

    # вызывается при чтении, например, x1 = vcard.x
    @property
    def x(self):
        return self.__x

    # вызывается при записи, например, vcard.x = 100
    @x.setter
    def x(self, val: int):
        self.__x = val
```
Для `CardView`, кроме методов инкапсуляции через @property, реализуем методы:

* `redraw(self, display: pygame.Surface)` - отрисовка карты
* `r(self)` - возвращает прямоугольник типа `pygame.Rect`
* `flip(self)` - перевернут карту (только для отладки обработки клика на карту)

* [commit](https://github.com/tatyderb/games_in_pygame/commit/da6a501c6d89eee9abd0d9c1913cca6a43f4af2d)
* [файлы](https://github.com/tatyderb/games_in_pygame/tree/da6a501c6d89eee9abd0d9c1913cca6a43f4af2d)

## Визуализация всех компонент

Нарисуем все компоненты игры на экране. Они ничего не будут делать полезного, только показывать начальное состояние игры. Чтобы потом отлаживать взаимодействие компонент, будем загружать данные, на которых мы отлаживали модель игры.

Для упрощения пусть будут 3 игрока, мы (интерактивный игрок) и 2 игрока с ИИ (искусственным интеллектом). Свои карты нарисуем просторно, чтобы было удобно кликать по ним мышкой для выбора. Карты других игроков нарисуем компактно. Нам интересно только количество карт. Сначала будем рисовать все руки "в открытую", чтобы убедиться, что мы не испортили карты при перерисовке.

### Расположение компонент на экране

```
ИгрокAI1 ИгрокAI2
 отбой колода
    Игрок 0
```
(нарисовать и на рисунке расставить размеры)

Никогда не пишите абсолютные размеры! Рассчитайте!!! Первые три правки "давай на 3 пикселя левее и поменяем колоду и отбой местами" докажут правоту тех, кто считал, а не хардкодил абсолютные значения.

```python
'''
# черновая прикидка расположения
# AI1  AI2
# TOP  DECK
# PLAYER
'''

# дано в конфигурации геометрии
XGAP = GEOM['xgap']                 # отступ по Х
YGAP = GEOM['ygap']                 # отступ по Y
DWIDTH, DHEIGHT = GEOM['display']   # размер экрана
CW, CH = GEOM['card']               # размер карты

# Y координаты рядов 0, 1, 2
R0Y = YGAP
R1Y = (DHEIGHT - CH) // 2 + YGAP
R2Y = DHEIGHT - CH - YGAP

# Х координаты компонент
PLAYERX = XGAP                      # игрока себя рисуем от левого края
AI1X = XGAP                         # AI1 рисуем от левого края
AI2X = DWIDTH // 2 + XGAP           # AI2 рисуем от центра (с отступом!)
TOPX = DWIDTH // 2 - XGAP - CW      # отбой от центра влево с отступом
DECKX = DWIDTH // 2 + XGAP          # колода от центра вправо с отступом
HAND_WIDTH = DWIDTH - 2 * XGAP      # ширина карт руки интерактивного игрока
COMPACT_HAND_WIDTH = DWIDTH // 2 - 2 * XGAP  # ширина карт AI
```

## Пишем View классы, которые только рисуют

Сначала разместим отбой и колоду. Для этого создадим классы `HeapView` и `DeckView`. И отладим их отрисовку.

```python
class HeapView:
    def __init__(self, heap: Heap, x: int, y: int):
        self.heap = heap
        self.x = x
        self.y = y

    def redraw(self, display: pygame.Surface):
        cv = CardView(self.heap.top(), self.x, self.y)
        cv.redraw(display)


class DeckView:
    def __init__(self, deck: Deck, x: int, y: int):
        self.deck = deck    # пока не используется, на всякий случай
        self.x = x
        self.y = y

    def redraw(self, display: pygame.Surface):
        CardView.redraw_cover(display, self.x, self.y)
```
Добавим код в `GameView.__init__` и `GameView.redraw`:
```python
class GameView:
    def __init__(self, game: Game, size: tuple[int, int], display: pygame.Surface):
        self.width, self.height = size
        self.display = display
        self.game = game

        # компоненты
        self.vheap = HeapView(game.heap, TOPX, R1Y)
        self.vdeck = DeckView(game.deck, DECKX, R1Y)
        
    def redraw(self):
        self.display.fill((0, 81, 44), (0, 0, self.width, self.height))
        # self.cv.redraw(self.display)
        self.vheap.redraw(self.display)
        self.vdeck.redraw(self.display)
        pygame.display.update()
```

* [commit](https://github.com/tatyderb/games_in_pygame/commit/6a618e9123c5da9b82aaa9c8e6a8e8221484e9d5)
* [файлы](https://github.com/tatyderb/games_in_pygame/tree/6a618e9123c5da9b82aaa9c8e6a8e8221484e9d5)

### Руки игроков

Заметим, что мы собираемся делать одного интерактивного игрока и двух не интерактивных. Поэтому нам нужно две разных визуализации руки. Своя рука должна рисоваться просторно, чтобы удобно было выбирать карту кликом мышки. Рука оппонентов должна показывать сколько карт.

```python
        # игроки, прибиты гвоздями 3 штуки
        self.players = [
            PlayerInteractiveView(game.players[0], PLAYERX, R2Y),
            PlayerCompactView(game.players[1], AI1X, R0Y),
            PlayerCompactView(game.players[2], AI2X, R0Y)
        ]

```

Поэтому общий код изображения игроков напишем в `PlayerView`, от него наследуем классы `PlayerCompactView` и `PlayerInteractiveView`, в которых будет разная отрисовка и далее разные реакции на клики мыши.

В реализации интерактивный игрок не может хорошо отрисовать больше 7 карт. Эластичную верстку, когда большее количество карт будет отрисовано внахлест, оставим отдельной задачей.

```python
class PlayerView:
    def __init__(self, player: Player, x: int, y: int):
        self.player = player
        self.x = x
        self.y = y
        self.hand_view = []
        self.update_hand()

    def update_hand(self):
        pass

    def redraw(self, display):
        for vcard in self.hand_view:
            vcard.redraw(display)


class PlayerCompactView(PlayerView):
    def update_hand(self):
        DXCARD = DXCARD_COMPACT
        self.hand_view = [CardView(card, self.x + DXCARD * i, self.y)
                          for i, card in enumerate(self.player.hand.cards)]


class PlayerInteractiveView(PlayerView):
    def update_hand(self):
        self.hand_view = [CardView(card, self.x + (DXCARD + CardView.width) * i, self.y)
                          for i, card in enumerate(self.player.hand.cards)]
```

* [commit](https://github.com/tatyderb/games_in_pygame/commit/c4129a4296668a09211da90e3416eca0c98e5546)
* [файлы](https://github.com/tatyderb/games_in_pygame/tree/c4129a4296668a09211da90e3416eca0c98e5546)





