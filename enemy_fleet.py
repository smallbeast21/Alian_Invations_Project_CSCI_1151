import pygame
from enemy_ship import EnemyShip

class EnemyFleet:
    def __init__(self, game) -> None:
        self.game = game
        self.fleet = pygame.sprite.Group()
        self.create_fleet()

    def create_fleet(self) -> None:
        # Create a sample enemy to get its dimensions.
        sample_enemy = EnemyShip(self.game)
        enemy_width = sample_enemy.rect.width
        enemy_height = sample_enemy.rect.height
        
        # Calculate available horizontal space
        # Leave a margin on the right so the enemy fleet stays further away from the rocket ship
        margin_right = enemy_width * 2  
        available_space_x = self.game.settings.screen_w - margin_right - enemy_width
        number_of_enemies_per_row = available_space_x // (enemy_width * 2)
        
        # Calculate vertical placement
        top_margin = enemy_height
        available_space_y = self.game.settings.screen_h - top_margin - enemy_height
        number_of_rows = available_space_y // (enemy_height * 2)
        if number_of_rows < 1:
            number_of_rows = 1

        # Create a grid of enemies (multiple rows and columns)
        for row in range(int(number_of_rows)):
            for col in range(int(number_of_enemies_per_row)):
                enemy = EnemyShip(self.game)
                # Place enemy starting from the left, spacing them evenly.
                enemy.rect.x = enemy_width + (enemy_width * 2 * col)
                # Vertically offset each row.
                enemy.rect.y = top_margin + (enemy_height * 2 * row)
                enemy.x = float(enemy.rect.x)
                self.fleet.add(enemy)
            
    def update(self) -> None:
        for enemy in self.fleet.sprites():
            enemy.update()
    
    def draw(self) -> None:
        for enemy in self.fleet.sprites():
            enemy.draw_enemy()
