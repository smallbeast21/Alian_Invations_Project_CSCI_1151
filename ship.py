# ship.py
import pygame
from settings import Settings

class Ship:
    """
    Represents the player's rocket ship.
    
    Attributes:
        game: Reference to the main game instance.
        settings: Game configuration settings.
        screen: Pygame display surface.
        original_image: Unrotated ship image.
        image: Rotated/scaled ship image.
        rect: Rect defining ship position.
        y (float): Precise vertical coordinate for movement.
        moving_up (bool), moving_down (bool): Movement flags.
    """
    def __init__(self, game) -> None:
        """
        Load the ship graphic, set its starting side, and initialize position/flags.

        Args:
            game: Reference to the AlienInvasion instance.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        # Load and scale the ship image
        self.original_image = pygame.image.load(self.settings.ship_file)
        self.original_image = pygame.transform.scale(
            self.original_image, (self.settings.ship_w, self.settings.ship_h)
        )
        
        # Set orientation & position based on starting side
        self.side = self.settings.ship_side
        self._set_orientation_and_position()
        
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def _set_orientation_and_position(self):
        """
        Rotate the ship image and place it at the appropriate edge based on self.side.
        """
        if self.side == 'left':
            self.image = pygame.transform.rotate(self.original_image, -90)
            self.rect = self.image.get_rect()
            self.rect.midleft = self.boundaries.midleft
        else:  # 'right'
            self.image = pygame.transform.rotate(self.original_image, 90)
            self.rect = self.image.get_rect()
            self.rect.midright = self.boundaries.midright

    def pick_side(self):

        self.side = 'left'
        self._set_orientation_and_position()
    
    def reset_position(self):
        """
        Reset the ship's position to its edge without changing side.
        """
        self._set_orientation_and_position()
        self.y = float(self.rect.y)

    def update(self):
        """
        Adjust the ship's vertical position based on movement flags, 
        then re-anchor horizontally to the chosen side.
        """
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = int(self.y)
        
        if self.side == 'left':
            self.rect.left = self.boundaries.left
        else:
            self.rect.right = self.boundaries.right

    def draw(self):
        """
        Draw the ship image at its current position.
        """
        self.screen.blit(self.image, self.rect)
