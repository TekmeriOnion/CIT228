class GameStats:
    """Track statistics for Flycatcher"""

    def __init__(self, fc_game):
        """Initialize stats"""
        self.settings = fc_game.settings
        self.reset_stats()
        # Start Flycatcher in an inactive state
        self.game_active = False

        # High score should never be reset
        self.high_score = 0
        # Used to report score at game over state
        self.last_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.score = 0