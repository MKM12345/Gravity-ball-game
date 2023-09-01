import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRAVITY = 0.5
BALL_SPEED = 5

# Colors
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Ball Game")

# Load assets
ball = pygame.image.load("assets/ball.png")
ball_rect = ball.get_rect()
ball_rect.center = (WIDTH // 2, HEIGHT // 2)

rect = pygame.image.load("assets/rect.png")
rect_rect = rect.get_rect()
rect_rect.center = (WIDTH // 2, HEIGHT // 2 + 100)

# Initialize ball variables
ball_velocity = [0, 0]
jumping = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                ball_velocity[1] = -10  # Jumping

    # Apply gravity
    ball_velocity[1] += GRAVITY

    # Update ball position
    ball_rect.move_ip(ball_velocity[0], ball_velocity[1])

    # Check collision with rect
    if ball_rect.colliderect(rect_rect):
        # Handle collision here

    # Draw everything
    screen.fill(WHITE)
    screen.blit(ball, ball_rect)
    screen.blit(rect, rect_rect)
    pygame.display.flip()
