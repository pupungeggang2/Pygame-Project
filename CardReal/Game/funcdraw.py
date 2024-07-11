import asset, const, var, UI
import pygame

def draw_field():
    pass

def draw_menu():
    pygame.draw.rect(var.screen, const.Color.white, UI.Menu.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.rect, 2)
    var.screen.blit(asset.Font.main_32.render('Paused', False, const.Color.black), UI.Menu.text_paused)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.button_resume, 2)
    var.screen.blit(asset.Font.main_32.render('Resume', False, const.Color.black), UI.Menu.text_resume)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.button_exit, 2)
    var.screen.blit(asset.Font.main_32.render('Exit', False, const.Color.black), UI.Menu.text_exit)

def draw_field():
    # Drawing Player
    pygame.draw.rect(var.screen, const.Color.black, [var.Field.position_player[0] - var.Field.camera[0] - 20, var.Field.position_player[1] - var.Field.camera[1] - 20, 40, 40], 2)

def draw_lower_bar():
    pygame.draw.rect(var.screen, const.Color.white, UI.Game.Lower_Bar.ability)
    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Lower_Bar.ability, 2)
    pygame.draw.rect(var.screen, const.Color.white, UI.Game.Lower_Bar.hand)
    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Lower_Bar.hand, 2)
    pygame.draw.rect(var.screen, const.Color.white, UI.Game.Lower_Bar.card_back)
    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Lower_Bar.card_back, 2)