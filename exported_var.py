import pygame
from constants import Window

class ExportedVar:
    window = pygame.display.set_mode((Window.WINDOW_WIDTH, Window.WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    def __init__(self):
        self.window = ExportedVar.window
        self.clock = ExportedVar.clock
