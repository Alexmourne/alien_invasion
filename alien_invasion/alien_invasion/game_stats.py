from game_functions import get_stored_highscore

class Game_Stats():
    """description of class"""
    def __init__(self, ai_settings):
        """"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #
        self.game_active = True

        #
        self.high_score = self.init_highscore()

    def reset_stats(self):
        """"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def init_highscore(self):
        self.highscore = get_stored_highscore(self.ai_settings)

        if self.highscore:
            return int(self.highscore)
        else:
            self.highscore = 0
            return self.highscore

