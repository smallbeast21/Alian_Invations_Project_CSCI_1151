# bullet.py
import pygame

class Bullet(pygame.sprite.Sprite):
    """
    Represents a bullet fired by the player's ship.

    Attributes:
        game: Reference to the main game instance.
        settings: Game configuration settings.
        screen: Pygame display surface.
        image: Surface representation of the bullet.
        rect: Rect defining bullet position.
        x (float): Precise horizontal coordinate for movement.
        direction (int): Horizontal travel direction (-1 left, +1 right).
    """
    def __init__(self, game, start_pos, direction=None) -> None:
        """
        Create a new bullet at the given start position with an optional direction.

        Args:
            game: The main AlienInvasion instance.
            start_pos (tuple): (x, y) coords where bullet is spawned.
            direction (int, optional): -1 for leftward, +1 for rightward travel.
                                       Defaults based on ship side.
        """
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        
        # Load and scale the bullet image
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, (15, 5))
        self.rect = self.image.get_rect(center=start_pos)
        
        self.x = float(self.rect.x)
        if direction is None:
            direction = -1 if game.ship.side == 'right' else 1
        self.direction = direction
        
    def update(self):
        """
        Move the bullet horizontally according to its direction and speed.
        """
        self.x += self.direction * self.settings.bullet_speed
        self.rect.x = int(self.x)
        
    def draw_bullet(self):
        """
        Draw the bullet on the screen at its current position.
        """
        self.screen.blit(self.image, self.rect)
