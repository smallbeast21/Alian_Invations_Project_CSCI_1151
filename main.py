import sys
import pygame
from settings import Settings
from ship import Ship

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
        
    def run_game(self) -> None:
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)
            
    def _update_screen(self) -> None:
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
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
