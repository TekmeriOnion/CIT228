import pygame
from pygame.sprite import Sprite

class Plant(Sprite):
    """A class for the plant protagonist and its movement and actions"""

    def __init__(self,fc_game):
        """initialize carnivorous plant and set starting position"""
        super().__init__()
        self.screen = fc_game.screen
        self.settings = fc_game.settings
        self.screen_rect = fc_game.screen.get_rect()

        # load the plant image and get its rect
        self.image = pygame.image.load('images/flytrap.png')
        self.rect = self.image.get_rect()

        # start each new plant at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store decimal value for plant's horizontal position
        self.x = float(self.rect.x)

        # movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """update the plant's position based on the movement flag"""
        # update the plant's x value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.plant_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.plant_speed
        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """draw the plant at its current location"""
        self.screen.blit(self.image,self.rect)
    
    def center_plant(self):
        """Center the plant on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)