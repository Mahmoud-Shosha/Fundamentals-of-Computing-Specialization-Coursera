"""
Clone of 2048 game.
"""
import random

import test_suites


# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """

    new_list = trail_zeros(line)
    new_list = adjacent_merge(new_list)
    new_list = trail_zeros(new_list)

    return new_list


def trail_zeros(line):
    """
    Put non-zero values at the beginning of the list,
    and zeros at the end of the list
    """

    # Create an empty list with the same size as line list
    new_line = [0 for dummy_num in line]

    # new_line_index points to the next index to be filled in the
    # new_line list
    new_line_index = 0

    for num in line:
        if num != 0:
            new_line[new_line_index] = num
            new_line_index += 1

    return new_line


def adjacent_merge(line):
    """
    Merge two equal adjacent numbers in a list,
    the first one becomes the double and the second become zero
    """

    index = 1
    new_line = list(line)
    while index < len(line):
        if new_line[index - 1] == new_line[index]:
            new_line[index - 1] = new_line[index - 1] * 2
            new_line[index] = 0
            index += 2
        else:
            index += 1

    return new_line


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Initialize the object and start a new game
        """
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = None
        self._initial_tiles = {UP: [(0, i) for i in range(grid_width)], DOWN: [(grid_height - 1, i)
                                                                              for i in range(grid_width)],
                              LEFT: [(i, 0) for i in range(grid_height)], RIGHT: [(i, grid_width - 1)
                                                                                  for i in range(grid_height)]}
        self._tiles_number = {UP: grid_height, DOWN: grid_height,
                             LEFT: grid_width, RIGHT: grid_width}
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_c in range(self._grid_width)]
                     for dummy_r in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        result = ""
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                result += str(self._grid[row][col]) + " "
            result += "\n"
        return result

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        line = []
        changed = False
        for initial_tile in self._initial_tiles[direction]:
            for tile in range(self._tiles_number[direction]):
                grid_row = initial_tile[0] + tile * OFFSETS[direction][0]
                grid_col = initial_tile[1] + tile * OFFSETS[direction][1]
                line.append(self._grid[grid_row][grid_col])
            line = merge(line)
            for tile in range(self._tiles_number[direction]):
                grid_row = initial_tile[0] + tile * OFFSETS[direction][0]
                grid_col = initial_tile[1] + tile * OFFSETS[direction][1]
                if self._grid[grid_row][grid_col] != line[tile]:
                    changed = True
                self._grid[grid_row][grid_col] = line[tile]
            line = []
        if changed:
            self.new_tile()
        # print changed
        # print self.grid

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # getting an empty cell
        empty_cells = []
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._grid[row][col] == 0:
                    empty_cells.append((row, col))

        if len(empty_cells) != 0:
            empty_cell = random.choice(empty_cells)
            # getting the value to be inserted: 2 or 4
            value = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
            # insert the value into the cell
            self._grid[empty_cell[0]][empty_cell[1]] = value

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

    def get_grid(self):
        """
        Return the grid
        """
        return self._grid




# Running tests

print("Test: trail_zeros() function")
test_suites.test_trail_zeros(trail_zeros)
print()

print("Test: adjacent_merge() function")
test_suites.test_adjacent_merge(adjacent_merge)
print()

print("Test: merge() function")
test_suites.test_merge(merge)
print()

print("Test: __init__() method in TwentyFortyEight class")
test_suites.TwentyFortyEight___init__(TwentyFortyEight)
print()

print("Test: get_grid() method in TwentyFortyEight class")
test_suites.TwentyFortyEight_get_grid(TwentyFortyEight)
print()

print("Test: get_grid_height() method in TwentyFortyEight class")
test_suites.TwentyFortyEight_get_grid_height(TwentyFortyEight)
print()

print("Test: get_grid_width() method in TwentyFortyEight class")
test_suites.TwentyFortyEight_get_grid_width(TwentyFortyEight)
print()

print("Test: get_tile() method in TwentyFortyEight class")
test_suites.TwentyFortyEight_get_tile(TwentyFortyEight)
print()

print("Test: set_tile() method in TwentyFortyEight class")
test_suites.TwentyFortyEight_set_tile(TwentyFortyEight)
print()

print("Test: __str__() method in TwentyFortyEight class")
test_suites.TwentyFortyEight___str__(TwentyFortyEight)
print()

print("Test: reset() method in TwentyFortyEight class")
test_suites.TwentyFortyEight_reset(TwentyFortyEight)
print()

print("Test: new_tile() method in TwentyFortyEight class")
test_suites.TwentyFortyEight_new_tile(TwentyFortyEight)
print()

print("Test: move() method in TwentyFortyEight class")
test_suites.TwentyFortyEight_move(TwentyFortyEight)
print()
