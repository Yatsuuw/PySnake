import pygame, sys
from constants import Colors, Window
from snake import Snake
from methodes import Methodes
from exported_var import ExportedVar

# Initialisation de Pygame
pygame.init()
pygame.display.set_caption("Snake Game")


# Fonction principale
def main():
    snake = Snake() # Initialisation du serpent
    food = Methodes.generate_food(snake)
    score = 0

    while True:
        ExportedVar.window.fill(Colors.BLACK) # Remplir la fenêtre d'une couleur

        for event in pygame.event.get(): # Gestion des évènements
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed() # Récupération des touches préssées par le joueur
        # Changements de direction du serpent en fonction des touchées préssées
        if keys[pygame.K_RIGHT] and snake.direction != "LEFT":
            snake.direction = "RIGHT"
        elif keys[pygame.K_LEFT] and snake.direction != "RIGHT":
            snake.direction = "LEFT"
        elif keys[pygame.K_UP] and snake.direction != "DOWN":
            snake.direction = "UP"
        elif keys[pygame.K_DOWN] and snake.direction != "UP":
            snake.direction = "DOWN"
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        snake.move() #Déplacement du serpent
        # Si la tête du serpent atteint la nourriture, le serpent grandit et une nouvelle position de nourriture est générée
        if snake.head == food:
            snake.grow()
            food = Methodes.generate_food(snake)
            score += 1
        else:
            snake.body.pop() # Supprime le dernier segment du corps du serpent

        # Vérifie les collisions et traitement du cas de défaite
        if snake.check_collision(food) and snake.direction != None:
            Methodes.display_message("Game Over! Press Q to Quit or R to Restart")
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                        elif event.key == pygame.K_r:
                            main()

        # Dessine le serpent et la nourriture
        snake.draw()
        pygame.draw.rect(ExportedVar.window, Colors.RED, (food[0] * Window.CELL_SIZE, food[1] * Window.CELL_SIZE, Window.CELL_SIZE, Window.CELL_SIZE))

        # Affichage du score à l'écran
        font = pygame.font.Font(None, 30)
        score_text = font.render(f"Score: {score}", True, Colors.WHITE)
        ExportedVar.window.blit(score_text, (10, 10))

        pygame.display.update() # Mettre à jour l'affichage
        ExportedVar.clock.tick(Window.FPS) # Limite le nombre d'images par seconde (vitesse du serpent)

if __name__ == "__main__":
    main()
