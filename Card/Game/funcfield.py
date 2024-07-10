import asset, UI, data, const, var

def move_player():
    if var.Pressed.left == True:
        var.Field.position_player[0] -= 200 / var.FPS

    if var.Pressed.right == True:
        var.Field.position_player[0] += 200 / var.FPS

    if var.Pressed.up == True:
        var.Field.position_player[1] -= 200 / var.FPS

    if var.Pressed.down == True:
        var.Field.position_player[1] += 200 / var.FPS