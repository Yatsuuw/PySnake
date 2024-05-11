import pygame
from constants import Window, Colors
from exported_var import ExportedVar

class Snake:
    def __init__(self):
        self.head = [Window.GRID_WIDTH // 2, Window.GRID_HEIGHT // 2]
        #self.body = [[self.head[0], self.head[1]], [self.head[0] - 1, self.head[1]], [self.head[0] - 2, self.head[1]]]
        self.body = [self.head]
        self.direction = None

    # Déplacements de la tête du serpent en fonction de sa direction
    def move(self):
        if self.direction == "RIGHT":
            self.head[0] += 1
        elif self.direction == "LEFT":
            self.head[0] -= 1
        elif self.direction == "UP":
            self.head[1] -= 1
        elif self.direction == "DOWN":
            self.head[1] += 1

        # Ajout de la nouvelle position de la tête à la liste du corps
        self.body.insert(0, list(self.head))

    def grow(self):
        self.move() # Le serpent grandit en appelant la méthode move()
        # Supprime la dernière case du corps du serpent s'il ne vient pas de manger de la nourriture
        if self.body[-1] != self.body[-2]:
            self.body.pop()
    
    def draw(self):
        # Dessine chaque segment du corps du serpent
        for segment in self.body:
            pygame.draw.rect(ExportedVar.window, Colors.GREEN, (segment[0] * Window.CELL_SIZE, segment[1] * Window.CELL_SIZE, Window.CELL_SIZE, Window.CELL_SIZE))

    # Vérifie les collisions avec les bords de la fenêtre et avec lui-même
    def check_collision(self, food_position):
        if self.head[0] >= Window.GRID_WIDTH or self.head[0] < 0 or self.head[1] >= Window.GRID_HEIGHT or self.head[1] < 0:
            if self.head != food_position: # Vérifie si la tête n'est pas sur la position de la nourriture
                return True
        for segment in self.body[1:]:
            if self.head == segment:
                return True
        return False
