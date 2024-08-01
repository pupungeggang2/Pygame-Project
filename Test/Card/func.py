import ast, random
import data, const, var

def point_inside_rect(x, y, r1, r2, r3, r4):
    return x > r1 and x < r1 + r3 and y > r2 and y < r2 + r4

def point_inside_rect_array(x, y, rect):
    return x > rect[0] and x < rect[0] + rect[2] and y > rect[1] and y < rect[1] + rect[3]

def convert_adventure_deck_to_game():
    var.Game.deck_card = []
    var.Game.deck_crystal = []
    
    for i in range(len(var.Adventure.deck_card)):
        var.Game.deck_card.append(ast.literal_eval(str(data.card[var.Adventure.deck_card[i]])))

    for i in range(len(var.Adventure.deck_crystal)):
        var.Game.deck_crystal.append(ast.literal_eval(str(data.crystal[var.Adventure.deck_crystal[i]])))

def shuffle_deck():
    temp_deck_card = []
    temp_deck_crystal = []

    while len(var.Game.deck_card) > 0:
        index = random.randint(0, len(var.Game.deck_card) - 1)
        temp_deck_card.append(var.Game.deck_card.pop(index))

    while len(var.Game.deck_crystal) > 0:
        index = random.randint(0, len(var.Game.deck_crystal) - 1)
        temp_deck_crystal.append(var.Game.deck_crystal.pop(index))

    var.Game.deck_card = temp_deck_card
    var.Game.deck_crystal = temp_deck_crystal

def change_start_card():
    for i in range(3):
        if var.Game.start_card_change[i] == True:
            var.Game.deck_card[i], var.Game.deck_card[i + 3] = var.Game.deck_card[i + 3], var.Game.deck_card[i]