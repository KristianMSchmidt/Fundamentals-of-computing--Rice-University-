"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors

Outdated version....!
"""

import poc_fifteen_gui


class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        #Tile zero is positioned at (i,j).
        condition_1 = self._grid[target_row][target_col] == 0

        #All tiles in rows i+1 or below are positioned at their solved location.
        condition_2 = True
        for row in range(target_row + 1, self._height):
            for col in range(self._width):
                if self.current_position(row, col) != (row, col):
                    condition_2 = False

        #All tiles in row i to the right of position (i,j) are positioned at their solved location.
        condition_3 = True
        for col in range(target_col + 1, self._width):
            if self.current_position(target_row, col) != (target_row, col):
                condition_3 = False

        return condition_1 and condition_2 and condition_3


    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, target_col), "Lower row invariant not satisfied before solving"

        move_string = ""

        #find current location of tile that should appear at "target position" = (target_row, target_col)
        target_tile = self.current_position(target_row, target_col)
        #known facts: 1) zero is positioned at target position. 2) target_tile = (k,l) must satisfy k< target_row or (k=i and l<j)

        # count vertical distance between target_tile and target_position
        vertical_displacement = target_row - target_tile[0]

        ## CASE 1: Target tile is vertically above target position and target_col != 0
        if target_tile[1] == target_col and target_col != 0:

            #position zero just below target_tile
            for dummy_number in range(vertical_displacement):
                move_string += "u"
                self.update_puzzle("u")
            for dummy_number in range(vertical_displacement - 1):
                self.update_puzzle("lddru")
                move_string += "lddru"
            self.update_puzzle("ld")
            move_string += "ld"

        # CASE 2: Target tile is not vertically above target position and target_colon !=0
        elif target_col != 0:
            if vertical_displacement >= 2:
                #in this case there is free space below target tile
                ver_shift = "d"
                opposite_ver_shift = "u"
            else:
                #in this case there is free space above target tile
                ver_shift = "u"
                opposite_ver_shift = "d"

            for dummy in range(vertical_displacement):
                move_string += "u"

            ####Nu staar nullet vertikalt ud for target_tile

            horizontal_displacement = target_col - target_tile[1]
            #print "horizontal_displacement", horizontal_displacement
            if horizontal_displacement < 0:
                direction_to_target = "r"
                opposite_direction = "l"

            else:
                direction_to_target = "l"
                opposite_direction = "r"

            number_of_loops = abs(horizontal_displacement)

            while number_of_loops > 0:
                for dummy in range(number_of_loops):
                    move_string += direction_to_target
                move_string += ver_shift
                for dummy in range(number_of_loops):
                    move_string += opposite_direction
                move_string += opposite_ver_shift
                number_of_loops -= 1

            for dummy in range(vertical_displacement):
                move_string += "d"
            self.update_puzzle(move_string)
            move_string += self.solve_interior_tile(target_row, target_col)

        error_message = "Lower row invariant not satisfied after solve interior tile at target position ({},{})".format(target_row, target_col)
        assert self.lower_row_invariant(target_row, target_col-1), error_message
        return move_string

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, 0), "Lower row invariant not satisfied before solving"
        move_string = ""
        target_col = 0
        #find current location of tile that should appear at "target position" = (target_row, target_col)
        target_tile = self.current_position(target_row, target_col)
        #known facts: 1) zero is positioned at target position. 2) target_tile = (k,l) must satisfy k< target_row or (k=i and l<j)

        # count vertical distance between target_tile and target_position
        vertical_displacement = target_row - target_tile[0]


        ##KODE GENBRUG START
        if vertical_displacement >= 2:
            #in this case there is free space below target tile
            ver_shift = "d"
            opposite_ver_shift = "u"

        else:
            #in this case there is free space above target tile
            ver_shift = "u"
            opposite_ver_shift = "d"

        for dummy in range(vertical_displacement):
            move_string += "u"

        ####Nu staar nullet vertikalt ud for target_tile

        horizontal_displacement = target_col - target_tile[1]

        if horizontal_displacement < 0:
            direction_to_target = "r"
            opposite_direction = "l"

        else:
            direction_to_target = "l"
            opposite_direction = "r"

        number_of_loops = abs(horizontal_displacement)

        while number_of_loops > 0:
            for dummy in range(number_of_loops):
                move_string += direction_to_target
            move_string += ver_shift
            for dummy in range(number_of_loops):
                move_string += opposite_direction
            move_string += opposite_ver_shift
            number_of_loops -= 1

        ### KODE GENBRUG STOPPER

        ###Some speciale cases
        if vertical_displacement == 1:
            if target_tile[1] == 0:
                move_string += "r"
            else:
                move_string += "urdl"

        ## More general situation
        else:
             current_target_tile_row = target_tile[0] + 1

             number_of_loops = target_row - 1 - current_target_tile_row

             while number_of_loops > 0:
                 move_string += "rddlu"
                 number_of_loops -= 1
             move_string += "rdl"

        #add long string
        if not (vertical_displacement == 1 and target_tile[1] == 0):
           move_string += "ruldrdlurdluurddlur"

        for dummy in range(self._width - 2):
            move_string += "r"

        #update puzzle, check invariant and return move string
        self.update_puzzle(move_string)
        error_message = "Lower row invariant not satisfied after solving col0 at pos({},{})".format(target_row, 0)
        assert self.lower_row_invariant(target_row-1, self._width-1), error_message
        return move_string

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""


def small_tests():
    """
    Some informal test code
    """
    pass
if __name__ == '__main__':
    small_tests()





# Start interactive simulation

#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))


##Snippets:
#Use of assertions and invarians when using solve_interior_tile
#...
#assert my_puzzle.lower_row_invariant(i,j)
#my_puzzle.solve_interior_tile(i, j)
#assert my_puzzle.lower_row_invariant(i, j - 1)
#...
#Use of assertions and invariants when using solve_col0_tile
#...
#assert my_puzzle.lower_row_invariant(i, 0)
#my_puzzle.solve_col0_tile(i)
#assert my_puzzle.lower_row_invariant(i - 1, n -1)
#...
