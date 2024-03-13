from launchgame import launch_game
from user_input import get_user_input
from game_board import GameBoard



if __name__ == '__main__':
    live_cells, rounds_num, board_size = get_user_input()
    # create the game board
    board = GameBoard(live_cells,board_size)
    # Launch the game : each round calculate the alive cells and print the board
    launch_game(board, rounds_num)
