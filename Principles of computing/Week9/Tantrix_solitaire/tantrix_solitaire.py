"""
Student facing code for Tantrix Solitaire
http://www.jaapsch.net/puzzles/tantrix.htm

Game is played on a grid of hexagonal tiles.
All ten tiles for Tantrix Solitaire and place in a corner of the grid.
Click on a tile to rotate it.  Cick and drag to move a tile.

Goal is to position the 10 provided tiles to form
a yellow, red or  blue loop of length 10
"""



# Core modeling idea - a triangular grid of hexagonal tiles are
# model by integer tuples of the form (i, j, k)
# where i + j + k == size and i, j, k >= 0.

# Each hexagon has a neighbor in one of six directions
# These directions are modeled by the differences between the
# tuples of these adjacent tiles

# Numbered directions for hexagonal grid, ordered clockwise at 60 degree intervals
DIRECTIONS = {0 : (-1, 0, 1), 1 : (-1, 1, 0), 2 : (0, 1, -1),
              3 : (1, 0, -1), 4 : (1, -1, 0), 5 : (0,  -1, 1)}

def reverse_direction(direction):
    """
    Helper function that returns opposite direction on hexagonal grid
    """
    num_directions = len(DIRECTIONS)
    return (direction + num_directions / 2) % num_directions



# Color codes for ten tiles in Tantrix Solitaire
# "B" denotes "Blue", "R" denotes "Red", "Y" denotes "Yellow"
SOLITAIRE_CODES = ["BBRRYY", "BBRYYR", "BBYRRY", "BRYBYR", "RBYRYB",
                "YBRYRB", "BBRYRY", "BBYRYR", "YYBRBR", "YYRBRB"]


# Minimal size of grid to allow placement of 10 tiles
MINIMAL_GRID_SIZE = 4



class Tantrix:
    """
    Basic Tantrix game class
    """

    def __init__(self, size, tile_value = None):
        """
        Create a triangular grid of hexagons with size + 1 tiles on each side.
        """
        assert size >= MINIMAL_GRID_SIZE, "Grid is too small!"
        # Initialize dictionary tile_value to contain codes for ten
        # tiles in Solitaire Tantrix in one 4x4 corner of grid
        self._size = size

        if tile_value == None:
            self._tile_value = {(0,size,0): "BBRRYY", (1,size-1,0): "BBRYYR", (2,size-2 ,0):"BBYRRY", (3,size-3,0): "BRYBYR",
                            (0,size-1,1):"RBYRYB", (1,size-2,1):"YBRYRB", (2,size-3,1): "BBRYRY",
                            (0,size-2,2):"BBYRYR", (1,size-3,2):"YYBRBR",
                            (0,size-3,3): "YYRBRB"}
        else:
            self._tile_value = tile_value

    def __str__(self):
        """
        Return string of dictionary of tile positions and values
        """
        s = "Tile positions and values: \n"
        for key, val in self._tile_value.items():
            s += str(key) +": "+ val +"\n"
        return s

    def get_tiling_size(self):
        """
        Return size of board for GUI
        """
        return self._size

    def tile_exists(self, index):
        """
        Return whether a tile with given index exists
        """
        for tile in self._tile_value.keys():
            if index == tile:
                return True
        return False

    def place_tile(self, index, code):
        """
        Play a tile with code at cell with given index
        """
        self._tile_value[index]=code

    def remove_tile(self, index):
        """
        Remove a tile at cell with given index
        and return the code value for that tile
        """
        code = self._tile_value[index]
        self._tile_value.pop(index)
        return code

    def rotate_tile(self, index):
        """
        Rotate a tile clockwise at cell with given index
        """
        code = self._tile_value[index]
        new_code = code[-1]+code[:-1]
        self._tile_value[index] = new_code

    def get_code(self, index):
        """
        Return the code of the tile at cell with given index
        """
        return self._tile_value[index]

    def get_neighbor(self, index, direction):
        """
        Return the index of the tile neighboring the tile with given index in given direction.
        Note that the returns postition may empty or outside the game board.
        """
        return (index[0] + direction[0], index[1] + direction[1], index[2] + direction[2])


    def is_legal(self):
        """
        Check whether a tile configuration obeys color matching rules for adjacent tiles
        """
        for index, code in self._tile_value.items():
            for direction_number, direction in DIRECTIONS.items():
                neighbor = self.get_neighbor(index, direction)
                if self.tile_exists(neighbor):
                    neighbor_code = self.get_code(neighbor)
                    if code[direction_number] != neighbor_code[(direction_number+3)%6]:
                        return False
        return True

    def get_outgoing_direction(self, index, color, ingoing_direction):
        """
        Returns an outgoing direction number corresponding to given index and color ("R", "B" or "Y")
        Ingoing_direction is relative to the tile in question
        """
        code = self.get_code(index)
        for direction_number in range(6):
            if code[direction_number] == color and direction_number != ingoing_direction:
                return direction_number


    def has_loop(self, color):
        """
        Check whether a tile configuration has a loop of size 10 of given color
        """
        if not self.is_legal():
            return False

        # choose arbitrary starting point
        first_index, first_code = self._tile_value.items()[0]
        investigation_number = 1
        index = first_index
        direction_number = self.get_outgoing_direction(first_index, color, None)

        # loop through neighboring tiles that match given color
        while index != first_index or investigation_number == 1:
            neighbor_index = self.get_neighbor(index, DIRECTIONS[direction_number])
            if not self.tile_exists(neighbor_index):
                return False
            neighbor_code = self.get_code(neighbor_index)
            neighbor_incomming_dir = (direction_number + 3 ) % 6
            if neighbor_code[neighbor_incomming_dir] != color:
                return False
            else:
                investigation_number += 1
                index = neighbor_index
                direction_number = self.get_outgoing_direction(index, color, neighbor_incomming_dir)

        if investigation_number == 10:
            return True
        return False

#t= Tantrix(6)
#print t.is_legal()

# run GUI for Tantrix
#import poc_tantrix_gui
#poc_tantrix_gui.TantrixGUI(Tantrix(6))
