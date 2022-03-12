import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from fly import Fly
from plant import Plant
from scoreboard import Scoreboard
from random import randrange

class Flycatcher:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Flycatcher")

        # Create an instance to store game stats
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.plant = Plant(self)
        self.plants = pygame.sprite.Group()
        self.plants.add(self.plant)
        self.flies = pygame.sprite.Group()

        # Make the play button
        self.play_button = Button(self, 'Play')

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            
            # Initialize timestamp
            self.timestamp = pygame.time.get_ticks()

            if self.stats.game_active:
                self.plant.update()
                self._update_flies()
            self._update_screen()

    def _check_events(self):
        # respond to keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Start new game when user clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:

            # Reset stats
            self.stats.reset_stats()
            self.stats.game_active = True

            self.sb.prep_score()
            self.sb.prep_lives()

            # Get rid of any remaining flies
            self.flies.empty()

            # Center the plant and launch a fly
            self.plant.center_plant()

            # Hide mouse cursor
            pygame.mouse.set_visible(False)

    
    def _check_keydown_events(self, event):
        """respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.plant.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.plant.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        """respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.plant.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.plant.moving_left = False

    def _check_fly_plant_collisions(self):
        """Respond to any fly-plant collisions""" 
        # Look for fly-plant collisions
        if pygame.sprite.groupcollide(self.plants, self.flies,False, True):
            pygame.mixer.Sound.play(self.settings.caught_sound)
            self.stats.score += self.settings.fly_points
            self.sb.prep_score()


    def _create_fly(self):
        # Create and launch a fly
        fly = Fly(self)
        fly_width, fly_height = fly.rect.size
        fly.x = (self.settings.screen_width / 2) + randrange((-.4 * self.settings.screen_width),(.4*self.settings.screen_width))
        fly.rect.x = fly.x
        fly.rect.y = fly_height
        self.flies.add(fly)
    
    def _check_flies_bottom(self):
        """Check if any flies have hit the bottom"""
        screen_rect = self.screen.get_rect()
        for fly in self.flies.sprites():
            if fly.rect.bottom >= screen_rect.bottom:
                # consequences of fly hitting bottom
                pygame.mixer.Sound.play(self.settings.crash_sound)
                if self.settings.plant_count > 0:
                    self.settings.plant_count -= 1
                    self.sb.prep_lives()
                    sleep(0.5)
                    self.flies.remove(fly)
                else:
                    self.stats.game_active = False
                    self.settings.plant_count = 3
                    self.settings.lastFly = 0
                    pygame.mouse.set_visible(True)

    def _update_flies(self):
        """update position of flies"""
        if not self.flies:
            self._create_fly()
            self.settings.lastFly = self.timestamp
        elif (self.timestamp - self.settings.lastFly) > 3000:
            self._create_fly()
            self.settings.lastFly = self.timestamp
        self._check_fly_plant_collisions()
        self.flies.update() 
        # Look for flies hitting bottom of screen
        self._check_flies_bottom()

    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
         # redraw screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.plant.blitme()
        self.flies.draw(self.screen)

        # show scores and plant lives
        self.sb.show_score()

        # Draw play button if game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    fc = Flycatcher()
    fc.run_game()