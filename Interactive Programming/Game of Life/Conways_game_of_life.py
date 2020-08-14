#Spillet lavet fra scratch 16/10 2017. 
#lille problem (kan hurtigt løses): Jeg tæller anderledes ved randen af skærmen, hvilket jeg nok ikke bør
#større problem: Progammet kører mega langsomt. Det bør optimeres


#GAME OF LIFE
import simplegui
import random

# Define global variables
CELL_SIZE= 20
GRID_SIZE = 300
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT =GRID_SIZE * CELL_SIZE

###Repræsentation af bord: (x,y): Mine/not, already_pressed/not, flag/not, active/not

game_is_on=False

def reset():
    global board
    board={}
    for i in range(1,GRID_SIZE+1):
        for j in range (1,GRID_SIZE+1):
             board[(i,j)]=False
    #board[(1,1)]=True
    #print board


def neighbor_positions(posi):
    # if posi[0]<1 or posi[0]>GRID_SIZE or posi[1]<1 or posi[1]>GRID_SIZE:
     #   print "Noget forlader skaermen..."

     i=posi[0]
     j=posi[1]

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
            return ((i, j-1), (i,j+1),(i-1,j-1),(i-1,j),(i-1,j+1))
     else:
        if j==1:
            return ((i-1,j),(i+1,j),(i-1,j+1),(i,j+1),(i+1,j+1))
        elif j==GRID_SIZE:
            return ((i,j-1),(i-1,j-1),(i-1,j),(i+1,j-1),(i+1,j))
        else:
            return ((i+1,j-1),(i+1,j),(i+1,j+1),(i-1,j-1),(i-1,j),(i-1,j+1), (i,j-1),(i,j+1))

#print neighbor_positions((4,5))
#print neighbor_positions((2,3))
#print neighbor_positions((3,3))
#print neighbor_positions((3,1))





time=1
def draw(canvas):
    global time

    #draw grid
    for i in range(GRID_SIZE-1):
        canvas.draw_line([CELL_SIZE+i*CELL_SIZE,0], [CELL_SIZE+i*CELL_SIZE, HEIGHT],2,"White")
    for i in range(GRID_SIZE-1):
        canvas.draw_line([0, CELL_SIZE+i*CELL_SIZE], [WIDTH, CELL_SIZE+i*CELL_SIZE],2,"White")
    #draw life
    for i in range(1,GRID_SIZE+1):
        for j in range(1,GRID_SIZE+1):
            if board[(i,j)]:
                canvas.draw_circle([(i-1)*CELL_SIZE+(0.5)*CELL_SIZE, (j-1)*CELL_SIZE+(0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"White", "White")

    #update
    time+=1

    if game_is_on and time%20==0:
        evolve()


def evolve():
    global board, game_is_on
    game_is_on=True

    new_board={}


    for key, value in board.items():

        if value and 2<=count_neighbors(key)<=3:
            new_board[key]=True

        elif not value and count_neighbors(key)==3:
            new_board[key]=True

        else:
            new_board[key]=False

    board=new_board

#Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overpopulation.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


def count_neighbors(x):
    number=0
    for position in neighbor_positions(x):
        if board[position]:
            number =number +1
    return(number)


def mouse_handler(click_pos):
    global pos, board
    pos=(1+click_pos[0]/CELL_SIZE, 1+click_pos[1]//CELL_SIZE)
    print pos
    print count_neighbors(pos)

    if not board[pos]:
        board[pos]=True
    else:
        board[pos]=False

    #print board

def keydown(key):
    global game_is_on

    if key == simplegui.KEY_MAP["space"]:
        if game_is_on:
            game_is_on=False
        else:
            game_is_on=True

def start_knap():
    global game_is_on

    if game_is_on:
        game_is_on=False
    else:
        game_is_on=True


# create frame and register handlers
frame = simplegui.create_frame("Game of life", WIDTH, HEIGHT)
frame.set_canvas_background('Black')
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler)

frame.add_button("Start/pause", start_knap,200)
frame.add_button("Reset", reset,200)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
reset()
