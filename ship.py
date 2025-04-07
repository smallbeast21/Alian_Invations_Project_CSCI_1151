import pygame
from settings import Settings

class Ship:
    def __init__(self, game) -> None:
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        # Load Ship
        self.original_image = pygame.image.load(self.settings.ship_file)
        self.original_image = pygame.transform.scale(
            self.original_image, (self.settings.ship_w, self.settings.ship_h)
        )
        
        # Pick Side
        self.side = self.settings.ship_side
        self._set_orientation_and_position()
        
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def _set_orientation_and_position(self):
        if self.side == 'left':
           
            self.image = pygame.transform.rotate(self.original_image, -90)
            self.rect = self.image.get_rect()
            self.rect.midleft = self.boundaries.midleft
        elif self.side == 'right':
          
            self.image = pygame.transform.rotate(self.original_image, 90)
            self.rect = self.image.get_rect()
            self.rect.midright = self.boundaries.midright

    def pick_side(self):
        if self.side == 'left':
            self.side = 'right'
        else:
            self.side = 'left'
        self._set_orientation_and_position()

    def update(self):
        
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = int(self.y)
        
        
        if self.side == 'left':
            self.rect.left = self.boundaries.left
        elif self.side == 'right':
            self.rect.right = self.boundaries.right

    def draw(self):
        self.screen.blit(self.image, self.rect)
