import pygame
import asset, UI, data, var, const

def shoot_projectile():
    pass

def spawn_monster():
    pass

def handle_projectile():
    pass

def handle_monster():
    pass

def wave_handle():
    pass

def player_tick():
    if var.Player.energy + var.Player.energy_gen / var.FPS > var.Player.energy_max:
        var.Player.energy = var.Player.energy_max
    else:
        var.Player.energy += var.Player.energy_gen / var.FPS

def game_tick():
    player_tick()
    wave_handle()