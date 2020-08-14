
###################################################
## SNAKE MIN HELT EGEN IMPLEMENTATION... UDEN HJÆLP
import simplegui
import random

CELL_SIZE=40
GRID_SIZE = 4
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT =GRID_SIZE * CELL_SIZE
DIRECTION="RIGHT"
time=1
HEAD_HISTORY=[]
WORM_LENGTH = 1
GAME_IS_ON=True
POINT=0
SPEED=30   #20 er hurtigt

def new_game():
    global CELLS, WORM_HEAD, HEAD_HISTORY, FOOD

    CELLS=make_blank_worm()

    x=random.randrange(0,GRID_SIZE)
    y=random.randrange(0,GRID_SIZE)

    WORM_HEAD=[x,y]
    #print "First Head", WORM_HEAD

    HEAD_HISTORY.append(WORM_HEAD)
    #print "primordial hovedhistorie", HEAD_HISTORY
    CELLS[x][y]=True

    food_defined=False

    while not food_defined:
        x1=random.randrange(0,GRID_SIZE)
        y1=random.randrange(0,GRID_SIZE)
        if (x1,y1) != (x,y):
            FOOD=[x1,y1]
            food_defined =True

def make_blank_worm():
    new_worm=[]

    for i in range(GRID_SIZE):
        new_worm.append([])
        for j in range(GRID_SIZE):
            new_worm[i].append([])
            new_worm[i][j]=False
    return(new_worm)


def update_worm_head(worm_head):
    global GAME_IS_ON

    if DIRECTION=="RIGHT":
        if worm_head[1]==GRID_SIZE-1:
            GAME_IS_ON=False
            print "du er doed"
        elif CELLS[worm_head[0]][worm_head[1]+1]:
            GAME_IS_ON=False
            print "du er doed"
        else:
            return([worm_head[0],worm_head[1]+1])

    elif DIRECTION=="LEFT":
        if worm_head[1]==0:
            GAME_IS_ON=False
            print "Doed!"
        elif CELLS[worm_head[0]][worm_head[1]-1]:
            GAMIS_IS_ON=False
            print "doed!"
        else:
            return([worm_head[0],worm_head[1]-1])


    elif DIRECTION=="UP":
        if worm_head[0]==0:
            GAME_IS_ON=False
            print "du er doed"
        elif CELLS[worm_head[0]-1][worm_head[1]]:
            GAME_IS_ON=False
            print "Du er doed"
        else:
            return([worm_head[0]-1,worm_head[1]])

    elif DIRECTION=="DOWN":
        if worm_head[0]==GRID_SIZE-1:
            GAME_IS_ON=False
            print "Du er doed!"
        elif CELLS[worm_head[0]+1][worm_head[1]]:
            GAME_IS_ON=False
            print "Du er doed"
        else:
            return([worm_head[0]+1,worm_head[1]])



def mutate_worm(worm):
    print "Unmuttted", worm
    if not is_alive(worm):
        print "dead"
        #new_worm=make_blank_worm()
        #new_game()
        quit()

    mutated_worm=make_blank_worm()

    if DIRECTION=="RIGHT":

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if j-1>=0 and worm[i][j-1]:
                    mutated_worm[i][j]=True


    elif DIRECTION=="LEFT":

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if j+1<GRID_SIZE-1 and worm[i][j+1]:
                    mutated_worm[i][j]=True

    elif DIRECTION=="UP":

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if i+1<GRID_SIZE-1 and worm[i+1][j]:
                    mutated_worm[i][j]=True

    elif DIRECTION=="DOWN":

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if i-1>0 and worm[i-1][j]==True:
                    mutated_worm[i][j]=True


    return(mutated_worm)  ##Bruges ikke

def update_food():
    global FOOD

    Changed=False

    while not Changed:
        x=random.randrange(0,GRID_SIZE)
        y=random.randrange(0,GRID_SIZE)
        #print x,y

        if not CELLS[x][y]:
            FOOD=[x,y]
            Changed=True
    #Changed=False
 # define draw

def draw(canvas):
    if GAME_IS_ON:
        draw_game_is_on(canvas)

    else:
        #print "POINTS=", POINT
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                #if CELLS[i][j]:
                canvas.draw_circle([(j+0.5)*CELL_SIZE, (i+0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"Red", "Red")
                n=GRID_SIZE**2
                canvas.draw_text(str(POINT)+"/"+str(n-1)+"  points", (WIDTH/8,HEIGHT/2), 30, 'Green')


def draw_game_is_on(canvas):
    global CELLS, WORM_HEAD, HEAD_HISTORY, WORM_LENGTH
    global time, POINT




    time=time+1

    #draw grid
    for i in range(GRID_SIZE-1):
        canvas.draw_line([CELL_SIZE+i*CELL_SIZE,0], [CELL_SIZE+i*CELL_SIZE, HEIGHT],2,"White")
    for i in range(GRID_SIZE-1):
        canvas.draw_line([0, CELL_SIZE+i*CELL_SIZE], [WIDTH, CELL_SIZE+i*CELL_SIZE],2,"White")


    # update wormhead
    #if time%100==0:
     #   SPEED=SPEED

    if time%SPEED==0:

        #print time

        WORM_HEAD=update_worm_head(WORM_HEAD)

        #print "AKTUELT WORM HEAD", WORM_HEAD
        #print "AKTUELT FOOD PLACE", FOOD
        if WORM_HEAD==FOOD:
            POINT +=1
            #print "its time to update food"
            WORM_LENGTH +=1
            update_food()


        #print "hovedhistorie", HEAD_HISTORY
        #print "opdateret hoved", WORM_HEAD

        HEAD_HISTORY.append(WORM_HEAD)

        #print "ny hovedhistorie", HEAD_HISTORY

        #CELLS[WORM_HEAD[0]][WORM_HEAD[1]]=True

        #CELLS[old_head[0]][old_head[1]]=False

        #print "range of worm length", range(WORM_LENGTH)


        for i in range(len(HEAD_HISTORY)-WORM_LENGTH):
            oldhead=HEAD_HISTORY[i]
            CELLS[oldhead[0]][oldhead[1]]=False
        for i in range(WORM_LENGTH):
            hoved=HEAD_HISTORY[-i-1]
            try:
                CELLS[hoved[0]][hoved[1]]=True
            except:
                print hoved




    #draw cells

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if CELLS[i][j]:
                canvas.draw_circle([(j+0.5)*CELL_SIZE, (i+0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"White", "White")

    #draw food
    canvas.draw_circle([(FOOD[1]+0.5)*CELL_SIZE, (FOOD[0]+0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"RED", "RED")



def keyup(key):

    global DIRECTION

    if key == simplegui.KEY_MAP["up"]:
        if not DIRECTION=="DOWN":
            DIRECTION="UP"
    if key == simplegui.KEY_MAP["down"]:
        if not DIRECTION =="UP":
            DIRECTION="DOWN"
    if key == simplegui.KEY_MAP["left"]:
        if not DIRECTION =="RIGHT":
            DIRECTION="LEFT"
    if key == simplegui.KEY_MAP["right"]:
        if not DIRECTION=="LEFT":
            DIRECTION="RIGHT"


# create frame and register handlers
frame = simplegui.create_frame("Dnake grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

frame.set_keyup_handler(keyup)

# start frame
frame.start()
new_game()
