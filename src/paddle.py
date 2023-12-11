import pygame
import src.images as img


class Paddle():
    def __init__(self, screen, x=0, y=0, height=100, move_gap=2, image= img.DEFAULT_SPRITE, left_side = True):
        self.paddle = None
        self.x = x
        self.y = y
        self.height = height
        self.move_gap = move_gap
        self.screen = screen

        rotated_image = pygame.transform.rotate(image, (1 - left_side*2) * 90)
        scaled_image = pygame.transform.scale_by(rotated_image, self.height / rotated_image.get_height())
        self.image = scaled_image
        self.width = self.image.get_width()

    def move_up(self):
        self.y = max(self.y - self.move_gap, self.screen.get_rect().top)

    def move_down(self):
        self.y = min(self.y + self.move_gap, self.screen.get_rect().bottom - self.height)

    def display(self):
        self.paddle = self.screen.blit(self.image, pygame.Rect(self.x, self.y, self.width, self.height))

