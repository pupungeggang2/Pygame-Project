import pygame, ast
import asset, UI, data, var, const
import funcphysics, funcdraw

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    var.screen.blit(asset.Font.main_32.render('Select level', False, const.Color.black), UI.Level_Select.text_title)
    pygame.draw.rect(var.screen, const.Color.black, UI.Level_Select.button_back, 2)
    funcdraw.draw_level()
    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.menu == False:
            if var.state == '':
                if funcphysics.point_inside_rect_array(x, y, UI.Level_Select.button_back):
                    var.scene = 'title'
                    var.state = ''

                if funcphysics.point_inside_rect(x, y, 80, 80, 80, 80):
                    var.Game.level = ast.literal_eval(str(data.level[1]))
                    var.scene = 'game'
                    var.state = 'start'