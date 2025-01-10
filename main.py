import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('pygbag Test')

# Define a color
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up a rectangle
rect_x, rect_y = 400, 300
rect_width, rect_height = 50, 50
rect_speed_x, rect_speed_y = 5, 5

# Main game loop
clock = pygame.time.Clock()

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the rectangle's position
    rect_x += rect_speed_x
    rect_y += rect_speed_y

    # Bounce the rectangle off the walls
    if rect_x + rect_width > 800 or rect_x < 0:
        rect_speed_x = -rect_speed_x
    if rect_y + rect_height > 600 or rect_y < 0:
        rect_speed_y = -rect_speed_y

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
