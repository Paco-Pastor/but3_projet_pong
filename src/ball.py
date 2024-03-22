import math
import random

import pygame
import src.images as img
from src.event import Event


class Ball:
    def __init__(self, screen, image=img.DEFAULT_BALL, x=0, y=0, radius=30, orientation=0, collides_object=None):
        if collides_object is None:
            collides_object = []
        self.screen = screen
        # -- Données de la balle
        self.hit_box = pygame.Rect(x, y, radius, radius)
        self.x = x
        self.y = y
        self.radius = radius

        self.moving = False
        # -- Données relatives au sprite
        self.sprite = image
        self.orientation = orientation
        self.direction = None

        self.image = None
        self.update_image()
        self.speed = 1.75
        self.collides_object = collides_object

        # event queue
        self.event = []


    """
    update_image uses the sprite to create an image of the ball with the current orientation,
    """
    def update_image(self):
        # rotate it
        rotated_image = pygame.transform.rotate(self.sprite, -self.orientation)
        # set it the right size
        scaled_image = pygame.transform.scale_by(rotated_image, self.radius / (self.sprite.get_width()))
        self.image = scaled_image

    """
    start allow the ball to move
    """
    def start(self):
        if not self.moving:
            self.direction = self.orientation
            self.moving = True

    """
    movement update the ball position / direction after some checks
    """
    def movement(self):
        # ball actually not moving, quit now
        if not self.moving:
            return

        # Ball is out of its parent borders : create an event and quit now
        if self.hit_box.left <= 0 or self.hit_box.right >= self.screen.get_width():
            self.moving = False
            on_left_side = self.hit_box.left <= 0
            event = Event(Event.BALL_OUT, on_left_side)
            self.event.append(event)
            return

        change_x, change_y = False, False

        # is the ball moving to the top of the screen?
        to_top = self.direction > 180

        # Ball touched a border
        if (to_top and self.hit_box.top <= 0) or (not to_top and self.hit_box.bottom > self.screen.get_height()):
            change_y = True

        # is the ball moving to the right of the screen?
        to_right = self.direction < 90 or self.direction > 270

        # Ball touched a paddle
        for get_object_hit_box, on_right in self.collides_object:
            if to_right == on_right:
                if self.does_collide_x_limited(get_object_hit_box(), on_right):
                    change_x = True
                    break

        # update the ball direction
        self.direction = self.new_direction(change_x, change_y)

        # update the ball position
        self.x = self.x + self.speed * math.cos(math.radians(self.direction))
        self.y = self.y + self.speed * math.sin(math.radians(self.direction))

    """
    does_collide_x_limited checks if the ball is colliding with another object, but ensure that they're not 
    already superposed (on the x plan)
    """
    def does_collide_x_limited(self, object_hit_box, on_right):
        test_y = object_hit_box.top < self.hit_box.centery < object_hit_box.bottom

        if on_right:
            test_x = object_hit_box.left < self.hit_box.right < object_hit_box.centerx
        else:
            test_x = object_hit_box.centerx < self.hit_box.left < object_hit_box.right

        return test_x and test_y

    """
    new_direction returns a new direction angle switch side when required + adding a small random variation
    """
    def new_direction(self, change_x, change_y):
        direction = self.direction

        to_right = direction < 90 or direction > 270
        to_top = direction > 180

        # change direction of the ball (impact with a wall)
        if change_y:
            delta = direction % 180 - 90
            if to_top:
                direction = (90 - delta) % 360
            else:
                direction = (270 - delta) % 360
            to_top = not to_top

        # change direction of the ball (impact with a paddle)
        if change_x:
            delta = (90 + direction) % 180
            if to_right:
                direction = (270 - delta) % 360
            else:
                direction = (90 - delta) % 360
            to_right = not to_right

        # add a small random variation (not perfect collision)
        if change_x or change_y:
            new_direction = 0
            stay = True
            while stay:
                random_angle = random.randint(-10, 10)
                new_direction = (random_angle + direction) % 360
                new_to_right = (new_direction < 90 or new_direction > 270)
                new_to_top = new_direction > 180
                stay = new_to_right != to_right or new_to_top != to_top or new_direction % 90 == 0
            direction = new_direction
        return direction

    """
    rotate just keep the balls rotating itself
    """
    def rotate(self):
        self.orientation = (self.orientation + 1) % 360


    """
    display print on the parent screen the ball
    """
    def display(self):
        self.rotate()
        self.update_image()
        image_rect = pygame.Rect((self.x - self.image.get_width() // 2, self.y - self.image.get_height() // 2,
                                  self.image.get_width(), self.image.get_height()))
        self.hit_box = pygame.Rect((self.x - self.radius // 2, self.y - self.radius // 2, self.radius, self.radius))
        self.screen.blit(self.image, image_rect)


    """
    read_event returns the event list and clear it
    """
    def read_event(self):
        events = self.event[:]
        self.event.clear()
        return events
