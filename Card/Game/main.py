import pygame, sys

import var
import const
import asset
import UI
import scenetitle
import scenefield
import scenegame

def init():
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

def handle_input():
    pass

init()
main()