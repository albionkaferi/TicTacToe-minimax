class TicTacToe:

    def __init__(self):
        self.board = [" "] * 9
        self.turn = "X"
    
    def display(self):
        print("")
        for i in range(9):
            print(self.board[i], end="")
            if ((i+1) % 3 == 0):
                if (i == 8):
                    print("\n")
                else:
                    print("\n----------")
            else:
                print(" | ", end="")

    def is_full(self):
        for spot in self.board:
            if spot == " ":
                return False
        return True
    
    def check_winner(self):
        empty = " "
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]  # diagonal
        ]
        for combination in winning_combinations:
            if self.board[combination[0]] != empty and self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]]:
                return self.board[combination[0]]
        return empty
    
    def possible_moves(self):
        moves = []
        for i in range(9):
            if self.board[i] == " ":
                moves.append(i)
        return moves
        
    def make_move(self, position):
        if position not in self.possible_moves():
            return False
        self.board[position] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
        return True
    
    def get_best_move(self, game, player, alpha, beta):
        winner = game.check_winner()
        if winner == "X":
            return 1, None
        if winner == "O":
            return -1, None
        if game.is_full():
            return 0, None

        if player == "X":
            best_value = float('-inf')
            best_move = None
            for move in game.possible_moves():
                game.board[move] = "X" # make the move
                evaluation, _ = self.get_best_move(game, "O", alpha, beta)
                game.board[move] = " "  # undo the move
                if evaluation > best_value:
                    best_value = evaluation
                    best_move = move
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return best_value, best_move

        else:
            best_value = float('inf')
            best_move = None
            for move in game.possible_moves():
                game.board[move] = "O" # make the move
                evaluation, _ = self.get_best_move(game, "X", alpha, beta)
                game.board[move] = " "  # undo the move
                if evaluation < best_value:
                    best_value = evaluation
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return best_value, best_move
