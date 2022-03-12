import pygame.font
from pygame.sprite import Group
from plant import Plant
from settings import Settings

class Scoreboard:
    """A class to report scoring info"""
    def __init__(self, fc_game):
        """Initialize scorekeeping attributes"""
        self.fc_game = fc_game
        self.screen = fc_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = fc_game.settings
        self.stats = fc_game.stats

        # Font settings for scoring info
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # Prep initial score image
        self.prep_score()
        self.prep_lives()
    
    def prep_score(self):
        """Turn score into rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_lives(self):
        """Turn lives into rendered image"""
        lives = round(self.settings.plant_count)
        life_str = "Lives: " + "{:,}".format(lives)
        self.life_img = self.font.render(life_str, True, self.text_color, self.settings.bg_color)

        # Display the lives at the top right under score
        self.life_rect = self.life_img.get_rect()
        self.life_rect.right = self.screen_rect.right - 20
        self.life_rect.top = self.score_rect.bottom + 5

    def show_score(self):
        """Draw score and life info to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.life_img, self.life_rect)
