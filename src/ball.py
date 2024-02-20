import math
import os
import random
import sys

import pygame
import src.images as img

def does_collide(p1, p2):
    test_p1_x = p1.left > p2.left and p1.left < p2.right
    test_p1_y = p1.top > p2.top and p1.top < p2.bottom
    test_p2_x = p2.left > p1.left and p2.left < p1.right
    test_p2_y = p2.top > p1.top and p2.top < p1.bottom
    return (test_p1_x or test_p2_x) and (test_p1_y or test_p2_y)


# Ball implements a Pong's ball usable with pygame

class Ball:
    # Create the Ball instance
    def __init__(self, screen, image=img.DEFAULT_BALL, x=0, y=0, radius=15, orientation=0, collides_object=[]):
        # -- Store data
        self.screen = screen
        # -- Ball data
        self.ball = None
        self.x = x
        self.y = y
        self.radius = radius

        # -- Sprite relatives data
        self.sprite = image
        self.orientation = orientation
        self.direction = None
        # - will be automatically defined in "update_image"
        self.image = None
        self.update_image()
        self.update_x = False
        self.update_y = False
        self.speed = 2
        self.collides_object = collides_object

    def update_image(self):
        rotated_image = pygame.transform.rotate(self.sprite, self.orientation)
        scaled_image = pygame.transform.scale_by(rotated_image, self.radius / (self.sprite.get_width()//2))
        self.image = scaled_image

    def start(self):
        self.direction = self.orientation

    def move(self):
        if self.direction is not None:
            self.x = self.x + self.speed * math.cos(Ball.radian(self.direction))
            self.y = self.y + self.speed * math.sin(Ball.radian(self.direction))

            monte = self.direction > 180
            droite = self.direction < 90 or self.direction > 270
            self.invalid_y = self.y - self.radius <= 0 or self.y + self.radius > self.screen.get_height()
            self.invalid_x  = False
            for i in self.collides_object:
                self.invalid_x = self.invalid_x or does_collide(self.ball, i())
            if self.x + self.radius <= 0 or self.x-self.radius >= self.screen.get_width():
                sys.exit()
            if (self.invalid_x and not self.update_x) or (self.invalid_y and not self.update_y) :

                if self.invalid_y:
                    monte = not monte
                    self.direction = (360-(self.direction+90))%360
                if self.invalid_x:
                    self.speed = min(self.speed*1.05, 5)
                    print(self.speed)
                    droite = not droite
                    self.direction = (360-(self.direction-90))%360

                self.direction = (self.direction + random.randint(-10,10))%360



            self.update_x = self.invalid_x
            self.update_y = self.invalid_y
            ok = not(self.invalid_x or self.invalid_y)

            while not ok:
                self.direction = (self.direction + 90)%360
                if self.direction%90==0:
                    self.direction = (self.direction + 1)%360

                ok_monte = (monte and self.direction > 180)
                ok_descend = (not monte and self.direction < 180)

                ok_droite = (droite and (self.direction < 90 or self.direction > 270))
                ok_gauche = (not droite and self.direction > 90 and self.direction<270)
                ok = (ok_gauche or ok_droite) and (ok_descend or ok_monte)


    def radian(degree):
        return math.radians(degree)
    def rotate(self):
        self.orientation = (self.orientation +1)%360
    def display(self):
        self.update_image()
        rect = pygame.Rect((self.x - self.image.get_width()//2, self.y - self.image.get_height()//2, self.image.get_width(), self.image.get_height()))
        self.ball = self.screen.blit(self.image, rect)
        direction = self.direction
        if direction == None:
            direction = self.orientation
        pygame.draw.line(self.screen, (255,255,0), (self.x, self.y), (self.x + 50*math.cos(Ball.radian(direction)), self.y + 50*math.sin(Ball.radian(direction))))
