import pygame, sys
from pygame.locals import *

pygame.init()
DISAPLYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_catption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
