class GameStats:
    #track statistics for Alien Invasion
    def __init__(self, ai_game):
        #initialise stats
        self.settings = ai_game.settings
        self.reset_stats()

        #start game inactive
        self.game_active = False

    def reset_stats(self):
        #statistics that update during game
        self.ships_left = self.settings.ship_limit