screen = None
resolution = [1280, 720]
FPS = 60
clock = None

scene = 'main'
state = 'start'
menu = False

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