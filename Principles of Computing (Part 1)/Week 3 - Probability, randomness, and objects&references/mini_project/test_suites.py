"""
Tests for the 2048 game
"""

from poc_simpletest import TestSuite

from poc_ttt_provided import TTTBoard, PLAYERX, PLAYERO, switch_player
from mini_project import (SCORE_CURRENT, SCORE_OTHER,
                          mc_trial, mc_update_scores, get_best_move, mc_move)


def test_mc_trial():
    """
    Tests for the function mc_trial()
    """
    print("Tests for 'mc_trial' function")
    test_suite = TestSuite()

    # Testing the zero dimension board
    ttt_board = TTTBoard(0)
    mc_trial(ttt_board, PLAYERX)
    result = ttt_board.check_win() is not None
    test_suite.run_test(result, True, '0')

    # Testing the board at the begining with player PLAYERX
    ttt_board = TTTBoard(3)
    mc_trial(ttt_board, PLAYERX)
    result = ttt_board.check_win() is not None
    test_suite.run_test(result, True, '1')

    # Testing the board at the begining with player PLAYERO
    ttt_board = TTTBoard(3)
    mc_trial(ttt_board, PLAYERO)
    result = ttt_board.check_win() is not None
    test_suite.run_test(result, True, '2')

    # Testing the board at in the game middle
    ttt_board = TTTBoard(3)
    ttt_board.move(0, 0, PLAYERO)
    ttt_board.move(0, 1, PLAYERO)
    mc_trial(ttt_board, PLAYERO)
    result = ttt_board.check_win() is not None
    test_suite.run_test(result, True, '3')

    # Testing the board at in the game end
    ttt_board = TTTBoard(3)
    ttt_board.move(0, 0, PLAYERO)
    ttt_board.move(0, 1, PLAYERO)
    ttt_board.move(0, 2, PLAYERO)
    mc_trial(ttt_board, PLAYERO)
    result = ttt_board.check_win() is not None
    test_suite.run_test(result, True, '4')

    # Testing the board when the board is full
    ttt_board = TTTBoard(2)
    ttt_board.move(0, 0, PLAYERO)
    ttt_board.move(0, 1, PLAYERO)
    ttt_board.move(1, 0, PLAYERO)
    ttt_board.move(1, 1, PLAYERO)
    mc_trial(ttt_board, PLAYERO)
    result = ttt_board.check_win() is not None
    test_suite.run_test(result, True, '5')

    # Show report
    test_suite.report_results()


def get_completed_board(ttt_board, winner):
    """
    make the player 'winner' the winner in this board
    """
    ttt_board.move(0, 0, winner)
    ttt_board.move(0, 1, winner)
    ttt_board.move(0, 2, winner)
    ttt_board.move(1, 1, switch_player(winner))


def test_mc_update_scores():
    """
    Tests for the function mc_update_scores()
    """
    print("Tests for 'mc_update_scores' function")
    test_suite = TestSuite()

    # Testing with machine player is winner, let machine player is PLAYERX
    ttt_board = TTTBoard(3)
    get_completed_board(ttt_board, PLAYERX)

    scores = [[5+SCORE_CURRENT, 0+SCORE_CURRENT, 0+SCORE_CURRENT],
              [0, 0-SCORE_OTHER, 0],
              [0, 0, 0]]
    passed_scores = [[5, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
    mc_update_scores(passed_scores, ttt_board, PLAYERX)
    test_suite.run_test(passed_scores, scores, '0')

    # Testing with machine player is winner, let machine player is PLAYERO
    ttt_board = TTTBoard(3)
    get_completed_board(ttt_board, PLAYERO)

    scores = [[5+SCORE_CURRENT, 0+SCORE_CURRENT, 0+SCORE_CURRENT],
              [0, 0-SCORE_OTHER, 0],
              [0, 0, 0]]
    passed_scores = [[5, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
    mc_update_scores(passed_scores, ttt_board, PLAYERO)
    test_suite.run_test(passed_scores, scores, '1')

    # Testing with machine player is loser
    ttt_board = TTTBoard(3)
    get_completed_board(ttt_board, PLAYERO)

    scores = [[5+SCORE_OTHER, 0+SCORE_OTHER, 0+SCORE_OTHER],
              [0, 0-SCORE_CURRENT, 0],
              [0, 0, 0]]
    passed_scores = [[5, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
    mc_update_scores(passed_scores, ttt_board, PLAYERX)
    test_suite.run_test(passed_scores, scores, '2')

    # Testing with machine player is loser Twice
    ttt_board = TTTBoard(3)
    ttt_board.move(0, 0, PLAYERO)
    ttt_board.move(1, 0, PLAYERO)
    ttt_board.move(2, 0, PLAYERO)
    ttt_board.move(1, 1, PLAYERX)

    scores = [[5+SCORE_OTHER+SCORE_OTHER, 0+SCORE_OTHER, 0+SCORE_OTHER],
              [0+SCORE_OTHER, 0-SCORE_CURRENT-SCORE_CURRENT, 0],
              [0+SCORE_OTHER, 0, 0]]
    mc_update_scores(passed_scores, ttt_board, PLAYERX)
    test_suite.run_test(passed_scores, scores, '3')

    # Testing a tie
    ttt_board = TTTBoard(3)
    ttt_board.move(0, 0, PLAYERO)
    ttt_board.move(0, 1, PLAYERX)
    ttt_board.move(0, 2, PLAYERX)
    ttt_board.move(1, 0, PLAYERX)
    ttt_board.move(1, 1, PLAYERX)
    ttt_board.move(1, 2, PLAYERO)
    ttt_board.move(2, 0, PLAYERO)
    ttt_board.move(2, 1, PLAYERO)
    ttt_board.move(2, 2, PLAYERX)

    scores = [[5, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    passed_scores = [[5, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
    mc_update_scores(passed_scores, ttt_board, PLAYERX)
    test_suite.run_test(passed_scores, scores, '4')


    # Show report
    test_suite.report_results()


def test_get_best_move():
    """
    Tests for the function get_best_move()
    """
    print("Tests for 'get_best_move' function")
    test_suite = TestSuite()

    # Testing with zeros scores
    ttt_board = TTTBoard(3)
    ttt_board.move(0, 0, PLAYERX)
    ttt_board.move(1, 1, PLAYERX)
    ttt_board.move(2, 2, PLAYERO)

    scores = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    max_score = get_best_move(ttt_board, scores)
    test_suite.run_test(scores[max_score[0]][max_score[1]], 0, '0')

    # Testing with one maximum
    scores = [[0, 0, 0],
              [0, 0, 5],
              [-55, 0, 0]]
    max_score = get_best_move(ttt_board, scores)
    test_suite.run_test(scores[max_score[0]][max_score[1]], 5, '1')

    # Testing with more than one maximum
    scores = [[0, 0, 5],
              [5, 0, 5],
              [-55, 0, 0]]
    max_score = get_best_move(ttt_board, scores)
    test_suite.run_test(scores[max_score[0]][max_score[1]], 5, '2')

    # Testing with maximum in non-empty squares
    scores = [[0, 0, 5],
              [5, 0, 5],
              [-55, 0, 30]]
    max_score = get_best_move(ttt_board, scores)
    test_suite.run_test(scores[max_score[0]][max_score[1]], 5, '3')


    test_suite.report_results()


def test_mc_move():
    """
    Tests for the function mc_move()
    """
    print("Tests for 'mc_move' function")
    test_suite = TestSuite()

    # Testing with zeros scores
    ttt_board = TTTBoard(3)
    ttt_board.move(0, 0, PLAYERX)
    ttt_board.move(0, 1, PLAYERX)
    ttt_board.move(2, 2, PLAYERO)

    nex_move_index = mc_move(ttt_board, PLAYERX, 1000)
    test_suite.run_test(nex_move_index, (0, 2), '0')



    test_suite.report_results()


# Running tests
test_mc_trial()
print()
test_mc_update_scores()
print()
test_get_best_move()
print()
test_mc_move()
