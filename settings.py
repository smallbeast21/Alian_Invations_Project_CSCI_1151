# settings.py
from pathlib import Path

class Settings:
    """
    Contains all configurable settings for the Alien Invasion game.

    Attributes:
        name (str): Title of the game window.
        screen_w (int): Width of the game screen.
        screen_h (int): Height of the game screen.
        FPS (int): Frames per second cap for the game loop.
        bg_file (Path): File path for the background image.
        ship_file (Path): File path for the ship image.
        enemy_file (Path): File path for enemy spaceship image.
        bullet_file (Path): File path for bullet image.
        ship_w (int): Width of the ship sprite.
        ship_h (int): Height of the ship sprite.
        ship_speed (float): Vertical movement speed of the ship.
        enemy_speed (float): Horizontal movement speed of enemies.
        bullet_speed (float): Horizontal movement speed of bullets.
        ship_side (str): Starting side for the ship ('left' or 'right').
    """
    def __init__(self) -> None:
        """
        Initialize game settings with default values and resource paths.
        """
        self.name = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        
        # Resource file paths
        self.bg_file = Path(__file__).parent / 'Assets' / 'images' / 'SpacePixalBackground.png'
        self.ship_file = Path(__file__).parent / 'Assets' / 'images' / 'YellowShip.png'
        self.enemy_file = Path(__file__).parent / 'Assets' / 'images' / 'ememyShip.png'
        self.bullet_file = Path(__file__).parent / 'Assets' / 'images' / 'WhiteDualLaser.png'
        
        # Sprite dimensions and speeds
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 8
        self.enemy_speed = 0.8
        self.bullet_speed = 15
        
        # Ship starting side (COULDNT GET LEFT TO WORK)
        self.ship_side = 'right'
