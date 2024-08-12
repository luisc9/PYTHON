import pygame

class Rocket:
    """A class to manage the rocket"""

    def __init__(self, rocketgame):
        """Initialize the rocket and set its starting position"""
        self.screen = rocketgame.screen
        self.settings = rocketgame.settings
        self.screen_rect = rocketgame.screen.get_rect()

        # Load the rocket image and get its rect
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()

        # Start each new rocket at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal valui for the rocket horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket' position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Udate rect  object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket in the current location"""
        self.screen.blit(self.image, self.rect)
