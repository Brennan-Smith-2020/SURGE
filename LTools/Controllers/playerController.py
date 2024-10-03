def update_position(Xposition, Yposition, speed=0.1):
    import pygame
    import sys
    import time
    keys = pygame.key.get_pressed()
    
    # Move the position based on key presses
    if keys[pygame.K_w]:
        Yposition -= speed
    if keys[pygame.K_s]:
        Yposition += speed
    if keys[pygame.K_a]:
        Xposition -= speed
    if keys[pygame.K_d]:
        Xposition += speed
    
    return Xposition, Yposition


### - DEBUGGING GAME LOOP

def debugger(): 
    import pygame
    import sys
    import time
    
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Move the Square for Debugging")

    # Initial positions and speed
    Xposition = 400
    Yposition = 300
    speed = 0.1

    def adjust_speed(speed):
        keys = pygame.key.get_pressed()
        
        # Increase or decrease speed with key presses
        if keys[pygame.K_UP]:  # Increase speed
            speed += 0.1
            time.sleep(0.1)
        if keys[pygame.K_DOWN]:  # Decrease speed
            speed -= 0.1  # Ensure speed doesn't go below 1
            time.sleep(0.1)
        
        return speed


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update position and speed
        Xposition, Yposition = update_position(Xposition, Yposition, speed)
        speed = adjust_speed(speed)

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw a rectangle at the current position
        pygame.draw.rect(screen, (255, 0, 0), (Xposition, Yposition, 50, 50))

        # Print the current speed and position
        print(f"Position: ({Xposition}, {Yposition}), Speed: {speed}")

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    debugger()

