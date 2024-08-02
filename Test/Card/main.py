import pygame, sys, ast

import pygame.threads
import asset, UI, data, const, var
import scene, func

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.resolution, pygame.SCALED)
    pygame.display.set_caption('Card Test')
    var.clock = pygame.time.Clock()

    load_font()
    load_image()
    load_data()

    func.start_game()
    func.shuffle_deck()

def load_font():
    pygame.font.init()
    asset.Font.main_32 = pygame.font.Font('Font/neodgm.ttf', 32)

def load_image():
    asset.Image.crystal_cost['any'] = pygame.image.load('Image/CrystalNormal.png')
    asset.Image.crystal_cost['fire'] = pygame.image.load('Image/CrystalFire.png')
    asset.Image.crystal_cost['water'] = pygame.image.load('Image/CrystalWater.png')
    asset.Image.crystal_cost['wind'] = pygame.image.load('Image/CrystalWind.png')
    asset.Image.crystal_cost['earth'] = pygame.image.load('Image/CrystalEarth.png')
    asset.Image.crystal_cost['light'] = pygame.image.load('Image/CrystalLight.png')
    asset.Image.crystal_cost['dark'] = pygame.image.load('Image/CrystalDark.png')

    asset.Image.crystal[1] = pygame.image.load('Image/CrystalNormal.png')
    asset.Image.crystal[2] = pygame.image.load('Image/CrystalFire.png')
    asset.Image.crystal[3] = pygame.image.load('Image/CrystalWater.png')
    asset.Image.crystal[4] = pygame.image.load('Image/CrystalWind.png')
    asset.Image.crystal[5] = pygame.image.load('Image/CrystalEarth.png')
    asset.Image.crystal[6] = pygame.image.load('Image/CrystalLight.png')
    asset.Image.crystal[7] = pygame.image.load('Image/CrystalDark.png')

    asset.Image.crystal_transparent['any'] = pygame.image.load('Image/CrystalNormal.png')
    asset.Image.crystal_transparent['fire'] = pygame.image.load('Image/CrystalFire.png')
    asset.Image.crystal_transparent['water'] = pygame.image.load('Image/CrystalWater.png')
    asset.Image.crystal_transparent['wind'] = pygame.image.load('Image/CrystalWind.png')
    asset.Image.crystal_transparent['earth'] = pygame.image.load('Image/CrystalEarth.png')
    asset.Image.crystal_transparent['light'] = pygame.image.load('Image/CrystalLight.png')
    asset.Image.crystal_transparent['dark'] = pygame.image.load('Image/CrystalDark.png')

    for img in asset.Image.crystal:
        asset.Image.crystal[img] = pygame.transform.scale(asset.Image.crystal[img], (60, 60))

    for img in asset.Image.crystal_transparent:
        asset.Image.crystal_transparent[img] = pygame.transform.scale(asset.Image.crystal_transparent[img], (60, 60))
        asset.Image.crystal_transparent[img].set_alpha(127)

def load_data():
    f = open('Data/data_card.txt')
    data.card = ast.literal_eval(f.read())
    f.close()

    f = open('Data/data_crystal.txt')
    data.crystal = ast.literal_eval(f.read())
    f.close()

def main():
    while True:
        var.clock.tick(var.FPS)
        handle_scene()
        handle_input()

def handle_scene():
    if var.scene == 'main':
        scene.loop()

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
            
            if var.scene == 'main':
                scene.mouse_up(x, y, button)

        if event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
            x = mouse[0]
            y = mouse[1]

            if var.scene == 'main':
                scene.mouse_motion(x, y)

if __name__ == '__main__':
    init()
    main()
