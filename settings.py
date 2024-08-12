class Settings:
    """Class to store all the settings of Rocket Game."""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_height = 600
        self.screen_width = 1200
        # White background
        self.bg_color = (255, 255, 255)
        #self.bg_color = (230, 230, 230)
        self.rocket_speed = 1.5
