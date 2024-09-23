import pygame
import asset, UI, data, var, const
import funcphysics, funcdraw, funcgame

def loop():
    if var.menu == False:
        if var.state == '':
            funcgame.game_tick()
            
    display()

def display():
    var.screen.fill(const.Color.white)

    funcdraw.draw_field()
    funcdraw.draw_lower()

    if var.state == 'start':
        funcdraw.draw_start()

    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.menu == False:
            if var.state == '':
                pass

            elif var.state == 'start':
                if funcphysics.point_inside_rect_array(x, y, UI.Game.Start.button_start):
                    var.state = ''