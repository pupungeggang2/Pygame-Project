import asset, var, const, UI
import pygame
import funcphysics

def init_game():
    pass

def move_player():
    pass

def move_camera():
    var.Field.camera[0] = var.Field.position_player[0] - 640
    var.Field.camera[1] = var.Field.position_player[1] - 360
    print(var.Field.camera)

def use_card():
    pass