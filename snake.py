import pygame,sys
from random import randint as randoms
from fruit import Fruits as points 

pygame.init()


x = 800 
y = 600
class Fruits():
    def __init__(self) -> None:
        self.x = random(x,y)
        self.y = random(x,y)

screen = pygame.display.set_mode((x,y))

clock = pygame.time.Clock()
#si la serpiente no choca no mere y si no muere el juego sigue
death = False

#mientras no este muerto el juego sigue
while not death:
    #mantiene la pantalla activa
    for event in pygame.event.get():
#si no se quiere seguir se puede cerrar
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#actualiza los fps
    pygame.display.update()
#la pantalla ahora es blanca
    screen.fill('white')
#mantiene los fps en 60
    clock.tick(60)
    