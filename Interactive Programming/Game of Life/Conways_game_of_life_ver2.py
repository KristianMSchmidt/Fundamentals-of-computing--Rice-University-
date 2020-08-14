#Spillet lavet fra scratch 16/10 2017.
#større problem: Progammet kører mega langsomt. Det bør optimeres. Også i denne "optimerede" version...
#tryk m for at lave magi. tryk p for at pause/starte, tryk g for at skyde glidere igang
#programmet skal køres i CodeSkulptor, hvis simpegui ikke er installeret

#GAME OF LIFE
import simplegui
import random



# Define global variables
CELL_SIZE= 15
GRID_SIZE = 50
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT =GRID_SIZE * CELL_SIZE

###Repræsentation af bord: (x,y): Mine/not, already_pressed/not, flag/not, active/not
alive=[]
pos=[10,25]
game_is_on=False

def reset():
    global alive

    alive = []

def neighbor_positions(posi):
    # if posi[0]<1 or posi[0]>GRID_SIZE or posi[1]<1 or posi[1]>GRID_SIZE:
     #   print "Noget forlader skaermen..."

     i=posi[0]
     j=posi[1]

     return ((i+1,j-1),(i+1,j),(i+1,j+1),(i-1,j-1),(i-1,j),(i-1,j+1), (i,j-1),(i,j+1))

def make_glider():
    global alive
    print pos
    glider=((0,2),(1,2),(2,2),(2,1),(1,0))
    glider2=[]
    for x in glider:
        glider2.append((x[0]+pos[0], x[1]-2+pos[1]))
    alive.extend(glider2)

def make_magic():
    global alive
    print "hj"
    magic=[(1,20),(2,20),(3,20),(4,20),(5,20),(6,20),(7,20),(8,20), (10,20),(11,20),(12,20),(13,20),(14,20), (18,20),(19,20),(20,20), (26,20),(27,20),(28,20),(29,20),(30,20),(31,20),(32,20),(34,20),(35,20),(36,20),(37,20),(38,20)]
    magic2=[]
    for x in magic:
        magic2.append((x[0]-1+pos[0],x[1]-20+pos[1]))
    alive.extend(magic2)

time=1

def draw(canvas):
    global time

    #draw grid
    for i in range(GRID_SIZE-1):
        canvas.draw_line([CELL_SIZE+i*CELL_SIZE,0], [CELL_SIZE+i*CELL_SIZE, HEIGHT],2,"White")
    for i in range(GRID_SIZE-1):
        canvas.draw_line([0, CELL_SIZE+i*CELL_SIZE], [WIDTH, CELL_SIZE+i*CELL_SIZE],2,"White")

    #draw life
    for cell in alive:
        i=cell[0]
        j=cell[1]
        canvas.draw_circle([(i-1)*CELL_SIZE+(0.5)*CELL_SIZE, (j-1)*CELL_SIZE+(0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"White", "White")

    #update
    time+=1

    if game_is_on and time%30==0:
        evolve()


def evolve():
    global alive, game_is_on
    game_is_on=True

    new_alive=[]

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i,j) in alive:
                if 2<=count_neighbors((i,j))<=3:
                    new_alive.append((i,j))
            else:
                if count_neighbors((i,j))==3:
                    new_alive.append((i,j))

    alive=new_alive

#Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overpopulation.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


def count_neighbors(x):
    number=0
    for position in neighbor_positions(x):
        if position in alive:
            number =number +1
    return(number)


def mouse_handler(click_pos):
    global pos
    pos=(1+click_pos[0]/CELL_SIZE, 1+click_pos[1]//CELL_SIZE)

    #print count_neighbors(pos)

    if not pos in alive:
        alive.append(pos)

    else:
        alive.remove(pos)

    #print board

def keydown(key):
    global game_is_on

    if key == simplegui.KEY_MAP["p"]:
        if game_is_on:
            game_is_on=False
        else:
            game_is_on=True
    if key == simplegui.KEY_MAP["g"]:
        make_glider()

    if key == simplegui.KEY_MAP["m"]:
        make_magic()

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
label = frame.add_label('', 200)
label2=frame.add_label("Rules are the simple:")
label22=frame.add_label("")
label3=frame.add_label("1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation")
lavel4=frame.add_label("2.Any live cell with two or three live neighbours lives on to the next generation")
lavel5=frame.add_label("3. Any live cell with more than three live neighbours dies, as if by overpopulation")
lavel6=frame.add_label("4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction")
lavel3=frame.add_label("")
lavel11=frame.add_label("")
lavel8=frame.add_label("To insert glider, press g")
lavel9=frame.add_label("To insert wild structure, press m")


# start frame
frame.start()
reset()
