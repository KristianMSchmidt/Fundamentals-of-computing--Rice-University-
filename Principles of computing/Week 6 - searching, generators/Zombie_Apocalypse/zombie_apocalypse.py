"""
Student portion of Zombie Apocalypse mini-project
By Kristian Moeller Schmidt. Copenhagen, Denmark
"""

import random
import poc_grid
import poc_queue

#import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None,
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        if  0 <= row <= self._grid_height and 0 <= col <= self._grid_width:
            self._zombie_list.append((row, col))
        else:
            raise ValueError("Invalid zombie position")

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)


    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        zombies = (zombie for zombie in self._zombie_list)
        return zombies

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        if  0 <= row <= self._grid_height and 0 <= col <= self._grid_width:
            self._human_list.append((row, col))
        else:
            raise ValueError("Invalid human position")


    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """

        height, width = self._grid_height, self._grid_width
        visited = poc_grid.Grid(height, width)
        distance_field = [[height * width for dummy in range(width)] for dummy in range(height)]
        boundary = poc_queue.Queue()

        if entity_type == HUMAN:
            for human in self.humans():
                visited.set_full(human[0], human[1])
                distance_field[human[0]][human[1]] = 0
                boundary.enqueue(human)

        if entity_type == ZOMBIE:
            for zombie in self.zombies():
                visited.set_full(zombie[0], zombie[1])
                distance_field[zombie[0]][zombie[1]] = 0
                boundary.enqueue(zombie)

        while len(boundary) > 0:
            current_cell = boundary.dequeue()
            current_cell_dist = distance_field[current_cell[0]][current_cell[1]]
            for neighbor_cell in visited.four_neighbors(current_cell[0], current_cell[1]):
                is_not_visited = visited.is_empty(neighbor_cell[0], neighbor_cell[1])
                is_passable = self.is_empty(neighbor_cell[0],neighbor_cell[1])
                if is_not_visited and is_passable:
                    visited.set_full(neighbor_cell[0], neighbor_cell[1])
                    boundary.enqueue(neighbor_cell)
                    distance_field[neighbor_cell[0]][neighbor_cell[1]] = current_cell_dist + 1

        # print "visited: \n", visited
        # print "distance-field"
        # for row in distance_field:
        #     print row

        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        new_human_list = []
        for human in self.humans():
            neighbor_cells = self.eight_neighbors(human[0], human[1])
            best_destinations = [human]
            highest_distance = zombie_distance_field[human[0]][human[1]]
            for neighbor_cell in neighbor_cells:
                no_obstacle = self.is_empty(neighbor_cell[0], neighbor_cell[1])
                if no_obstacle:
                    distance = zombie_distance_field[neighbor_cell[0]][neighbor_cell[1]]
                    if distance == highest_distance:
                        best_destinations.append(neighbor_cell)
                    elif distance > highest_distance:
                        highest_distance = distance
                        best_destinations = [neighbor_cell]
            new_human_list.append(random.choice(best_destinations))
        self._human_list = new_human_list

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        new_zombie_list = []
        for zombie in self.zombies():
            neighbor_cells = self.four_neighbors(zombie[0], zombie[1])
            best_destinations = [zombie]
            least_distance = human_distance_field[zombie[0]][zombie[1]]
            for neighbor_cell in neighbor_cells:
                no_obstacle = self.is_empty(neighbor_cell[0], neighbor_cell[1])
                if no_obstacle:
                    distance = human_distance_field[neighbor_cell[0]][neighbor_cell[1]]
                    if distance == least_distance:
                        best_destinations.append(neighbor_cell)
                    elif distance < least_distance:
                        least_distance = distance
                        best_destinations = [neighbor_cell]
            new_zombie_list.append(random.choice(best_destinations))
        self._zombie_list = new_zombie_list

#
# #height = 5 dvs 5 rows
# # apoc = Apocalypse(5,6,[(3,3), (2,3), (1,3), (0,3)],[(0,3)],[(1,1),(0,1),(1,0),(0,0)])
# # apoc.compute_distance_field(ZOMBIE)
# apoc_2 = Apocalypse(4,4, [(2,2)], [(0,0)], [(1,1)])
# print "ol list", apoc_2._human_list
# df=apoc_2.compute_distance_field(ZOMBIE)
# apoc_2.move_humans(df)
# print "new list", apoc_2._human_list

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Apocalypse(30, 40))
