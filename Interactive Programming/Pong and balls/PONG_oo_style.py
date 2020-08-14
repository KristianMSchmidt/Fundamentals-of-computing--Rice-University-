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
HUMAN_PAD_SPEED = 5     #4 works
COMP_PAD_SPEED =5

#PADLET_SPEED_FACTOR=0.3  #0.62
#GAME_LENGTH=3

#global variables


def new_game():
    global paddles, paddle1, paddle2
    global balls, extra_balls, extra_balls_in_play

    ball1=Ball([WIDTH/2, HEIGHT/2],[-4,-2],[0,0], "Yellow")
    ball2=Ball([WIDTH/2, HEIGHT/2],[5,1],[0,0], "Red")
    ball3=Ball([WIDTH/2, HEIGHT/2],[3,3],[0,0], "Green")
    ball4=Ball([WIDTH/2, HEIGHT/2],[2,3],[0,0], "Orange")
    ball5=Ball([WIDTH/2, HEIGHT/2],[-1.5,4],[0,0],"Lime")
    ball6=Ball([WIDTH/2, HEIGHT/2],[-1,4],[0,0], "Brown")
    all_balls=[ball1, ball2, ball3, ball4, ball5,ball6]
    random.shuffle(all_balls)

    balls=[all_balls[0]]
    extra_balls=[all_balls[i] for i in range(1,len(all_balls))]
    extra_balls_in_play=0

    paddle1=Paddle(PAD_WIDTH/2)
    paddle2=Paddle(WIDTH-PAD_WIDTH/2)
    paddles=[paddle1,paddle2]

    label.set_text('   GRAVITY LEVEL: '+str(balls[0].acc[1]))


class Ball:
    def __init__(self, pos=[WIDTH/2, HEIGHT/2], vel=[0,0], acc=[0,0], color="White"):
        self.pos=pos
        self.vel=vel
        self.acc=acc
        self.radius=BALL_RADIUS
        self.color=color

    def __str__(self):
        return self.color +" ball"

    def set_vel(vel):
        self.vel[0]=vel[0]
        self.vel[1]=vel[1]

    def set_pos(pos):
        self.pos[0]=pos[0]
        self.pos[1]=pos[1]

    def add_gravity(self,c):
        self.acc[1]+= c

    #def is_about_to_hit_wall(self):
     #   if self.vel[0]<0:
      #      critical=PAD_WIDTH+self.radius
       #     if self.pos[0]>=critical and self.pos[0]+self.vel[0]<critical:
        #        print "venstre"
         #       return (True, 0)
        #if self.vel[0]>0:
         #  critical=WIDTH-PAD_WIDTH-self.radius
          #  if self.pos[0]<=critical and self.pos[0]+self.vel[0]>critical:
           #     print "hoejre"
            #    return (True, 1)



    def move(self):
        hor_standard = PAD_WIDTH+self.radius<=self.pos[0]+self.vel[0]<=WIDTH-PAD_WIDTH-self.radius
        ver_standard = self.radius<=self.pos[1]+self.vel[1]<=HEIGHT-self.radius
        situations=[hor_standard, ver_standard]

        for i in [0,1]:
            if situations[i]:
                self.vel[i] += self.acc[i]
            else:
                self.vel[i] = - self.vel[i]
            self.pos[i] += self.vel[i]

    def draw(self,canvas):
        canvas.draw_circle(self.pos, self.radius, 1, self.color, self.color)


class Paddle:

    def __init__(self, xloc, pos=HEIGHT/2, vel=0,score=0, comp_control=False):
        self.xloc=xloc
        self.pos=pos
        self.vel=vel
        self.height=PAD_HEIGHT
        self.width=PAD_WIDTH
        self.score=score
        self.comp_control=comp_control

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


    def is_saved(self, ball):
        #if ball.is_about_to_hit_wall()==(True,0):

        if self.xloc<WIDTH/2 and ball.pos[0]+ball.vel[0]<PAD_WIDTH+BALL_RADIUS:
            if (ball.pos[1]+(3.0/4.0)*BALL_RADIUS)<(self.pos-HALF_PAD_HEIGHT) or (ball.pos[1]-(3.0/4.0)*BALL_RADIUS/2)>(self.pos+HALF_PAD_HEIGHT):
                #self.score -=1
                paddle2.add_one_to_score()
                #print ball
                return False
            else:
                #self.score +=1
                ball.vel[0] *=OTHER_SPEED_FACTOR
                ball.vel[1] *=OTHER_SPEED_FACTOR
                return True
        elif self.xloc>WIDTH/2 and ball.pos[0]+ball.vel[0]>WIDTH-PAD_WIDTH-BALL_RADIUS:

            if (ball.pos[1]+(3.0/4.0)*BALL_RADIUS/2)<(self.pos-HALF_PAD_HEIGHT) or (ball.pos[1]-(3.0/4.0)*BALL_RADIUS/2)>(self.pos+HALF_PAD_HEIGHT):
                #self.score -=1
                paddle1.add_one_to_score()
                return False
            else:
                #self.score +=1
                ball.vel[0] *=OTHER_SPEED_FACTOR
                ball.vel[1] *=OTHER_SPEED_FACTOR

                return True
        else:
            return False


    def get_nearest_arriving_ball(self, ball_list):
        left_going_balls=[]
        right_going_balls=[]

        for ball in ball_list:
            if ball.vel[0]>0:
                right_going_balls.append(ball)
            elif ball.vel[0]<0:
                left_going_balls.append(ball)

        dist_lst=[]

        if self.xloc<WIDTH/2 and len(left_going_balls)>0:
            for ball in left_going_balls:
                dist=abs(ball.pos[0]-BALL_RADIUS-self.xloc)+abs(ball.pos[1]-self.pos)
                dist_lst.append(dist)

            index=dist_lst.index(min(dist_lst))
            nball=left_going_balls[index]

        elif self.xloc>WIDTH/2 and len(right_going_balls)>0:
            for ball in right_going_balls:
                dist=abs(ball.pos[0]-BALL_RADIUS-self.xloc)+abs(ball.pos[1]-self.pos)
                dist_lst.append(dist)
            index=dist_lst.index(min(dist_lst))
            nball=right_going_balls[index]
        else:
            nball=ball_list[0]

        return (nball)

    def auto_play(self,ball_list):

        nball=self.get_nearest_arriving_ball(ball_list)

        self.is_saved(nball)

        if self.pos<nball.pos[1]:
            self.vel= COMP_PAD_SPEED
        else:
            self.vel= -COMP_PAD_SPEED

        self.move()

    def play(self,ball_list):
        if self.comp_control:
            self.auto_play(ball_list)
        else:
            self.move()
            self.is_saved(self.get_nearest_arriving_ball(balls))



def draw(canvas):
     # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(paddle1.score)+"      "+str(paddle2.score), (250, 40), 40, 'White')

     #move and draw balls
    for ball in balls:
        ball.move()
        ball.draw(canvas)

    #move and draw paddles
    for paddle in paddles:
            paddle.play(balls)
            paddle.draw(canvas)

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
    global extra_balls_in_play

    if extra_balls_in_play<=len(extra_balls)-1:
        balls.append(extra_balls[extra_balls_in_play])
        extra_balls_in_play +=1

def gravity():
    for ball in balls:
        ball.add_gravity(GRAVITATIONAL_CONSTANT)
    label.set_text('   Gravity is '+str(balls[0].acc[1]))


def less_gravity():
    for ball in balls:
        ball.add_gravity(-GRAVITATIONAL_CONSTANT)
    label.set_text('   Gravity is '+str(balls[0].acc[1]))

def comp_right():
    if paddle2.comp_control:
        paddle2.comp_control=False
    else:
        paddle2.comp_control=True

def comp_left():
    if paddle1.comp_control:
        paddle2.comp_control=False
    else:
        paddle1.comp_control=True

def human_right():
    paddle2.comp_control=False

def human_left():
    paddle1.comp_control=False

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New game/Reset", new_game, 100)
frame.add_label("",100)
#frame.add_button("Decrese ball radius", decr_radius, 100)
#frame.add_button("Increase ball radius", incr_radius,100)
frame.add_button("More balls!", one_more_ball,100)
#frame.add_button("Decrease paddlet height", decr_pad_height,100)
#frame.add_button("Increase paddlet height", incr_pad_height,100)
#frame.add_button("Vertical", vertical, 100)
frame.add_label("",100)

frame.add_button("More gravity!", gravity,100)
frame.add_button("Less gracity!", less_gravity,100)
frame.add_label("")
label=frame.add_label("   GRAVITY: 0")
label6=frame.add_label("")
frame.add_button("Computer plays right (on/off)", comp_right,150)
frame.add_button("Computer plays left (on/off)!", comp_left,150)
#frame.add_button("Computer plays right!", comp_right,100)
#frame.add_button("Human plays left!", human_left,100)
label5=frame.add_label("")
label5=frame.add_label("KEYBOARD CONTROL:")

label2=frame.add_label("Left player: up/down is q/a")
label3=frame.add_label("Right player: use arrow keys")
label6=frame.add_label("")

frame.start()
new_game()
