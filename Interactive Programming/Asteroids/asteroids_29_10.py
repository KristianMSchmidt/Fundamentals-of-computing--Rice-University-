#Min projektopgave om Asteroids

import simplegui
import math
import random

# globals for user interface

WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started=False
missiles=set()

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")


# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
#soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


#helper funktion to check for collision betwen a group and a sprite object
def group_collide(group, other_object):
    was_collision=False
    group_copy=set(group)

    for element in group_copy:
        if element.collision(other_object):
            group.remove(element)
            was_collision=True

    return was_collision

#helper funktion to check for collisions between two groups and remove

def group_group_collision(group1, group2):
    copy1=set(group1)
    number_of_collides=0

    for element in copy1:
        if group_collide(group2, element):
            group1.remove(element)
            number_of_collides +=1

    return(number_of_collides)

#helper function to draw a bunch of sprites
def process_sprite_group(sprite_group, canvas):
    group_copy=set(sprite_group)

    for sprite in group_copy:
        if sprite.update():
            sprite_group.remove(sprite)
        else:
            sprite.draw(canvas)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)


    def update(self):
        self.angle += self.angle_vel

        #thrust acceleration
        forward=angle_to_vector(self.angle)
        acc_const = 0.1 #0.05

        if self.thrust:
            self.vel[0] += acc_const*forward[0]
            self.vel[1] += acc_const*forward[1]
            ship_thrust_sound.play()
            self.image_center=[135,45]

        else:
            ship_thrust_sound.rewind()
            self.image_center=[45,45]

        #friction:
        fric_const= 0.01
        self.vel[0] *= (1-fric_const)
        self.vel[1] *=(1-fric_const)

        # update position
        self.pos[0] = (self.pos[0]+ self.vel[0])%WIDTH
        self.pos[1] = (self.pos[1]+ self.vel[1])%HEIGHT



    def shoot(self):
        forward=angle_to_vector(self.angle)

        pos=[self.pos[0]+self.radius*forward[0],self.pos[1]+self.radius*forward[1]]

        shot_vel_factor=10

        vel0=self.vel[0]+shot_vel_factor*forward[0]
        vel1=self.vel[1]+shot_vel_factor*forward[1]

        a_missile = Sprite(pos, [vel0, vel1], 0, 0, missile_image, missile_info, missile_sound)
        missiles.add(a_missile)

# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):

        #update angle
        self.angle += self.angle_vel

        #update postition
        self.pos[0] = (self.pos[0]+self.vel[0])%WIDTH
        self.pos[1] = (self.pos[1]+self.vel[1])%HEIGHT

        #update age
        self.age += 1.5
        if self.age>self.lifespan:
            return True
        else:
            return False


    def collision(self, other_object):
        if other_object.radius+self.radius<dist(other_object.pos,self.pos):
            return False
        else:
            return True


def draw(canvas):
    global time, lives, score, started, rocks

    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship
    my_ship.draw(canvas)

    #update ship
    my_ship.update()

    #update and draw all rocks, missiles
    process_sprite_group(rocks,canvas)
    process_sprite_group(missiles, canvas)

    #remove collided asteroids and update lives
    if group_collide(rocks, my_ship):
        lives -=1
        if lives<1:
            ship_thrust_sound.rewind()
            started=False
            init_ship_and_rock()

    #update score and effect of fired missiles
    score += group_group_collision(rocks, missiles)

    #draw score and remaining lives
    canvas.draw_text("Lives", [WIDTH/20,HEIGHT/10], 25, "White")
    canvas.draw_text("   "+str(lives), [WIDTH/20,HEIGHT/7], 25, "White")
    canvas.draw_text("Score", [17*WIDTH/20,HEIGHT/10], 25, "White")
    canvas.draw_text("    "+str(score), [17*WIDTH/20,HEIGHT/7], 25, "White")

    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(),
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                          splash_info.get_size())



# timer handler that spawns a rock
def rock_spawner():
    x_pos=WIDTH* random.randrange(1,100)/100
    y_pos=HEIGHT*random.randrange(1,100)/100
    pos=(x_pos,y_pos)

    velocity_constant = 1+ 0.8 * math.sqrt((3*score+1)/10)  #higher means faster rocks
    x_vel=velocity_constant*random.choice([-1,1])*random.random()
    y_vel=velocity_constant*random.choice([-1,1])*random.random()
    vel=(x_vel,y_vel)

    angle= 2*math.pi*random.random()

    ang_vel_constant=0.10
    angle_vel=random.choice([-1,1])*ang_vel_constant*random.random()

    a_rock=Sprite(pos, vel, angle, angle_vel, asteroid_image, asteroid_info)

    if len(rocks)<10 and started and dist(pos, my_ship.pos)>200:
        rocks.add(a_rock)



# keydown handler
def keydown(key):
    global started

    #constant determining ships ang. velocity
    angle_vel_constant=math.pi/40

    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = -angle_vel_constant

    if key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel =  angle_vel_constant


    if not started:
        return


    if key == simplegui.KEY_MAP["space"]:
            my_ship.shoot()

    if key == simplegui.KEY_MAP["up"]:
        my_ship.thrust=True

    if key == simplegui.KEY_MAP["down"]:
        my_ship.thrust=False


def keyup(key):

    if key == simplegui.KEY_MAP["up"]:
        my_ship.thrust=False

    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel =0

    if key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = 0


def start(click):
    global started, score, lives
    score=0
    lives=3

    started=True
    soundtrack.rewind()
    soundtrack.play()


# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and rock
def init_ship_and_rock():
    global my_ship, rocks
    my_ship = Ship([3*WIDTH / 5, 3*HEIGHT / 9], [0, 0], -0.5, ship_image, ship_info)
    a_rock=Sprite([WIDTH/4, HEIGHT/4], [1,1],0, 0.05, asteroid_image, asteroid_info)
    rocks=set([a_rock])
init_ship_and_rock()

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(start)

timer = simplegui.create_timer(500, rock_spawner)

# get things rolling
timer.start()
frame.start()

#print my_ship.image
#print "image center", my_ship.image_center
#print "umage size", my_ship.image_size
#print "image radius", my_ship.radius
      
