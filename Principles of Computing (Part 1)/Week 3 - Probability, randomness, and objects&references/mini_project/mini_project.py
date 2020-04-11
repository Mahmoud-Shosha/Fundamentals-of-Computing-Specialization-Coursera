"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1000         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 2.0   # Score for squares played by the other player

# Add your functions here.


def mc_trial(board, player):
    """
    :param board: The current board
    :param player: The next player to move
    :return: None (But modify the board input)
    Playing a game by making random moves, alternating between players
    """
    # Loop while the game is in progress
    while board.check_win() is None:
        # move the player to a random enpty square
        empty_square = random.choice(board.get_empty_squares())
        board.move(empty_square[0], empty_square[1], player)
        # Switch to the other player
        player = provided.switch_player(player)
    # print(board)


def mc_update_scores(scores, board, player):
    """
    :param scores: A grid of scores (the same dimension as the board)
    :param board: A board from a completed game
    :param player: The machine player
    :return: None (But modify the scores input)
    Update the scores grid using board
    """
    # Get the winner player
    winner = board.check_win()

    # No update as no winner
    if winner == provided.DRAW:
        return
    # Choose scores according to winner
    if winner == player:
        score_current = SCORE_CURRENT
        score_other = -1 * SCORE_OTHER
    else:
        score_current = -1 * SCORE_CURRENT
        score_other = SCORE_OTHER

    for row, dummy_element in enumerate(scores):
        for col, dummy_element in enumerate(scores):
            if board.square(row, col) == player:
                scores[row][col] += score_current
            elif board.square(row, col) == provided.switch_player(player):
                scores[row][col] += score_other


def get_best_move(board, scores):
    """
    :param board: A current board
    :param scores: A grid of scores
    :return: A tuple of form (row, col)
    Find all the empty squares in the board and return the one with maximum score
    """
    # get the index of the first empty square
    first_empty_square_index = board.get_empty_squares()[0]
    # get the score for it
    max_score = scores[first_empty_square_index[0]][first_empty_square_index[1]]
    # put it in the max_score_tuples list
    max_score_tuples = [first_empty_square_index]
    for row, row_list in enumerate(scores):
        for col, score in enumerate(row_list):
            if board.square(row, col) != provided.EMPTY:
                continue
            if score > max_score:
                max_score = score
                max_score_tuples = [(row, col)]
            elif score == max_score:
                max_score_tuples.append((row, col))

    return random.choice(max_score_tuples)


def mc_move(board, player, trials):
    """
    :param board: A current board
    :param player: The machine player
    :param trials: Number of tials to run
    :return: A tuple of form (row, col), which is the next move to the machine player
    Use Monte Carlo simulation to determine the next move for the machine player
    """
    scores = [[0 for dummy_i in range(board.get_dim())]
              for dummy_j in range(board.get_dim())]

    for dummy_trial in range(trials):
        new_board = board.clone()
        mc_trial(new_board, player)
        mc_update_scores(scores, new_board, player)
    return get_best_move(board, scores)


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
