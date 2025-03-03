"""
An example of creating a distance field using Manhattan distance
"""
import grid_class as grid

GRID_HEIGHT = 6
GRID_WIDTH = 8

class GridPlus(grid.Grid):
    """
    Extend Grid class to support Game of Life
    """
    def set_cell(self, row, col, val):
        self._cells[row][col] = val

    def get_cells(self):
        return self._cells

def manhattan_distance(row0, col0, row1, col1):
    """
    Compute the Manhattan distance between the cells
    (row0, col0) and (row1, col1)
    """
    return abs(row0 - row1) + abs(col0 - col1)

def create_distance_field(entity_list):
        """
        Create a Manhattan distance field that contains the minimum distance to
        each entity (zombies or humans) in entity_list
        Each entity is represented as a grid position of the form (row, col)
        """
        my_grid = GridPlus(GRID_HEIGHT, GRID_WIDTH)
        cells = my_grid.get_cells()
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                dist = min ([manhattan_distance(ent[0], ent[1], row, col) for ent in entity_list])
                my_grid.set_cell(row,col, dist)
        return my_grid

def print_field(field):
    """
    Print a distance field in a human readable manner with
    one row per line
    """
    print field
    print ""

def run_example():
    """
    Create and print a small distance field
    """
    field = create_distance_field([[4, 0],[2, 5]])
    print_field(field)

run_example()


# Sample output for the default example
#[4, 5, 5, 4, 3, 2, 3, 4]
#[3, 4, 4, 3, 2, 1, 2, 3]
#[2, 3, 3, 2, 1, 0, 1, 2]
#[1, 2, 3, 3, 2, 1, 2, 3]
#[0, 1, 2, 3, 3, 2, 3, 4]
#[1, 2, 3, 4, 4, 3, 4, 5]
