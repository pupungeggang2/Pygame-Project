import pygame, sys
import asset, UI, const, var
import funcphysics, funcdraw, funcfield

def loop():
    if var.menu == False:
        if var.state == '':
            funcfield.move_player()
            funcfield.camera_adjust()

    display()

def display():
    var.screen.fill(const.Color.white)

    pygame.draw.rect(var.screen, const.Color.black, UI.Field.button_menu, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.button_info, 2)

    funcdraw.draw_field()

    if var.state == 'info':
        funcdraw.draw_info()

    if var.menu == True:
        funcdraw.draw_menu()

    pygame.display.update()

def mouse_up(x, y, button):
    if button == 1:
        if var.menu == True:
            if funcphysics.point_inside_rect_array(x, y, UI.Menu.button_resume):
                var.menu = False

            elif funcphysics.point_inside_rect_array(x, y, UI.Menu.button_exit):
                var.menu = False
                var.scene = 'title'
                var.state = ''

        elif var.menu == False:
            if funcphysics.point_inside_rect_array(x, y, UI.Field.button_menu):
                var.menu = True

            if var.state == '':
                if funcphysics.point_inside_rect_array(x, y, UI.Field.button_info):
                    var.state = 'info'

            elif var.state == 'info':
                if funcphysics.point_inside_rect_array(x, y, UI.Info.button_close):
                    var.state = ''

def key_down(key):
    if key == pygame.K_w:
        var.Pressed.up = True

    elif key == pygame.K_a:
        var.Pressed.left = True

    elif key == pygame.K_s:
        var.Pressed.down = True

    elif key == pygame.K_d:
        var.Pressed.right = True

    if var.menu == True:
        if key == pygame.K_r:
            var.menu = False

        elif key == pygame.K_e:
            var.menu = False
            var.scene = 'title'
            var.state = ''

    if var.menu == False:
        if key == pygame.K_ESCAPE:
            var.menu = True

        if var.state == '':
            if key == pygame.K_i:
                var.state = 'info'

        elif var.state == 'info':
            if key == pygame.K_i:
                var.state = ''

def key_up(key):
    if key == pygame.K_w:
        var.Pressed.up = False

    elif key == pygame.K_a:
        var.Pressed.left = False

    elif key == pygame.K_s:
        var.Pressed.down = False

    elif key == pygame.K_d:
        var.Pressed.right = False