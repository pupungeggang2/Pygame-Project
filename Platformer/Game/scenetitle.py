import pygame
import asset, UI, data, const, var
import funcphysics

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    var.screen.blit(asset.Font.main_32.render('Desserterria Adventure', False, const.Color.black), UI.Title.text_title)
    pygame.draw.rect(var.screen, const.Color.black, UI.Title.button_start, 2)
    var.screen.blit(asset.Font.main_32.render('Start Game', False, const.Color.black), UI.Title.text_start)
    pygame.draw.rect(var.screen, const.Color.black, UI.Title.button_erase, 2)
    var.screen.blit(asset.Font.main_32.render('Erase Data', False, const.Color.black), UI.Title.text_erase)

    pygame.draw.rect(var.screen, const.Color.black, UI.Title.cursor[var.Selected.Cursor.title], 2)

    pygame.display.update()

def mouse_up(x, y, button):
    if button == 0:
        if var.menu == False:
            if var.state == '':
                if funcphysics.point_inside_rect_array(x, y, UI.Title.button_start):
                    var.scene = 'field'
                    var.state = ''

def key_down(key):
    if var.menu == False:
        if var.state == '':
            if key == pygame.K_UP:
                var.Selected.Cursor.title = (var.Selected.Cursor.title + 1) % 2
                
            if key == pygame.K_DOWN:
                var.Selected.Cursor.title = (var.Selected.Cursor.title - 1) % 2

            if key == pygame.K_RETURN:
                if var.Selected.Cursor.title == 0:
                    var.scene = 'field'
                    var.state = ''
                    var.Selected.Cursor.title = 0

def key_up(key):
    pass