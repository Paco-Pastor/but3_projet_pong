import pygame

from src.GameArea import GameArea
#from src.GameArea import draw_score_player1,draw_score_player2


def start():
    pygame.init()
    pygame.font.init()

    clock = pygame.time.Clock()
    FPS = 200
    
    WIDTH, HEIGHT = 900, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    #GameArea.draw_score_player1()
    #GameArea.draw_score_player2()
    game = GameArea(screen, clock, FPS)

    while True:
        game.execute_once()
