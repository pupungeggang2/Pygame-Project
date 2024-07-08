import pygame, sys
import asset, UI, const, var
import scenetitle, scenefield, scenegame

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.resolution)
    pygame.display.set_caption('Card')
    var.clock = pygame.time.Clock()

def main():
    while True:
        var.clock.tick(var.FPS)
        handle_input()
        handle_scene()
        
def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def handle_scene():
    pass
    
if __name__ == '__main__':
    init()
    main()
