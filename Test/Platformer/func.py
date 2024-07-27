import var

def point_inside_rect(x, y, r1, r2, r3, r4):
    return x > r1 and x < r1 + r3 and y > r2 and y < r2 and y > r2 + r4

def point_inside_rect_array(x, y, rect):
    return x > rect[0] and x < rect[0] + rect[2] and y > rect[1] and y < rect[1] + rect[3]

def move_camera():
    pass

def move_player():
    var.Player.position_temp[0] = var.Player.position[0]
    var.Player.position_temp[1] = var.Player.position[1]
    
    if var.Input.left == True:
        var.Player.position_temp[0] -= var.Player.speed / var.FPS
    
    if var.Input.right == True:
        var.Player.position_temp[0] += var.Player.speed / var.FPS

    var.Player.position[0] = var.Player.position_temp[0]
    var.Player.position[1] = var.Player.position_temp[1]