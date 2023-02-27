import pygame
from pygame.constants import QUIT

pygame.init()

screen = width, heigth = 800, 600

WHITE = 255, 255, 255
BLACK = 0, 0, 0
YELLOW = 255, 255, 0
RED = 255, 0, 0

main_surface = pygame.display.set_mode(screen)


ball = pygame.Surface((20, 20))
ball.fill(WHITE)
ball_rect = ball.get_rect()
ball_speed = [1, 1]


is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_rect = ball_rect.move(ball_speed)

    if ball_rect.bottom >= heigth or ball_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]
        ball.fill(YELLOW)

    if ball_rect.right >= width or ball_rect.left <= 0:
        ball_speed[0] = - ball_speed[0]
        ball.fill(RED)
    
    main_surface.fill(BLACK)
    main_surface.blit(ball, ball_rect)


    pygame.display.flip()