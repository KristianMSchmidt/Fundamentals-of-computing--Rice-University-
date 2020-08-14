"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors

This is the final and wel testet original version (handed in).
Can solve any nxm puzzle by fixed moves (does not use tree search).
Is very fast - but uses many moves.

"""

#import poc_fifteen_gui

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
        #print "Update puzzle called with string:", move_string, "\n to below puzzle:"
        #print self
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
        if self._grid[target_row][target_col] != 0:
            return False

        #All tiles in rows i+1 or below are positioned at their solved location.
        for row in range(target_row + 1, self._height):
            for col in range(self._width):
                if self.current_position(row, col) != (row, col):
                    return False

        #All tiles in row i to the right of position (i,j) are positioned at their solved location.
        for col in range(target_col + 1, self._width):
            if self.current_position(target_row, col) != (target_row, col):
                return False

        return True

    def position_tile(self, target_row, target_col, vertical_displacement, horizontal_displacement):
        """
        Helper function. Moves zero vertically up to prior row position of target_tile and rearranges (while keeping
        invariants) such that target_tile ends up beging placed just above this new positin of the zeroself.
        .........     ..x......             .x.....    ....0..
        ........x     ..0......             .......    ....x..        .......    .....x           ..x.....   .....0
        .........     .........     or      .......    .......   or   x.....0    .....0     or    .......0   .....x
        .........     .........             .......    .......
        ..0......     .........             .....0.    .......

        """
        move_string = ""

        if vertical_displacement >= 2 or (vertical_displacement == 1 and horizontal_displacement) > 0:
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

        if horizontal_displacement < 0:
            direction_to_target = "r"
            opposite_direction = "l"

        else:
            direction_to_target = "l"
            opposite_direction = "r"

        number_of_loops = abs(horizontal_displacement)

        while number_of_loops > 0:
            #Dette loops kunne godt optimeres. Ingen grund til at gaa helt tilbage hver gang.
            #Men det betyder meget lidt i en 4x4 puzzle
            for dummy in range(number_of_loops):
                move_string += direction_to_target
            move_string += ver_shift
            for dummy in range(number_of_loops):
                move_string += opposite_direction
            move_string += opposite_ver_shift
            number_of_loops -= 1

        return move_string

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, target_col), "Lower row invariant not satisfied before solving"
        target_tile = self.current_position(target_row, target_col)
        vertical_displacement = target_row - target_tile[0]
        horizontal_displacement = target_col - target_tile[1]

        ## CASE 1: Target tile is vertically above target position and target_col != 0
        move_string = ""

        if target_tile[1] == target_col and target_col != 0:

            #position zero just above target_tile.
            for dummy_number in range(vertical_displacement):
                move_string += "u"
                self.update_puzzle("u")

            #move target_tile vertically down to desired position
            for dummy_number in range(vertical_displacement - 1):
                self.update_puzzle("lddru")
                move_string += "lddru"

            # place zero at next target_postition
            self.update_puzzle("ld")
            move_string += "ld"

        # CASE 2: Target tile is not vertically above target position and target_colon !=0
        elif target_col != 0:
            move_string = self.position_tile(target_row, target_col, vertical_displacement, horizontal_displacement)

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
        target_col = 0
        target_tile = self.current_position(target_row, target_col)
        vertical_displacement = target_row - target_tile[0]
        horizontal_displacement = target_col - target_tile[1]

        move_string = self.position_tile(target_row, target_col, vertical_displacement, horizontal_displacement)

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

        #add long string in all but the most special case
        if not (vertical_displacement == 1 and target_tile[1] == 0):
           move_string += "ruldrdlurdluurddlur"

        #move zero tile to next target position to solve
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

        if self._grid[0][target_col] != 0:
            return False

        if self.current_position(1, target_col) != (1, target_col):
            return False

        for row in range(self._height):
            for col in range(self._width):
                if (row >= 2 or col > target_col) and self.current_position(row, col) != (row, col):
                    return False
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """

        if self._grid[1][target_col] != 0:
            return False

        for row in range(self._height):
            for col in range(self._width):
                if (row >= 2 or col > target_col) and self.current_position(row, col) != (row, col):
                    return False
        return True

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        error_message = "row1 invariant not satisfied prior to solving col{}".format(target_col)
        assert self.row1_invariant(target_col), error_message

        target_row = 1
        target_tile = self.current_position(target_row, target_col)
        vertical_displacement = target_row - target_tile[0]
        horizontal_displacement = target_col - target_tile[1]

        move_string = self.position_tile(target_row, target_col, vertical_displacement, horizontal_displacement)

        if target_tile[0] == 1:
            move_string += "u"

        self.update_puzzle(move_string)
        error_message = "row0 invariant not satisfied after to solving row 1 in col{}".format(target_col)
        assert self.row0_invariant(target_col), error_message
        return move_string


    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        error_message = "row0 invariant not satisfied prior to solving col{}".format(target_col)
        assert self.row0_invariant(target_col), error_message

        move_string = "ld"
        self.update_puzzle(move_string)

        #special case
        if self.current_position(0,target_col) == (0, target_col):
            return move_string

        target_row = 0
        target_tile = self.current_position(target_row, target_col)

        #Nota Bene: This is a bit different than usual
        current_zero_pos = (1, target_col - 1)
        vertical_displacement = current_zero_pos[0] - target_tile[0]
        horizontal_displacement = current_zero_pos[1] - target_tile[1]

        more_moves = self.position_tile(target_row, target_col, vertical_displacement, horizontal_displacement)
        move_string += more_moves

        if target_tile[0] == 1:
            add_moves = "uld"
        else:
            add_moves = "ld"

        move_string += add_moves

        trick_move = "urdlurrdluldrruld"
        move_string += trick_move

        self.update_puzzle(more_moves + add_moves + trick_move)
        error_message = "row1 invariant for col {} not satisfied after to solving row 0 in col{}".format(target_col-1, target_col)
        assert self.row1_invariant(target_col-1), error_message
        return move_string

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        assert self.row1_invariant(1), "Phase 1 and 2 of solution proces not completed prior to solving 2x2 puzzle"
        one_tile_pos = self.current_position(0,1)

        #postiton on 1_tile determines the 3 solvable constallations, where 0_tile is at pos (1,1)
        if one_tile_pos == (0,0):
            move_string = "ul"
        elif one_tile_pos == (1,0):
            move_string = "uldrul"
        elif one_tile_pos == (0,1):
            move_string = "lu"

        self.update_puzzle(move_string)
        assert self.row0_invariant(0), "Puzzle not solved correctly"
        return(move_string)

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """

        # Move zero to bottom right positition
        move_string_0 = ""
        zero_pos = self.current_position(0,0)
        for dummy in range(self._height - zero_pos[0] - 1):
            move_string_0 += "d"
        for dummy in range(self._width - zero_pos[1] - 1):
            move_string_0 += "r"
        self.update_puzzle(move_string_0)

        #Phase 1:
        move_string_1 = ""
        for row in range(self._height - 1, 1, -1):
            for col in range(self._width - 1, -1, -1):
                if col > 0:
                    move = self.solve_interior_tile(row, col)
                    assert self.lower_row_invariant(row, col-1)
                else:
                    move = self.solve_col0_tile(row)
                    assert self.lower_row_invariant(row-1, self._width-1)
                move_string_1 += move

        #Phase 2:
        move_string_2 = ""
        for col in range(self._width -1, 1, -1):
            move1 = self.solve_row1_tile(col)
            assert self.row0_invariant(col)
            move0 = self.solve_row0_tile(col)
            assert self.row1_invariant(col-1)
            move_string_2 += move1 + move0

        #Phase 3:
        move_string_3 = self.solve_2x2()
        assert self.row0_invariant(0)
        return move_string_0 + move_string_1 + move_string_2 + move_string_3

#puzzle=Puzzle(4, 4, [[15, 11, 8, 12], [14, 10, 9, 13], [2, 6, 1, 4], [3, 7, 5, 0]])
#print puzzle
#puzzle.update_puzzle("uuullldrurdldrurdldruuullldrulddrurdldruldrurulldrdluurdlldruuldrdlururulddruurddluuldrullddrudrurulldrdluulddruurdruldlurdruldlul")
#print puzzle

def print_solution_string_to_text_file():
    """
    Print solution string and other information to quotable text file
    """
    puzzle = Puzzle(4, 4, [[0, 1, 2, 3],
                           [4, 5, 6, 7],
                           [8, 9, 10, 11],
                          [12, 13, 14, 15]])
    puzzle.update_puzzle("ddruldrrulddruldruu")

    ##Joe Warren's challenge puzzle. Tile by tile solution is about 250 moves. Best solution is about 80 moves.
    puzzle=Puzzle(4, 4, [[15, 11, 8, 12], [14, 10, 9, 13], [2, 6, 1, 4], [3, 7, 5, 0]])
    #puzzle.solve_puzzle()

    filehandle = open('output_document.txt', 'w')
    filehandle.write('Puzzle to solve: \n')
    filehandle.write(str(puzzle) +"\n")
    sol=puzzle.solve_puzzle()
    filehandle.write("Solution string to puzzle: " + sol + "\n")
    filehandle.write("\nLength of solution string: " + str(len(sol)) + "\n\n")
    filehandle.write("Solved puzzle:\n" + str(puzzle) +"\n")
    filehandle.close()


if __name__ == '__main__':
    print_solution_string_to_text_file()


# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))
