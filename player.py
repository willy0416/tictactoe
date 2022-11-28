import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class ComputerPlayer(Player):

    def get_move(self, game):
        square = random.choice(game.poss_moves())
        return square

class HumanPlayer(Player):

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.poss_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val
