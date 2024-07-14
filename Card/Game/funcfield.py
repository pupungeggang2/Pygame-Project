import data, const, var
import funcphysics

def move_player():
    temp_position = [var.Field.position_player[0], var.Field.position_player[1]]

    if var.Pressed.left == True:
        temp_position[0] -= 200 / var.FPS

    if var.Pressed.right == True:
        temp_position[0] += 200 / var.FPS

    if var.Pressed.up == True:
        temp_position[1] -= 200 / var.FPS

    if var.Pressed.down == True:
        temp_position[1] += 200 / var.FPS

    var.Field.position_player[0] = temp_position[0]
    var.Field.position_player[1] = temp_position[1]

def move_camera():
    var.Field.camera[0] = var.Field.position_player[0] - 640
    var.Field.camera[1] = var.Field.position_player[1] - 360

def move_field():
    for i in range(len(var.Field.connection)):
        if funcphysics.point_inside_rect_array(var.Field.position_player[0], var.Field.position_player[1], var.Field.connection[i][0]):
            var.Field.position_player = [var.Field.connection[i][2][0], var.Field.connection[i][2][1]]
            load_field(var.Field.connection[i][1])
            break

def load_field(place):
    var.Field.place = place
    var.Field.thing = data.field[var.Field.place]['thing']
    var.Field.wall = data.field[var.Field.place]['wall']
    var.Field.connection = data.field[var.Field.place]['connection']
    var.Field.village = data.field[var.Field.place]['village']