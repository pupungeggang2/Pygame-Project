import sys, ast, pygame
import asset, UI, data, const, var
import scenetitle, scenefield

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.resolution, pygame.SCALED)
    pygame.display.set_caption('Desserterria')
    var.clock = pygame.time.Clock()

    load_font()
    load_image()
    load_data()

def load_font():
    pygame.font.init()

    try:
        asset.Font.main_32 = pygame.font.Font('Font/neodgm.ttf', 32)
    except:
        asset.Font.main_32 = pygame.font.SysFont(None, 32)

def load_image():
    pass

def load_data():
    pass

def main():
    while True:
        handle_scene()
        handle_input()

def handle_scene():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'field':
        scenefield.loop()

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            x = mouse[0]
            y = mouse[1]
            button = event.button

            if var.scene == 'title':
                scenetitle.mouse_up(x, y, button)

            elif var.scene == 'field':
                scenefield.mouse_up(x, y, button)

        if event.type == pygame.KEYDOWN:
            key = event.key

            if var.scene == 'title':
                scenetitle.key_down(key)

            elif var.scene == 'field':
                scenefield.key_down(key)

        if event.type == pygame.KEYUP:
            key = event.key

            if var.scene == 'title':
                scenetitle.key_up(key)

            elif var.scene == 'field':
                scenefield.key_up(key)


if __name__ == '__main__':
    init()
    main()