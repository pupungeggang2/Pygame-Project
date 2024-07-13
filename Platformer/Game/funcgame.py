import data, const, var

def move_player():
    temp_position = [var.Player.position[0], var.Player.position[1]]
    var.Player.position[0] = temp_position[0]
    var.Player.position[1] = temp_position[1]

def move_camera():
    temp_position = [var.Player.position[0] - 640, var.Player.position[1] - 320]

    if temp_position[0] < 0:
        temp_position[0] = 0

    if temp_position[1] < 0:
        temp_position[1] = 0

    var.Field.camera[0] = temp_position[0]
    var.Field.camera[1] = temp_position[1]