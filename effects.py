from entities import *
from random import randrange


class particles:
    def __init__(self):
        self.prts1 = []

    def effect1(self):
        self.prts1.append([b.x - 7, b.y + 7, randrange(-2, 2), randrange(-2, 2), 10, (randrange(255), randrange(255), randrange(255))])
        for prt in self.prts1:
            pygame.draw.circle(wn, prt[5], [prt[0], prt[1]], prt[4])
            prt[0] += prt[2]
            prt[1] += prt[3]
            prt[4] -= 0.2
            if prt[4] <= 0:
                self.prts1.remove(prt)


prtcls = particles()