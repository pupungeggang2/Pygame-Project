import pygame
import asset, UI, data, const, var

def draw_start():
    pygame.draw.rect(var.screen, const.Color.white, UI.Start.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Start.rect, 2)

    if var.state == 'start':
        var.screen.blit(asset.Font.main_32.render('Select start card.', False, const.Color.black), UI.Start.text_title)

    if var.state == 'start_confirm':
        var.screen.blit(asset.Font.main_32.render('Confirm', False, const.Color.black), UI.Start.text_title)

    for i in range(3):
        draw_card(UI.Start.button_start_card[i], var.Game.deck_card[i])

        if var.state == 'start':
            if var.Game.start_card_change[i] == True:
                pygame.draw.rect(var.screen, const.Color.blue, UI.Start.button_start_card[i], 10)

    pygame.draw.rect(var.screen, const.Color.black, UI.Start.button_start, 2)
    var.screen.blit(asset.Font.main_32.render('Start', False, const.Color.black), UI.Start.text_start)
    
def draw_card(position, card):
    pygame.draw.rect(var.screen, const.Color.white, [position[0], position[1], 240, 320])
    pygame.draw.rect(var.screen, const.Color.black, [position[0], position[1], 240, 320], 2)

    for i in range(len(card['crystal'])):
        var.screen.blit(asset.Image.crystal_cost[card['crystal'][i]], [position[0] + UI.Card.crystal[i][0], position[1] + UI.Card.crystal[i][1]])

    if card['type'] == 'unit':
        var.screen.blit(asset.Font.main_32.render(str(card['stat'][0]), False, const.Color.black), [position[0] + UI.Card.attack[0], position[1] + UI.Card.attack[1]])
        var.screen.blit(asset.Font.main_32.render(str(card['stat'][1]), False, const.Color.black), [position[0] + UI.Card.hp[0], position[1] + UI.Card.hp[1]])

def draw_field():
    for i in range(14):
        pygame.draw.rect(var.screen, const.Color.white, UI.Field.unit[i])
        pygame.draw.rect(var.screen, const.Color.black, UI.Field.unit[i], 2)

    pygame.draw.rect(var.screen, const.Color.white, UI.turn_end)
    pygame.draw.rect(var.screen, const.Color.black, UI.turn_end, 2)

def draw_lower():
    for i in range(len(var.Game.hand_card)):
        draw_card(UI.Lower.hand_card[i], var.Game.hand_card[i])

    if var.Game.selected_hand_card != -1:
        draw_card(UI.Lower.hand_card_pop[var.Game.selected_hand_card], var.Game.hand_card[var.Game.selected_hand_card])

    for i in range(len(var.Game.hand_crystal)):
        var.screen.blit(asset.Image.crystal[var.Game.hand_crystal[i]['ID']], UI.Lower.hand_crystal[i])

    if var.Game.selected_hand_crystal != -1:
        pygame.draw.rect(var.screen, const.Color.blue, UI.Lower.hand_crystal[i], 2)

def draw_crystal_slot():
    temp_card = var.Game.hand_card[var.Game.selected_hand_card]

    for i in range(len(temp_card['crystal'])):
        pygame.draw.rect(var.screen, const.Color.black, UI.Lower.card_crystal_slot[i], 2)
        var.screen.blit(asset.Image.crystal_transparent[temp_card['crystal'][i]], UI.Lower.card_crystal_slot[i])

        if temp_card['crystal_filled'][i] != -1:
            var.screen.blit(asset.Image.crystal[temp_card['crystal_filled'][i]], UI.Lower.card_crystal_slot[i])

    pygame.draw.rect(var.screen, const.Color.black, UI.Lower.card_cancel, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Lower.card_confirm, 2)