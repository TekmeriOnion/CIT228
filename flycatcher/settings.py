from pygame import mixer

class Settings:
    """A class to store all settings for Flycatcher"""

    def __init__(self):
        """initialize game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (235,164,77)

        # Fly settings
        self.fly_speed = 4

        # initialize and time since last fly
        self.lastFly = 2500

        # Plant settings
        self.plant_count = 3
        self.plant_speed = 1
        
        # Scoring
        self.fly_points = 100

        # Sound settings
        self.caught_sound = mixer.Sound('sounds/caught.mp3')
        self.crash_sound = mixer.Sound('sounds/nope.mp3')
