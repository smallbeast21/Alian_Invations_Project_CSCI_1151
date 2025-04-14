import pygame

class EnemyShip(pygame.sprite.Sprite):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        
        # Load enemy image and optionally scale it
        self.image = pygame.image.load(self.settings.enemy_file)
        self.image = pygame.transform.scale(self.image, (70, 55))
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        
    def update(self):
        # Move enemy rightwards
        self.x += self.settings.enemy_speed
        self.rect.x = int(self.x)
        
    def draw_enemy(self):
        self.screen.blit(self.image, self.rect)
