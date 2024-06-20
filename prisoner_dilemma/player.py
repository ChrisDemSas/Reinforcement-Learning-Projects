### Implementation of the Player class

from strategy import *

class Player:
    """ Implementation of one player for the Predator-Prey game.

    === Attributes ===
    score: The current score of the player.
    decision: The decision made by the player: Defect or Co-operate.
    algorithm: The algorithm of the player, q-learning vs manual vs random.
    """

    score: int
    decision: str
    algorithm: str

    def __init__(self, algorithm: str, epsilon: float = None) -> None:
        """Initialize the Player class."""

        self.score = 0
        self.decision = ''

        if algorithm == 'Manual':
            self.algorithm = 'Manual'
            self.strategy = 'Manual'
        elif algorithm == 'Random':
            self.algorithm = 'Random'
            self.strategy = Random()
        elif algorithm == 'Q-Learning':
            self.algorithm = 'Q-Learning'
            self.strategy = QLearning(epsilon)
    
    def _update_decision(self, decision: int) -> None:
        """Take in a decision and then update self.decision.

        Pre-Condition:
        Decision must be either Cooperate or Defect.
        """

        if decision == 1:
            self.decision = 'Cooperate'
        elif decision == 0:
            self.decision = 'Defect'
    
    def add_score(self, new_score: int) -> None:
        """Add a score for the player."""

        self.score += new_score
    
    def make_decision(self, opponent_feedback = None) -> None:
        """Take in an opponent decision if algroithm is QLearning."""

        if self.algorithm == 'Q-Learning':
            self.strategy.fit(opponent_feedback)
            action = self.strategy.choose_action()
        elif self.algorithm == 'Random':
            action = self.strategy.choose_action()
        elif self.algorithm == 'Manual':
            action = input("What is your decision?")
        
        self._update_decision(action)
    
    def print_decision(self) -> str:
        """Print the decision."""

        return self.decision
