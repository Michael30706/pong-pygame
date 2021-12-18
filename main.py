import pygame
from entities import *
from effects import *
pygame.init()
FPS = 60
clock = pygame.time.Clock()
while True:
    clock.tick(FPS)
    wn.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
            quit()
    p.draw()
    p.move()
    e.draw()
    e.AI()
    prtcls.effect1()
    b.draw()
    b.move()
    pygame.display.update()
