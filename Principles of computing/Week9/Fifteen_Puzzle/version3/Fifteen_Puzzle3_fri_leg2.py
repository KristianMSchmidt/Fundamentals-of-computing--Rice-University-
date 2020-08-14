"""
Loyd's Fifteen puzzle - solver.
Note that solved configuration has the blank (zero) tile in upper left

By Kristian. Latest version.
This version does (almost!) only move by tree search. However a tile-by-tile approach is still implementet.

NB: The recursion depth has to be quite deep for this version to work (approximately 17).
NBB: Solves Joe Warrens challenge puzzle in 130 moves (versus 236 moves in my first implementation) paa 7000 sek.
NBB: There is a lot of "unused code" in this program.

NBBB: Code is messy and not optimized for speed
"""
#import poc_fifteen_gui
import time

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
        # #Tile zero is positioned at (i,j).
        # if self._grid[target_row][target_col] != 0:
        #     return False

        #All tiles in rows i+1 or below are positioned at their solved location.
        if (target_row, target_col) == (3,3):
            return False

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
        input         output                 input      output         input    output           input     output
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

            ### THIS IS VERY INEFFICIENT as it will result in "ddduuu" sequences.
            ## Solution is to refactor some of above code
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

        if target_col == 0 and self._grid[0][target_col] != 0:
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

        # if self._grid[1][target_col] != 0:
        #     return False

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

        The assumptions right now is, that zero is at position (1,1) and thas puzzle is solvable
        Future development: I ought to add an assertion that 2x2 puzzle is solvable!
        """
        assert self.row1_invariant(1), "Phase 1 and 2 of solution proces not completed prior to solving 2x2 puzzle"
        one_tile_pos = self.current_position(0,1)

        #To avoid errors if user mistakenly applies method to solved puzzle:
        if self.row0_invariant(0):
            return ""

        #Postiton of 1_tile determines the 3 solvable constallations, where 0_tile is at pos (1,1)
        if one_tile_pos == (0,0):
            move_string = "ul"
        elif one_tile_pos == (1,0):
            move_string = "uldrul"
        elif one_tile_pos == (0,1):
            move_string = "lu"

        self.update_puzzle(move_string)
        assert self.row0_invariant(0), "Puzzle not solved correctly"
        return(move_string)


    def legal_directions(self):
        """
        Returns list of legal directions
        """
        zero_row, zero_col = self.current_position(0, 0)

        legal_moves = []
        if zero_row > 0:
            legal_moves.append("u")
        if zero_row < self._height - 1:
            legal_moves.append("d")
        if zero_col > 0:
            legal_moves.append("l")
        if zero_col < self._width - 1:
            legal_moves.append("r")
        return legal_moves

    def score_position(self):
        """
        ## This solution is inefficient - which is serious at it is part of the tree search
        Return the highest score, where the corresponding posistion is "solved" according to below matric
                             [[16, -1,10,8],
                             [-1, 12, 11,9],
                             [7, 6, 5, 4 ],
                             [3, 2 , 1, -1]]

        """
        row_col_score = [(3,2,1), (3,1,2), (3,0,3), (2,3,4),(2,2,5), (2,1,6), (2,0,7),(1,3,8),(0,3,9), (1,2,10),
              (0,2,11),(1,1,12), (0,0,16)]

        highest_score = - 7
        next_target_tile = self.current_position(3,3)
        next_target_position = (3,3)

        for element_number in range(len(row_col_score)):
           row, col, score = row_col_score[element_number]
           if row == 0:
               if self.row0_invariant(col):
                   highest_score = score
                   next_target_tile = self.current_position(row, col)
                   next_target_position = (row, col)
           elif row == 1:
              if self.row1_invariant(col):
                  highest_score = score
                  next_target_tile = self.current_position(row, col)
                  next_target_position = (row, col)
           else:
              if self.lower_row_invariant(row,col):
                highest_score = score
                next_target_tile = self.current_position(row, col)
                next_target_position = (row, col)


        return highest_score, next_target_tile, next_target_position


    def manhattan_distance(self,x,y,a,b):
        """
        computes manhattan distance between (x,y) and (a,b)
        """
        return abs(x-a) + abs(y-b)


    def tree_search(self, move_string = "", recursion_depth = 18):
        """
        Performs tree search.
        Ideas as how to make search more efficient:

        1) Make moves illegal if they move well-positioned tile (unless target position is col 0 or row 0)
        2) Do BFS instead of depth first search
        3) If Manhattan distance from zero to target_tile plus manhattan distance from target_tile to target position
        is to big, than apply fixed moves right away insted of tree search
        """
        score = self.score_position()[0]

        if recursion_depth == 0:
            return (score, move_string)

        if score == 16:
            return (16, move_string)

        legal_directions = self.legal_directions()
        if move_string != "":
            last_direction = move_string[-1]
            if last_direction == "u" and "d" in legal_directions:
                legal_directions.remove("d")
            if last_direction == "d" and "u" in legal_directions:
                legal_directions.remove("u")
            if last_direction == "l" and "r" in legal_directions:
                legal_directions.remove("r")
            if last_direction == "r" and "r" in legal_directions:
                legal_directions.remove("r")

        best_score = 0
        best_move = ""


        #To avoid making moves to obtain initial position
        if score > best_score or (score == best_score and len(move_string)<len(best_move)):
            best_score = score
            best_move = move_string

        for direction in legal_directions:
            subtree = self.clone()
            subtree.update_puzzle(direction)
            score, move = subtree.tree_search(move_string + direction, recursion_depth - 1)
            if score > best_score or (score == best_score and len(move)<len(best_move)):
                best_score = score
                best_move = move

        return (best_score, best_move)

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string

        """

        score, next_target_tile, next_target_position = self.score_position()
        print "current_score:", score
        print "next target tile", next_target_tile
        print "next target position", next_target_position

        if score == 16:
           print self
           print "Puzzle solved"
           return ""

        zero_row, zero_col = self.current_position(0, 0)

        dist = self.manhattan_distance(zero_row, zero_col, next_target_tile[0], next_target_tile[1]) + self.manhattan_distance(next_target_tile[0], next_target_tile[1], next_target_position[0], next_target_position[1])
        print "manhattan distance", dist
        if dist > 8:
            print "FIXED MOVES TOWARDS NEXT TARGET"
            move = ""
            if next_target_tile[0] <= zero_row:
                ver_dir = "u"
            else:
                ver_dir = "d"
            if next_target_tile[1] <= zero_col:
                hor_dir = "l"
            else:
                hor_dir = "r"
            for dummy in range(abs(zero_row-next_target_tile[0])):
                move += ver_dir
            for dummy in range(abs(zero_col- next_target_tile[1])):
                move += hor_dir
            self.update_puzzle(move)
            return move + self.solve_puzzle()

        else:
            print "Performing 'depth first' Tree search on below puzzle:\n {} \n Please wait...".format(self)

            best_score, best_move = self.tree_search()
            if best_move == "":
                move_message = "''"
            else:
                move_message = best_move
            print "Best move from tree search is {} with score {}\n".format(move_message, best_score)

        if best_move != "":
            game_state = best_score
            self.update_puzzle(best_move)
            print "Above tree search move applied with resulting puzzle:\n", self
            return best_move + self.solve_puzzle()



def small_tests():

    ##Joe Warrens challenge puzzle. My rigid tile by tile solution is about 236 moves. Optimal solution is about 80 moves.
    puzzle=Puzzle(4, 4, [[15, 11, 8, 12], [14, 10, 9, 13], [2, 6, 1, 4], [3, 7, 5, 0]])
    #print len(puzzle.solve_puzzle())


    ##Easier puzzle:
    puzzle = Puzzle(4, 4, [[0, 1, 2, 3],
                           [4, 5, 6, 7],
                           [8, 9, 10, 11],
                          [12, 13, 14, 15]])
    #puzzle.update_puzzle("ddruldrrulddruldruu")
    #print puzzle
    #print puzzle.score_position()
    #print len(puzzle.solve_puzzle())

    puzzle = Puzzle(4, 4, [[4, 6, 8, 0],
                           [1, 5, 7, 3],
                           [2, 9, 10, 11],
                          [12, 13, 14, 15]])

    #print puzzle.score_position()
    #print puzzle.row0_invariant(0)
    #print len(puzzle.solve_puzzle())



#    puzzle = Puzzle(4, 4, [[1, 0, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    #puzzle.update_puzzle("rrdlurdlurdlrrdduldrulurdllluurdlur")
    #puzzle.solve_puzzle("")


    puzzle = Puzzle(4, 4, [[6, 1, 2, 3],
                           [4, 5, 10, 7],
                           [8, 9, 0, 11],
                           [12, 13, 14, 15]])
    #puzzle.solve_puzzle("")

    ##Unsolvable puzzle
    puzzle = Puzzle(4, 4, [[6, 1, 2, 3],
                           [4, 10, 7, 5],
                           [8, 9, 0, 11],
                           [12, 13, 14, 15]])
    #puzzle.solve_puzzle("")



def print_solution_string_to_text_file():
    """
    Print solution string and other information to quotable text file
    """
    ##Joe Warrens challenge puzzle. My rigid tile by tile solution is about 236 moves. Optimal solution is about 80 moves.
    puzzle=Puzzle(4, 4, [[15, 11, 8, 12], [14, 10, 9, 13], [2, 6, 1, 4], [3, 7, 5, 0]])

    sol=puzzle.solve_puzzle()
    print sol
    print len(sol)

    filehandle = open('output_document.txt', 'w')
    filehandle.write('Puzzle to solve: \n')
    filehandle.write(str(puzzle) +"\n")

    filehandle.write("Solution string to puzzle: " + sol + "\n")
    filehandle.write("\nLength of solution string: " + str(len(sol)) + "\n\n")
    filehandle.write("Solved puzzle:\n" + str(puzzle) +"\n")
    filehandle.close()
print_solution_string_to_text_file()


if __name__ == '__main__':
    small_tests()

# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))
