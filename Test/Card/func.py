import ast, random
import UI, data, const, var

def point_inside_rect(x, y, r1, r2, r3, r4):
    return x > r1 and x < r1 + r3 and y > r2 and y < r2 + r4

def point_inside_rect_array(x, y, rect):
    return x > rect[0] and x < rect[0] + rect[2] and y > rect[1] and y < rect[1] + rect[3]

# Game start
def start_game():
    var.Game.deck_card = []
    var.Game.deck_crystal = []
    
    for i in range(len(var.Adventure.deck_card)):
        var.Game.deck_card.append(ast.literal_eval(str(data.card[var.Adventure.deck_card[i]])))

    for i in range(len(var.Adventure.deck_crystal)):
        var.Game.deck_crystal.append(ast.literal_eval(str(data.crystal[var.Adventure.deck_crystal[i]])))

    var.Game.hand_card = []
    var.Game.hand_crystal = []

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

# Basic draw function
def draw_from_deck_card(condition = ''):
    if len(var.Game.hand_card) < 8:
        if len(var.Game.deck_card) > 0:
            var.Game.hand_card.append(var.Game.deck_card.pop(0))

def draw_from_deck_crystal(condition = ''):
    if len(var.Game.deck_crystal) > 0:
        var.Game.hand_crystal.append(var.Game.deck_crystal.pop(0))

# Turn
def return_crystal():
    var.Game.deck_crystal += var.Game.hand_crystal
    var.Game.hand_crystal = []

def turn_one_start():
    for i in range(3):
        draw_from_deck_card()

    var.Game.selected_hand_card = -1
    var.Game.selected_hand_crystal = -1

def turn_start():
    var.Game.turn += 1

    if var.Game.max_energy < 8:
        var.Game.max_energy += 1

    draw_from_deck_card()

    for i in range(var.Game.max_energy + var.Game.extra_energy):
        draw_from_deck_crystal()

def turn_end():
    return_crystal()

# Card play
def select_hand_card():
    var.Game.selected_hand_card = -1

    for i in range(len(var.Game.hand_card)):
        if i < len(var.Game.hand_card) - 1:
            if point_inside_rect_array(var.Input.mouse_pos[0], var.Input.mouse_pos[1], UI.Lower.card_select_area[i]):
                var.Game.selected_hand_card = i

        else:
            if point_inside_rect_array(var.Input.mouse_pos[0], var.Input.mouse_pos[1], UI.Lower.card_select_area_final[i]):
                var.Game.selected_hand_card = len(var.Game.hand_card) - 1

def fill_card_slot(card_index, crystal_index, selected_slot):
    if var.Game.hand_card[card_index]['crystal_filled'][selected_slot] == -1:
        if var.Game.hand_card[card_index]['crystal'][selected_slot] == 'any' or var.Game.hand_crystal[crystal_index]['element'] == 'all':
            var.Game.hand_card[card_index]['crystal_filled'][selected_slot] = var.Game.hand_crystal[crystal_index]['ID']
            var.Game.hand_crystal.pop(crystal_index)
            var.Game.selected_hand_crystal = -1

        else:
            if var.Game.hand_card[card_index]['crystal'][selected_slot] == var.Game.hand_crystal[crystal_index]['element']:
                var.Game.hand_card[card_index]['crystal_filled'][selected_slot] = var.Game.hand_crystal[crystal_index]['ID']
                var.Game.hand_crystal.pop(crystal_index)
                var.Game.selected_hand_crystal = -1

def check_card_cost(card):
    for i in range(len(card['crystal_filled'])):
        if card['crystal_filled'][i] == -1:
            return False
        
    return True

# Handle Effect
def effect_parse(effect):
    effect_parsed = []
    effect_parsed = effect.split('|')

    return effect_parsed

def add_to_effect_queue(effect, fb):
    effect_parsed = effect_parse(effect)

    if fb == 'front':
        var.Game.effect_queue = effect_parsed + var.Game.effect_queue

    else:
        var.Game.effect_queue = var.Game.effect_queue + effect_parsed

def effect_queue_empty_check():
    if len(var.Game.effect_queue) > 0:
        return False
    
    var.Game.effect_var = {}
    return True

def perform_effect_line(effect):
    pass