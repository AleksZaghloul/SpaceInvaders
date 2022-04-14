filename = 'high_scores.txt'

class GameStats:
    #track statistics for Alien Invasion
    def __init__(self, ai_game):
        #initialise stats
        self.settings = ai_game.settings
        self.reset_stats()

        #start game inactive
        self.game_active = False

        self.check_score_file()
        self.update_high_score_file()

    def reset_stats(self):
        #statistics that update during game
        self.ships_left = self.settings.ship_limit

        self.score = 0
        self.level = 0

    def check_score_file(self):
        with open(filename) as file_object:
            for line in file_object:
                scores_list = int(line)
        self.high_score = scores_list

    def update_high_score_file(self):
        with open(filename, 'w') as file_object:
            file_object.write(str(self.high_score))