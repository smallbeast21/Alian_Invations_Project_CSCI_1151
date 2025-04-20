# enemy_ship.py
import pygame

class EnemyShip(pygame.sprite.Sprite):
    """
    Represents a single enemy spaceship.

    Attributes:
        game: Reference to the main game instance.
        settings: Game configuration settings.
        screen: Pygame display surface.
        image: Surface representation of the enemy.
        rect: Rect defining enemy position.
        x (float): Precise horizontal coordinate for movement.
    """
    def __init__(self, game) -> None:
        """
        Load and prepare the enemy ship sprite.

        Args:
            game: The main AlienInvasion instance.
        """
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        
        # Load and scale the enemy image
        self.image = pygame.image.load(self.settings.enemy_file)
        self.image = pygame.transform.scale(self.image, (70, 55))
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        
    def update(self):
        """
        Update the enemy's x-coordinate based on settings.enemy_speed.
        """
        self.x += self.settings.enemy_speed
        self.rect.x = int(self.x)
        
    def draw_enemy(self):
        """
        Draw the enemy on the screen at its current position.
        """
        self.screen.blit(self.image, self.rect)
