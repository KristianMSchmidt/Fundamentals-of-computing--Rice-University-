# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
INITIAL_SPEED = 55  #50 is slow, 40 is standard, 30 is fast
#LEFT = False
#RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos=[WIDTH/2, HEIGHT/2]
ball_vel=[0,0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global number_of_saves

    number_of_saves=0
    ball_pos=[WIDTH/2, HEIGHT/2]

    v_hor=random.randrange(120, 240) # pixels per second.
    v_ver=random.randrange(60, 180)


    if direction=="LEFT":
        ball_vel=[v_hor/INITIAL_SPEED,-v_ver/INITIAL_SPEED]

    elif direction == "RIGHT":
        ball_vel=[-v_hor/INITIAL_SPEED,-v_ver/INITIAL_SPEED]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, number_of_saves  # these are ints

    paddle1_pos=HEIGHT/2
    paddle2_pos=HEIGHT/2

    score1=0
    score2=0

    number_of_saves=0

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
    global score1, score2, number_of_saves, paddle1_pos, paddle2_pos, ball_pos, ball_vel



    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[1]<=BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    elif ball_pos[1]>HEIGHT-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]


    if ball_pos[0]-BALL_RADIUS <= PAD_WIDTH:
        if save1():
            number_of_saves +=1
            ball_vel[0] = - ball_vel[0]
            ball_vel[0]=ball_vel[0]*1.1
            ball_vel[1]=ball_vel[1]*1.1
        else:
            print "Total number of saves:", number_of_saves
            score2 +=1
            spawn_ball ("LEFT")

    if ball_pos[0]+BALL_RADIUS >= WIDTH-PAD_WIDTH:
        if save2():
            number_of_saves +=1
            ball_vel[0] = - ball_vel[0]
            ball_vel[0]=ball_vel[0]*1.1
            ball_vel[1]=ball_vel[1]*1.1
        else:
            print "Total number of saves:",number_of_saves
            score1 +=1
            spawn_ball ("RIGHT")






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
    canvas.draw_text(str(score1)+"/"+str(score2), (200, 40), 40, 'Red')


def keydown(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -10
    if key == simplegui.KEY_MAP["q"]:
        paddle1_vel=-10
    if key == simplegui.KEY_MAP["a"]:
        paddle1_vel=10
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel=10

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

def button_handler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New game", button_handler, 100)

# start frame
new_game()
frame.start()
