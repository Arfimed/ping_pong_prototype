import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
FPS = 60

WIDTH = 700 #ширина
HEIGHT = 500 #высота
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")

WHITE = (255, 255, 255)

#задать фон сцены
img = pygame.image.load('stol.png')
new_img = pygame.transform.scale(img, (700, 500))


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        """

        :rtype: object
        """
        # иницализируем картинку спрайта, его положение по x, y и скорость спрайта
        super().__init__()

        # каждый спрайт должен хранить свойство image - изображение
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))  # добавляем изображние спрайта
        self.speed = player_speed  # скорость спрайта

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x  # положение прямоугольника по x
        self.rect.y = player_y  # положение прямоугольника по y

    def reset(self):
        # отрисовка изображения с помощью blit
        # при размещении указываются координаты
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    """класс со спрайтом-ракетой"""
    def update_r(self):
        """метод для управления правой ракеткой стрелками клавиатуры"""
        keys = pygame.key.get_pressed()  # создаем событие "нажатия клавиши"
        if keys[pygame.K_UP] and self.rect.y > 0:  # если левая стрелка вверх нажата и спрайт не уходит за пределы верхней части экрана
            self.rect.y -= self.speed  # прямоугольник спрайта будет двигаться вверх
        if keys[pygame.K_DOWN] and self.rect.y <= 430:  # если правая стрелка вниз нажата и спрайт не уходит за пределы нижней части экрана
            self.rect.y += self.speed  # прямоугольник спрайта будет двигаться вниз

    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys [pygame.K_s] and self.rect.y < 430:
            self.rect.y += self.speed



racket1 = Player('racket.jpg', 10, 200,4, 80, 100)#картинка x, y, скорость, размер ширина размер широта
racket2 = Player('racket.jpg', 590, 200,4, 80, 100)
finish = False
while True:
#проверка собыитий выхода из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if not finish:
            window.fill(WHITE)
            window.blit(new_img,(0,0))
            racket1.update_l()
            racket2.update_r()
            
            racket1.reset()
            racket2.reset()

            pygame.display.update()
    clock.tick(FPS)
