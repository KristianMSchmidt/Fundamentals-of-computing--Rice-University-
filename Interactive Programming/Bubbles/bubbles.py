# Basic infrastructure for Bubble Shooter

import simplegui
import random
import math

# Global constants
WIDTH = 800
HEIGHT = 600
FIRING_POSITION = [WIDTH // 2, HEIGHT]
FIRING_LINE_LENGTH = 60
FIRING_ANGLE_VEL_INC = 0.05
BUBBLE_RADIUS = 20
COLOR_LIST = ["Red", "Green", "Blue", "Yellow"]

# global variables
firing_angle = math.pi / 2
firing_angle_vel = 0
bubble_stuck = True

#sound for firing
firing_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Collision8-Bit.ogg")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)

def add_vectors(v,w):
    return [v[0]+w[0],v[1]+w[1]]

def vector_times_constant(v,c):
    return [c*v[0],c*v[1]]

# spawn bubble

def spawn():
    global bubble
    bubble=Bubble(firing_sound)

# class defintion for Bubbles
class Bubble:

    def __init__(self, sound=None):
        self.pos=list(FIRING_POSITION)
        self.vel=[0,0]
        self.color=random.choice(COLOR_LIST)
        self.sound=sound

    def update(self):
        if not BUBBLE_RADIUS<self.pos[0] +self.vel[0] < WIDTH-BUBBLE_RADIUS:
            self.vel[0]= - self.vel[0]

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]


    def fire_bubble(self, vel):
        self.sound.play()
        dir=angle_to_vector(-firing_angle)
        self.vel=vector_times_constant(dir,vel)

    def is_stuck(self):
        pass

    def collide(self, bubble):
        pass

    def draw(self, canvas):
        canvas.draw_circle(self.pos, BUBBLE_RADIUS, 5, "White", self.color)


# define keyhandlers to control firing_angle
def keydown(key):
    global a_bubble, firing_angle_vel, bubble_stuck

    if key == simplegui.KEY_MAP["left"]:
        firing_angle_vel += FIRING_ANGLE_VEL_INC
    if key == simplegui.KEY_MAP["right"]:
        firing_angle_vel=-FIRING_ANGLE_VEL_INC
    if key == simplegui.KEY_MAP["space"]:
        bubble.fire_bubble(3)

def keyup(key):
    global firing_angle_vel

    if key == simplegui.KEY_MAP["left"]:
        firing_angle_vel -= FIRING_ANGLE_VEL_INC

    if key == simplegui.KEY_MAP["right"]:
        firing_angle_vel += FIRING_ANGLE_VEL_INC


# define draw handler
def draw(canvas):
    global firing_angle, a_bubble, bubble_stuck

    # update firing angle
    firing_angle += firing_angle_vel

    # draw firing line

    direction=angle_to_vector(-firing_angle)
    arrow=vector_times_constant(direction,FIRING_LINE_LENGTH)
    end_point_of_firing_line = add_vectors(FIRING_POSITION, arrow)

    canvas.draw_line(FIRING_POSITION, end_point_of_firing_line, 4, "White")

    # update a_bubble and check for sticking
    bubble.update()

    # draw a bubble and stuck bubbles
    bubble.draw(canvas)

# create frame and register handlers
frame = simplegui.create_frame("Bubble Shooter", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# create initial buble and start frame
spawn()
frame.start()
