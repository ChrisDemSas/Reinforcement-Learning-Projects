from player import Player

class PrisonerDilemma:
    """Implementation of the Prisoner Dilemma Game.
    
    === Attributes ===
    player_one: First Player
    player_two: Second Player
    round: The current round
    """

    player_one: type
    player_two: type
    round: int

    def __init__(self, player_one: Player, player_two: Player) -> None:
        """Initialize the Predator Prey Game."""

        self.player_one = player_one
        self.player_two = player_two
        self.round = 1
    
    def place_decision(self, decision: str, player_number: int) -> None:
        """Place a decision for a player.
        
        Pre-Condition: player_number must be int and between 1 and 2.
        """

        if player_number == 1:
            self.player_one.update_decision(decision)
        elif player_number == 2:
            self.player_two.update_decision(decision)

    def battle(self) -> str:
        """Displays the battle results of the game and adds the score."""

        one_decision = self.player_one.decision
        two_decision = self.player_two.decision

        if one_decision == 'Cooperate' and two_decision == 'Cooperate':
            self.player_one.add_score(2)
            self.player_two.add_score(2)
            return 'Both Players Draw!'
        elif one_decision == 'Cooperate' and two_decision == 'Defect':
            self.player_two.add_score(5)
            return 'Player 2 Wins!'
        elif one_decision == 'Defect' and two_decision == 'Cooperate':
            self.player_one.add_score(5)
            return 'Player 1 Wins!'
        else:
            return 'Both Players Lose!'
    
    def update_round(self) -> None:
        """Updates the self.round."""

        self.round += 1
    