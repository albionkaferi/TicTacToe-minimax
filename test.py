import time
from tic_tac_toe import TicTacToe

class Test(TicTacToe):
    def __init__(self):
        super().__init__()
        self.calls = 0
    
    def minimax(self, game, player):
        self.calls += 1
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
                evaluation, _ = self.minimax(game, "O")
                game.board[move] = " "  # undo the move
                if evaluation > best_value:
                    best_value = evaluation
                    best_move = move
            return best_value, best_move
        else:
            best_value = float('inf')
            best_move = None
            for move in game.possible_moves():
                game.board[move] = "O" # make the move
                evaluation, _ = self.minimax(game, "X")
                game.board[move] = " "  # undo the move
                if evaluation < best_value:
                    best_value = evaluation
                    best_move = move
            return best_value, best_move
    

    def minimax_pruning(self, game, player, alpha, beta):
        self.calls += 1
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
                evaluation, _ = self.minimax_pruning(game, "O", alpha, beta)
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
                evaluation, _ = self.minimax_pruning(game, "X", alpha, beta)
                game.board[move] = " "  # undo the move
                if evaluation < best_value:
                    best_value = evaluation
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return best_value, best_move
    

def main():
    game = Test()
    move_num = 1
    while game.check_winner() == " " and not game.is_full():
        print("----------------------")
        print(f"Move {move_num}")
        
        game.calls = 0
        start_time = time.time()
        _, move1 = game.minimax(game, game.turn)
        end_time = time.time()
        regular_elapsed_time = round(end_time - start_time, 3)
        regular_calls = game.calls
        
        game.calls = 0
        start_time = time.time()
        _, move2 = game.minimax_pruning(game, game.turn, float("-inf"), float("inf"))
        end_time = time.time()
        pruning_elapsed_time = round(end_time - start_time, 3)
        pruning_calls = game.calls

        print("regular calls: ", regular_calls)
        print("pruning calls: ", pruning_calls)
        print("regular time: ", regular_elapsed_time)
        print("pruning time: ", pruning_elapsed_time)
        print(f"Same move? {move1==move2}")

        game.make_move(move1)
        move_num += 1

        print("----------------------\n\n")

if __name__ == "__main__":
    main()