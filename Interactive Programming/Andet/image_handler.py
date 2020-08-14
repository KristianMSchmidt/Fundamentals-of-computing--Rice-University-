# Image positioning problem

###################################################
# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300

# load test image
image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png')
print image.get_width()
print image.get_height()

# mouseclick handler
def click(pos):
    global position
    position=pos
    print position

position=(50,50)

# draw handler
def draw(canvas):
    canvas.draw_image(image, (95/2, 93/2), (95, 92), position, (95,93))


# create frame and register draw handler
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)


# start frame
frame.start()
