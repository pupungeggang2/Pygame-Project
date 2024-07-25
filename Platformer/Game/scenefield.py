import pygame
import asset, UI, data, const, var
import funcphysics, funcdraw

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    pygame.draw.rect(var.screen, const.Color.black, UI.Field.button_back, 2)

    funcdraw.draw_field()

    if var.menu == True:
        funcdraw.draw_menu()

    pygame.display.update()

def mouse_up(x, y, button):
    pass

def key_down(key):
    if var.menu == True:
        if key == pygame.K_ESCAPE:
            var.menu = False

        if key == pygame.K_UP:
            var.Selected.Cursor.menu = (var.Selected.Cursor.menu + 1) % 2

        if key == pygame.K_DOWN:
            var.Selected.Cursor.menu = (var.Selected.Cursor.menu - 1) % 2

        if key == pygame.K_RETURN:
            if var.Selected.Cursor.menu == 0:
                var.menu = False
                var.Selected.Cursor.menu = 0

            elif var.Selected.Cursor.menu == 1:
                var.menu = False
                var.scene = 'title'
                var.state = ''
                var.Selected.Cursor.menu = 0

    elif var.menu == False:
        if key == pygame.K_ESCAPE:
            var.menu = True

def key_up(key):
    pass