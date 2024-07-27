import pygame
import asset, UI, data, const, var
import func, draw

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    draw.draw_field()

    pygame.display.flip()

def key_up(key):
    pass

def key_down(key):
    pass