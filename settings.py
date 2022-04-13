import alien
class Settings:
    #A class to store all settings for alien invasion
    def __init__(self):
        #initialise the game's settings.
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 215, 230)

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1