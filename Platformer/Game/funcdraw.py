import pygame
import asset, UI, data, const, var

def draw_field():
    pygame.draw.rect(var.screen, const.Color.black, [var.Player.position[0] - var.Field.camera[0] - 20, var.Player.position[1] - var.Field.camera[1] - 20, 40, 40], 2)

def draw_menu():
    pygame.draw.rect(var.screen, const.Color.white, UI.Menu.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.rect, 2)
    var.screen.blit(asset.Font.main_32.render('Paused', False, const.Color.black), UI.Menu.text_paused)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.button_resume, 2)
    var.screen.blit(asset.Font.main_32.render('Resume', False, const.Color.black), UI.Menu.text_resume)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.button_exit, 2)
    var.screen.blit(asset.Font.main_32.render('Exit', False, const.Color.black), UI.Menu.text_exit)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.cursor[var.Selected.Cursor.menu], 2)