import pygame
import asset, UI, data, const, var
import func, draw

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    if var.state == 'start' or var.state == 'start_confirm':
        draw.draw_start()

    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.menu == False:
            if var.state == 'start':
                for i in range(3):
                    if func.point_inside_rect_array(x, y, UI.Start.button_start_card[i]):
                        if var.Game.start_card_change[i] == True:
                            var.Game.start_card_change[i] = False

                        else:
                            var.Game.start_card_change[i] = True

                if func.point_inside_rect_array(x, y, UI.Start.button_start):
                    func.change_start_card()
                    var.state = 'start_confirm'
