import pygame
import asset, UI, data, const, var

def draw_menu():
    pygame.draw.rect(var.screen, const.Color.white, UI.Menu.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.rect, 2)
    var.screen.blit(asset.Font.main_32.render('Paused', False, const.Color.black), UI.Menu.text_paused)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.button_resume, 2)
    var.screen.blit(asset.Font.main_32.render('Resume [R]', False, const.Color.black), UI.Menu.text_resume)
    pygame.draw.rect(var.screen, const.Color.black, UI.Menu.button_exit, 2)
    var.screen.blit(asset.Font.main_32.render('Exit [E]', False, const.Color.black), UI.Menu.text_exit)

def draw_field():
    pygame.draw.rect(var.screen, const.Color.black, [var.Player.position[0] - var.Field.camera[0] - 20, var.Player.position[1] - var.Field.camera[1] - 20, 40, 40], 2)

    for i in range(len(var.Field.tile)):
        temp_tilemap = var.Field.tile[i]

        for j in range(len(temp_tilemap['block'])):
            for k in range(len(temp_tilemap['block'][j])):
                if temp_tilemap['block'][j][k] != 0:
                    temp_rect = [temp_tilemap['start'][0] + k * 40, temp_tilemap['start'][1] + j * 40, 40, 40]
                    pygame.draw.rect(var.screen, const.Color.black, temp_rect, 2)

    for i in range(len(var.Field.thing)):
        pass

    for i in range(len(var.Field.connection)):
        pygame.draw.rect(var.screen, const.Color.black, var.Field.connection[i][0], 2)