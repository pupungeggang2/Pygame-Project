screen = None
resolution = [1280, 720]
FPS = 60
clock = None

menu = False
scene = 'main'
state = ''

class Input():
    jump = False
    left = False
    right = False

class Player():
    position = [120, 620]
    position_temp = [120, 620]
    speed = 240
    y_speed = 0

    ground = False
    stepping = -1
    jump_num = 1
    jump_power = -400
    jump_time = 0

class Field():
    thing = [
        {'type' : 'wall', 'rect' : [80, 640, 320, 80]},
        {'type' : 'wall', 'rect' : [80, 320, 320, 80]},
        {'type' : 'wall', 'rect' : [800, 320, 80, 400]}
    ]
    camera = [0, 0]
    gravity = 1200