"""
Module: track game statistics and handle high-score persistence.

Assets:
- None (no external assets used here)
"""

from pathlib import Path
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import AlienInvasion

class GameStats:
    """
    Track statistics for Alien Invasion.

    Attributes:
        game: Reference to main game instance.
        settings: Game settings.
        ship_left (int): Number of ships remaining.
        score (int): Current score.
        level (int): Current game level.
        hi_score (int): Highest score recorded.
    """
    def __init__(self, game: 'AlienInvasion') -> None:
        """
        Initialize statistics; load high score from disk.
        """
        self.game = game
        self.settings  = game.settings
        self.max_score = 0
        self._init_saved_scores()
        self.reset_stats()

    def _init_saved_scores(self) -> None:
        """
        Load high score from file or initialize to zero.
        """
        path = self.settings.scores_file
        if path.exists() and path.stat().st_size > 0:
            try:
                data = json.loads(path.read_text())
                self.hi_score = data.get('hi_score', 0)
            except Exception:
                self.hi_score = 0
        else:
            self.hi_score = 0
            self.save_scores()

    def reset_stats(self) -> None:
        """
        Reset statistics for a new game.
        """
        self.ship_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def save_scores(self) -> None:
        """
        Save high score to disk.
        """
        data = {'hi_score': self.hi_score}
        try:
            Path(self.settings.scores_file).write_text(json.dumps(data, indent=4))
        except Exception as e:
            print(f"Error saving scores: {e}")

    def update(self, collisions) -> None:
        """
        Update score and high score when aliens are destroyed.
        """
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()
        self.save_scores()

    def _update_score(self, collisions) -> None:
        """
        Add points for each collision detected.
        """
        self.score += len(collisions) * self.settings.alien_points

    def _update_max_score(self) -> None:
        """
        Track maximum score seen this session.
        """
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_hi_score(self) -> None:
        """
        Update stored high score if current score exceeds it.
        """
        if self.score > self.hi_score:
            self.hi_score = self.score

    def update_level(self) -> None:
        """
        Increment game level when a fleet is cleared.
        """
        self.level += 1
