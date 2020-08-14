# Move a ball

###################################################
# Student should add code where relevant to the following.


import simplegui

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    #print ball_radius
    canvas.draw_circle((200,200), ball_radius, 5, "Black", "Blue")
    #canvas.draw_text("hej", [45,80], 20, "White")

    # Event handlers for buttons
def increase_radius():
    global ball_radius
    ball_radius = ball_radius + 5

def decrease_radius():
    global ball_radius
    print ball_radius
    if ball_radius-5<=0:
        print "Error!"
    else:
        ball_radius= ball_radius-5

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", HEIGHT, WIDTH)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)


# Start the frame animation
frame.start()
