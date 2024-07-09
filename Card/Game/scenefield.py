import pygame, sys
import asset, UI, const, var
import funcphysics

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    pygame.draw.rect(var.screen, const.Color.black, UI.Field.button_menu, 2)

    pygame.draw.rect(var.screen, const.Color.black, UI.Field.button_info, 2)

    pygame.display.update()

def mouse_up(x, y, button):
    pass

def key_down(key):
    pass

def key_up(key):
    pass
