# Alian Invations Part 2
# Ishmael Kaloko
# 04/13/2025

"""
LAB 12
This is the first part of my Alian Invations project that where the player 
controls a spaceship that is fixed to either the left or right border of 
the screen and moves only vertically. The game has a full-screen background 
image, and the spaceship is designed to always face inward towards the center of 
the screen. The ship's position can be toggled between the left and right edges 
by pressing the 'T' key, while the up and down or W and S  keys allow for 
vertical movement. 

LAB 13 Addons
This version of my Alien Invasions project has a better ending game idea. 
The rocket ship starts on the right side of the window in this version. 
An enemy fleet has more than one row and column spaced along the screen with 
sufficient distance from the right edge. The player can shoot bullets 
by pressing the SPACE key. When an enemy spaceship is hit by a bullet, the enemy 
is destroyed. When any enemy spaceship hits the rocket ship or reaches the right 
ide of the window, the game resets and becomes difficult.
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from enemy_fleet import EnemyFleet
from bullet import Bullet

class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        # Load and scale background
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_w, self.settings.screen_h)
        )
        
        self.clock = pygame.time.Clock()
        self.running = True

        # Create the ship
        self.ship = Ship(self)
        
        # Create enemy fleet 
        self.enemy_fleet = EnemyFleet(self)
        
        # Create bullet group
        self.bullets = pygame.sprite.Group()
        
    def run_game(self) -> None:
        while self.running:
            self._check_events()
            self.ship.update()
            self.enemy_fleet.update()
            self.bullets.update()
            
            self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)
            
    def _check_collisions(self) -> None:
        
        collisions = pygame.sprite.groupcollide(self.enemy_fleet.fleet, self.bullets, True, True)
        
        for enemy in self.enemy_fleet.fleet.sprites():
            if enemy.rect.colliderect(self.ship.rect) or enemy.rect.right >= self.settings.screen_w:
                self._reset_game()
                break
        
    def _reset_game(self) -> None:
        # Reset the game: clear enemy fleet and bullets, then recreate the enemy fleet.
        self.enemy_fleet.fleet.empty()
        self.bullets.empty()
        self.enemy_fleet.create_fleet()
        self.ship.reset_position()
        
    def _update_screen(self) -> None:
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        # Draw all bullets.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemy_fleet.draw()
        pygame.display.flip()
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.ship.moving_down = True
                elif event.key == pygame.K_t:
                    self.ship.pick_side()
                elif event.key == pygame.K_SPACE:
                    
                    bullet_start = self.ship.rect.midleft
                    new_bullet = Bullet(self, bullet_start)
                    self.bullets.add(new_bullet)
                #quit button
                elif event.key == pygame.K_q:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            #Release Key
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.ship.moving_down = False

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
