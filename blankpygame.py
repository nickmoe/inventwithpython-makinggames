import pygame, sys
from pygame.locals import *

pygame.init()

size = (400, 300)
DISAPLYSURF = pygame.display.set_mode(size)
pygame.display.set_caption('Hello World!')

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()
