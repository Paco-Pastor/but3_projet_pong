import pygame

from src.GameArea import GameArea

pygame.init()

clock = pygame.time.Clock()
FPS = 150

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

game = GameArea(screen, clock, FPS)
while True:
    game.execute_once()