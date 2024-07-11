import pygame
import asset, UI, data, const, var

def draw_level(num_of_level):
    for i in range(num_of_level):
        row = i // 6
        col = i % 6
        pygame.draw.rect(var.screen, const.Color.black, [UI.Level_Select.button_level_start[0] + UI.Level_Select.button_level_interval[0] * col, UI.Level_Select.button_level_start[1] + UI.Level_Select.button_level_interval[1] * row, UI.Level_Select.button_level_size[0], UI.Level_Select.button_level_size[1]], 2)
