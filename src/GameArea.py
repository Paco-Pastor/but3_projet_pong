import pygame, sys

from src.ball import Ball
from src.event import Event
from src.paddle import Paddle


# GameArea est l'objet qui gère la session de jeu.
class GameArea:
    def __init__(self, screen, clock, FPS, scoremax):
        # -- Stockage des valeurs données
        self.clock = clock
        self.FPS = FPS
        self.screen = screen
        self.scoremax = scoremax

        # -- Création des sous-surfaces
        self.border_rect = None
        self.border_area = None

        self.game_rect = None
        self.game_area = None

        # -- Création des composants
        self.paddle = None
        self.opponent_paddle = None

        self.ball = None
        # -- Gestionnaire de clés (utilisé pour les événements simultanés et continus)
        self.key_list = None

        self.score = [0, 0]
        self.reset()

    # Réinitialisation du jeu
    def reset(self):
        # -- Création des sous-surfaces
        self.border_rect = pygame.Rect(self.screen.get_width() * 0.05, self.screen.get_height() * 0.05,
                                       self.screen.get_width() * 0.9,
                                       self.screen.get_height() * 0.9)
        self.border_area = self.screen.subsurface(self.border_rect)

        self.game_rect = pygame.Rect(self.border_rect.left + 2, self.border_rect.top + 2, self.border_rect.width - 4,
                                     self.border_rect.height - 4)
        self.game_area = self.screen.subsurface(self.game_rect)

        # -- Création des composants
        self.paddle = Paddle(self.game_area)
        self.opponent_paddle = Paddle(self.game_area, x=self.game_area.get_width() - self.paddle.width, left_side=False)

        self.ball = Ball(self.game_area, x=self.game_area.get_width() // 2, y=self.game_area.get_height() // 2,
                         collides_object=[[lambda: pygame.Rect(self.paddle.x, self.paddle.y, self.paddle.paddle.width,
                                                              self.paddle.paddle.height), False],
                                          [lambda: pygame.Rect(self.opponent_paddle.x, self.opponent_paddle.y,
                                                              self.opponent_paddle.paddle.width,
                                                              self.opponent_paddle.paddle.height), True]])
     
        self.key_list = self.key_list = {pygame.K_DOWN: False, pygame.K_UP: False}

    # Exécution du jeu une fois
    def execute_once(self):
        self.input_management()
        self.display()
        self.clock.tick(self.FPS)
        for event in self.read_event():
            self.handling_event(event)

    # Gestion des événements du jeu
    def handling_event(self, event):
        # Lorsque la balle sort à droite ou à gauche de l'écran, ajout d'un point au score du joueur correspondant
        if event.type == Event.BALL_OUT:
            i = 0
            if event.extra:
                i = 1
            self.score[i] += 1
            self.reset()
            if self.score[0] == self.scoremax or self.score[1] == self.scoremax:
                pygame.quit()

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

        # CETTE UTILISATION EST UNIQUEMENT POUR DES TESTS. CE N'EST PAS UN COMPORTEMENT DE "OPPONENT_PADDLE" VALIDE
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

        self.paddle.display()
        self.opponent_paddle.display()
        self.ball.rotate()
        self.ball.movement()
        self.ball.display()
        pygame.display.update()
