import pygame
import sys

from src.ball import Ball
from src.event import Event
from src.paddle import Paddle


# GameArea est l'objet qui gère la session de jeu.
class Game:

    def __init__(self, screen, clock, FPS, score_max, player_count, bot_expert):
        # -- Stockage des valeurs données
        self.clock = clock
        self.FPS = FPS
        self.screen = screen
        self.score_max = score_max
        self.player_count = player_count
        self.bot_expert = bot_expert
        # -- Création des sous-surfaces

        self.border_rect = None
        self.border_area = None

        self.game_rect = None
        self.game_area = None

        # -- Création des composants
        self.left_paddle = None
        self.right_paddle = None

        self.ball = None
        # -- Gestionnaire de clés (utilisé pour les événements simultanés et continus)
        self.key_list = None

        self.score = [0, 0]
        self.fresh_start()

    # Réinitialisation du jeu
    def fresh_start(self):
        # -- Création des sous-surfaces
        self.border_rect = pygame.Rect(self.screen.get_width() * 0.05, self.screen.get_height() * 0.05,
                                       self.screen.get_width() * 0.9,
                                       self.screen.get_height() * 0.9)
        self.border_area = self.screen.subsurface(self.border_rect)

        self.game_rect = pygame.Rect(self.border_rect.left + 2, self.border_rect.top + 2, self.border_rect.width - 4,
                                     self.border_rect.height - 4)
        self.game_area = self.screen.subsurface(self.game_rect)

        # -- Création des composants
        test_paddle = Paddle(self.game_area)
        self.left_paddle = Paddle(self.game_area,
                                  y=self.game_area.get_height() // 2 - test_paddle.height // 2)
        self.right_paddle = Paddle(self.game_area,
                                   x=self.game_area.get_width() - self.left_paddle.width,
                                   y=self.game_area.get_height() // 2 - test_paddle.height // 2,
                                   left_side=False)
        self.ball = Ball(self.game_area, x=self.game_area.get_width() // 2, y=self.game_area.get_height() // 2,
                         collides_object=[[lambda: pygame.Rect(self.left_paddle.x, self.left_paddle.y,
                                                               self.left_paddle.hit_box.width,
                                                               self.left_paddle.hit_box.height), False],
                                          [lambda: pygame.Rect(self.right_paddle.x, self.right_paddle.y,
                                                               self.right_paddle.hit_box.width,
                                                               self.right_paddle.hit_box.height), True]])

        self.key_list = self.key_list = {pygame.K_DOWN: False, pygame.K_UP: False, pygame.K_z: False, pygame.K_s: False}

    # Exécution du jeu une fois
    def execute_once(self):
        self.input_management()
        if self.player_count == 1:
            self.one_player_action()
        else:
            self.two_players_action()
        self.display()
        self.clock.tick(self.FPS)
        for event in self.read_event():
            if not self.handling_event(event):
                return False
        return True

    # Gestion des événements du jeu
    def handling_event(self, event):
        # Lorsque la balle sort à droite ou à gauche de l'écran, ajout d'un point au score du joueur correspondant
        if event.type == Event.BALL_OUT:
            i = 0
            if event.extra:
                i = 1
            self.score[i] += 1
            self.fresh_start()
            if self.score[0] == self.score_max or self.score[1] == self.score_max:
                return False
        return True

    # Gestion des événements de l'utilisateur
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

            if self.key_list[pygame.K_z] and self.key_list[pygame.K_s]:
                self.key_list[pygame.K_z] = False
                self.key_list[pygame.K_s] = False

    """
    one_player_action handle the paddle movements when there is only one player
    the "bot" paddle has two levels
        - Normal : fail 40% of the time
        - Bot : Never fail + center itself when ball is far
    """

    def one_player_action(self):
        for e in self.key_list.keys():
            if e == pygame.K_UP and self.key_list[e]:
                self.left_paddle.move_up()

            elif e == pygame.K_DOWN and self.key_list[e]:
                self.left_paddle.move_down()

        # not bot expert mode : fail 40% of the time
        if not self.bot_expert:
            if pygame.time.get_ticks() % 5 < 2:
                return

        # allowed error for the bot
        approximation = self.right_paddle.hit_box.height // 2
        # distance x between the right border and the ball
        distance = self.game_area.get_width() - self.ball.hit_box.centerx
        # if ball is too far, bot can't place its paddle using the ball y
        if distance < self.screen.get_width() // 4:
            approximation = approximation * 0.8
            if self.ball.hit_box.centery < self.right_paddle.hit_box.centery - approximation:
                self.right_paddle.move_up()

            elif self.ball.hit_box.centery > self.right_paddle.hit_box.centery + approximation:
                self.right_paddle.move_down()


        elif self.bot_expert:
            # if bot expert mod is selected, when the ball is too far the bot adjust its paddle position to be in the
            # middle in the screen
            if self.right_paddle.hit_box.centery < self.game_area.get_height() // 2 - approximation:
                self.right_paddle.move_down()
            elif self.right_paddle.hit_box.centery > self.game_area.get_height() // 2 + approximation:
                self.right_paddle.move_up()

    """
    two_players_action handles the paddle movement when there is two players
    """

    def two_players_action(self):
        for e in self.key_list.keys():
            if e == pygame.K_UP and self.key_list[e]:
                self.right_paddle.move_up()

            elif e == pygame.K_DOWN and self.key_list[e]:
                self.right_paddle.move_down()

            elif e == pygame.K_z and self.key_list[e]:
                self.left_paddle.move_up()

            elif e == pygame.K_s and self.key_list[e]:
                self.left_paddle.move_down()

    # Lecture des événements
    def read_event(self):
        events = []
        events += self.ball.read_event()
        return events

    # Affichage du jeu à l'écran
    def display(self):
        self.screen.fill((0, 0, 0))
        self.border_area.fill((255, 255, 255))
        self.game_area.fill((0, 0, 0))

        self.draw_score_player1()
        self.draw_score_player2()

        # position of the line
        # if one player, 75% of the screen (ball detection zone of the bot)
        # if two players, middle of the screen
        x_position_line = self.game_area.get_width() // 4 * (4 - self.player_count)
        pygame.draw.line(self.game_area, (255, 255, 255), (x_position_line, 0),
                         (x_position_line, self.game_area.get_height()))

        self.left_paddle.display()
        self.right_paddle.display()

        self.ball.rotate()
        self.ball.movement()
        self.ball.display()
        pygame.display.update()

    def draw_score_player1(self):
        font = pygame.font.Font(None, 32)
        WHITE = (255, 255, 255)
        score_text = font.render("Score: " + str(self.score[0]), True, WHITE)
        self.screen.blit(score_text, (10, 5))

    def draw_score_player2(self):
        font = pygame.font.Font(None, 32)
        WHITE = (255, 255, 255)
        score_text = font.render("Score: " + str(self.score[1]), True, WHITE)
        self.screen.blit(score_text, (self.screen.get_width() - 100, 5))

    def run(self):
        running = True
        while running:
            running = self.execute_once()
