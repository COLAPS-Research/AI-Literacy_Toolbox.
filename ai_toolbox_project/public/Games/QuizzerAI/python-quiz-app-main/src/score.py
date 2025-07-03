"""Score class"""


class Score:
    """Class to keep track of the score"""

    def __init__(self):
        """Initialize the score"""
        self.score = 0

    def increase_score(self, value: int = 1):
        """Increase the score by the given value"""
        self.score += value

    def reset_score(self):
        """Reset the score to 0"""
        self.score = 0
 
    def get_score(self):
        """Return the current score"""
        return self.score

    def decrease_score(self, value: int = 1):
        """Decrease the score by the given value"""
        self.score -= value
