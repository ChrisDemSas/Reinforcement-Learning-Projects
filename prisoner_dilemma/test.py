from strategy import *
from player import *
from game import *

epsilon = 0.005

player_one = Player('Q-Learning', epsilon)
player_two = Player('Random')
game = PrisonerDilemma(player_one, player_two)

counter = 0
while counter < 20:
    player_two.make_decision()
    player_two_decision = player_two.print_decision()

    player_one.make_decision(opponent_feedback=player_two_decision)
    player_one_decision = player_one.print_decision()

    print(game.battle())

    counter += 1



