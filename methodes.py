import random, pygame
from constants import Colors, Window
from exported_var import ExportedVar

class Methodes:
    def __init__(self):
        pass

    def generate_food(snake):
        # Génère une nouvelle position de nourriture qui n'est pas sur le serpent
        while True:
            food = [random.randint(0, Window.GRID_WIDTH - 1), random.randint(0, Window.GRID_HEIGHT - 1)] # Position initiale de la nourriture
            if food not in snake.body:
                return food

    def display_message(message):
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, Colors.WHITE)
        text_rect = text.get_rect(center=(Window.WINDOW_WIDTH //2, Window.WINDOW_HEIGHT // 2))
        ExportedVar.window.blit(text, text_rect)
        pygame.display.update()
