import pygame
import asset, UI, data, const, var
import func, draw

def loop():
    if var.state == '':
        func.select_hand_card()

    display()

def display():
    var.screen.fill(const.Color.white)

    var.screen.blit(asset.Font.main_32.render('Turn : ' + str(var.Game.turn), False, const.Color.black), UI.text_title)

    draw.draw_field()
    draw.draw_lower()

    if var.state == 'card_play':
        draw.draw_crystal_slot()

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

            elif var.state == 'start_confirm':
                if func.point_inside_rect_array(x, y, UI.Start.button_start):
                    var.state = ''
                    func.turn_one_start()
                    func.turn_start()

            elif var.state == '':
                if var.Game.selected_hand_card != -1:
                    var.state = 'card_play'
                    var.Game.selected_hand_crystal = -1

                if func.point_inside_rect_array(x, y, UI.turn_end):
                    func.turn_end()
                    pygame.time.wait(1000)
                    func.turn_start()

            elif var.state == 'card_play':
                if func.point_inside_rect_array(x, y, UI.Lower.card_cancel):
                    var.state = ''
                    var.Game.selected_hand_card = -1

                for i in range(len(var.Game.hand_crystal)):
                    if func.point_inside_rect_array(x, y, UI.Lower.hand_crystal[i]):
                        var.Game.selected_hand_crystal = i

                for i in range(len(var.Game.hand_card[var.Game.selected_hand_card]['crystal_filled'])):
                    if func.point_inside_rect_array(x, y, UI.Lower.card_crystal_slot[i]):
                        func.fill_card_slot(var.Game.selected_hand_card, var.Game.selected_hand_crystal, i)

                for i in range(14):
                    if func.point_inside_rect_array(x, y, UI.Lower.card_confirm):
                        if func.check_card_cost(var.Game.hand_card[var.Game.selected_hand_card]) == True:
                            var.state = 'card_effect'
                            func.add_to_effect_queue(var.Game.hand_card[var.Game.selected_hand_card]['effect'], 'back')
                            print(var.Game.effect_queue)
                            var.Game.hand_card.pop(var.Game.selected_hand_card)
                            var.Game.selected_hand_card = -1
                        else:
                            pass

def mouse_motion(x, y):
    var.Input.mouse_pos = [x, y]