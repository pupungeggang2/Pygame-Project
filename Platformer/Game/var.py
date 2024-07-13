screen = None
resolution = [1280, 720]
FPS = 60
clock = None

scene = 'title'
state = ''
menu = False

save = {}

class Field():
    place = 'home_town'
    tile = []
    thing = []
    connection = []
    gravity = 400
    camera = [0, 0]

class Player():
    position = [20, 20]
    jump_power = -400
    jump_num = 1
    jump_time = 0
    jump_time_max = 1
    ground = False