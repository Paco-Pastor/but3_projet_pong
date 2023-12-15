import pygame


class PaddleSprite:
    def __init__(self):
        self.default = None
        self.large = None

    def setDefault(self, path):
        self.default = pygame.image.load(path)

    def setLarge(self, path):
        self.large = pygame.image.load(path)


DEFAULT = PaddleSprite()
DEFAULT.setDefault("./img/default_paddle.png")
DEFAULT.setLarge("./img/large_paddle.png")