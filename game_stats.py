class GameStats:
    def __init__(self,di_game):
        self.settings = di_game.settings
        self.reset_stats()
        self.game_active = True
    def reset_stats(self):
        self.dragons_left = self.settings.dragon_limit