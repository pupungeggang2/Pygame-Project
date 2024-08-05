import sys, pygame
import var, const

from OpenGL.GL import *
from OpenGL.GLU import *

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.resolution, pygame.SCALED|pygame.OPENGL)
    var.screen_ui = pygame.display.set_mode(var.resolution, pygame.SCALED)
    pygame.display.set_caption('GL Test')
    var.clock = pygame.time.Clock()

def main():
    while True:
        var.clock.tick(var.FPS)
    
        handle_input()
        var.screen.fill((0, 0, 0))
        pygame.draw.rect(var.screen, (0, 255, 0), (0, 0, 40, 40))
        pygame.display.flip()

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    init()
    main()