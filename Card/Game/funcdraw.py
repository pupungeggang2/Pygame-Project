import var, const, asset, UI
import pygame

def draw_menu():
    pygame.draw.rect(var.screen, const.Color.white, UI.Menu.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.rect, 2)
    var.screen.blit(asset.Font.neodgm_32.render('Paused', False, const.Color.black), UI.Menu.text_pause)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.button_resume, 2)
    var.screen.blit(asset.Font.neodgm_32.render('Resume [R]', False, const.Color.black), UI.Menu.text_resume)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.button_exit, 2)
    var.screen.blit(asset.Font.neodgm_32.render('Exit to title [E]', False, const.Color.black), UI.Menu.text_exit)

def draw_field():
    pass