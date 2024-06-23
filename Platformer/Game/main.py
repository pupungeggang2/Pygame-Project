import pygame, sys
import var, const, asset, UI
import scenetitle, scenegame

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.resolution)
    pygame.display.set_caption('Platformer')
    var.clock = pygame.time.Clock()

def main():
    while True:
        var.clock.tick(var.FPS)
        handle_scene()
        handle_input()

def handle_scene():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'scenegame':
        scenegame.loop()

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

if __name__ == '__main__':
    init()
    main()