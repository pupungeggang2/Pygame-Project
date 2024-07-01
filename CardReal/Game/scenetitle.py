import sys, pygame
import asset, const, var, UI
import funcphysics

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    var.screen.blit(asset.Font.neodgm_32.render('Card Real', False, const.Color.black), UI.Title.text_title)
    pygame.draw.rect(var.screen, const.Color.black, UI.Title.button_start, 2)
    var.screen.blit(asset.Font.neodgm_32.render('Start Game', False, const.Color.black), UI.Title.text_start)
    pygame.draw.rect(var.screen, const.Color.black, UI.Title.button_erase, 2)
    var.screen.blit(asset.Font.neodgm_32.render('Erase Data', False, const.Color.black), UI.Title.text_erase)

    pygame.display.update()

def mouse_up(x, y, button):
    if button == 1:
        if var.menu == False:
            if var.state == '':
                if funcphysics.point_inside_rect_array(x, y, UI.Title.button_start):
                    var.scene = 'ready'
                    var.state = ''

def key_down(key):
    if var.menu == False:
        if var.state == '':
            if key == pygame.K_s:
                var.scene = 'ready'
                var.state = ''

def key_up(key):
    pass