import random
import sys
import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)

# Initialize display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Game Project")

def main():
    """Main function containing the entire game logic."""
    clock = pygame.time.Clock()
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game logic
        # Add game logic here

        # Render game elements
        window.fill(BACKGROUND_COLOR)
        # Add rendering logic here
        pygame.display.flip()

        # Control frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()