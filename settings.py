from pathlib import Path

class Settings:
    def __init__(self) -> None:
        self.name = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        
        #Had to use tis path style that takes the parent of the script(Folder)
         #and goes through that path to pull the assets or anything else
         #because the one from your video would not work me


        #BG
        self.bg_file = \
        Path(__file__).parent / 'Assets' / 'images' / 'SpacePixalBackground.png'
        
        #Ship
        self.ship_file = \
        Path(__file__).parent / 'Assets' / 'images' / 'YellowShip.png'

        #Space Ship
        self.enemy_file = \
        Path(__file__).parent / 'Assets' / 'images' / 'ememyShip.png'

        #Bullet\
        self.bullet_file = \
        Path(__file__).parent / 'Assets' / 'images' / 'WhiteDualLaser.png'


        
        # Ship settings
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 8

        #Settings
        self.enemy_speed = 1
        self.bullet_speed = 10
        
        # Which border to start on: 'left' or 'right'
        self.ship_side = 'right'
