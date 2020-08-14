
#WORMS/SNAKE

import simplegui
import random

# Define global variables
CELL_SIZE= 35
GRID_SIZE = 3
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT =GRID_SIZE * CELL_SIZE
DIRECTION="RIGHT"
SPEED=25  #15 er hurtigt #20 er middel #30 er langsomt


def new_game():
    global WORM, FOOD, POINT, time, WORM_HEAD, DIRECTION, GAME_IS_ON
    global time2, m, lst

    time2=1
    m=0
    lst=[]

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


def update_worm_head(old_head):

    if DIRECTION=="RIGHT":
        nyt=[old_head[0],old_head[1]+1]
    elif DIRECTION=="LEFT":
        nyt=[old_head[0],old_head[1]-1]
    elif DIRECTION=="UP":
        nyt=[old_head[0]-1,old_head[1]]
    elif DIRECTION=="DOWN":
        nyt=[old_head[0]+1,old_head[1]]
    return(nyt)


def update_food():

    Changed=False
    while not Changed:
        x=random.randrange(0,GRID_SIZE)
        y=random.randrange(0,GRID_SIZE)
        if not [x,y] in WORM:
            if [x,y] != FOOD:
                new_food=[x,y]
                Changed=True
    return(new_food)

def draw(canvas):

    global WORM_HEAD, WORM
    global time, time2, POINT, OLD_WORM,m,lst, GAME_IS_ON, FOOD

    #draw grid
    for i in range(GRID_SIZE-1):
        canvas.draw_line([CELL_SIZE+i*CELL_SIZE,0], [CELL_SIZE+i*CELL_SIZE, HEIGHT],2,"White")
    for i in range(GRID_SIZE-1):
        canvas.draw_line([0, CELL_SIZE+i*CELL_SIZE], [WIDTH, CELL_SIZE+i*CELL_SIZE],2,"White")

    #update time
    time=time+1

    if time%SPEED==0:

        #make a copy of worm before update
        OLD_WORM=list(WORM)

        #update worm_head
        WORM_HEAD=update_worm_head(WORM_HEAD)

        #Check if run into walls:
        if WORM_HEAD[0]<0 or WORM_HEAD[0]>=GRID_SIZE or WORM_HEAD[1]<0 or WORM_HEAD[1]>=GRID_SIZE:
            GAME_IS_ON=False
            print "Du er doed....ind i muren. Score: ", POINT

        #update worm
        WORM.append(WORM_HEAD)


        #Decide if worm is to be prolonged in next frame
        if WORM_HEAD==FOOD:
            POINT +=1
            if POINT==GRID_SIZE**2:
                print "Du har vundet. Score: ", POINT
                OLD_WORM=list(WORM)
                GAME_IS_ON=False
            else:
                FOOD=update_food()

        elif WORM_HEAD in WORM[1:len(WORM)-1]:
            GAME_IS_ON=False
            print "Du er doed... ind i egen hale. Score: ", POINT

        else:
            WORM.pop(0)

    #draw food
    canvas.draw_circle([(FOOD[1]+0.5)*CELL_SIZE, (FOOD[0]+0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"RED", "RED")


    #draw worm
    if not GAME_IS_ON:
        WORM=list(OLD_WORM)
        time=0

    try:
        for x in WORM:
            j=x[1]
            i=x[0]
            canvas.draw_circle([(j+0.5)*CELL_SIZE, (i+0.5)*CELL_SIZE], 0.5*CELL_SIZE, 2,"White", "White")
    except:
        quit()

    if not GAME_IS_ON:
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
            except:
                print "Kør programmet igen, hvis du vil spille videre"
                quit()

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
