screen = None
resolution = [1280, 720]
FPS = 60
clock = None

scene = 'title'
state = ''
menu = False

class Selected():
    class Cursor():
        title = 0
        menu = 0

class Player():
    speed = 200
    ground = True
    stepping = -1
    position = [80, 640]

    jump_power = 0
    jump_time = 0
    jump_num = 1
    y_speed = 0

class Field():
    camera = [0, 0]
    tile = []
