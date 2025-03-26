import json
import os

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0

    def _load_high_score(self):
        """Load all high scores from a file."""
        filename = 'high_scores.json'
        if os.path.exists(filename):
            with open(filename) as f:
                return json.load(f)
        else:
            return {
                "easy": 0, 
                "normal": 0,
                "hard": 0
            }
        
    def load_high_score_for_difficulty(self, difficulty):
        """Load high score for a specific difficulty."""
        scores = self._load_high_score()
        return scores.get(difficulty, 0)
    
    def save_high_score(self, difficulty):
        """Save the high score for a specific difficulty."""
        scores = self._load_high_score()
        scores[difficulty] = self.high_score
        with open('high_scores.json', 'w') as f:
            json.dump(scores, f)

    