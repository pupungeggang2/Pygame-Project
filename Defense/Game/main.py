import pygame, sys
import data, asset, UI, var, const
import scenetitle, scenelevelselect, scenegame

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.resolution)
    pygame.display.set_caption('Defense')
    var.clock = pygame.time.Clock()

    load_image()
    load_font()
    load_data()

def load_image():
    pass

def load_font():
    try:
        asset.Font.main_32 = pygame.font.Font('Font/neodgm.ttf', 32)
    except:
        asset.Font.main_32 = pygame.font.SysFont(None, 32)

def load_data():
    pass

def main():
    while True:
        var.clock.tick(var.FPS)
        handle_input()
        handle_scene()

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            x = mouse[0]
            y = mouse[1]
            button = event.button

            if var.scene == 'title':
                scenetitle.mouse_up(x, y, button)

            elif var.scene == 'level_select':
                scenelevelselect.mouse_up(x, y, button)

            elif var.scene == 'game':
                scenegame.mouse_up(x, y, button)

def handle_scene():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'level_select':
        scenelevelselect.loop()

    elif var.scene == 'game':
        scenegame.loop()
init()
main()