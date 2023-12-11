import pygame
import pygame_menu

pygame.init()

# couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# paramètres de l'écran
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
# framerate
clock = pygame.time.Clock()
FPS = 60

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

def start_the_game():
    print("start")

#fonction du menu
def menu():
    menu = pygame_menu.Menu('Pong eternal', WIDTH, HEIGHT,theme=menutheme)
    menu.add.selector('Mode :', [('1 joueur', 1), ('2 joueurs', 2)])
    menu.add.button('Jouer', start_the_game)
    menu.add.button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(screen)

#fonction princiaple
def main():
    running = True
    while running :
        menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(FPS)   

main()
