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


#fonction du menu
def start_menu(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    menu = pygame_menu.Menu('Pong eternal', width, height,theme=menutheme)
    menu.add.selector('Mode :', [('1 joueur', 1), ('2 joueurs', 2)])
    menu.add.button('Jouer', start)
    menu.add.button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(screen)