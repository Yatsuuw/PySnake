# Classe contenant les codes couleur RGB (constantes) pour le jeu
class Colors:
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 102)
    BLACK = (0, 0, 0)
    RED = (213, 50, 80)
    GREEN = (0, 255, 0)
    BLUE = (50, 153, 213)

    def __init__(self):
        self.white = Colors.WHITE
        self.yellow = Colors.YELLOW
        self.black = Colors.BLACK
        self.red = Colors.RED
        self.green = Colors.GREEN
        self.blue = Colors.BLUE

# Classe contenant les paramètres (constantes) de la fenêtre de jeu
class Window:
    GRID_SIZE = 20
    GRID_WIDTH = 30
    GRID_HEIGHT = 20
    CELL_SIZE = 20
    WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
    WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE

    FPS = 9

    def __init__(self):
        self.gridSize = Window.GRID_SIZE
        self.gridWidth = Window.GRID_WIDTH
        self.gridHeight = Window.GRID_HEIGHT
        self.cellSize = Window.CELL_SIZE
        self.windowWidth = Window.WINDOW_WIDTH
        self.windowHeight = Window.WINDOW_HEIGHT
        self.fps = Window.FPS
