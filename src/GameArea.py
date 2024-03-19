import pygame, sys

from src.ball import Ball
from src.event import Event
from src.paddle import Paddle


# GameArea is the object which manage the game session.
class GameArea:
    def __init__(self, screen, clock, FPS):
        # -- Store given values
        self.clock = clock
        self.FPS = FPS
        self.screen = screen

        # -- Create subsurfaces
        self.border_rect = None
        self.border_area = None

        self.game_rect = None
        self.game_area = None

        # -- Create components
        self.paddle = None
        self.opponent_paddle = None

        self.ball = None
        # -- Key manager (used for simultaneous and continuous events)
        self.key_list = None

        self.score = [0, 0]
        self.reset()

    def reset(self):
        # -- Create subsurfaces
        self.border_rect = pygame.Rect(self.screen.get_width() * 0.05, self.screen.get_height() * 0.05,
                                       self.screen.get_width() * 0.9,
                                       self.screen.get_height() * 0.9)
        self.border_area = self.screen.subsurface(self.border_rect)

        self.game_rect = pygame.Rect(self.border_rect.left + 2, self.border_rect.top + 2, self.border_rect.width - 4,
                                     self.border_rect.height - 4)
        self.game_area = self.screen.subsurface(self.game_rect)

        # -- Create components
        self.paddle = Paddle(self.game_area)
        self.opponent_paddle = Paddle(self.game_area, x=self.game_area.get_width() - self.paddle.width, left_side=False)

        self.ball = Ball(self.game_area, x=self.game_area.get_width() // 2, y=self.game_area.get_height() // 2,
                         collides_object=[lambda: pygame.Rect(self.paddle.x, self.paddle.y, self.paddle.paddle.width,
                                                              self.paddle.paddle.height),
                                          lambda: pygame.Rect(self.opponent_paddle.x, self.opponent_paddle.y,
                                                              self.opponent_paddle.paddle.width,
                                                              self.opponent_paddle.paddle.height)])
        # -- Key manager (used for simultaneous and continuous events)
        self.key_list = self.key_list = {pygame.K_DOWN: False, pygame.K_UP: False}

    # Executes once the program.
    def execute_once(self):
        self.input_management()
        self.display()
        self.clock.tick(self.FPS)
        for event in self.read_event():
            self.handling_event(event)

    def handling_event(self, event):
        if event.type == Event.BALL_OUT:
            i = 0
            if event.extra:
                i = 1
            self.score[i] += 1
            self.reset()

    # Fetch the event and use them
    def input_management(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                self.key_list[e.key] = True
                if e.key == pygame.K_SPACE:
                    self.ball.start()

            elif e.type == pygame.KEYUP:
                self.key_list[e.key] = False

            if self.key_list[pygame.K_UP] and self.key_list[pygame.K_DOWN]:
                self.key_list[pygame.K_UP] = False
                self.key_list[pygame.K_DOWN] = False

        # THIS USAGE IS ONLY FOR TEST. NOT A VALID "OPPONENT_PADDLE" BEHAVIOUR
        for e in self.key_list.keys():
            if e == pygame.K_UP and self.key_list[e]:
                self.paddle.move_up()
                self.opponent_paddle.move_down()

            elif e == pygame.K_DOWN and self.key_list[e]:
                self.paddle.move_down()
                self.opponent_paddle.move_up()

            elif e == pygame.K_e and self.key_list[e]:
                self.key_list[e] = False
                self.paddle.size_up()
                self.opponent_paddle.size_down()

            elif e == pygame.K_f and self.key_list[e]:
                self.key_list[e] = False
                self.paddle.size_down()
                self.opponent_paddle.size_up()

    def read_event(self):
        events = []
        events += self.ball.read_event()
        return events

    # Display it on screen
    def display(self):
        self.screen.fill((0, 0, 0))
        self.border_area.fill((255, 255, 255))
        self.game_area.fill((0, 0, 0))

        self.paddle.display()
        self.opponent_paddle.display()
        self.ball.rotate()
        self.ball.move()
        self.ball.display()
        pygame.display.update()
