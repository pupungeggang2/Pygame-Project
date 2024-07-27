import pygame
import asset, UI, data, const, var
import func, draw

def loop():
    display()

    if var.menu == False:
        if var.state == '':
            func.move_player()

def display():
    var.screen.fill(const.Color.white)

    draw.draw_field()

    pygame.display.flip()

def key_down(key):
    if key == pygame.K_LEFT:
        var.Input.left = True

    elif key == pygame.K_RIGHT:
        var.Input.right = True

def key_up(key):
    if key == pygame.K_LEFT:
        var.Input.left = False

    elif key == pygame.K_RIGHT:
        var.Input.right = False