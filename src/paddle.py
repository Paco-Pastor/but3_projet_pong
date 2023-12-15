import pygame
import src.images as img


class Paddle():
    def __init__(self, screen, x=0, y=0, height=100, move_gap=2, image= img.DEFAULT, left_side = True):
        self.paddle = None
        self.x = x
        self.y = y
        self.height = height
        self.width = 0
        self.move_gap = move_gap
        self.screen = screen

        self.large = False
        self.sprite = image
        self.left_side = left_side
        self.update_image(True)


    def update_image(self, factor_height = False):
        if self.large:
            used_image = self.sprite.large
        else:
            used_image = self.sprite.default
        rotated_image = pygame.transform.rotate(used_image, (1 - self.left_side * 2) * 90)
        if factor_height:
            scaled_image = pygame.transform.scale_by(rotated_image, self.height / rotated_image.get_height())
            self.width = scaled_image.get_width()
        else:
            scaled_image = pygame.transform.scale_by(rotated_image, self.width/ rotated_image.get_width())
            self.height = scaled_image.get_height()
        self.image = scaled_image
        self.width = self.image.get_width()


    def move_up(self):
        self.y = max(self.y - self.move_gap, self.screen.get_rect().top)

    def move_down(self):
        self.y = min(self.y + self.move_gap, self.screen.get_rect().bottom - self.height)

    def size_up(self):
        if not self.large:
            self.large = True
            self.y += self.height//2
            self.update_image()
            self.y -= self.height//2
            self.y = max(self.screen.get_rect().top, min(self.y, self.screen.get_rect().bottom - self.height))


    def size_down(self):
        if self.large:
            self.large = False
            self.y += self.height//2
            self.update_image()
            self.y -= self.height//2
            self.y = max(self.screen.get_rect().top, min(self.y, self.screen.get_rect().bottom - self.height))
    def display(self):
        self.paddle = self.screen.blit(self.image, pygame.Rect(self.x, self.y, self.width, self.height))

