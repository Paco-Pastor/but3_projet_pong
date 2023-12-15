import pygame


class PaddleSprite:
    def __init__(self):
        self.default = None
        self.large = None

    def set_default(self, path):
        self.default = pygame.image.load(path)

    def set_large(self, path):
        self.large = pygame.image.load(path)


DEFAULT = PaddleSprite()
DEFAULT.set_default("./img/default_paddle.png")
DEFAULT.set_large("./img/large_paddle.png")