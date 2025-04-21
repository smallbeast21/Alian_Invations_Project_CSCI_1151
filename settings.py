"""
settings.py

Module: game configuration and asset paths.

Assets:
- WhiteDualLaser.png (Bullet): laser sprite from Kenney.nl – https://kenney.nl/assets/space-shooter-extension
- RetroTech.ttf (Font): RetroTech font from DaFont – https://www.dafont.com/retrotech.font
"""

from pathlib import Path

class Settings:
    """
    Contains all configurable settings for the Alien Invasion game.

    Attributes:
        name (str): Title of the game window.
        screen_w (int): Width of the game screen.
        screen_h (int): Height of the game screen.
        FPS (int): Frames per second for the game loop.
        bg_file (Path): Path to background image.
        ship_file (Path): Path to ship image.
        enemy_file (Path): Path to enemy image.
        bullet_file (Path): Path to bullet image.
        ship_w (int): Width of the ship sprite.
        ship_h (int): Height of the ship sprite.
        ship_speed (float): Vertical movement speed of the ship.
        starting_ship_count (int): Number of ship lives at start.
        enemy_speed (float): Horizontal movement speed of enemies.
        bullet_speed (float): Horizontal movement speed of bullets.
        alien_points (int): Points awarded per alien destroyed.
        ship_side (str): Starting side of the ship ('left' or 'right').
        difficulty_scale (float): Scaling factor for difficulty.
        scores_file (Path): Path for saving high score data.
        button_w (int): Width of the Play button.
        button_h (int): Height of the Play button.
        button_color (tuple): RGB color of the Play button.
        text_color (tuple): RGB color for text elements.
        button_font_size (int): Font size for button text.
        HUD_font_size (int): Font size for HUD text.
        font_file (Path): Path to font file for UI text.
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
        base = Path(__file__).parent / 'Assets'
        self.bg_file = base / 'images' / 'SpacePixalBackground.png'
        self.ship_file = base / 'images' / 'YellowShip.png'
        self.enemy_file = base / 'images' / 'ememyShip.png'
        self.bullet_file = base / 'images' / 'WhiteDualLaser.png'

        # Sprite dimensions and speeds
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 8
        self.starting_ship_count = 3
        self.enemy_speed = 0.8
        self.bullet_speed = 15
        self.alien_points = 50

        # Ship starting side
        self.ship_side = 'right'

        # UI settings
        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)
        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 28  # increased for clearer score display

        # Font file path
        self.font_file = base / 'Fonts' / 'RetroTech.ttf'

        # Scoring and difficulty
        self.difficulty_scale = 1.1
        self.scores_file = Path(__file__).parent / 'Assets' / 'file' / 'scores.json'

    def initialize_dynamic_settings(self) -> None:
        """
        Initialize settings that change throughout the game.
        """
        self.ship_speed = 8
        self.starting_ship_count = 3
        self.enemy_speed = 0.8
        self.bullet_speed = 15
        self.ship_side = 'right'

    def increase_difficulty(self) -> None:
        """
        Increase speed settings for difficulty progression.
        """
        self.ship_speed *= self.difficulty_scale
        self.enemy_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
