import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class StupidComputerPlayer(Player):

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

class GoodComputerPlayer(Player):
    def get_move(self, game):
        if len(game.poss_moves()) == 9:
            square = random.choice(game.poss_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None,
                    'score': state.num_empty_squares() + 1 if other_player == max_player else
                        -1 * (state.num_empty_squares() + 1)}

        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -float("inf")}
        else:
            best = {'position': None, 'score': float("inf")}

        for move in state.poss_moves():
            state.make_move(move, player)
            sim_score = self.minimax(state, other_player)
            state.board[move] = ' '
            state.current_winner = None
            sim_score['position'] = move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best