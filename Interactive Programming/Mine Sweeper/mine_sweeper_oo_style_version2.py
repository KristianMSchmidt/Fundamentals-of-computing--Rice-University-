import simplegui
import random

# Define global variables
CELL_SIZE= 35
GRID_SIZE = 10
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT =GRID_SIZE * CELL_SIZE
NUMBER_OF_MINES=(GRID_SIZE**2)/6

class Cell:
    def __init__(self, position, mined, flagged, tested, neighbor_mines):
        self.position=position
        self.is_mined=mined
        self.is_flagged=flagged
        self.is_tested=tested
        self.center=[((position[0]-1)+0.5)*CELL_SIZE,((position[1]-1)+0.5)*CELL_SIZE]
        self.radius=0.5*CELL_SIZE
        self.corners = [((position[0]-1)*CELL_SIZE, (position[1]-1)*CELL_SIZE), ((position[0]-1)*CELL_SIZE, position[1]*CELL_SIZE),(position[0]*CELL_SIZE, (position[1])*CELL_SIZE), (position[0]*CELL_SIZE, (position[1]-1)*CELL_SIZE)]   #draw cells:     def __str__(self):
        self.neighbor_mines=neighbor_mines

    def set_neighbor_mines(self, number):
        self.neighbor_mines=number

    def __str__(self):

        s="(" + str(self.position[0]) +","+str(self.position[1]) +"): "

        if self.is_mined:
            s += "Mined. "
        else:
            s += "Unmined. "
        if self.is_flagged:
            s+= "Flagged. "
        else:
            s+="Unflagged. "
        if self.is_tested:
            s+="Tested. "
        else:
            s+="Untested. "
        s+="N-mines:"+str(self.neighbor_mines)

        return s

    def draw(self,canvas):

        if self.is_tested:
            canvas.draw_polygon(self.corners,4, "Green", "Green")
            if self.neighbor_mines>0:
                canvas.draw_text(str(self.neighbor_mines), ((self.position[0]-0.7)*CELL_SIZE, (self.position[1]-0.2)*CELL_SIZE), 25, "White")

        if not game_is_on:
            if self.is_mined:
                canvas.draw_circle(self.center, self.radius, 2,"Red", "Red")

        if self.is_flagged:
            canvas.draw_circle(self.center, self.radius, 2,"White", "White")


    def flag(self):
        if self.is_tested:
            pass
        else:
            self.is_flagged =True

    def un_flag(self):
        self.is_flagged=False

    def test(self):
        self.is_tested=True

    def mine(self):
        self.is_mined=True


class Board:
    def __init__(self):

        raw_cells=[Cell((n+1,m+1),False,False,False,0) for n in range(GRID_SIZE) for m in range(GRID_SIZE)]

        number=0

        while number<NUMBER_OF_MINES:
            n=random.randrange(0,GRID_SIZE**2)
            if not raw_cells[n].is_mined:
                raw_cells[n].mine()
                number +=1

        self.cells=raw_cells


    def won(self):
        for cell in self.cells:
            if (cell.is_flagged != cell.is_mined) or (not cell.is_tested and not cell.is_flagged):
                return False
        return True


    def __str__(self):

        s="Board consist of:"

        for cell in self.cells:
            s += str(cell)+"; "
        return s

    def draw(self,canvas):
        for cell in self.cells:
            cell.draw(canvas)

    def get_cell(self,searched_pos):
        for cell in self.cells:
            if cell.position ==searched_pos:
                return (cell)

    def neighbor_cells(self, some_cell):
        i=some_cell.position[0]
        j=some_cell.position[1]

        n_cells=[]
        for x in [(i+1,j-1),(i+1,j),(i+1,j+1),(i-1,j-1),(i-1,j),(i-1,j+1), (i,j-1),(i,j+1)]:
            if 1<=x[0]<=GRID_SIZE and 1<=x[1]<=GRID_SIZE:
                n_cells.append(self.get_cell(x))
        return n_cells

    def count_neighbor_mines(self, some_cell):
        number_of_n_mines=0
        for cell in self.neighbor_cells(some_cell):
            if cell.is_mined:
                number_of_n_mines += 1
        return(number_of_n_mines)

    def set_n_numbers(self):
        for cell in self.cells:
            cell.set_neighbor_mines(self.count_neighbor_mines(cell))

    def mine_sweep(self, some_cell):
        some_cell.test()

        if self.count_neighbor_mines(some_cell)==0:
            for x in self.neighbor_cells(some_cell):
                if (not x.is_tested) and self.count_neighbor_mines(x)==0:
                    if not x.is_flagged:
                        self.mine_sweep(x)
                else:
                    if not x.is_flagged:
                        x.is_tested=True

def draw(canvas):

    #draw board:
    board.draw(canvas)

    #draw grid
    for i in range(GRID_SIZE-1):
        canvas.draw_line([CELL_SIZE+i*CELL_SIZE,0], [CELL_SIZE+i*CELL_SIZE, HEIGHT],2,"White")
    for i in range(GRID_SIZE-1):
        canvas.draw_line([0, CELL_SIZE+i*CELL_SIZE], [WIDTH, CELL_SIZE+i*CELL_SIZE],2,"White")


def mouse_handler(click_pos):
    global active_cell, game_is_on, won

    if not game_is_on:
        return()

    else:
        mouse_pos=(1+click_pos[0]/CELL_SIZE, 1+click_pos[1]//CELL_SIZE)
        if board.get_cell(mouse_pos)==active_cell:
            if active_cell.is_tested:
                pass
            else:
                if active_cell.is_mined:
                    print "BANG! Game over"
                    won=False
                    game_is_on=False
                else:
                    active_cell.test()
                    board.mine_sweep(board.get_cell(mouse_pos))

                    if board.won():
                        print "du har vundet"#won_control()
                        game_is_on=False
    active_cell=board.get_cell(mouse_pos)

def keydown(key):
    global game_is_on

    if (not game_is_on) or active_cell.is_tested:
        return()

    else:
        if key == simplegui.KEY_MAP["space"]:

            if active_cell != None:
                if not active_cell.is_flagged:
                    active_cell.flag()
                    if board.won():
                        print "du har vundet"
                        game_is_on=False

                else:
                    active_cell.un_flag()

def new_game():
    global board, game_is_on, active_cell
    board=Board()
    board.set_n_numbers()

    game_is_on=True
    active_cell = None

  # create frame and register handlers
frame = simplegui.create_frame("Mine sweeper", WIDTH, HEIGHT)
frame.set_canvas_background('Grey')
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler)

frame.add_button("New game", new_game,200)

frame.set_keydown_handler(keydown)

# start frame
frame.start()
new_game()
