import pygame


# Skin de la balle et des paddles
class PaddleSkin:
    def __init__(self, default, large):
        self.default = pygame.image.load(default)
        self.large = pygame.image.load(large)


# PaddleSkin Constant
DEFAULT_PADDLE_SKIN = PaddleSkin("./src/img/default_paddle.png", "./src/img/large_paddle.png")
DEFAULT_BALL = pygame.image.load("./src/img/default_ball.png")
