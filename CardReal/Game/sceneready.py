import sys, pygame
import asset, const, var, UI
import funcphysics, funcdraw

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    var.screen.blit(asset.Font.neodgm_32.render('Select Character', False, const.Color.black), UI.Ready.text_title)

    pygame.draw.rect(var.screen, const.Color.black, UI.Ready.button_back, 2)

    for i in range(6):
        pygame.draw.rect(var.screen, const.Color.black, UI.Ready.button_character[i], 2)

    pygame.draw.rect(var.screen, const.Color.black, UI.Ready.button_start, 2)
    var.screen.blit(asset.Font.neodgm_32.render('Start', False, const.Color.black), UI.Ready.text_start)

    pygame.display.update()

def mouse_up(x, y, button):
    if button == 1:
        if var.menu == False:
            if var.state == '':
                if funcphysics.point_inside_rect_array(x, y, UI.Ready.button_back):
                    var.scene = 'title'
                    var.state = ''
                    var.Selected.character = -1

                for i in range(6):
                    if funcphysics.point_inside_rect_array(x, y, UI.Ready.button_character[i]):
                        var.Selected.character = i

                if funcphysics.point_inside_rect_array(x, y, UI.Ready.button_start):
                    if var.Selected.character != -1:
                        var.scene = 'game'
                        var.state = ''
                        var.Selected.character = -1

def key_down(key):
    pass

def key_up(key):
    pass