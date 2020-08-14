# Display "This is easy?"

###################################################
# Student should add code where relevant to the following.

import simplegui

count=0
# Draw handler
def draw(canvas):
    global count
    count=count+1
    canvas.draw_text(str(count)+"  "+ str(count**2), [60, 110], 24, "White")

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("This is easy", 400, 200)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()
