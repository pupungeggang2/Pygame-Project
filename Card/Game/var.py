screen = None
resolution = [1280, 720]
FPS = 60
clock = None

scene = 'title'
state = ''
menu = False

save = {}

class Pressed():
    left = False
    right = False
    up = False
    down = False

class Field():
    position_player = [0, 0]
    place = ''
    thing = []
    connection = []
    wall = []
    village = True
    camera = [0, 0]

class Player():
    pass

class Adventure():
    adventure = False

class Game():
    pass