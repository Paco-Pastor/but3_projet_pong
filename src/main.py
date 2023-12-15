import time

import pygame, sys
from src.paddle import Paddle

pygame.init()

clock = pygame.time.Clock()
FPS = 150

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

paddle = Paddle(screen)
opponentPaddle = Paddle(screen, x=screen.get_width()-paddle.width, left_side=False)
keyList = {pygame.K_DOWN: False, pygame.K_UP: False}
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN:
            keyList[e.key] = True

        elif e.type == pygame.KEYUP:
            keyList[e.key] = False

        if keyList[pygame.K_UP] and keyList[pygame.K_DOWN]:
            keyList[pygame.K_UP] = False
            keyList[pygame.K_DOWN] = False

    for e in keyList.keys():
        if e == pygame.K_UP and keyList[e]:
            paddle.move_up()
            opponentPaddle.move_down()

        elif e == pygame.K_DOWN and keyList[e]:
            paddle.move_down()
            opponentPaddle.move_up()

        elif e == pygame.K_e and keyList[e]:
            keyList[e] = False
            paddle.size_up()
            opponentPaddle.size_down()

        elif e == pygame.K_f and keyList[e]:
            keyList[e] = False
            paddle.size_down()
            opponentPaddle.size_up()

    screen.fill((0,0,0))
    paddle.display()
    opponentPaddle.display()
    pygame.display.update()
    clock.tick(FPS)
