import pygame


class Ship():
    #a class to manage the ship
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get its rect
        self.image = pygame.image.load('images\ship.png')
        self.image.set_colorkey((255, 0, 255))
        self.rect = self.image.get_rect()

        #start each new ship in bottom centre
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a deciml valur for horizontal position
        self.x = float(self.rect.x)

        #movement flags
        self.moving_left = False
        self.moving_right = False
    
    def update(self):
        #update the ship's position based on movement flags
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        #draw ship at current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        #after hit create new ship in centre
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)