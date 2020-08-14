# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
INITIAL_SPEED = 40  #50 is slow, 40 is standard, 35 is fast
PADLET_SPEED_FACTOR=0.62 #0.62 også okay
DEFAULT=True
VERTICAL=False
GRAVITY =False
max_game_length=3  #Terminates automatically at this point
#LEFT = False
#RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos=[WIDTH/2, HEIGHT/2]
ball_vel=[0,0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global number_of_saves
    global paddle1_pos, paddle2_pos
    paddle1_pos=HEIGHT/3
    paddle2_pos=HEIGHT/3

    number_of_saves=0
    ball_pos=[WIDTH/2, HEIGHT/2]

    v_hor=random.randrange(120, 240) # pixels per second.
    v_ver=random.randrange(60, 180)


    if direction=="LEFT":
        ball_vel=[v_hor/INITIAL_SPEED,-v_ver/INITIAL_SPEED]

    elif direction == "RIGHT":
        ball_vel=[-v_hor/INITIAL_SPEED,-v_ver/INITIAL_SPEED]

    initial_ball_velocity=math.sqrt(ball_vel[0]**2+ball_vel[1]**2)
    print ""
    print "Initial ball velocity: ",initial_ball_velocity

# define event handlers


def set_or_reset_global_variables():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, number_of_saves  # these are ints
    global number_of_saves_lst
    number_of_saves_lst=[]

    paddle1_pos=HEIGHT/3
    paddle2_pos=HEIGHT/3


    score1=0
    score2=0

    number_of_saves=0

    paddle1_vel=0
    paddle2_vel=0



def first_new_game():
    global GAME_IS_ON
    set_or_reset_global_variables()
    GAME_IS_ON=True

def new_game():
    global GAME_IS_ON
    set_or_reset_global_variables()
    GAME_IS_ON=True
    paddle1_vel=0
    paddle2_vel=0

    x=random.randrange(0,2)

    if x==0:
        spawn_ball("LEFT")
    else:
        spawn_ball("RIGHT")

def save1():

    if (ball_pos[1]+(3.0/4.0)*BALL_RADIUS)<(paddle1_pos-HALF_PAD_HEIGHT) or (ball_pos[1]-(3.0/4.0)*BALL_RADIUS/2)>(paddle1_pos+HALF_PAD_HEIGHT):
       return False
    else:
        return True

def save2():

    if (ball_pos[1]+(3.0/4.0)*BALL_RADIUS/2)<(paddle2_pos-HALF_PAD_HEIGHT) or (ball_pos[1]-(3.0/4.0)*BALL_RADIUS/2)>(paddle2_pos+HALF_PAD_HEIGHT):
       return False
    else:
        return True




def draw(canvas):
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1)+"      "+str(score2), (250, 40), 40, 'Green')



    if GAME_IS_ON:
        draw_game_is_on(canvas)

    else:
        if score1>score2:
            message="Left player won!"
        elif score1<score2:
            message="Right player won!"

        canvas.draw_text(message, (200,80),30,"Green")
        #print str(max(number_of_saves_lst))
        #message2 = "Maximum number of saves in a round: "+str(max(number_of_saves_lst))
        #canvas.draw_text(message2, (200,140),20,"Green")


        canvas.draw_circle([ball_pos[0], ball_pos[1]],BALL_RADIUS, 1, "White", "White")

def draw_game_is_on(canvas):
    global score1, score2, number_of_saves, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global GAME_IS_ON
    global number_of_saves_lst


    # update ball

    if GRAVITY:
        ball_vel[1]+=0.1


    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[1]<=BALL_RADIUS or ball_pos[1]>HEIGHT-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]


    if ball_pos[0]-BALL_RADIUS <= PAD_WIDTH:
        if save1():
            #if not paddle1_vel ==0:
            #    score1 +=0.1
            number_of_saves +=1
            if not paddle1_vel==0:
                ball_vel[0] = - 1.10*ball_vel[0]
                ball_vel[1]=1.10*ball_vel[1]
            else:
                ball_vel[0] = -ball_vel[0]
                ball_vel[1]= ball_vel[1]

            if VERTICAL or GRAVITY:

                if ball_vel[1]*paddle1_vel>0:
                    ball_vel[1]=ball_vel[1]*1.1
                elif ball_vel[1]*paddle1_vel<0 and ball_vel[1]>1:
                    ball_vel[1]=ball_vel[1]*0.7

            #ball_vel[1]=ball_vel[1]*1.1
            #if ball_vel[1]*paddle1_vel>0:
            #    ball_vel[1]=1.30*ball_vel[1]
            #if ball_vel[1]*paddle1_vel<0:
             #   ball_vel[1]=0.50*ball_vel[1]
            #elif ball_vel[1]*paddle1_vel>0:
             #   ball_vel[1]=1.10*ball_vel[1]
            #else:
            #    ball_vel[1]=1.10*ball_vel[1]

        else:
            #print "Number of saves:", number_of_saves
            number_of_saves_lst.append(number_of_saves)
            score2 +=1
            print "Ball velocity: ",math.sqrt(ball_vel[0]**2+ball_vel[1]**2)
            print ball_vel[0],ball_vel[1]
            print "Number of saves", number_of_saves
            if score2<max_game_length: #and score1<max_game_length:
                spawn_ball ("LEFT")
            else:

                GAME_IS_ON=False
                ball_pos=[WIDTH/2, HEIGHT/2]
    if ball_pos[0]+BALL_RADIUS >= WIDTH-PAD_WIDTH:
        if save2():
            #if not paddle2_vel==0:
            #    score2 +=0.1
            number_of_saves +=1
            if not paddle2_vel==0:
                ball_vel[0] = - 1.1*ball_vel[0]
                ball_vel[1]= 1.1*ball_vel[1]
            else:
                ball_vel[0] = -ball_vel[0]
                ball_vel[1]=ball_vel[1]

            if VERTICAL or GRAVITY:

                if ball_vel[1]*paddle2_vel>0:
                    ball_vel[1]=ball_vel[1]*1.1
                elif ball_vel[1]*paddle2_vel<0 and ball_vel[1]>1:
                    ball_vel[1]=0.7*ball_vel[1]
            #if ball_vel[1]*paddle2_vel<0:
             #   ball_vel[1]=0.50*ball_vel[1]
        else:
            #print "Number of saves:",number_of_saves
            number_of_saves_lst.append(number_of_saves)
            print "Max ball velocity: ", math.sqrt(ball_vel[0]**2+ball_vel[1]**2)
            print ball_vel[0],ball_vel[1]
            print "Number of saves: ", number_of_saves

            score1 +=1
            if score1<max_game_length: #and score2<max_game_length:
                spawn_ball ("RIGHT")
            else:
                GAME_IS_ON=False
                ball_pos=[WIDTH/2, HEIGHT/2]

    # draw ball
    canvas.draw_circle([ball_pos[0],ball_pos[1]],BALL_RADIUS, 1, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos-HALF_PAD_HEIGHT)<=0:
        paddle1_pos=HALF_PAD_HEIGHT

        if paddle1_vel>=0:
             paddle1_pos += paddle1_vel

    elif (paddle1_pos+HALF_PAD_HEIGHT)>=HEIGHT:
        paddle1_pos=HEIGHT-HALF_PAD_HEIGHT
        if paddle1_vel<=0:
            paddle1_pos += paddle1_vel
    else:
         paddle1_pos += paddle1_vel


    if (paddle2_pos-HALF_PAD_HEIGHT)<=0:
        paddle2_pos=HALF_PAD_HEIGHT
        if paddle2_vel>=0:
            paddle2_pos +=paddle2_vel

    elif (paddle2_pos+HALF_PAD_HEIGHT)>=HEIGHT:
        paddle2_pos=HEIGHT-HALF_PAD_HEIGHT
        if paddle2_vel<=0:
            paddle2_pos += paddle2_vel

    else:
        paddle2_pos += paddle2_vel


    # draw paddles

    canvas.draw_line([HALF_PAD_WIDTH,paddle1_pos-HALF_PAD_HEIGHT], [HALF_PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT],PAD_WIDTH, "White")
    canvas.draw_line([WIDTH-HALF_PAD_WIDTH,paddle2_pos-HALF_PAD_HEIGHT], [WIDTH-HALF_PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT],PAD_WIDTH, "White")



    #spawn_ball(LEFT) or spawn_ball(RIGHT) to


    # draw scores
    #canvas.draw_text(str(score1)+"/"+str(score2), (200, 40), 40, 'Red')


def keydown(key):
    global paddle1_vel, paddle2_vel

    #x=10
    import math
    #x=abs(1*ball_vel[0])+0.2*abs(ball_vel[1])
    x=min([PADLET_SPEED_FACTOR*(abs(ball_vel[0])+abs(ball_vel[1])),150])
    #if GRAVITY:
     #   x=10
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -x
    if key == simplegui.KEY_MAP["q"]:
        paddle1_vel=-x
    if key == simplegui.KEY_MAP["a"]:
        paddle1_vel=x
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel=x

def decr_radius():
    global BALL_RADIUS

    if BALL_RADIUS*0.95>0:
        BALL_RADIUS = BALL_RADIUS*0.95


def incr_radius():
    global BALL_RADIUS
    if BALL_RADIUS*1.1<HEIGHT/2:
        BALL_RADIUS=BALL_RADIUS*1.1


def decr_pad_height():
    global PAD_HEIGHT, HALF_PAD_HEIGHT

    if PAD_HEIGHT*0.95>0:
        PAD_HEIGHT = PAD_HEIGHT*0.95
        HALF_PAD_HEIGHT=PAD_HEIGHT/2

def incr_pad_height():
    global PAD_HEIGHT, HALF_PAD_HEIGHT
    if PAD_HEIGHT*1.05<WIDTH:
        PAD_HEIGHT = PAD_HEIGHT*1.05
        HALF_PAD_HEIGHT=PAD_HEIGHT/2


def reset():
    global BALL_RADIUS, PAD_HEIGHT, PAD_HEIGHT, HALF_PAD_HEIGHT
    global PADLET_SPEED_FACTOR
    global DEFAULT, VERTICAL, GRAVITY
    DEFAULT=True
    VERTICAL = False
    GRAVITY=False
    PADLET_SPEED_FACTOR=0.62
    BALL_RADIUS=20
    PAD_HEIGHT=80

    HALF_PAD_HEIGHT = PAD_HEIGHT/2.0

def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["q"]:
        paddle1_vel=0
    if key == simplegui.KEY_MAP["a"]:
        paddle1_vel=0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel=0
    if key == simplegui.KEY_MAP["w"]:
        quit()
    if key == simplegui.KEY_MAP["n"]:
        new_game()
    if key == simplegui.KEY_MAP["1"]:
        decr_radius()

def incr_padlet_speed():
    global PADLET_SPEED_FACTOR
    PADLET_SPEED_FACTOR +=0.02

def vertical():
    global VERTICAL
    VERTICAL=True

def gravity():
    global GRAVITY, VERTICAL
    GRAVITY=True
    VERTICAL = True

def button_handler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New game", button_handler, 100)
frame.add_button("Decrese ball radius", decr_radius, 100)
frame.add_button("Increase ball radius", incr_radius,100)
frame.add_button("Increase paddlet speed", incr_padlet_speed,100)
frame.add_button("Decrease paddlet height", decr_pad_height,100)
frame.add_button("Increase paddlet height", incr_pad_height,100)
frame.add_button("Vertical", vertical, 100)
frame.add_button("Gravity", gravity,100)
frame.add_button("Reset", reset,100)

# start frame
first_new_game()
frame.start()
