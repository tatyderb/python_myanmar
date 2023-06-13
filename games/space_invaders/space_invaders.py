import pygame as pg
import random

from mysize import display_width, display_height

pg.init()

display_size = (display_width, display_height)
# создаем окно
display = pg.display.set_mode(display_size)

# Заголовок и иконка окна
pg.display.set_caption('Space Invaders')

# сначала создаем рисунок, потом этот рисунок передаем в иконку
icon_img = pg.image.load('src/ufo.png')
pg.display.set_icon(icon_img)

# фон
background_img = pg.image.load('src/background.png')

# игрок
player_img = pg.image.load('src/player.png')
player_width = player_img.get_width()
player_height = player_img.get_height()
player_gap = 10                                     # расстояние от игрока до низа окна
player_x = display_width // 2 - player_width // 2   # будет потом меняться
player_y = display_height - player_height - player_gap
print(f'{player_x=} {player_y=}')
player_speed = 10
player_dx = 0

# пуля
bullet_img = pg.image.load('src/bullet.png')
bullet_width = bullet_img.get_width()
bullet_height = bullet_img.get_height()
bullet_x = 0
bullet_y = 0
bullet_dy = -5
bullet_alive = False

# противник
enemy_img = pg.image.load('src/enemy.png')

enemy_width = enemy_img.get_width()
enemy_height = enemy_img.get_height()
enemy_x, enemy_y, enemy_dx, enemy_dy = 0, 0, 0, 0
default_enemy_y = 10
enemy_alive = False

# text example
font = pg.font.Font('src/04B_19.TTF', 32)
hihg_score_font = pg.font.Font('src/04B_19.TTF', 64)
restart_font = pg.font.SysFont('None', 48)

sound_bullet = pg.mixer.Sound('src/laser.wav')
sound_bullet.set_volume(0.5)

pg.mixer.music.load('src/background.wav')
pg.mixer.music.set_volume(0.3)
pg.mixer.music.play(-1)

def bullet_update():
    global bullet_y, bullet_alive, enemy_alive
    if not bullet_alive:
        return

    bullet_y += bullet_dy
    if bullet_y < 0:
        bullet_alive = False

    # пересекает ли пуля противника?
    rect_bullet = pg.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
    rect_enemy = pg.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    if rect_enemy.colliderect(rect_bullet):
        # пуля попала в противника
        bullet_alive = False
        enemy_alive = False
        print('Bang!')

def bullet_create():
    """Создает пулю над игроком, середина игрока равна середине пули.
    bullet_x + bullet_width / 2 = player_x + player_width / 2
    bullet_x = player_x + player_width / 2 - bullet_width / 2
    """
    global bullet_x, bullet_y, bullet_alive
    bullet_x = player_x + player_width / 2 - bullet_width / 2
    # низ пули равен верху игрока
    bullet_y = player_y - bullet_height
    bullet_alive = True
    sound_bullet.play()

def enemy_center_create():
    """Создает противника посередине экрана вверху."""
    global enemy_x, enemy_y, enemy_alive
    enemy_x = display_width // 2 - enemy_width // 2
    enemy_y = 0
    enemy_alive = True

def enemy_random_create():
    global enemy_x, enemy_y, enemy_dx, enemy_dy, enemy_alive
    enemy_x = random.randint(0, display_width)
    enemy_y = default_enemy_y
    enemy_dx = random.randint(-2, 2)
    enemy_dy = random.randint(1, 3)
    enemy_alive = True

def enemy_create():
    # enemy_center_create()
    enemy_random_create()


def enemy_update():
    global enemy_x, enemy_y, enemy_alive
    if not enemy_alive:
        enemy_create()
    enemy_x += enemy_dx
    enemy_y += enemy_dy
    if enemy_x < 0 or enemy_x > display_width or enemy_y < 0 or enemy_y > display_height:
        enemy_alive = False

def model_update():
    player_update()
    bullet_update()
    enemy_update()

def player_update():
    global player_x
    player_x += player_dx
    # игрок не должен выходить за пределы экрана
    if player_x < 0:
        player_x = 0
    if player_x + player_width > display_width:
        player_x = display_width - player_width

def display_redraw():
    # display.fill('dark blue', (0, 0, display_width, display_height))
    display.blit(background_img, (0, 0))
    display.blit(player_img, (player_x, player_y))
    if bullet_alive:
        display.blit(bullet_img, (bullet_x, bullet_y))
    if enemy_alive:
        display.blit(enemy_img, (enemy_x, enemy_y))

    # надпись
    score_surface = font.render(f'Score: 123', True, 'red')
    display.blit(score_surface, (10, 10))

    other_surface = restart_font.render('Game Over', True, (255, 255, 255))
    w = other_surface.get_width()
    display.blit(other_surface, ((display_width - w)/2, display_height/2))

    pg.display.update()

def event_process():
    global player_dx
    for event in pg.event.get():
        # окно
        # press X button - quit
        if event.type == pg.QUIT:
            return False
        # игрок
        # a/d и <- и ->
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_a or event.key == pg.K_RIGHT or event.key == pg.K_d:
                player_dx = 0
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                player_dx = -player_speed
            if event.key == pg.K_RIGHT or event.key == pg.K_d:
                player_dx = player_speed

        # пуля
        if event.type == pg.MOUSEBUTTONDOWN:
            key = pg.mouse.get_pressed()
            print(f'{key=} {bullet_alive=}')
            if key[0] and not bullet_alive:
                bullet_create()

    return True


# создали часы
FPS = 24  # frame per second
clock = pg.time.Clock()

enemy_create()
running = True
while running:
    model_update()
    display_redraw()
    running = event_process()
    clock.tick(FPS)

# после цикла
pg.quit()
