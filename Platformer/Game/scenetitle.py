import pygame
import asset, UI, data, const, var
import funcphysics

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    var.screen.blit(asset.Font.main_32.render('Desserterria Adventure', False, const.Color.black), UI.Title.text_title)
    pygame.draw.rect(var.screen, const.Color.black, UI.Title.button_start, 2)
    var.screen.blit(asset.Font.main_32.render('Start Game', False, const.Color.black), UI.Title.text_start)
    pygame.draw.rect(var.screen, const.Color.black, UI.Title.button_erase, 2)
    var.screen.blit(asset.Font.main_32.render('Erase Data', False, const.Color.black), UI.Title.text_erase)

    pygame.display.flip()

def mouse_up(x, y, button):
    pass

def key_down(key):
    pass

def key_up(key):
    pass