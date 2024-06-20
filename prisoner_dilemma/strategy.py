from random import randint, uniform
import torch
from torch import Tensor

class Strategy:
    """Implementation of the strategies that can be used for the Predator Prey Game.

    Note: This is an inherited class.
    
    === Attributes ===
    decision: str
    """

    decision: str

    def __init__(self) -> None:
        """Initialize the strategy class."""

        self.decision = None
        self.actions = {"1": "Cooperate", "0": "Defect"}
    
    def return_decision(self) -> str:
        """Return the decision."""

        return self.decision

    def choose_action(self) -> str:
        """Use a strategy and then output a decision."""

        raise NotImplementedError
    
    def update_decision(self, decision: int) -> None:
        """Take in a decision and update self.decision by choosing an action."""

        self.decision = self.actions[str(decision)]

class Random(Strategy):
    """Implementation of the random strategy class.
    
    === Attributes ===
    decision: str
    """

    def __init__(self) -> None:
        """Initialize the random strategy class."""

        Strategy.__init__(self)
    
    def choose_action(self) -> str:
        """Choose an action using random number."""

        number = randint(0, 1)

        return number


class QLearning(Strategy):
    """Implementation of the QLearning strategy for 1 round only.
    
    # Some notes:
    Need to implement a value function.
    Rewards: 
        +2 For winning
        -2 For Losing

    === Attributes ===
    value: The total number of rewards based on a reward function
    epsilon: Probability of exploring
    step_size: The step size of the Q-Learning.
    """

    
    def __init__(self, epsilon: float) -> None:
        """Initialize the Q Learning for one round of Prisoner's Dilemma.
        """
        Strategy.__init__(self)
        
        self.value = torch.Tensor([0, 0]) # Value Function
        self.epsilon = epsilon
        #self.opponent = Random()

    def _update_value_function(self, decision: int, reward: int, episodes: int) -> None:
        """Take in a step size and then update the value function by taking in a decision:
        
        0: Defect
        1: Cooperate
        """

        self.value[decision] += (1/episodes) * (reward - self.value[decision])

    def fit(self, opponent_decision: str = None) -> None:
        """Take in the number of episodes, step size and epsilon and fit the epsilon greedy algorithm.
        """

        counter = 0

        probability = uniform(0, 1)

        if probability < (1 - self.epsilon):
            if counter == 0:
                decision = 1
            else:
                decision = int(torch.argmax(self.value))
            
        else:
            decision = randint(0, 1)
        
        if opponent_decision == 'Defect':
            opponent_decision = 0
        else:
            opponent_decision = 1
            
        if (opponent_decision == 1) and (decision == 1):
            self._update_value_function(counter, decision, 1)
        elif (opponent_decision == 1) and (decision == 0):
            self._update_value_function(counter, decision, 2)
        elif (opponent_decision == 0) and (decision == 1):
            self._update_value_function(counter, decision, -2)
        elif (opponent_decision == 0) and (decision == 0):
            self._update_value_function(counter, decision, 0)
        
    def choose_action(self) -> str:
        """Choose the best action using torch.argmax."""

        return int(torch.argmax(self.value))

