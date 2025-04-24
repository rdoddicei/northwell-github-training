# filepath: basic-game-project/basic-game-project/src/game.py

import random
import sys
import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Game Project")

# Game variables
running = True
clock = pygame.time.Clock()

def game_loop():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic goes here

        # Fill the background
        window.fill((0, 0, 0))

        # Render game elements here

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()