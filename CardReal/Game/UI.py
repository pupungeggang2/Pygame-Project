class Title():
    text_title = [8, 8]
    button_start = [160, 160, 960, 80]
    text_start = [168, 184]
    button_erase = [160, 240, 960, 80]
    text_erase = [168, 264]

class Ready():
    text_title = [8, 8]
    button_back = [1220, 20, 40, 40]
    button_start = [1040, 600, 160, 80]
    text_start = [1048, 624]
    button_character = [
        [160, 160, 160, 160], [400, 160, 160, 160], [640, 160, 160, 160], [160, 400, 160, 160], [400, 400, 160, 160], [640, 400, 160, 160]
    ]

class Game():
    button_menu = [1220, 20, 40, 40]

    class Start():
        rect = [160, 80, 960, 560]
        text_title = [168, 88]
        button_start = [560, 520, 160, 80]
        button_select = [[240, 160, 160, 160], [560, 160, 160, 160], [880, 160, 160, 160]]
        text_start = [568, 544]
    
    class Lower_Bar():
        ability = [40, 600, 80, 80]
        hand = [120, 600, 640, 80]
        card_back = [760, 600, 80, 80]

class Menu():
    rect = [320, 240, 640, 240]
    text_paused = [328, 264]
    button_resume = [320, 320, 640, 80]
    text_resume = [328, 344]
    button_exit = [320, 400, 640, 80]
    text_exit = [328, 424]