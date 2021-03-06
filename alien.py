import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #represents a single alien from a fleet
    def __init__(self, ai_game):
        #initialize the alien and starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings


        #load the alien image and set its rect attribute
        self.image = pygame.image.load("images\\alien.png")
        self.rect = self.image.get_rect()

        #start each new alien near the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store alien exact position
        self.x = float(self.rect.x)

    def check_edges(self):
        #returns true if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        #move alien to the right or left
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x