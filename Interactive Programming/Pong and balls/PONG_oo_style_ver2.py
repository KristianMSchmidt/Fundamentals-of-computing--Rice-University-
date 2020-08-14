# Implementation of classic arcade game Pong

import simplegui
import random
import math

# Globals constants
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_HEIGHT = PAD_HEIGHT/2
HALF_PAD_WIDTH = PAD_WIDTH/2
GRAVITATIONAL_CONSTANT=0.1
OTHER_SPEED_FACTOR=1 #SET TO 1.05 if you want to increase speed of saved ball by 5%
HUMAN_PAD_SPEED = 4     #4 works
COMP_PAD_SPEED =4

#PADLET_SPEED_FACTOR=0.3  #0.62
#GAME_LENGTH=3

#global variables


#def make_ball2():

#    colors = ["Yellow", "Red","Green", "Orange", "Lime", "Brown", "Teal", "Grey", "Navy", "Olive", "Fuchsia", "Purple"]
#    color_number=random.randrange(1,13)
#    color=colors[color_number]
#    pos=[WIDTH/2, HEIGHT/2]

def make_balls():
    global all_balls

    colors = ["Yellow", "Red","Green", "Orange", "Lime", "Brown", "Teal", "Grey", "Navy", "Olive", "Fuchsia", "Purple"]
    color_number=random.randrange(1,13)


    pos=[WIDTH/2, HEIGHT/2]

    ball1=Ball([WIDTH/2, HEIGHT/2],[-4,-2],[0,0], "Yellow")
    ball2=Ball([WIDTH/2, HEIGHT/2],[4,2],[0,0], "Red")
    ball3=Ball([WIDTH/2, HEIGHT/2],[3,-3],[0,0], "Green")
    ball4=Ball([WIDTH/2, HEIGHT/2],[-3,3],[0,0], "Orange")
    ball5=Ball([WIDTH/2, HEIGHT/2],[-1.5,4],[0,0],"Lime")
    ball6=Ball([WIDTH/2, HEIGHT/2],[1.5,4],[0,0], "Brown")
    ball7=Ball([WIDTH/2, HEIGHT/2],[-3,-3],[0,0], "Teal")
    ball8=Ball([WIDTH/2, HEIGHT/2],[3,3],[0,0], "Grey")
    ball9=Ball([WIDTH/2, HEIGHT/2],[3,-1],[0,0], "Navy")
    ball10=Ball([WIDTH/2, HEIGHT/2],[-3,1],[0,0], "Olive")
    ball11=Ball([WIDTH/2, HEIGHT/2],[-2.2,4],[0,0],"Fuchsia")
    ball12=Ball([WIDTH/2, HEIGHT/2],[2.2,-4],[0,0], "Purple")

    all_balls=[ball1, ball2, ball3, ball4, ball5,ball6,ball7,ball8,ball9,ball10,ball11,ball12]
    random.shuffle(all_balls)

def print_balls_in_play():
    print "Number of balls in play: ", len(balls_in_play)
    print "Max number is 12"
    print ""

def spawn_ball():
    if len(dead_balls)>0:
        for ball in dead_balls:
             ball.reset()
             dead_balls.remove(ball)

    random.shuffle(all_balls)
    for ball in all_balls:
        if not ball in balls_in_play:
            balls_in_play.append(ball)
            print_balls_in_play()
            return()

def print_new_game():

    print "NEW GAME"
    print " "
    print "Left paddle plays by algoritm", paddle1.algorithm
    print "Right paddle plays by algoritm", paddle2.algorithm
    print ""

def new_game():
    global paddles, paddle1, paddle2
    global balls_in_play,dead_balls, COMP_PAD_SPEED

    COMP_PAD_SPEED=4
    dead_balls=[]
    balls_in_play =[]

    paddle1=Paddle(PAD_WIDTH/2)
    paddle2=Paddle(WIDTH-PAD_WIDTH/2)
    paddles=[paddle1,paddle2]

    "choose algorithms for paddles"
    paddle1.algorithm=2
    paddle2.algorithm=1
    print_new_game()

    make_balls()
    spawn_ball()
#    label.set_text('   GRAVITY LEVEL: '+str(balls_in_play[0].acc[1]))

class Ball:
    def __init__(self, pos=[WIDTH/2, HEIGHT/2], vel=[0,0], acc=[0,0], color="White"):
        self.pos=pos
        self.vel=vel
        self.initial_pos=pos
        self.initial_vel=vel
        self.acc=acc
        self.radius=BALL_RADIUS
        self.color=color

    def __str__(self):
        return self.color +" ball"

    def reset(self):
        self.vel=self.initial_vel
        self.pos=[WIDTH/2,HEIGHT/2]     #self.initial_pos burde virke?

    def set_vel(vel):
        self.vel[0]=vel[0]
        self.vel[1]=vel[1]

    def set_pos(self,pos):
        self.pos[0]=pos[0]
        self.pos[1]=pos[1]

    def add_gravity(self,c):
        self.acc[1]+= c

    def update_vel(self):
        self.vel[0] += self.acc[0]
        self.vel[1] += self.acc[1]

    def update_pos(self):
        self.pos[0] += self.vel[0]

        if self.pos[1]<=HEIGHT-self.radius:
            self.pos[1] += self.vel[1]
        else:
            self.pos[1]=HEIGHT-self.vel

    def is_to_hit_roof_or_floor(self):
        if not self.radius<=self.pos[1]+self.vel[1]<=HEIGHT-self.radius:
            return True
        else:
            return False

    def has_crossed_left_border(self):
        if self.pos[0]<PAD_WIDTH+self.radius:
            return True
        else: return False

    def has_crossed_right_border(self):
        if self.pos[0]>WIDTH-PAD_WIDTH-self.radius:
            return True
        else: return False

    def is_vertically_within_paddle(self,paddle):
        ball_not_to_high = self.pos[1]+(4.0/5.0)*BALL_RADIUS>paddle.pos-HALF_PAD_HEIGHT
        ball_not_to_low = self.pos[1]-(4.0/5.0)*BALL_RADIUS/2<paddle.pos+HALF_PAD_HEIGHT
        if (ball_not_to_high and ball_not_to_low):
            return True
        else: return False

    def has_hit_left_paddle(self):
        if self.has_crossed_left_border():
            return self.is_vertically_within_paddle(paddle1)

    def has_hit_right_paddle(self):
        if self.has_crossed_right_border():
            return self.is_vertically_within_paddle(paddle2)



    def dies(self):
        if self.has_crossed_right_border():
            if not self.has_hit_right_paddle():
                paddle1.add_one_to_score()
                return True

        if self.has_crossed_left_border():
            if not self.has_hit_left_paddle():
                paddle2.add_one_to_score()
                return True

    def move(self):

        self.update_vel()

        if self.is_to_hit_roof_or_floor():
            self.vel[1] = - self.vel[1]

        if self.has_hit_left_paddle() or self.has_hit_right_paddle():
            self.vel[0]= -self.vel[0]*OTHER_SPEED_FACTOR
            self.vel[1]= self.vel[1]*OTHER_SPEED_FACTOR

        if self.dies():
            dead_balls.append(self)

            if len(balls_in_play)<2:
                spawn_ball()
            balls_in_play.remove(self)
            print_balls_in_play()

        self.update_pos()


    def draw(self,canvas):
        canvas.draw_circle(self.pos, self.radius, 1, self.color, self.color)

class Paddle:

    def __init__(self, xloc, pos=HEIGHT/2, vel=0,score=0, comp_control=True, algorithm=1):
        self.xloc=xloc
        self.pos=pos
        self.vel=vel
        self.height=PAD_HEIGHT
        self.width=PAD_WIDTH
        self.score=score
        self.comp_control=comp_control
        self.algorithm=algorithm

    def set_pos(self,y):
        self.pos=y

    def add_one_to_score(self):
        self.score +=1

    def set_vel(self, v):
        self.vel=v

    def move(self):
        if  self.height/2 <= self.pos + self.vel <= HEIGHT-self.height/2:
            self.pos += self.vel

    def draw(self, canvas):
        canvas.draw_line([self.xloc,self.pos-self.height/2], [self.xloc, self.pos+self.height/2], self.width, "White")



    def arriving_balls(self,ball_list):
        arriving_balls= []

        for ball in ball_list:
            if (self.xloc-ball.pos[0])/ball.vel[0] >0:
                arriving_balls.append(ball)

        return(arriving_balls)

    def critical_ball(self,ball_list):
        arriving_balls=self.arriving_balls(ball_list)
        lst=[]

        if len(arriving_balls)==0:
            crit_ball=ball_list[0]
        else:
            for ball in arriving_balls:
                lst.append(abs(self.xloc-ball.pos[0]))
            index=lst.index(min(lst))
            crit_ball=arriving_balls[index]

        return crit_ball

    def nearest_arriving_ball(self, ball_list):

        arriving_balls=self.arriving_balls(ball_list)

        if len(arriving_balls)==0:
            nball=ball_list[0]

        else:
            dist_lst=[]
            for ball in arriving_balls:

                dist=abs(ball.pos[1]-self.pos) + abs(ball.pos[0]-self.xloc)  #overvej  -BALL_RADIUS? Ovrevej at beregne tætte afstand til padden hjørner
                dist_lst.append(dist)

            index=dist_lst.index(min(dist_lst))
            nball=arriving_balls[index]

        return nball

    def auto_play(self,ball_list):

        nball=self.nearest_arriving_ball(ball_list)
        crit_ball=self.critical_ball(ball_list)

        if self.algorithm==1:
            ball_to_follow=nball

        if self.algorithm==2:
            ball_to_follow=crit_ball

        if self.algorithm==3:
             if abs(self.xloc-nball.pos[0])<4*BALL_RADIUS:
                ball_to_follow=nball
             else:
                ball_to_follow=crit_ball

##algorithm 4 not done.... skal simpelthen regne det rigtige sted ud

     #if self.algorithm == 4:
    #        ball_to_follow=crit_ball
       #    if crit_ball==old_crit_ball:
        #        pass
        #    else:
        #        virtual_ball=Ball(crit_ball.pos, crit_ball.vel, [0,0],"White",True)
#
#                while not virtual_ball.pos[0]>WIDTH-BALL_RADIUS-PAD_WIDTH:
#                    virtual_ball.move_virtual()
#                print virtual_ball.pos


        #common for all algorithms:

        if self.pos<ball_to_follow.pos[1]:
            self.vel= COMP_PAD_SPEED
        else:
            self.vel= -COMP_PAD_SPEED

        self.move()


    def play(self,ball_list):
        if self.comp_control:
            self.auto_play(ball_list)
        else:
            self.move()


time=0
def draw(canvas):
    global time
    time +=1

     # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(paddle1.score)+"      "+str(paddle2.score), (250, 40), 40, 'White')

     #move and draw balls
    for ball in balls_in_play:
        ball.move()
        ball.draw(canvas)

    #move and draw paddles
    for paddle in paddles:
            paddle.play(balls_in_play)
            paddle.draw(canvas)

    if time%300==0:
        spawn_ball()

inputs = {"up":[1,-HUMAN_PAD_SPEED], "down":[1,HUMAN_PAD_SPEED], "q":[0,-HUMAN_PAD_SPEED], "a":[0,HUMAN_PAD_SPEED]}

def keydown(key):
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            pad_nr=inputs[i][0]
            paddles[pad_nr].set_vel(inputs[i][1])

def keyup(key):
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            pad_nr=inputs[i][0]
            paddles[pad_nr].set_vel(0)


def one_more_ball():
    spawn_ball()

def all_balls():
    for ball in all_balls:
        spawn_ball()

def gravity():
    for ball in balls_in_play:
        ball.add_gravity(GRAVITATIONAL_CONSTANT)
    label.set_text('   Gravity is '+str(balls_in_play[0].acc[1]))


def less_gravity():
    for ball in balls_in_play:
        ball.add_gravity(-GRAVITATIONAL_CONSTANT)
    label.set_text('   Gravity is '+str(balls_in_play[0].acc[1]))

def comp_right():
    if paddle2.comp_control:
        paddle2.set_vel(0)
        paddle2.comp_control=False
    else:
        paddle2.comp_control=True

def comp_left():
    global paddle1_vel
    if paddle1.comp_control:
        paddle1.comp_control=False
        paddle1.set_vel(0)
    else:
        paddle1.comp_control=True

def human_right():
    paddle2.comp_control=False

def human_left():
    paddle1.comp_control=False

def reset_score():
    paddle1.score=0
    paddle2.score=0

def make_computer_faster():
    global COMP_PAD_SPEED
    COMP_PAD_SPEED +=1

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game", new_game, 100)

frame.add_button("Reset score", reset_score, 100)
frame.add_label("",100)
#frame.add_button("Decrese ball radius", decr_radius, 100)
#frame.add_button("Increase ball radius", incr_radius,100)
frame.add_button("One more ball...", one_more_ball,100)
frame.add_button("All balls!",all_balls, 100)
#frame.add_button("Decrease paddlet height", decr_pad_height,100)
#frame.add_button("Increase paddlet height", incr_pad_height,100)
#frame.add_button("Vertical", vertical, 100)
frame.add_label("",100)
frame.add_label("",100)

frame.add_button("Increase computer paddle speed", make_computer_faster,200)
#frame.add_button("Less gracity!", less_gravity,100)
frame.add_label("")
#label=frame.add_label("   GRAVITY: 0")
label6=frame.add_label("")
frame.add_button("Human plays right (on/off)", comp_right,200)
frame.add_button("Human plays left (on/off)!", comp_left,200)
#frame.add_button("Computer plays right!", comp_right,100)
#frame.add_button("Human plays left!", human_left,100)
label5=frame.add_label("")
label5=frame.add_label("KEYBOARD CONTROL:")

label2=frame.add_label("Left player: up/down is q/a")
label3=frame.add_label("Right player: use arrow keys")
label6=frame.add_label("")

frame.start()
new_game()
