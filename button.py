"""
Module: defines the Play button for starting the game.

Assets:
- Uses RetroTech.ttf (system font file, see settings.py)
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import AlienInvasion

class Button:
    """
    A clickable button to start the game.

    Attributes:
        game: Reference to main game instance.
        screen: Pygame display surface.
        rect: Rect for button area.
        msg_image: Rendered text surface.
        msg_image_rect: Rect for text.
    """
    def __init__(self, game: 'AlienInvasion', msg: str) -> None:
        """
        Initialize button attributes and render message.
        """
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.rect = pygame.Rect(
            0, 0,
            self.settings.button_w,
            self.settings.button_h
        )
        self.rect.center = self.screen.get_rect().center

        # Convert Path to string for font
        self.font     = pygame.font.Font(
            str(self.settings.font_file),
            self.settings.button_font_size
        )
        self._prep_msg(msg)

    def _prep_msg(self, msg: str) -> None:
        """
        Render the button message as an image.
        """
        self.msg_image = self.font.render(
            msg,
            True,
            self.settings.text_color,
            None
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self) -> None:
        """
        Draw button rectangle and text.
        """
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos) -> bool:
        """
        Return True if mouse_pos is inside button area.
        """
        return self.rect.collidepoint(mouse_pos)
