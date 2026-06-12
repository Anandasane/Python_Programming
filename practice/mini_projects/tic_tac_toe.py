# Problem Statement:
# Write a Python program to play a simple tic-tac-toe game for a given list of moves.
#
# Intuition:
# The board has 9 positions. After each move, check all winning combinations.
#
# Input:
moves_input = input("Enter move positions separated by spaces (0-8): ")

# Logic:
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def display(self):
        rows = []
        for index in range(0, 9, 3):
            rows.append(" | ".join(self.board[index:index + 3]))
        return "\n".join(rows)

    def make_move(self, position):
        if self.board[position] != " ":
            return False
        self.board[position] = self.current_player
        return True

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def winner(self):
        winning_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6),
        ]
        for first, second, third in winning_positions:
            if self.board[first] == self.board[second] == self.board[third] != " ":
                return self.board[first]
        return None

    def is_full(self):
        return " " not in self.board

    def is_over(self):
        return self.winner() is not None or self.is_full()


game = TicTacToe()
moves = [int(value) for value in moves_input.split()]
for move in moves:
    if 0 <= move <= 8:
        game.make_move(move)
        if game.is_over():
            break
        game.switch_player()

winner = game.winner()

# Output:
print(game.display())
if winner:
    print(f"Winner: {winner}")
elif game.is_full():
    print("Game is a draw.")
else:
    print("Game continues.")
