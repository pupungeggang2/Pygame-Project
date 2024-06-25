import pygame, sys

import var, const, asset, UI
import scenetitle, scenefield, scenegame

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.resolution)
    pygame.display.set_caption('Card')
    var.clock = pygame.time.Clock()
    load_font()
    load_image()

def main():
    while True:
        var.clock.tick(var.FPS)
        handle_input()
        handle_scene()

def load_font():
    pygame.font.init()
    asset.Font.neodgm_32 = pygame.font.Font('Font/neodgm.ttf', 32)

def load_image():
    pass

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

            elif var.scene == 'game':
                scenegame.mouse_up(x, y, button)

        if event.type == pygame.KEYDOWN:
            key = event.key

            if var.scene == 'title':
                scenetitle.key_down(key)

            elif var.scene == 'field':
                scenefield.key_down(key)

            elif var.scene == 'game':
                scenegame.key_down(key)

        if event.type == pygame.KEYUP:
            key = event.key

            if var.scene == 'title':
                scenetitle.key_up(key)

            elif var.scene == 'field':
                scenefield.key_up(key)

            elif var.scene == 'game':
                scenegame.key_up(key)

def handle_scene():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'field':
        scenefield.loop()

    elif var.scene == 'game':
        scenegame.loop()

init()
main()