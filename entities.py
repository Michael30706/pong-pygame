import pygame
from screen import *
pygame.init()


class player:
    def __init__(self):
        self.x = 0
        self.y = wn.get_height() / 2
        self.rct = pygame.Rect([self.x, self.y, 30, 200])

    def move(self):
        self.rct = pygame.Rect([self.x, self.y, 30, 200])
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 7
        if keys[pygame.K_s]:
            self.y += 7


    def draw(self):
        pygame.draw.rect(wn, (255, 255, 255), self.rct)


class enemy:
    def __init__(self):
        self.x = wn.get_width()
        self.y = wn.get_height() / 2
        self.ball_pos = [wn.get_width() / 2, wn.get_height() / 2]

    def AI(self):
        if self.y + 100 > b.y:
            self.y -= 6
        else:
            self.y += 6


    def draw(self):
        pygame.draw.rect(wn, (255, 255, 255), [self.x - 30, self.y, 30, 200])


class ball:
    def __init__(self):
        self.x = wn.get_height() / 2
        self.y = wn.get_width() / 2
        self.vel = [9, 8]
        self.rct = pygame.Rect([self.x, self.y, 15, 15])


    def draw(self):
        self.rct = pygame.Rect([self.x, self.y, 15, 15])
        pygame.draw.circle(wn, (255, 255, 255), [self.x, self.y], 15)

    def move(self):
        self.x += self.vel[0]
        self.y += self.vel[1]
        if self.y >= wn.get_height():
            self.vel[1] *= -1
        if self.y <= 0:
            self.vel[1] *= -1
        if (0 < self.x < 30 and p.y - 120 < self.y < p.y + 200) or \
                (wn.get_width() - 30 < self.x < wn.get_width() and e.y - 120 < self.y < e.y + 200):
            self.vel[0] *= -1
        if self.x >= wn.get_width() or self.x <= 0:
            self.x, self.y = wn.get_width() / 2, wn.get_height() / 2



p = player()
e = enemy()
b = ball()