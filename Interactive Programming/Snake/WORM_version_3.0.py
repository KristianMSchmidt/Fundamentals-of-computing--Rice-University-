
#WORMS/SNAKE

import simplegui
import random

# Define global variables
CELL_SIZE= 35
GRID_SIZE = 7
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT =GRID_SIZE * CELL_SIZE
DIRECTION="RIGHT"
SPEED=15  #15 er hurtigt #20 er middel #30 er langsomt


def new_game():
    global WORM, FOOD, POINT, time,WORM_HEAD, WORM_LENGTH, DIRECTION, GAME_IS_ON
    global time2, m, lst

    time2=1
    m=0
    lst=[]

    WORM_LENGTH = 1
    time=1
    DIRECTION= "RIGHT"
    POINT=1
    GAME_IS_ON=True

    x=random.randrange(0,GRID_SIZE)

    WORM_HEAD=[x,0]
    WORM= [[x,0]]

    food_defined=False

    while not food_defined:
        x1=random.randrange(0,GRID_SIZE)
        y1=random.randrange(0,GRID_SIZE)
        if (x1,y1) != (x,0):
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

    global WORM_HEAD, WORM_LENGTH, WORM
    global time, time2, POINT, OLD_WORM,m,lst, GAME_IS_ON


    #draw grid
    for i in range(GRID_SIZE-1):
        canvas.draw_line([CELL_SIZE+i*CELL_SIZE,0], [CELL_SIZE+i*CELL_SIZE, HEIGHT],2,"White")
    for i in range(GRID_SIZE-1):
        canvas.draw_line([0, CELL_SIZE+i*CELL_SIZE], [WIDTH, CELL_SIZE+i*CELL_SIZE],2,"White")

    #update time
    time=time+1


    if time%SPEED==0:


        #update worm_head
        WORM_HEAD=update_worm_head(WORM_HEAD)

        #update food, score and worm_length
        if not WORM_HEAD==FOOD:
            WORM.append(WORM_HEAD)
            WORM.pop(0)

        else:
            POINT +=1
            WORM_LENGTH +=1
            if WORM_LENGTH==GRID_SIZE**2:
                print "Du har vundet!"
                GAME_IS_ON=False
            else:
                update_food()
            WORM.append(WORM_HEAD)

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

        time2= time2+1

        changed = False

        if time2>50 and time2%50==0:

            try:
                while len(lst)+len(OLD_WORM)<GRID_SIZE**2 and not changed:
                    x=random.randrange(GRID_SIZE)
                    y=random.randrange(GRID_SIZE)

                    if (x,y) not in lst and [x,y] not in OLD_WORM and [x,y] != FOOD:
                        lst.append((x,y))
                        changed = True
            except: quit()

        for ball in lst:
             j=ball[1]
             i=ball[0]
             canvas.draw_circle([(j+0.5)*CELL_SIZE, (i+0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"Red", "Red")

        n=GRID_SIZE**2
        canvas.draw_text(str(POINT)+"/"+str(n), (WIDTH/8,HEIGHT/2), 65, 'Green')


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

def button_handler():
    new_game()

# create frame and register handlers
frame = simplegui.create_frame("Snake grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("New game", button_handler,200)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
new_game()
