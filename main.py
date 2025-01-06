import pygame
from pool import Pool
from stuff import *

window = pygame.display.set_mode((800, 800), pygame.RESIZABLE)

pool = Pool(window)

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    
    pool.render()

    pygame.display.flip()