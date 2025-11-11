class Fruits():
    def __init__(self) -> None:
        self.x = random.randint(0, cell_size - FRUIT_SIZE)
        self.y = random.randint(0, cell_number - FRUIT_SIZE)
        self.position = vector2(self.x, self.y)
    def appears(self):
        rect = pygame.Rect(int(self.position.x), int(self.position.y), FRUIT_SIZE, FRUIT_SIZE)
        pygame.draw.rect(screen,FRUIT_COLOR,rect)