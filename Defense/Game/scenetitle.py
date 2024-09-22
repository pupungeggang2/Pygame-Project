import pygame
import asset, UI, data, var, const
import funcphysics

def loop():
    display()

def display():
    var.screen.blit(const.Color.white)
    pygame.display.flip()

def mouse_up(x, y, button):
    pass