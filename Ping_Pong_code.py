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
img = pygame.image.load("trans.png")

finish = False
while True:
#проверка собыитий выхода из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if not finish:
            window.fill(WHITE)

            pygame.display.update()
    clock.tick(FPS)