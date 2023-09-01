from tic_tac_toe import TicTacToe

def main():
    game = TicTacToe()

    while game.check_winner() == " " and not game.is_full():
        game.display()
        
        move = -1
        while True:
            choice = input("Enter a position or 'ai': ")
            if choice.isdigit() or choice.lower() == 'ai':
                break
            else:
                print("Invalid input. Please try again.")
        
        if choice.isdigit():
            move = int(choice) - 1
        else:
            _, move = game.get_best_move(game, game.turn, float("-inf"), float("inf"))

        game.make_move(move)


    game.display()
    winner = game.check_winner()
    if winner != " ":
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()