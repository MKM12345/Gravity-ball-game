import pygame

def move_ball(ball_rect, ball_velocity, GRAVITY):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball_velocity[1] = -10  # Jumping

    # Apply gravity
    ball_velocity[1] += GRAVITY

    # Update ball position
    ball_rect.move_ip(ball_velocity[0], ball_velocity[1])
