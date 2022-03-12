import pygame
from pygame.sprite import Sprite
from random import randrange

class Fly(Sprite):
    """A class to represent a single fly in the fleet"""
    
    def __init__(self, fc_game):
        """Initialize fly and set starting position"""
        super().__init__()
        self.screen = fc_game.screen
        self.settings = fc_game.settings

        # Load fly image and set rect attribute
        self.image = pygame.image.load('images/fly.png')
        self.rect = self.image.get_rect()

        # Start each new fly near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store fly's exact horizontal position
        self.x = float(self.rect.x)

        # Store fly's exact vertical position
        self.y = float(self.rect.y)

    def check_left_edge(self):
        """Return True if fly is within one move of screen's left edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.left <= self.settings.fly_speed:
            return True
    
    def check_right_edge(self):
        """Return True if fly is within one move of screen's right edge"""
        screen_rect = self.screen.get_rect()
        if (self.rect.right + self.settings.fly_speed) >= screen_rect.right:
            return True


    def update(self):
        """Move fly both left/right and down with a degree of unpredictability"""
        speed = self.settings.fly_speed
        if self.check_left_edge():
            self.x += randrange(0,speed)
            self.rect.x = self.x
            self.y += randrange(0,speed)
            self.rect.y = self.y
        elif self.check_right_edge():
            self.x += randrange((speed*-1),0)
            self.rect.x = self.x
            self.y += randrange(0,speed)
            self.rect.y = self.y
        else:
            self.x += randrange((speed*-1),speed)
            self.rect.x = self.x
            self.y += randrange(0,speed)
            self.rect.y = self.y