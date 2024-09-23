import pygame, sys, ast
import data, asset, UI, var, const
import scenetitle, scenelevelselect, scenegame

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.resolution)
    pygame.display.set_caption('Defense')
    var.clock = pygame.time.Clock()

    load_image()
    load_font()
    load_data()
    load_save()

def load_image():
    asset.Image.spawn = pygame.image.load('Image/Spawn.png')
    asset.Image.Icon.life = pygame.image.load('Image/Icon/IconLife.png')

def load_font():
    try:
        asset.Font.main_32 = pygame.font.Font('Font/neodgm.ttf', 32)
    except:
        asset.Font.main_32 = pygame.font.SysFont(None, 32)

def load_data():
    f = open('Data/card.txt', 'r')
    data.card = ast.literal_eval(f.read())
    f.close()
    f = open('Data/level.txt', 'r')
    data.level = ast.literal_eval(f.read())
    f.close()
    f = open('Data/monster.txt', 'r')
    data.monster = ast.literal_eval(f.read())
    f.close()
    f = open('Data/unit.txt', 'r')
    data.unit = ast.literal_eval(f.read())
    f.close()

def load_save():
    try:
        f = open('Save/save.txt', 'r')
        var.save = ast.literal_eval(f.read())
        f.close()
    except:
        f = open('Save/save.txt', 'w')
        f.write(str({}))
        f.close()
        f = open('Save/save.txt', 'r')
        var.save = ast.literal_eval(f.read())
        f.close()

def main():
    while True:
        var.clock.tick(var.FPS)
        handle_input()
        handle_scene()

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            x = mouse[0]
            y = mouse[1]
            button = event.button

            if var.scene == 'title':
                scenetitle.mouse_up(x, y, button)

            elif var.scene == 'level_select':
                scenelevelselect.mouse_up(x, y, button)

            elif var.scene == 'game':
                scenegame.mouse_up(x, y, button)

def handle_scene():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'level_select':
        scenelevelselect.loop()

    elif var.scene == 'game':
        scenegame.loop()
init()
main()