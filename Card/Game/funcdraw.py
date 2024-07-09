import pygame
import asset, UI, var, const

def draw_menu():
    pygame.draw.rect(var.screen, const.Color.white, UI.Menu.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.rect, 2)
    var.screen.blit(asset.Font.main_32.render('Paused', False, const.Color.black), UI.Menu.text_pause)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.button_resume, 2)
    var.screen.blit(asset.Font.main_32.render('Resume', False, const.Color.black), UI.Menu.text_resume)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.button_exit, 2)
    var.screen.blit(asset.Font.main_32.render('Exit to title', False, const.Color.black), UI.Menu.text_exit)
