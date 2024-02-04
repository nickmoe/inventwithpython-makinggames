import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')


WHITE = (255, 255, 255)
RIGHT = 1
DOWN = 2
LEFT = 3
UP = 4
catImg = pygame.image.load('resources/images/cat.png')
boundary = ((10, 10), (280, 220))
catx = 10
caty = 10
movespeed = 5
direction = RIGHT

while True: # main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == RIGHT:
        catx += movespeed
        if catx == boundary[1][0]:
            direction = DOWN
    elif direction == DOWN:
        caty += movespeed
        if caty == boundary[1][1]:
            direction = LEFT
    elif direction == LEFT:
        catx -= movespeed
        if catx == boundary[0][0]:
            direction = UP
    elif direction == UP:
        caty -= movespeed
        if caty == boundary[0][1]:
            direction = RIGHT
    
    DISPLAYSURF.blit(catImg, (catx, caty))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
