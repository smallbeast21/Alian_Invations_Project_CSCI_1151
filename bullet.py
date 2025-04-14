import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, start_pos) -> None:
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        
        # Load bullet image
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, (15, 5))
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        
        self.x = float(self.rect.x)
        
    def update(self):
        self.x -= self.settings.bullet_speed
        self.rect.x = int(self.x)
        
    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
