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

LAB 13 (Edits)
- Added Starting adding Doc strings to methods
- Fix the left right issue to only let the ship be on the right (Too many issues)
- Added Req File

LAB 14 Addons
This update adds a proper start screen and on-screen status so you always know
 what’s happening. When the game loads (or after losing all lives), a big “Play”
button appears—click to begin (or press Q to quit anytime). The mouse pointer 
hides during play. Once in, a HUD shows your score, session best, all-time highz
score, level, and remaining lives (as ship icons). After each wave or lost 
life, the wave resets and speeds up your ship, bullets, and enemies—making 
things tougher each round.


Module: the primary game loop handling initialization, events, updates, and rendering.

Assets:
- Integrates all sprites, HUD, and button assets defined in other modules.
"""

import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from enemy_fleet import EnemyFleet
from bullet import Bullet
from button import Button
from hud import HUD

class AlienInvasion:
    """
    Manage game initialization, main loop, and overall orchestration.
    """
    def __init__(self) -> None:
        """
        Initialize pygame, hide cursor, load resources, and create game objects.
        """
        pygame.init()
        self.settings    = Settings()
        self.settings.initialize_dynamic_settings()

        self.screen      = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)
        pygame.mouse.set_visible(False)

        # Load and scale background
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg,
            (self.settings.screen_w, self.settings.screen_h)
        )

        # Game state and entities
        self.clock        = pygame.time.Clock()
        self.running      = True
        self.game_active  = False

        self.game_stats   = GameStats(self)
        self.hud          = HUD(self)
        self.play_button  = Button(self, 'Play')

        self.ship         = Ship(self)
        self.enemy_fleet  = EnemyFleet(self)
        self.bullets      = pygame.sprite.Group()

    def run_game(self) -> None:
        """
        Enter main game loop: events, updates, collisions, and rendering.
        """
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.enemy_fleet.update()
                self.bullets.update()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self) -> None:
        """
        Handle bullet-enemy collisions, ship hits, and level completion.
        """
        # Bullet vs. enemy
        collisions = pygame.sprite.groupcollide(
            self.enemy_fleet.fleet,
            self.bullets,
            True,
            True
        )
        if collisions:
            self.game_stats.update(collisions)
            self.hud.update_scores()

        # Ship hit or enemy breach
        for enemy in self.enemy_fleet.fleet.sprites():
            if (enemy.rect.colliderect(self.ship.rect) or
                enemy.rect.right >= self.settings.screen_w):
                self._ship_hit()
                break

        # Level cleared
        if not self.enemy_fleet.fleet:
            self.settings.increase_difficulty()
            self.game_stats.update_level()
            self.hud.update_level()
            self._reset_level()

    def _ship_hit(self) -> None:
        """
        Respond to ship being hit: lose a life or end game if no lives left.
        """
        self.game_stats.ship_left -= 1
        self.hud.update_scores()

        if self.game_stats.ship_left > 0:
            self._reset_level()
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _reset_level(self) -> None:
        """
        Prepare for next wave: clear bullets and enemies, recreate fleet, and center ship.
        """
        self.bullets.empty()
        self.enemy_fleet.fleet.empty()
        self.enemy_fleet.create_fleet()
        self.ship.reset_position()

    def _check_events(self) -> None:
        """
        Process keyboard and mouse events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.KEYDOWN and self.game_active:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP and self.game_active:
                self._check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_active:
                if self.play_button.check_clicked(event.pos):
                    self._start_game()

    def _start_game(self) -> None:
        """
        Begin a new game: reset stats, difficulty, HUD, and game entities.
        """
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.hud.update_scores()
        self.hud.update_level()

        self.enemy_fleet.fleet.empty()
        self.enemy_fleet.create_fleet()
        self.bullets.empty()
        self.ship.reset_position()

        self.game_active = True
        pygame.mouse.set_visible(False)

    def _check_keydown(self, event) -> None:
        """
        Respond to key presses for movement and firing.
        """
        if event.key in (pygame.K_UP, pygame.K_w):
            self.ship.moving_up = True
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            direction = -1 if self.ship.side == 'right' else 1
            start = (
                self.ship.rect.midleft if direction == -1
                else self.ship.rect.midright
            )
            self.bullets.add(Bullet(self, start, direction))
        elif event.key == pygame.K_q:
            self._quit_game()

    def _check_keyup(self, event) -> None:
        """
        Respond to key releases for movement.
        """
        if event.key in (pygame.K_UP, pygame.K_w):
            self.ship.moving_up = False
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.ship.moving_down = False

    def _update_screen(self) -> None:
        """
        Draw background, sprites, HUD or play button, then flip display.
        """
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemy_fleet.draw()

        if self.game_active:
            self.hud.draw()
        else:
            pygame.mouse.set_visible(True)
            self.play_button.draw()

        pygame.display.flip()

    def _quit_game(self) -> None:
        """
        End game loop, save scores, and quit pygame.
        """
        self.game_stats.save_scores()
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
