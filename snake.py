
from numpy import full
import pygame,sys,random
from pygame.math import Vector2 as vector2 

FRUIT_COLOR = (126, 166, 114)
FRUIT_SIZE = 20

cell_size = 800 
cell_number = 600
class Fruits():
    def __init__(self) -> None:
        self.x = random.randint(0, cell_size - FRUIT_SIZE)
        self.y = random.randint(0, cell_number - FRUIT_SIZE)
        self.position = vector2(self.x, self.y)
    def appears(self):
        rect = pygame.Rect(int(self.position.x), int(self.position.y), FRUIT_SIZE, FRUIT_SIZE)
        pygame.draw.rect(screen,FRUIT_COLOR,rect)

class Snake():
    def __init__(self) -> None:
        self.body = [vector2(100,100), vector2(120,100), vector2(140,100)]
        self.direction = vector2(1,0)
    def grown(self):
        for score in self.body:
            x_pos = int(score.x)
            y_pos = int(score.y)
            groth = pygame.Rect(x_pos, y_pos, FRUIT_SIZE, FRUIT_SIZE)
            pygame.draw.rect(screen,('yellow'),groth)
    def movement(self):
        new_head = self.body[0] + self.direction * FRUIT_SIZE
        # wrap horizontally
        if new_head.x >= cell_size:
            new_head.x = 0
        elif new_head.x < 0:
            new_head.x = cell_size - FRUIT_SIZE
        # wrap vertically
        if new_head.y >= cell_number:
            new_head.y = 0
        elif new_head.y < 0:
            new_head.y = cell_number - FRUIT_SIZE
        # update body: add new head, drop last
        self.body = [new_head] + self.body[:-1]
        
pygame.init()  # type: ignore[attr-defined]


WHITE = (255, 255, 255)


screen = pygame.display.set_mode((cell_size,cell_number))

clock = pygame.time.Clock()
#si la serpiente no choca no mere y si no muere el juego sigue

#creamos la serpiente


death = False

#mientras no este muerto el juego sigue

#ya existe la creaciion ded frutas asi que ahora debemos implementarla

fruit = Fruits()
snake = Snake()

scree_update = pygame.USEREVENT  # type: ignore[attr-defined]
pygame.time.set_timer(scree_update,150)
while not death:
    #mantiene la pantalla activa
    for event in pygame.event.get():
#si no se quiere seguir se puede cerrar
        if event.type == pygame.QUIT:  # type: ignore[attr-defined]
            pygame.quit()  # type: ignore[attr-defined]
            sys.exit()
        if event.type == scree_update:
            snake.movement()
        if event.type == pygame.KEYDOWN:  # type: ignore[attr-defined]
            if event.key == pygame.K_UP and snake.direction.y != 1:  # type: ignore[attr-defined]
                snake.direction = vector2(0,-1)
            elif event.key == pygame.K_DOWN and snake.direction.y != -1:  # type: ignore[attr-defined]
                snake.direction = vector2(0,1)
            elif event.key == pygame.K_LEFT and snake.direction.x != 1:  # type: ignore[attr-defined]
                snake.direction = vector2(-1,0)
            elif event.key == pygame.K_RIGHT and snake.direction.x != -1:  # type: ignore[attr-defined]
                snake.direction = vector2(1,0)
    #hacems que no se vaya verguiado volao sino que se vaya lento

    #la pantalla ahora es blanca
    screen.fill(WHITE)
    fruit.appears()
    snake.grown()
    #actualiza los fps
    pygame.display.update()
    #mantiene los fps en 60
    clock.tick(60)
    