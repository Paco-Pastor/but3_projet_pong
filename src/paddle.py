import pygame
import src.images as img


# Paddle implements a Pong's paddle usable with pygame
class Paddle:
    # Create the Paddle instance
    def __init__(self, screen, x=0, y=0, height=100, move_gap=2, image=img.DEFAULT_PADDLE_SKIN, left_side=True):
        # -- Store screen information
        self.screen = screen
        # -- Paddle data
        self.paddle = None
        self.x = x
        self.y = y
        self.height = height
        self.move_gap = move_gap
        # - will be automatically defined in "update_image"
        self.width = None

        # -- Sprite relatives data
        self.large = False
        self.sprite = image
        self.left_side = left_side
        # - will be automatically defined in "update_image"
        self.image = None

        self.update_image(True)

    # Update the image to display : which image, its size, its rotation, ...
    def update_image(self, factor_height=False):
        if self.large:
            used_image = self.sprite.large
        else:
            used_image = self.sprite.default
        rotated_image = pygame.transform.rotate(used_image, (1 - self.left_side * 2) * 90)
        if factor_height:
            scaled_image = pygame.transform.scale_by(rotated_image, self.height / rotated_image.get_height())
            self.width = scaled_image.get_width()
        else:
            scaled_image = pygame.transform.scale_by(rotated_image, self.width / rotated_image.get_width())
            self.height = scaled_image.get_height()
        self.image = scaled_image
        self.width = self.image.get_width()

    # make Y position of the Paddle high without getting out of the borders
    def move_up(self):
        self.y = max(self.y - self.move_gap, self.screen.get_rect().top)

    # make Y position of the Paddle higher without getting out of the borders
    def move_down(self):
        self.y = min(self.y + self.move_gap, self.screen.get_rect().bottom - self.height)

    # update the paddle image and position into large paddle
    def size_up(self):
        if not self.large:
            self.large = True
            self.y += self.height // 2
            self.update_image()
            self.y -= self.height // 2
            self.y = max(self.screen.get_rect().top, min(self.y, self.screen.get_rect().bottom - self.height))

    # update the paddle image and position into default paddle
    def size_down(self):
        if self.large:
            self.large = False
            self.y += self.height // 2
            self.update_image()
            self.y -= self.height // 2
            self.y = max(self.screen.get_rect().top, min(self.y, self.screen.get_rect().bottom - self.height))

    # display the paddle on the screen
    def display(self):
        self.screen.fill( (255,0,0),pygame.Rect(self.x, self.y, self.width, self.height))
        self.paddle = self.screen.blit(self.image, pygame.Rect(self.x, self.y, self.width, self.height))
