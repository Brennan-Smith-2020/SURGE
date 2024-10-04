import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Color Grid")

def grid(gridSize, screenSize):
    TileSpacing = []
    for y in range(0, screenSize[1], gridSize):
        for x in range(0, screenSize[0], gridSize):
            TileSpacing.append((x, y))  # Store the position as a tuple
    return TileSpacing

# Create a grid of tiles with a size of 30 pixels
gridSize = 30
TileSpacing = grid(gridSize, (800, 600))

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Initialize colors for each tile (each tile gets a random color)
colors = [random_color() for _ in TileSpacing]

def debug():
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear the screen

        # Draw all rectangles in the grid
        for index, position in enumerate(TileSpacing):
            pygame.draw.rect(screen, colors[index], (position[0], position[1], gridSize, gridSize))

        pygame.display.flip()  # Update the display

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    debug()