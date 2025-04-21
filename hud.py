"""
Module: displays Heads‑Up Display (score, high score, lives, level).

Assets:
- Uses RetroTech.ttf (system font file, see settings.py)
"""

import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_stats import GameStats
    from main import AlienInvasion

class HUD:
    """
    Manage on-screen display of scores, levels, and lives.
    """
    def __init__(self, game: 'AlienInvasion') -> None:
        """
        Initialize HUD elements and prepare initial renderings.
        """
        self.game  = game
        self.screen = game.screen
        self.settings = game.settings
        self.stats = game.game_stats

        # Ensure font path is a string
        self.font       = pygame.font.Font(
            str(self.settings.font_file),
            self.settings.HUD_font_size
        )
        self.padding = 20
        self._setup_life_image()
        self.update_scores()
        self.update_level()

    def _setup_life_image(self) -> None:
        """
        Load and scale ship icon for life indicators.
        """
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(
            self.life_image,
            (self.settings.ship_w, self.settings.ship_h)
        )
        self.life_rect = self.life_image.get_rect()

    def update_scores(self) -> None:
        """
        Re-render score, max score, and hi-score images.
        """
        self._update_max_score()
        self._update_score()
        self._update_hi_score()

    def _update_score(self) -> None:
        """
        Render current score image.
        """
        score_str = f"Score: {self.stats.score:,.0f}"
        self.score_image = self.font.render(
            score_str, True, self.settings.text_color
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top   = self.max_score_rect.bottom + self.padding
        self.score_rect.right = self.screen.get_rect().right - self.padding

    def _update_max_score(self) -> None:
        """
        Render max session score image.
        """
        max_str = f"Max: {self.stats.max_score:,.0f}"
        self.max_score_image = self.font.render(
            max_str, True, self.settings.text_color
        )
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.top   = self.padding
        self.max_score_rect.right = self.screen.get_rect().right - self.padding

    def _update_hi_score(self) -> None:
        """
        Render all-time high score image.
        """
        hi = self.stats.hi_score
        hi_str = f"Hi-Score: {hi:,.0f}"
        self.hi_score_image = self.font.render(
            hi_str, True, self.settings.text_color
        )
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (
            self.screen.get_rect().centerx, self.padding)

    def update_level(self) -> None:
        """
        Render current level image.
        """
        lvl_str = f"Level: {self.stats.level}"
        self.level_image = self.font.render(
            lvl_str, True, self.settings.text_color
        )
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top  = self.life_rect.bottom + self.padding

    def _draw_lives(self) -> None:
        """
        Draw ship icons equal to lives left.
        """
        x, y = self.padding, self.padding
        for _ in range(self.stats.ship_left):
            self.screen.blit(self.life_image, (x, y))
            x += self.life_rect.width + self.padding

    def draw(self) -> None:
        """
        Draw all HUD elements on the screen.
        """
        self.screen.blit(self.hi_score_image,  self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image,     self.score_rect)
        self._draw_lives()
        self.screen.blit(self.level_image,     self.level_rect)
