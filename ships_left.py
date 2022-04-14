import pygame
from pygame.sprite import Sprite


class LittleShip(Sprite):
    #a class to manage the ship
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get its rect
        self.image = pygame.image.load('images\littleship.png')
        self.rect = self.image.get_rect()