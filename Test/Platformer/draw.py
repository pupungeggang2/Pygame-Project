import pygame
import asset, UI, data, const, var

def draw_field():
    for i in range(len(var.Field.thing)):
        if var.Field.thing[i]['type'] == 'wall':
            temp_rect = [var.Field.thing[i]['rect'][0] - var.Field.camera[0], var.Field.thing[i]['rect'][1] - var.Field.camera[1], var.Field.thing[i]['rect'][2], var.Field.thing[i]['rect'][3]]
            pygame.draw.rect(var.screen, const.Color.black, temp_rect, 2)

    temp_rect = [var.Player.position[0] - var.Field.camera[0] - 20, var.Player.position[1] - var.Field.camera[1] - 20, 40, 40]
    pygame.draw.rect(var.screen, const.Color.black, temp_rect, 2)