import pygame
import asset, UI, data, const, var
import funcdraw

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    funcdraw.draw_level(20)
    pygame.display.update()

def mouse_up(x, y, button):
    pass

def key_down(key):
    pass

def key_up(key):
    pass
