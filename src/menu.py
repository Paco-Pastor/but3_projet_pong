import pygame_menu

from src.GameArea import GameArea
import pygame

# création du menu
fontmenu = pygame_menu.font.FONT_8BIT

imagemenu = pygame_menu.baseimage.BaseImage(
    image_path="assets/background.jpg",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)

menutheme = pygame_menu.Theme(
    background_color=imagemenu,
    widget_font=fontmenu,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    title_font=fontmenu,
    title_offset=[250, 0]

)


class Menu(pygame_menu.Menu):
    def __init__(self, title, width, height, theme):
        self.screen = pygame.display.set_mode((width, height))
        super().__init__(title, width, height, theme=theme)

        pygame.display.set_caption(title)
        self.game_mode_selector = self.add.selector('Mode :', [('1 joueur', 1), ('2 joueurs', 2)])
        self.score_max_selector = self.add.selector('Score maximal :', [('5', 5), ('10', 10), ('20', 20)])
        self.add.button('Jouer', self.start_game)
        self.add.button('Quitter', pygame_menu.events.EXIT)
        self.mainloop(self.screen)

    def start_game(self):
        game_mode_value = self.game_mode_selector.get_value()[0][1]
        score_max_value = self.score_max_selector.get_value()[0][1]

        clock = pygame.time.Clock()
        FPS = 200

        game = GameArea(self.screen, clock, FPS, score_max_value, game_mode_value)
        running = True
        while running:
            running = game.execute_once()


# fonction du menu
def start_menu(width, height):
    pygame.init()
    Menu('Pong eternal', width, height, menutheme)
