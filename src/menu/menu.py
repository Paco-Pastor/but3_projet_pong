import pygame_menu
from game.startgame import start_the_game

#création du menu
fontmenu = pygame_menu.font.FONT_8BIT

imagemenu = pygame_menu.baseimage.BaseImage(
    image_path="ressources/images/background.jpg",
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
def start_menu(width, height,screen):
    menu = pygame_menu.Menu('Pong eternal', width, height,theme=menutheme)
    menu.add.selector('Mode :', [('1 joueur', 1), ('2 joueurs', 2)])
    menu.add.button('Jouer', start_the_game)
    menu.add.button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(screen)