import var, const, asset, UI
import funcphysics, funcdraw
import pygame

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    pygame.draw.rect(var.screen, const.Color.black, UI.Field.button_menu, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.button_info, 2)

    if var.menu == True:
        funcdraw.draw_menu()

    pygame.display.update()

def mouse_up(x, y, button):
    if button == 1:
        if var.menu == False:
            if funcphysics.point_inside_rect_array(x, y, UI.Field.button_menu):
                var.menu = True

            if funcphysics.point_inside_rect_array(x, y, UI.Field.button_info):
                pass

        elif var.menu == True:
            if funcphysics.point_inside_rect_array(x, y, UI.Menu.button_resume):
                var.menu = False

            elif funcphysics.point_inside_rect_array(x, y, UI.Menu.button_exit):
                var.menu = False
                var.scene = 'title'
                var.state = ''


def key_down(key):
    if var.menu == False:
        if key == pygame.K_ESCAPE:
            var.menu = True

    elif var.menu == True:
        if key == pygame.K_ESCAPE:
            var.menu = False

        elif key == pygame.K_r:
            var.menu = False

        elif key == pygame.K_e:
            var.menu = False
            var.scene = 'title'
            var.state = ''

def key_up(key):
    pass