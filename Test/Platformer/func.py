import var

def point_inside_rect(x, y, r1, r2, r3, r4):
    return x > r1 and x < r1 + r3 and y > r2 and y < r2 and y > r2 + r4

def point_inside_rect_array(x, y, rect):
    return x > rect[0] and x < rect[0] + rect[2] and y > rect[1] and y < rect[1] + rect[3]

def two_rect_collide(rect1, rect2):
    pass

def move_camera():
    var.Field.camera = [var.Player.position[0] - 640, var.Player.position[1] - 360]

    if var.Field.camera[0] < 0:
        var.Field.camera[0] = 0

    elif var.Field.camera[0] + 1280 > var.Field.size[0]:
        var.Field.camera[0] -= var.Field.size[0] - 1280

    if var.Field.camera[1] < 0:
        var.Field.camera[1] = 0

    elif var.Field.camera[1] + 720 > var.Field.size[1]:
        var.Field.camera[1] -= var.Field.size[1] - 720

def move_player():
    var.Player.position_temp[0] = var.Player.position[0]
    var.Player.position_temp[1] = var.Player.position[1]
    
    # Horizontal
    if var.Input.left == True:
        var.Player.position_temp[0] -= var.Player.speed / var.FPS
    
    if var.Input.right == True:
        var.Player.position_temp[0] += var.Player.speed / var.FPS

    # Vertical


    var.Player.position[0] = var.Player.position_temp[0]
    var.Player.position[1] = var.Player.position_temp[1]