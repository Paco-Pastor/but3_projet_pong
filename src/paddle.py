import pygame
import src.images as img  # Importation des images

# La classe Paddle implémente une raquette pour le jeu Pong utilisable avec Pygame
class Paddle:
    # Création de l'instance de la raquette
    def __init__(self, screen, x=0, y=0, height=100, move_gap=2, image=img.DEFAULT_PADDLE_SKIN, left_side=True):
        # -- Stockage des informations sur l'écran
        self.screen = screen
        # -- Données de la raquette
        self.hit_box = None
        self.x = x
        self.y = y
        self.height = height
        self.move_gap = move_gap
        # - sera automatiquement défini dans "update_image"
        self.width = None

        # -- Données relatives au sprite
        self.large = False
        self.sprite = image
        self.left_side = left_side
        # - sera automatiquement défini dans "update_image"
        self.image = None

        self.update_image(True)

    # Mettre à jour l'image à afficher : quelle image, sa taille, sa rotation, ...
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
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)

    # Déplacer la raquette vers le haut sans dépasser les bords de l'écran
    def move_up(self):
        self.y = max(self.y - self.move_gap, self.screen.get_rect().top)

    # Déplacer la raquette vers le bas sans dépasser les bords de l'écran
    def move_down(self):
        self.y = min(self.y + self.move_gap, self.screen.get_rect().bottom - self.height)

    # Mettre à jour l'image et la position de la raquette en une grande raquette
    def size_up(self):
        if not self.large:
            self.large = True
            self.y += self.height // 2
            self.update_image()
            self.y -= self.height // 2
            self.y = max(self.screen.get_rect().top, min(self.y, self.screen.get_rect().bottom - self.height))

    # Mettre à jour l'image et la position de la raquette en une raquette par défaut
    def size_down(self):
        if self.large:
            self.large = False
            self.y += self.height // 2
            self.update_image()
            self.y -= self.height // 2
            self.y = max(self.screen.get_rect().top, min(self.y, self.screen.get_rect().bottom - self.height))

    # Afficher la raquette à l'écran
    def display(self):
        self.hit_box = self.screen.blit(self.image, pygame.Rect(self.x, self.y, self.width, self.height))
