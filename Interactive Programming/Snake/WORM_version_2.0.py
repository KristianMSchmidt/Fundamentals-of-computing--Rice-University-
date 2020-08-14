
###################################################
## SNAKE MIN HELT EGEN IMPLEMENTATION...
## KODEN HER ER SMARTERE END i VERSION 1, MEN MULIGVIS IKKE HELT UDEN
##BUGS. LAVET UDEN HJÆLP

import simplegui
import random

# Define global variables
CELL_SIZE= 40
GRID_SIZE = 8
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT =GRID_SIZE * CELL_SIZE
DIRECTION="RIGHT"
SPEED=20   #20 er hurtigt


def new_game():
    global WORM, FOOD, POINT, time, HEAD_HISTORY,WORM_HEAD, WORM_LENGTH, DIRECTION, GAME_IS_ON

    WORM_LENGTH = 1
    time=1
    DIRECTION= "RIGHT"
    POINT=0
    GAME_IS_ON=True

    x=random.randrange(0,GRID_SIZE)
    y=random.randrange(0,GRID_SIZE)

    WORM_HEAD=[x,y]
    WORM= [[x,y]]
    HEAD_HISTORY=[[x,y]]
    food_defined=False

    while not food_defined:
        x1=random.randrange(0,GRID_SIZE)
        y1=random.randrange(0,GRID_SIZE)
        if (x1,y1) != (x,y):
            FOOD=[x1,y1]
            food_defined =True


def update_worm_head(worm_head):
    global GAME_IS_ON

    if DIRECTION=="RIGHT":
        nyt=[worm_head[0],worm_head[1]+1]
    elif DIRECTION=="LEFT":
        nyt=[worm_head[0],worm_head[1]-1]
    elif DIRECTION=="UP":
        nyt=[worm_head[0]-1,worm_head[1]]
    elif DIRECTION=="DOWN":
        nyt=[worm_head[0]+1,worm_head[1]]

    if nyt in WORM or nyt[0]<0 or nyt[0]>=GRID_SIZE or nyt[1]<0 or nyt[1]>=GRID_SIZE:
        GAME_IS_ON=False
        print "Du er doed"
    return(nyt)

def update_food():
    global FOOD

    Changed=False

    while not Changed:
        x=random.randrange(0,GRID_SIZE)
        y=random.randrange(0,GRID_SIZE)
        if not [x,y] in WORM:
            if [x,y] != FOOD:
                FOOD=[x,y]
                Changed=True

 # define draw


def draw(canvas):

    global WORM_HEAD, WORM_LENGTH,HEAD_HISTORY, WORM
    global time, POINT, OLD_WORM


    #draw grid
    for i in range(GRID_SIZE-1):
        canvas.draw_line([CELL_SIZE+i*CELL_SIZE,0], [CELL_SIZE+i*CELL_SIZE, HEIGHT],2,"White")
    for i in range(GRID_SIZE-1):
        canvas.draw_line([0, CELL_SIZE+i*CELL_SIZE], [WIDTH, CELL_SIZE+i*CELL_SIZE],2,"White")

    #update time
    time=time+1


    if time%SPEED==0:
        #print "worm", WORM


        #update worm_head
        WORM_HEAD=update_worm_head(WORM_HEAD)
        HEAD_HISTORY.append(WORM_HEAD)

        #update food, score and worm_length
        if WORM_HEAD==FOOD:
            POINT +=1
            WORM_LENGTH +=1
            update_food()


        #update worm
        NEW_WORM=[]
        for i in range(WORM_LENGTH):
            NEW_WORM.append(HEAD_HISTORY[-i-1])

        WORM=NEW_WORM

    #draw food
    canvas.draw_circle([(FOOD[1]+0.5)*CELL_SIZE, (FOOD[0]+0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"RED", "RED")


    #draw worm
    if GAME_IS_ON:
        OLD_WORM=list(WORM)
        try:
            for x in WORM:
                j=x[1]
                i=x[0]
                canvas.draw_circle([(j+0.5)*CELL_SIZE, (i+0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"White", "White")
        except:
            pass

    else:
        #print "spillet er slut"
        time=0

        for x in OLD_WORM:
            j=x[1]
            i=x[0]
            canvas.draw_circle([(j+0.5)*CELL_SIZE, (i+0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"White", "White")

        n=GRID_SIZE**2
        canvas.draw_text(str(POINT)+"/"+str(n-1)+"  points", (WIDTH/8,HEIGHT/2), 50, 'Green')



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
