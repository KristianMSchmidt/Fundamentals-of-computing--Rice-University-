
###################################################
# Student should enter code below

import simplegui

BALL_RADIUS = 60
GRID_SIZE = 30
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS


# define draw
def draw(canvas):
    center=[BALL_RADIUS,BALL_RADIUS]
    for j in range(1,GRID_SIZE+1):
        for i in range(1,GRID_SIZE+1):

            canvas.draw_circle(center,BALL_RADIUS,1,"White", "Blue")
            center = [center[0]+2*BALL_RADIUS, center[1]]
        center=[BALL_RADIUS,center[1]+2*BALL_RADIUS]

        # define draw

def draw2(canvas):
    center=[BALL_RADIUS,BALL_RADIUS]
    for j in range(1,GRID_SIZE+1):
        for i in range(1,GRID_SIZE+1):
            canvas.draw_circle([BALL_RADIUS+(i-1)*2*BALL_RADIUS, BALL_RADIUS+(j-1)*2*BALL_RADIUS],BALL_RADIUS,1,"White", "Blue")

# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw2)

# start frame
frame.start()
