screen = None
resolution = [1280, 720]
FPS = 60
clock = None

save = {
    
}

scene = 'title'
state = ''
menu = False

class Select():
    pass

class Player():
    life = 20
    generator_level = 1
    generator_speed = 0.5
    max_crystal = 6
    deck_crystal = []
    hand_crystal = []
    deck_card = []
    hand_card = []

class Game():
    camera = [-240, -120]
    level = []
    unit_player = []
    unit_monster = []
    projectile = []