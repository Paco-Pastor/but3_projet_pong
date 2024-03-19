import pygame
from src.score import Score
from src.GameArea import GameArea

score_player1 = Score()
score_player2 = Score()

def start():
    pygame.init()

    clock = pygame.time.Clock()
    FPS = 200

    WIDTH, HEIGHT = 900, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")

    game = GameArea(screen, clock, FPS)

    

    while True:
        game.execute_once()
