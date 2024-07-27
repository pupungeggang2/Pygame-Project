import pygame, sys, ast
import asset, UI, data, const, var
import scene

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.resolution, pygame.SCALED)
    pygame.display.set_caption('Platformer Test')
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
        var.clock.tick(var.FPS)
        handle_input()
        handle_scene()

def handle_scene():
    if var.scene == 'main':
        scene.loop()

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            key = event.key

            if var.scene == 'main':
                scene.key_down(key)

        if event.type == pygame.KEYUP:
            key = event.key

            if var.scene == 'main':
                scene.key_up(key)

if __name__ == '__main__':
    init()
    main()