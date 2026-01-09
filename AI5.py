import random

class TicTacToe:
    def __init__(self):
        self.board = []

    def create_board(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def get_random_first_player(self):
        return random.choice(['X', 'O'])

    def fix_spot(self, row, col, player):
        if self.board[row][col] == '-':
            self.board[row][col] = player
            return True
        return False

    def is_player_win(self, player):
        for row in self.board:
            if all(spot == player for spot in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_board_filled(self):
        return all(spot != '-' for row in self.board for spot in row)

    def show_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def start(self):
        self.create_board()
        player = self.get_random_first_player()
        while True:
            print(f"Player {player}'s turn")
            self.show_board()
            row, col = map(int, input("Enter row and column (1-3): ").split())
            if not self.fix_spot(row - 1, col - 1, player):
                print("Spot already taken, try again.")
                continue
            if self.is_player_win(player):
                print(f"Player {player} wins!")
                break
            if self.is_board_filled():
                print("It's a draw!")
                break
            player = 'O' if player == 'X' else 'X'
        self.show_board()

# Driver Code
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
