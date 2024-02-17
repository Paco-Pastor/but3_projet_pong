import pygame

from GameArea import GameArea

pygame.init()

clock = pygame.time.Clock()
FPS = 200

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

game = GameArea(screen, clock, FPS)


while True:
    game.execute_once()