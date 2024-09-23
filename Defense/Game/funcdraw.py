import pygame
import asset, UI, data, const, var

def draw_level():
    pygame.draw.rect(var.screen, const.Color.black, [80, 80, 80, 80], 2)

def draw_start():
    pygame.draw.rect(var.screen, const.Color.white, UI.Game.Start.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Start.rect, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Start.button_start, 2)
    var.screen.blit(asset.Font.main_32.render('Start', False, const.Color.black), UI.Game.Start.text_start)

def draw_field():
    for i in range(len(var.Game.level['block'])):
        for j in range(len(var.Game.level['block'][i])):
            temp_rect = [UI.Game.Field.cell_size[0] * j - var.Game.camera[0], UI.Game.Field.cell_size[1] * i - var.Game.camera[1], UI.Game.Field.cell_size[0], UI.Game.Field.cell_size[1]]
            pygame.draw.rect(var.screen, const.Color.black, temp_rect, 2)

    for i in range(len(var.Game.level['spawn'])):
        temp_spawn = var.Game.level['spawn'][i]
        temp_position = [temp_spawn[0] - var.Game.camera[0] - 40, temp_spawn[1] - var.Game.camera[1] - 40]
        var.screen.blit(asset.Image.spawn, temp_position)

def draw_lower():
    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Lower.generator, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Lower.ability, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Lower.hand_card, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Lower.hand_energy, 2)

    var.screen.blit(asset.Image.Icon.life, UI.Game.Lower.icon_life)
    var.screen.blit(asset.Font.main_32.render(str(var.Player.life), False, const.Color.black), UI.Game.Lower.text_life)