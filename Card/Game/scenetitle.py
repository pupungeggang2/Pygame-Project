import sys, pygame
import asset, UI, data, const, var
import funcphysics

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    var.screen.blit(asset.Font.main_32.render('Card', False, const.Color.black), UI.Title.text_title)
    pygame.draw.rect(var.screen, const.Color.black, UI.Title.button_start, 2)
    var.screen.blit(asset.Font.main_32.render('Start Game', False, const.Color.black), UI.Title.text_start)
    pygame.draw.rect(var.screen, const.Color.black, UI.Title.button_erase, 2)
    var.screen.blit(asset.Font.main_32.render('Erase Data', False, const.Color.black), UI.Title.text_erase)

    pygame.display.update()

def mouse_up(x, y, button):
    if button == 1:
        if var.menu == False:
            if var.state == '':
                if funcphysics.point_inside_rect_array(x, y, UI.Title.button_start):
                    var.scene = 'field'
                    var.state = ''
                    var.Field.place = var.save['place']
                    var.Field.position_player = data.field[var.Field.place]['spawn']
                    var.Field.wall = data.field[var.Field.place]['wall']
                    var.Field.thing = data.field[var.Field.place]['thing']
                    var.Field.connection = data.field[var.Field.place]['connection']
                    var.Field.village = data.field[var.Field.place]['village']
                    print(var.Field.village)

def key_down(key):
    pass

def key_up(key):
    pass