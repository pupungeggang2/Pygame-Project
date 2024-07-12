import data, const, var

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

def load_field(place):
    var.Field.place = place
    var.Field.thing = data.field[var.Field.place]['thing']
    var.Field.wall = data.field[var.Field.place]['wall']
    var.Field.connection = data.field[var.Field.place]['connection']
    var.Field.village = data.field[var.Field.place]['village']