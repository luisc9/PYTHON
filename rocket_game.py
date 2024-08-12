import sys

import pygame

from settings import Settings

from rocket import Rocket

class RocketGame:
    """General class to managage game assets and behaviours"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        # Set background color
        self.settings = Settings()

        # Specific size for window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Full screen
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_height = self.screen.get_rect().height
        #self.settings.screen_width = self.screen.get_rect().width

        pygame.display.set_caption("Rocket game!!!")

        self.rocket = Rocket(self)

    def run_game(self):
        """Start main loop for the game"""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            # Move the rocket to the right
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the rocket to the left
            self.rocket.moving_left = True
        elif event.key == pygame.K_q:
            # Quit game at any moment if player presses Q
            sys.exit()
        elif event.key == pygame.K_UP:
            # Move the rocket up
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            # Move the rocket down
            self.rocket.moving_down = True

    def _check_keyup_events(self, event):
        """Respond to keyup"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        """Update images on screen and flip to new screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game
    rocketgame = RocketGame()
    rocketgame.run_game()