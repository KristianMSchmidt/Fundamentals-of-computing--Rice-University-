# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui

WIDTH = 1000
HEIGHT = 1000
radius = 1


# Timer handler
def tick():
    global radius
    radius=radius+1


# Draw handler
def draw_handler(canvas):
    canvas.draw_circle([WIDTH/2, HEIGHT/2], radius, 10, 'Yellow', 'Orange')

# Create frame and timer
frame = simplegui.create_frame("Home", WIDTH, HEIGHT)
timer = simplegui.create_timer(100,tick)
frame.set_draw_handler(draw_handler)

# Start timer
frame.start()
timer.start()
