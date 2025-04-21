"""
Module: manages a fleet of enemy ships.

Assets:
- Uses EnemyShip class (see enemy_ship.py)
"""

import pygame
from enemy_ship import EnemyShip

class EnemyFleet:
    """
    Manages a fleet of enemy spaceships arranged in rows along the horizontal axis.
    """
    def __init__(self, game) -> None:
        """
        Build the initial fleet formation.
        """
        self.game  = game
        self.fleet = pygame.sprite.Group()
        self.create_fleet()

    def create_fleet(self) -> None:
        """
        Calculate spacing and populate the fleet group.
        """
        sample_enemy  = EnemyShip(self.game)
        enemy_width   = sample_enemy.rect.width
        enemy_height  = sample_enemy.rect.height

        screen_h = self.game.settings.screen_h
        screen_w = self.game.settings.screen_w

        # Horizontal and vertical spacing calculations
        margin_right = enemy_width * 2
        available_x  = screen_w - margin_right - enemy_width
        per_row      = available_x // (enemy_width * 3)

        top_margin   = enemy_height
        available_y  = screen_h - (top_margin * 2)
        full_rows    = available_y // (enemy_height * 3)

        number_of_rows = max(1, full_rows - 1) + 2

        for row in range(int(number_of_rows)):
            for col in range(int(per_row)):
                enemy = EnemyShip(self.game)
                enemy.rect.x = enemy_width + (enemy_width * 3 * col)
                enemy.rect.y = top_margin + (enemy_height * 3 * row)
                enemy.x  = float(enemy.rect.x)
                self.fleet.add(enemy)

    def update(self) -> None:
        """
        Move each enemy toward the ship's side.
        """
        direction = 1 if self.game.ship.side == 'right' else -1
        for enemy in self.fleet.sprites():
            enemy.x += self.game.settings.enemy_speed * direction
            enemy.rect.x = int(enemy.x)

    def draw(self) -> None:
        """
        Draw all enemies to the screen.
        """
        for enemy in self.fleet.sprites():
            enemy.draw_enemy()
