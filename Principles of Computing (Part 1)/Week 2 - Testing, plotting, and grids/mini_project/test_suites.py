"""
Tests for the 2048 game
"""

from poc_simpletest import TestSuite


def test_trail_zeros(trail_zeros):
    """
    Tests for the function trail_zeros()
    """

    test_suite = TestSuite()

    # empty list
    test_suite.run_test(trail_zeros([]), [])
    # list with one item
    test_suite.run_test(trail_zeros([0, ]), [0, ])
    test_suite.run_test(trail_zeros([8, ]), [8, ])
    # list with two items
    test_suite.run_test(trail_zeros([0, 5]), [5, 0])
    test_suite.run_test(trail_zeros([5, 0]), [5, 0])
    # list with three items
    test_suite.run_test(trail_zeros([-1, 6, 0]), [-1, 6, 0])
    test_suite.run_test(trail_zeros([-1, 0, 6]), [-1, 6, 0])
    test_suite.run_test(trail_zeros([0, -1, 6]), [-1, 6, 0])
    # list with more than one zero
    test_suite.run_test(trail_zeros([0, 0, 6]), [6, 0, 0])

    test_suite.report_results()


def test_adjacent_merge(adjacent_merge):
    """
    Tests for the function adjacent_merge()
    """

    test_suite = TestSuite()

    # empty list
    test_suite.run_test(adjacent_merge([]), [])
    # list with one item
    test_suite.run_test(adjacent_merge([0, ]), [0, ])
    test_suite.run_test(adjacent_merge([9, ]), [9, ])
    # list with two items
    test_suite.run_test(adjacent_merge([0, 0]), [0, 0])
    test_suite.run_test(adjacent_merge([9, 9]), [18, 0])
    # list with three items
    test_suite.run_test(adjacent_merge([3, 3, 0]), [6, 0, 0])
    test_suite.run_test(adjacent_merge([3, 3, 3]), [6, 0, 3])
    test_suite.run_test(adjacent_merge([0, 3, 3]), [0, 6, 0])
    # list with four items
    test_suite.run_test(adjacent_merge([3, 3, 3, 0]), [6, 0, 3, 0])
    test_suite.run_test(adjacent_merge([3, 3, 0, 3]), [6, 0, 0, 3])
    test_suite.run_test(adjacent_merge([3, 3, 3, 3]), [6, 0, 6, 0])
    test_suite.run_test(adjacent_merge([3, 0, 3, 3]), [3, 0, 6, 0])

    test_suite.report_results()


def test_merge(merge):
    """
    Tests for the function merge()
    """

    test_suite = TestSuite()

    test_suite.run_test(merge([]), [])
    test_suite.run_test(merge([4, 0, 4, 4]), [8, 4, 0, 0])
    test_suite.run_test(merge([0, 0, 0, 4]), [4, 0, 0, 0])

    test_suite.report_results()


def TwentyFortyEight___init__(TwentyFortyEight):
    """
    Tests for the function __init__()  in TwentyFortyEight class
    """

    test_suite = TestSuite()

    # test height, width, initial_tiles, cells_number
    # and reset() method call for an empty grid
    twenty_forty_eight = TwentyFortyEight(0, 0)
    test_suite.run_test(twenty_forty_eight._grid_height, 0)
    test_suite.run_test(twenty_forty_eight._grid_width, 0)
    test_suite.run_test(len(twenty_forty_eight._grid), 0)
    test_suite.run_test(twenty_forty_eight._tiles_number[1], 0)
    test_suite.run_test(twenty_forty_eight._tiles_number[2], 0)
    test_suite.run_test(twenty_forty_eight._tiles_number[3], 0)
    test_suite.run_test(twenty_forty_eight._tiles_number[4], 0)

    # test height, width, initial_tiles, cells_number
    # and reset() method call for a non-empty  grid
    twenty_forty_eight = TwentyFortyEight(5, 6)
    test_suite.run_test(twenty_forty_eight._grid_height, 5)
    test_suite.run_test(twenty_forty_eight._grid_width, 6)
    test_suite.run_test(twenty_forty_eight._initial_tiles[1],
                        [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)])
    test_suite.run_test(twenty_forty_eight._initial_tiles[2],
                        [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)])
    test_suite.run_test(twenty_forty_eight._initial_tiles[3],
                        [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])
    test_suite.run_test(twenty_forty_eight._initial_tiles[4],
                        [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5)])
    test_suite.run_test(len(twenty_forty_eight._grid), 5)
    test_suite.run_test(len(twenty_forty_eight._grid[0]), 6)
    test_suite.run_test(twenty_forty_eight._tiles_number[1], 5)
    test_suite.run_test(twenty_forty_eight._tiles_number[2], 5)
    test_suite.run_test(twenty_forty_eight._tiles_number[3], 6)
    test_suite.run_test(twenty_forty_eight._tiles_number[4], 6)

    test_suite.report_results()


def TwentyFortyEight_get_grid(TwentyFortyEight):
    """
    Tests for the function get_grid()  in TwentyFortyEight class
    """

    test_suite = TestSuite()

    # test grid for an empty grid
    twenty_forty_eight = TwentyFortyEight(0, 0)
    test_suite.run_test(len(twenty_forty_eight.get_grid()), 0)

    # test grid for a non-empty grid
    twenty_forty_eight = TwentyFortyEight(5, 6)
    test_suite.run_test(len(twenty_forty_eight.get_grid()), 5)
    test_suite.run_test(len(twenty_forty_eight.get_grid()[0]), 6)
    test_suite.run_test(len(twenty_forty_eight.get_grid()[5 - 1]), 6)

    test_suite.report_results()


def TwentyFortyEight_get_grid_height(TwentyFortyEight):
    """
    Tests for the function get_grid_height()  in TwentyFortyEight class
    """

    test_suite = TestSuite()

    # test height for an empty grid
    twenty_forty_eight = TwentyFortyEight(0, 0)
    test_suite.run_test(twenty_forty_eight.get_grid_height(), 0)

    # test height for a non-empty grid
    twenty_forty_eight = TwentyFortyEight(5, 6)
    test_suite.run_test(twenty_forty_eight.get_grid_height(), 5)

    test_suite.report_results()


def TwentyFortyEight_get_grid_width(TwentyFortyEight):
    """
    Tests for the function get_grid_width()  in TwentyFortyEight class
    """

    test_suite = TestSuite()

    # test width for an empty grid
    twenty_forty_eight = TwentyFortyEight(0, 0)
    test_suite.run_test(twenty_forty_eight.get_grid_width(), 0)

    # test width for a non-empty grid
    twenty_forty_eight = TwentyFortyEight(5, 6)
    test_suite.run_test(twenty_forty_eight.get_grid_width(), 6)

    test_suite.report_results()


def TwentyFortyEight_get_tile(TwentyFortyEight):
    """
    Tests for the function get_tile()  in TwentyFortyEight class
    """

    test_suite = TestSuite()

    # test a cell for a non-empty grid
    twenty_forty_eight = TwentyFortyEight(5, 6)
    twenty_forty_eight._grid[0][0] = 25
    twenty_forty_eight._grid[0][2] = 26
    twenty_forty_eight._grid[3][2] = 27
    twenty_forty_eight._grid[4][5] = 28
    test_suite.run_test(twenty_forty_eight.get_tile(0, 0), 25)
    test_suite.run_test(twenty_forty_eight.get_tile(0, 2), 26)
    test_suite.run_test(twenty_forty_eight.get_tile(3, 2), 27)
    test_suite.run_test(twenty_forty_eight.get_tile(4, 5), 28)

    test_suite.report_results()


def TwentyFortyEight_set_tile(TwentyFortyEight):
    """
    Tests for the function set_tile()  in TwentyFortyEight class
    """

    test_suite = TestSuite()

    # test a cell for a non-empty grid
    twenty_forty_eight = TwentyFortyEight(5, 6)
    twenty_forty_eight.set_tile(0, 0, 25)
    twenty_forty_eight.set_tile(0, 2, 26)
    twenty_forty_eight.set_tile(3, 2, 27)
    twenty_forty_eight.set_tile(4, 5, 28)
    test_suite.run_test(twenty_forty_eight.get_tile(0, 0), 25)
    test_suite.run_test(twenty_forty_eight.get_tile(0, 2), 26)
    test_suite.run_test(twenty_forty_eight.get_tile(3, 2), 27)
    test_suite.run_test(twenty_forty_eight.get_tile(4, 5), 28)

    test_suite.report_results()


def TwentyFortyEight___str__(TwentyFortyEight):
    """
    Tests for the function __str__()  in TwentyFortyEight class
    """

    test_suite = TestSuite()

    # test an empty grid
    twenty_forty_eight = TwentyFortyEight(0, 0)
    test_suite.run_test(str(twenty_forty_eight), "")
    # test a non-empty grid
    twenty_forty_eight = TwentyFortyEight(55, 32)
    result = ""
    for i in range(55):
        for j in range(32):
            result += str(twenty_forty_eight.get_tile(i, j)) + " "
        result += "\n"
    test_suite.run_test(str(twenty_forty_eight), result)

    test_suite.report_results()


def TwentyFortyEight_reset(TwentyFortyEight):
    """
    Tests for the function reset()  in TwentyFortyEight class
    """

    test_suite = TestSuite()

    # test with an empty grid
    twenty_forty_eight = TwentyFortyEight(0, 0)
    test_suite.run_test(len(twenty_forty_eight.get_grid()), 0)

    # test with a non-empty grid at the beginning of the game
    twenty_forty_eight = TwentyFortyEight(50, 13)
    test_suite.run_test(len(twenty_forty_eight.get_grid()), 50)
    test_suite.run_test(len(twenty_forty_eight.get_grid()[0]), 13)
    test_suite.run_test(len(twenty_forty_eight.get_grid()[50 - 1]), 13)
    non_zeros = 0
    for i in range(50):
        for j in range(13):
            if twenty_forty_eight.get_tile(i, j) != 0:
                non_zeros += 1
    test_suite.run_test(non_zeros, 2)

    # test with a non-empty grid with more than two tiles added before
    twenty_forty_eight = TwentyFortyEight(13, 50)
    test_suite.run_test(len(twenty_forty_eight.get_grid()), 13)
    test_suite.run_test(len(twenty_forty_eight.get_grid()[0]), 50)
    test_suite.run_test(len(twenty_forty_eight.get_grid()[13 - 1]), 50)
    twenty_forty_eight.set_tile(0, 0, 2)
    twenty_forty_eight.set_tile(3, 4, 8)
    twenty_forty_eight.set_tile(5, 4, 27)
    twenty_forty_eight.set_tile(5, 6, 4)
    twenty_forty_eight.set_tile(1, 49, 15)
    twenty_forty_eight.reset()
    non_zeros = 0
    for i in range(13):
        for j in range(50):
            if twenty_forty_eight.get_tile(i, j) != 0:
                non_zeros += 1
    test_suite.run_test(non_zeros, 2)

    test_suite.report_results()


def TwentyFortyEight_new_tile(TwentyFortyEight):
    """
    Tests for the function new_tile()  in TwentyFortyEight class
    """

    test_suite = TestSuite()

    # empty grid
    twenty_forty_eight = TwentyFortyEight(0, 0)
    tows = 0
    fours = 0
    wrongs = 0
    for i in range(0):
        for j in range(0):
            if twenty_forty_eight.grid[i][j] == 2:
                tows += 1
            elif twenty_forty_eight.grid[i][j] == 4:
                fours += 1
            elif twenty_forty_eight.grid[i][j] != 0:
                wrongs += 1
    test_suite.run_test(tows + fours, 0)
    test_suite.run_test(wrongs, 0)

    # add two tiles at the begininng of the game
    twenty_forty_eight = TwentyFortyEight(50, 13)
    tows = 0
    fours = 0
    wrongs = 0
    for i in range(50):
        for j in range(13):
            if twenty_forty_eight._grid[i][j] == 2:
                tows += 1
            elif twenty_forty_eight._grid[i][j] == 4:
                fours += 1
            elif twenty_forty_eight._grid[i][j] != 0:
                wrongs += 1
    test_suite.run_test(tows + fours, 2)
    test_suite.run_test(wrongs, 0)

    # add new tile to become three tiles
    twenty_forty_eight.new_tile()
    tows = 0
    fours = 0
    wrongs = 0
    for i in range(50):
        for j in range(13):
            if twenty_forty_eight._grid[i][j] == 2:
                tows += 1
            elif twenty_forty_eight._grid[i][j] == 4:
                fours += 1
            elif twenty_forty_eight._grid[i][j] != 0:
                wrongs += 1
    test_suite.run_test(tows + fours, 3)
    test_suite.run_test(wrongs, 0)

    # add three tiles to become six tiles
    twenty_forty_eight.new_tile()
    twenty_forty_eight.new_tile()
    twenty_forty_eight.new_tile()
    tows = 0
    fours = 0
    wrongs = 0
    for i in range(50):
        for j in range(13):
            if twenty_forty_eight._grid[i][j] == 2:
                tows += 1
            elif twenty_forty_eight._grid[i][j] == 4:
                fours += 1
            elif twenty_forty_eight._grid[i][j] != 0:
                wrongs += 1
    test_suite.run_test(tows + fours, 6)
    test_suite.run_test(wrongs, 0)

    test_suite.report_results()


def TwentyFortyEight_move(TwentyFortyEight):
    """
    Tests for the function move()  in TwentyFortyEight class
    """

    test_suite = TestSuite()

    # test a cell for a non-empty grid, MOVING UP
    twenty_forty_eight = TwentyFortyEight(3, 4)
    for i in range(3):
        for j in range(4):
            twenty_forty_eight.get_grid()[i][j] = 0
    twenty_forty_eight.set_tile(0, 1, 2)
    twenty_forty_eight.set_tile(0, 2, 2)
    twenty_forty_eight.set_tile(0, 3, 7)
    twenty_forty_eight.set_tile(1, 2, 4)
    twenty_forty_eight.set_tile(1, 3, 7)
    twenty_forty_eight.set_tile(2, 1, 2)
    twenty_forty_eight.set_tile(2, 3, 7)
    print('up')
    twenty_forty_eight.move(1)
    expected = [[0, 4, 2, 14],
                [0, 0, 4, 7],
                [0, 0, 0, 0]]
    changed = {}
    is_changed = False
    for i in range(3):
        for j in range(4):
            if twenty_forty_eight.get_grid()[i][j] != expected[i][j]:
                is_changed = True
                changed['index'] = (i, j)
                changed['value'] = twenty_forty_eight.get_grid()[i][j]
    if is_changed:
        expected[changed['index'][0]][changed['index'][1]] = changed['value']
    test_suite.run_test(is_changed, True)
    test_suite.run_test(twenty_forty_eight.get_grid(), expected)

    # moving up again to test when no tiles moved
    print('up AGAIN')
    for i in range(3):
        for j in range(4):
            twenty_forty_eight.get_grid()[i][j] = 0
    twenty_forty_eight.set_tile(0, 1, 2)
    twenty_forty_eight.set_tile(0, 2, 2)
    twenty_forty_eight.set_tile(0, 3, 7)
    twenty_forty_eight.set_tile(1, 2, 4)
    twenty_forty_eight.set_tile(1, 3, 7)
    twenty_forty_eight.set_tile(2, 1, 2)
    twenty_forty_eight.set_tile(2, 3, 7)
    twenty_forty_eight.move(1)
    expected = twenty_forty_eight.get_grid()
    twenty_forty_eight.move(1)
    test_suite.run_test(twenty_forty_eight.get_grid(), expected)

    # test a cell for a non-empty grid, MOVING DOWN
    for i in range(3):
        for j in range(4):
            twenty_forty_eight.get_grid()[i][j] = 0
    twenty_forty_eight.set_tile(0, 1, 2)
    twenty_forty_eight.set_tile(0, 2, 2)
    twenty_forty_eight.set_tile(0, 3, 7)
    twenty_forty_eight.set_tile(1, 2, 4)
    twenty_forty_eight.set_tile(1, 3, 7)
    twenty_forty_eight.set_tile(2, 1, 2)
    twenty_forty_eight.set_tile(2, 3, 7)
    print('down')
    twenty_forty_eight.move(2)
    expected = [[0, 0, 0, 0],
                [0, 0, 2, 7],
                [0, 4, 4, 14]]
    changed = {}
    is_changed = False
    for i in range(3):
        for j in range(4):
            if twenty_forty_eight.get_grid()[i][j] != expected[i][j]:
                is_changed = True
                changed['index'] = (i, j)
                changed['value'] = twenty_forty_eight.get_grid()[i][j]
    if is_changed:
        expected[changed['index'][0]][changed['index'][1]] = changed['value']
    test_suite.run_test(is_changed, True)
    test_suite.run_test(twenty_forty_eight.get_grid(), expected)

    # test a cell for a non-empty grid, MOVING LEFT
    for i in range(3):
        for j in range(4):
            twenty_forty_eight.get_grid()[i][j] = 0
    twenty_forty_eight.set_tile(0, 1, 2)
    twenty_forty_eight.set_tile(0, 2, 2)
    twenty_forty_eight.set_tile(0, 3, 7)
    twenty_forty_eight.set_tile(1, 2, 4)
    twenty_forty_eight.set_tile(1, 3, 7)
    twenty_forty_eight.set_tile(2, 1, 2)
    twenty_forty_eight.set_tile(2, 3, 7)
    print('left')
    twenty_forty_eight.move(3)
    expected = [[4, 7, 0, 0],
                [4, 7, 0, 0],
                [2, 7, 0, 0]]
    changed = {}
    is_changed = False
    for i in range(3):
        for j in range(4):
            if twenty_forty_eight.get_grid()[i][j] != expected[i][j]:
                is_changed = True
                changed['index'] = (i, j)
                changed['value'] = twenty_forty_eight.get_grid()[i][j]
    if is_changed:
        expected[changed['index'][0]][changed['index'][1]] = changed['value']
    test_suite.run_test(is_changed, True)
    test_suite.run_test(twenty_forty_eight.get_grid(), expected)

    # test a cell for a non-empty grid, MOVING RIGHT
    for i in range(3):
        for j in range(4):
            twenty_forty_eight.get_grid()[i][j] = 0
    twenty_forty_eight.set_tile(0, 1, 2)
    twenty_forty_eight.set_tile(0, 2, 2)
    twenty_forty_eight.set_tile(0, 3, 7)
    twenty_forty_eight.set_tile(1, 2, 4)
    twenty_forty_eight.set_tile(1, 3, 7)
    twenty_forty_eight.set_tile(2, 1, 2)
    twenty_forty_eight.set_tile(2, 3, 7)
    print('right')
    twenty_forty_eight.move(4)
    expected = [[0, 0, 4, 7],
                [0, 0, 4, 7],
                [0, 0, 2, 7]]
    changed = {}
    is_changed = False
    for i in range(3):
        for j in range(4):
            if twenty_forty_eight.get_grid()[i][j] != expected[i][j]:
                is_changed = True
                changed['index'] = (i, j)
                changed['value'] = twenty_forty_eight.get_grid()[i][j]
    if is_changed:
        expected[changed['index'][0]][changed['index'][1]] = changed['value']
    test_suite.run_test(is_changed, True)
    test_suite.run_test(twenty_forty_eight.get_grid(), expected)

    test_suite.report_results()





















