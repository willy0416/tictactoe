import time
from player import HumanPlayer, StupidComputerPlayer, GoodComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range((j * 3), ((j + 1) * 3))] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def poss_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']
        # moves = []
        # for i, x in enumerate(self.board):
        #     if x == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.poss_moves())
        # return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check rows
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check columns
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        if not square % 2:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!")
                return letter

            letter = 'O' if letter == 'X' else 'X'
    
        time.sleep(0.5)

    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    print("Welcome to TicTacToe!")
    time.sleep(1)
    valid_input_1 = False
    polite = False
    while not valid_input_1:
        letter_choice = input("Would you like to move first or second? Respond with 1 or 2: ")
        try:
            turn = int(letter_choice)
            if turn not in [1, 2]:
                raise ValueError
            if turn == 1:
                x_player = HumanPlayer('X')
            else: 
                o_player = HumanPlayer('O')
                polite = True
            valid_input_1 = True
        except ValueError:
            print("Invalid input. Try again and don't be naughty.")
    valid_input_2 = False
    while not valid_input_2:
        opp = input("Would you like to play a dumb computer (0), a smart computer (1), or a human (2)? ")
        try:
            int_opp = int(opp)
            if int_opp not in [0, 1, 2]:
                raise ValueError
            if int_opp == 0 and not polite:
                o_player = StupidComputerPlayer('O')
            elif not int_opp:
                x_player = StupidComputerPlayer('X')
            
            if int_opp == 1 and not polite:
                o_player = GoodComputerPlayer('O')
            elif int_opp == 1:
                x_player = GoodComputerPlayer('X')
            
            if int_opp == 2 and not polite:
                o_player = HumanPlayer('O')
            elif int_opp == 2:
                x_player = HumanPlayer('X')
            valid_input_2 = True
        
        except ValueError:
            print("Give a number 0-2 ya doofus.")



        
    
    # while not valid_square:
    #     square = input(f"{self.letter}'s turn. Input move (0-8): ")
    #     try:
    #         val = int(square)
    #         if val not in game.poss_moves():
    #             raise ValueError
    #         valid_square = True
    #     except ValueError:
    #         print("Invalid square. Try again.")
    # return val
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)