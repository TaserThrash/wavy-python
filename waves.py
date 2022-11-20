import pygame
pygame.init()

w = 200
h = 200

win = pygame.display.set_mode((w, h))

from math import *

t = 0



while True:
    win.fill('white')
    t += 0.25
    
    for x in range(0, w >> 1, 2):
        for y in range(-8, h + 8, 2):
            d = ((x) ** 2 + (y - h / 2) ** 2) ** 0.5
            z = cos(d / 8 + t) * 8
            c = (0, 255, 0)
            pygame.draw.rect(win, c, (w / 2 - x, y - z, 1, 1))
            pygame.draw.rect(win, c, (x + w / 2, y - z, 1, 1))
            
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    pygame.time.delay(10)
