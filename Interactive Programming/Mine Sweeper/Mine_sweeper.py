
#MINE SWEEPER. Jeg har lavet spillet fra bunden, uden hjælp. 16/10/2017

import simplegui
import random

# Define global variables
CELL_SIZE= 35
GRID_SIZE = 7
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT =GRID_SIZE * CELL_SIZE
NUMBER_OF_MINES=(GRID_SIZE**2)/6

###Repræsentation af bord: (x,y): Mine/not, already_pressed/not, flag/not, active/not

def new_game():
    global board, mines_list, game_is_on, active_pos, number_of_flags
    number_of_flags=0
    game_is_on=True

    active_pos=None  # no active mouse position before first click

    board={}

    mines_list=[]

    while len(mines_list)<NUMBER_OF_MINES:
        x=random.randrange(0,GRID_SIZE)
        y=random.randrange(0,GRID_SIZE)
        if (x+1,y+1) not in mines_list:
            mines_list.append((x+1,y+1))

    #print "To minesweep: Mouse click twice on square"
    #print "To place or remove flag: Mouse click and press Space-button"
    #print ""
    #print "Number of mines", NUMBER_OF_MINES


    #print "mines ", mines_list

    for i in range(1,GRID_SIZE+1):
        for j in range(1,GRID_SIZE+1):
            if (i,j) in mines_list:
                board[(i,j)]=[True, False, False]
            else:
                board[(i,j)]=[False, False, False]


    #print board



def neighbor_positions(pos):
     i=pos[0]
     j=pos[1]
     if i==1:
        if j==1:
            return ((i,j+1),(i+1,j+1),(i+1,j))
        elif j==GRID_SIZE:
            return ((i,j-1),(i+1,j),(i+1,j-1))
        else:
            return ((i, j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1))
     elif i==GRID_SIZE:
        if j==1:
            return ((i,j+1),(i-1,j),(i-1,j+1))
        elif j==GRID_SIZE:
            return ((i-1,j),(i-1,j-1),(i,j-1))
        else:
            return ((i, j-1),(i,j+1),(i-1,j-1),(i-1,j),(i-1,j+1))
     else:
        if j==1:
            return ((i-1,j),(i+1,j),(i-1,j+1),(i,j+1),(i+1,j+1))
        elif j==GRID_SIZE:
            return ((i,j-1),(i-1,j-1),(i-1,j),(i+1,j-1),(i+1,j))
        else:
            return ((i+1,j-1),(i+1,j),(i+1,j+1),(i-1,j-1),(i-1,j),(i-1,j+1), (i,j-1),(i,j+1))

#print neighbor_positions((2,3))
#print neighbor_positions((3,3))

def mine(pos):

    if board[pos][0]:
        return (1)
    else:
        return (0)


def count_neighbor_mines(pos):
    number_of_mines=0
    for position in neighbor_positions(pos):
        number_of_mines += mine(position)
    return(number_of_mines)

    #position: Mine/not, Already pressed/not, flag/not

#Make test board
test2={}
for i in range(1,GRID_SIZE+1):
    for j in range(1,GRID_SIZE+1):
        test2[(i,j)]=[False,False,False]


def draw(canvas):
    global game_is_on
    #draw grid
    for i in range(GRID_SIZE-1):
        canvas.draw_line([CELL_SIZE+i*CELL_SIZE,0], [CELL_SIZE+i*CELL_SIZE, HEIGHT],2,"White")
    for i in range(GRID_SIZE-1):
        canvas.draw_line([0, CELL_SIZE+i*CELL_SIZE], [WIDTH, CELL_SIZE+i*CELL_SIZE],2,"White")

    for i in range(1,GRID_SIZE+1):
        for j in range(1,GRID_SIZE+1):
            if board[(i,j)][2]: #flag or not
                canvas.draw_circle([(i-1)*CELL_SIZE+(0.5)*CELL_SIZE, (j-1)*CELL_SIZE+(0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"White", "White")
            if board[(i,j)][1]: #aldready pressed (not dead)
                #canvas.draw_circle([(i-1)*CELL_SIZE+(0.5)*CELL_SIZE, (j-1)*CELL_SIZE+(0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"Green", "Green")

                n=count_neighbor_mines((i,j))
                #if n != 0:
                canvas.draw_text(str(n), ((i-0.7)*CELL_SIZE, j*CELL_SIZE-0.2*CELL_SIZE), 25, "White")

            if not game_is_on:
                if not won:
                    if board[(i,j)][0]: #draw mines (dead)
                        canvas.draw_circle([(i-1)*CELL_SIZE+(0.5)*CELL_SIZE, (j-1)*CELL_SIZE+(0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"Red", "Red")

            if not game_is_on:
                if won:
                    if board[(i,j)][0]: #draw mines (dead)
                        canvas.draw_circle([(i-1)*CELL_SIZE+(0.5)*CELL_SIZE, (j-1)*CELL_SIZE+(0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"Green", "Green")

               # else:
                #    if board[(i,j)][0]: #draw mines (won)
                 #       canvas.draw_circle([(i-1)*CELL_SIZE+(0.5)*CELL_SIZE, (j-1)*CELL_SIZE+(0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"White", "White")


                #else:
                 #   n=count_neighbor_mines((i,j))
                  #  canvas.draw_text(str(n), ((i-0.7)*CELL_SIZE, j*CELL_SIZE-0.2*CELL_SIZE), 25, "White")


def button_handler():
    new_game()


def mine_sweeper(pos):
    board[pos][1]=True

    if count_neighbor_mines(pos)==0:
        for x in neighbor_positions(pos):
            if not board[x][1] and count_neighbor_mines(x)==0:
                if not board[x][2]:
                    mine_sweeper(x)
            else:
                if not board[x][2]:
                    board[x][1]=True


def mouse_handler(click_pos):
    global active_pos,mouse_pos, game_is_on, won

    if not game_is_on:
        pass
        #print "Press New Game"
    else:
        mouse_pos=(1+click_pos[0]/CELL_SIZE, 1+click_pos[1]//CELL_SIZE)

        if mouse_pos==active_pos:
            if board[mouse_pos][2]:
                pass
            else:
                if mouse_pos in mines_list:
                    print ("BANG! Game over")
                    won=False
                    game_is_on=False
                else:
                    mine_sweeper(mouse_pos)
                    won_control()

    active_pos=mouse_pos

def won_control():
    global game_is_on,won

    won=True

    for pos in board:
        if (board[pos][0] != board[pos][2]) or ((not board[pos][1] and (not board[pos][0] or not board[pos][2]))):
            won=False


    if won:
        print ("Du har vundet!!!")
        game_is_on=False
        for key in board:
            if board[key][0]==False and board[key][2]==False:
                board[key][1]=True
    return won

def keydown(key):
    global number_of_flags

    if not game_is_on:
        pass

    else:
        if key == simplegui.KEY_MAP["space"]:

            if active_pos != None and not board[active_pos][1]:
                if board[active_pos][2]==False: #
                    board[active_pos][2]=True   # flag af position
                    number_of_flags +=1
                    #print "number of flags: ",number_of_flags
                    won_control()

                else:
                    board[active_pos][2]=False # remove draw flag at position
                    number_of_flags -=1
                    #print "number of flags: ", number_of_flags

       # print board


# create frame and register handlers
frame = simplegui.create_frame("Mine sweeper", WIDTH, HEIGHT)
frame.set_canvas_background('Grey')
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler)

frame.add_button("New game", button_handler,200)

frame.set_keydown_handler(keydown)

# start frame
frame.start()
new_game()
