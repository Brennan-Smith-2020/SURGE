import pygame
import sys
from playerController import update_position
import time

import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("")

# Initial positions and speed
Xposition = 400
Yposition = 300
speed = 0.1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update position and speed
    Xposition, Yposition = update_position(Xposition, Yposition, speed)

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw a rectangle at the current position
    pygame.draw.rect(screen, (255, 0, 0), (Xposition, Yposition, 50, 50))

    # Print the current speed and position
    print(f"Position: ({Xposition}, {Yposition}), Speed: {speed}")

     # Update the display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
