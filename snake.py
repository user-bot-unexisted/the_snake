import pygame

import sys 

pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
#si la serpiente no choca no mere y si no muere el juego sigue
death = False

#mientras no este muerto el juego sigue
while not death:
    #mantiene la pantalla activa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)