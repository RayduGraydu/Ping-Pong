'''Модули'''
from pygame import *
from random import randint

init()
font.init()
lenght = 1

# Главный класс
class GameSprite(sprite.Sprite):

    def __init__(self, game_image, height, width, x, y, speed):     # основной набор параметров
        super().__init__()
        self.image = transform.scale(image.load(game_image), (height, width))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))    # отображение

# Класс игрока
class Player(GameSprite):

    # управление за счет клавиш для первого спрайта
    def update_keys(self):

        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 365:
            self.rect.y += self.speed

    # управление за счет стрелок для вторго спрайта
    def update_arrows(self):

        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 365:
            self.rect.y += self.speed

# подключение
'''Создание интерфейса'''
size = (700, 500)

win = display.set_mode(size)
display.set_caption('Шутер')
win.fill((0,255,255))

# флаги
run = True
finish = False

fps = 60
clock = time.Clock()

# Спрайты
racket1 = Player('racket.png', 80, 130, 10, 100, 5)
racket2 = Player('racket.png', 80, 130, 600, 100, 5)
ball = Player('ball.png', 50, 40, 350, 250, 3)

balls = sprite.Group()
balls.add(ball)

dir_x = 1
dir_y = 1

# Игровой цикл
while run:

    for i in event.get(): # обработка событий
        if i.type == QUIT: # Если нажат крестик, то окно закрывается
            run = False

    # Пока финиш не равен True, то...
    if finish != True:

        win.fill((0,255,255))   # окно заполняется цветом

        racket1.update_keys() # ракетка 1
        racket1.reset()

        racket2.update_arrows() # ракетка 2
        racket2.reset()

        '''Мяч'''
        ball.reset()

        # Движение мяча
        ball.rect.x += ball.speed*dir_x
        ball.rect.y += ball.speed*dir_y

        if ball.rect.y > 450 or ball.rect.y < 0:
            dir_y *= -1

        if sprite.collide_rect(racket1, ball):
            dir_x *= -1

        if sprite.collide_rect(racket2, ball):
            dir_x *= -1

        # Счет

        if ball.rect.x < 0:
            winner1 = font.Font(None, 60).render(f'Игрок 2 выиграл', True, (0,255,0))
            win.blit(winner1, (200,230))
            finish = True 

        if ball.rect.x > 700:
            winner2 = font.Font(None, 60).render(f'Игрок 1 выиграл', True, (0,255,0))
            win.blit(winner2, (200,250))
            finish = True

    display.update()
    clock.tick(fps)

