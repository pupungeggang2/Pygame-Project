screen = None
resolution = [1280, 720]
FPS = 60
clock = None

scene = 'title'
state = ''
menu = False

class Selected():
    character = -1

class Player():
    id = -1
    hand = []
    deck = []
    attack = 0
    defense = 0

class Field():
    enemy = []