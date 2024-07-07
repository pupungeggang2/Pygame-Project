import sys, pygame
import asset, const, var, UI
import scenetitle, sceneready, scenegame
import json

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.resolution)
    pygame.display.set_caption('Card Real Time')
    var.clock = pygame.time.Clock()
    load_font()
    load_image()
    load_data()

def load_font():
    pygame.font.init()
    asset.Font.neodgm_32 = pygame.font.Font('Font/neodgm.ttf', 32)

def load_image():
    pass

def load_data():
    f = open('Data/card.txt', 'r')
    const.Data.card = json.load(f)
    f.close()
    f = open('Data/equipment.txt', 'r')
    const.Data.equipment = json.load(f)
    f.close()
    f = open('Data/item.txt', 'r')
    const.Data.item = json.load(f)
    f.close()
    f = open('Data/start_deck.txt', 'r')
    const.Data.start_deck = json.load(f)
    f.close()

def main():
    while True:
        var.clock.tick(var.FPS)
        handle_scene()
        handle_input()

def handle_scene():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'ready':
        sceneready.loop()

    elif var.scene == 'game':
        scenegame.loop()

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
            
            elif var.scene == 'ready':
                sceneready.mouse_up(x, y, button)

            elif var.scene == 'game':
                scenegame.mouse_up(x, y, button)

        if event.type == pygame.KEYDOWN:
            key = event.key

            if var.scene == 'title':
                scenetitle.key_down(key)

            elif var.scene == 'ready':
                sceneready.key_down(key)

            elif var.scene == 'game':
                scenegame.key_down(key)

        if event.type == pygame.KEYUP:
            key = event.key

            if var.scene == 'title':
                scenetitle.key_up(key)

            elif var.scene == 'ready':
                sceneready.key_up(key)

            elif var.scene == 'game':
                scenegame.key_up(key)

if __name__ == '__main__':
    init()
    main()