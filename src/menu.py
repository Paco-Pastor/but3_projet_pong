import pygame_menu
from src.game import start
import pygame

#création du menu
fontmenu = pygame_menu.font.FONT_8BIT

imagemenu = pygame_menu.baseimage.BaseImage(
    image_path="assets/background.jpg",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)

menutheme = pygame_menu.Theme(
    background_color=imagemenu,
    widget_font=fontmenu,
    title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE,
    title_font=fontmenu,
    title_offset=[250,0]

)

scoremax = None

# Création de la classe pour récupérer la valeur du score max choisi par le joueur
class MenuHandler:
    def __init__(self):
        self.scoremax = ('5', 1)

    def update_scoremax(self, item, indice):
        self.scoremax = item[0][1]

    def run(self):
        print(self.scoremax)
        start(self.scoremax)

#fonction du menu
def start_menu(width, height):
    pygame.init()
    menuHandler = MenuHandler()
    screen = pygame.display.set_mode((width, height))
    menu = pygame_menu.Menu('Pong eternal', width, height,theme=menutheme)
    menu.add.selector('Mode :', [('1 joueur', 1), ('2 joueurs', 2)])
    menu.add.selector('Score maximal :', [('5', 5), ('10', 10), ('20', 20)], onchange=menuHandler.update_scoremax)
    menu.add.selector('Graphisme :', [('faible', 1), ('moyen', 2), ('haut', 3), ('Photo realiste', 4)],default=1)
    menu.add.button('Jouer', menuHandler.run)
    menu.add.button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(screen)
