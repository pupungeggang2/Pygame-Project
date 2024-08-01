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