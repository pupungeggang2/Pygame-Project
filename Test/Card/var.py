screen = None
resolution = [1280, 720]
FPS = 60
clock = None

scene = 'main'
state = 'start'
menu = False

class Input():
    mouse_pos = [0, 0]

class Adventure():
    deck_card = [1, 1, 1001, 2, 3, 3]
    deck_crystal = [1, 1, 1, 1, 1, 1, 1, 1]

class Game():
    start_card_change = [False, False, False]
    turn = 0
    deck_card = []
    deck_crystal = []
    hand_card = []
    hand_crystal = []
    
    power = 0
    unit = 0
    extra_energy = 0
    extra_draw = 0
    max_energy = 0

    selected_hand_card = -1
    selected_hand_crystal = -1

    card_input = [-1, -1]

    effect_queue = []
    effect_var = {}