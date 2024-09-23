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
    energy = 3
    energy_max = 6
    energy_gen = 0.5
    deck_card = []
    hand_card = []

class Game():
    camera = [-240, -120]
    level = []
    unit_player = []
    unit_monster = []
    projectile = []